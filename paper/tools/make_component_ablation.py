"""Build the single-column component-ablation figure from the six source PNGs.

Requires Pillow and PyMuPDF. Images are embedded without image adjustments.
Run from paper/: python tools/make_component_ablation.py --preview OUTPUT.png
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import io
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import pymupdf


ROOT = Path(__file__).resolve().parents[1]
WIDTH_PT = 236.25  # Column width in the project's current CVPR style.
CANVAS = (1540, 1006)
SCALE = WIDTH_PT / CANVAS[0]
METHODS = [
    ("ours", "(a) Ours", ("ours.png", "ours-2.png")),
    ("without_CCM", "(b) w/o CCM", ("without CCM.png", "without CCM-2.png")),
    ("without_GCM", "(c) w/o GCM", ("without GCM.png", "without GCM-2.png")),
]
REGIONS = [
    [(204, 4, 396, 100), (140, 166, 236, 262)],
    [(116, 12, 308, 108), (368, 144, 464, 240)],
]
COLORS = ["#EDAA22", "#24A4CF"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rgb(color):
    return tuple(int(color[i:i + 2], 16) / 255 for i in (1, 3, 5))


def png_bytes(im):
    buf = io.BytesIO()
    im.save(buf, format="PNG")
    return buf.getvalue()


def build(source_dir):
    items, sources = [], []
    for row in range(2):
        top = 6 + row * 464
        for col, (key, label, names) in enumerate(METHODS):
            path = source_dir / names[row]
            data = path.read_bytes()
            im = Image.open(io.BytesIO(data))
            if im.size != (504, 280) or im.mode != "RGB":
                raise ValueError(f"Unexpected image size or mode: {path}")
            x = 6 + col * 512
            items.append(("image", (x, top, 504, 280), data))
            sources.append({"file": names[row], "sha256": digest(data),
                            "method": key, "scene_row": row + 1, "pixels": list(im.size)})
            for j, box in enumerate(REGIONS[row]):
                left, y, right, bottom = box
                bounds = (x + left, top + y, right - left, bottom - y)
                items.append(("rect", bounds, "#FFFFFF", 6.0))
                items.append(("rect", bounds, COLORS[j], 3.3))
                crop_x = x if j == 0 else x + 338
                crop_w = 332 if j == 0 else 166
                items.append(("image", (crop_x, top + 284, crop_w, 166), png_bytes(im.crop(box))))
                items.append(("rect", (crop_x, top + 284, crop_w, 166), COLORS[j], 3.3))
    for col, (_, label, _) in enumerate(METHODS):
        items.append(("text", 258 + col * 512, 987, label, 9.0))
    return items, sources


def export(items, output, preview, font_path):
    doc = pymupdf.open()
    page = doc.new_page(width=WIDTH_PT, height=CANVAS[1] * SCALE)
    page.insert_font(fontname="FigureFont", fontfile=str(font_path))
    font = pymupdf.Font(fontfile=str(font_path))
    canvas = Image.new("RGB", CANVAS, "white") if preview else None
    draw = ImageDraw.Draw(canvas) if canvas else None
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH_PT / 72 * 25.4:.6f}mm" '
           f'height="{CANVAS[1] * SCALE / 72 * 25.4:.6f}mm" viewBox="0 0 {CANVAS[0]} {CANVAS[1]}">',
           '<title>Completion component ablations</title>',
           '<desc>Two scene rows compare Ours, removal of CCM, and removal of GCM. '
           'Matching wide and square crops appear beneath each overview.</desc>',
           f'<rect width="{CANVAS[0]}" height="{CANVAS[1]}" fill="white"/>']
    for item in items:
        if item[0] in ("image", "rect"):
            x, y, w, h = item[1]
            rect = pymupdf.Rect(x * SCALE, y * SCALE, (x + w) * SCALE, (y + h) * SCALE)
            if item[0] == "image":
                data = item[2]
                page.insert_image(rect, stream=data)
                if canvas:
                    im = Image.open(io.BytesIO(data))
                    if im.size != (w, h):
                        im = im.resize((w, h), Image.Resampling.NEAREST)
                    canvas.paste(im, (x, y))
                embedded = base64.b64encode(data).decode("ascii")
                svg.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" '
                           f'href="data:image/png;base64,{embedded}" style="image-rendering:pixelated"/>')
            else:
                color, width = item[2:]
                page.draw_rect(rect, color=rgb(color), width=width * SCALE)
                if draw:
                    draw.rectangle((x, y, x + w, y + h), outline=color, width=round(width))
                svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
                           f'stroke="{color}" stroke-width="{width}" fill="none"/>')
        else:
            _, center, baseline, text, size = item
            left = center * SCALE - font.text_length(text, fontsize=size) / 2
            page.insert_text((left, baseline * SCALE), text, fontsize=size,
                             fontname="FigureFont", color=(0.06, 0.06, 0.06))
            if draw:
                raster_font = ImageFont.truetype(str(font_path), round(size / SCALE))
                text_w = draw.textlength(text, font=raster_font)
                draw.text((center - text_w / 2, baseline), text, font=raster_font,
                          fill="#111111", anchor="ls")
            svg.append(f'<text x="{center}" y="{baseline}" font-family="Times New Roman, serif" '
                       f'font-size="{size / SCALE:.6f}" text-anchor="middle">{html.escape(text)}</text>')
    doc.set_metadata({"title": "Completion component ablations",
                      "subject": "Author-provided experimental renderings; matched crops; no image adjustments"})
    doc.subset_fonts()
    output.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output, garbage=4, deflate=True)
    doc.close()
    svg.append("</svg>")
    output.with_suffix(".svg").write_text("\n".join(svg), encoding="utf-8")
    if canvas:
        preview.parent.mkdir(parents=True, exist_ok=True)
        ppi = CANVAS[0] / (WIDTH_PT / 72)
        canvas.save(preview, dpi=(ppi, ppi))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=ROOT / "fig/source/component-ablation")
    parser.add_argument("--output", type=Path, default=ROOT / "fig/fig06-component-ablation.pdf")
    parser.add_argument("--preview", type=Path)
    parser.add_argument("--font-file", type=Path, default=Path(r"C:\Windows\Fonts\times.ttf"))
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    items, sources = build(args.source_dir)
    export(items, args.output, args.preview, args.font_file)
    if args.manifest:
        record = {"sources": sources, "method_order": [m[0] for m in METHODS],
                  "source_roi_boxes": REGIONS, "roi_coordinate_convention": "left,top,right,bottom; half-open pixels",
                  "canvas_pixels": list(CANVAS), "width_pt": WIDTH_PT,
                  "height_pt": CANVAS[1] * SCALE, "font_size_pt": 9.0,
                  "image_adjustments": [], "detail_display_interpolation": "nearest neighbor",
                  "source_images_embedded_at_native_resolution": True,
                  "pdf_sha256": digest(args.output.read_bytes()),
                  "svg_sha256": digest(args.output.with_suffix('.svg').read_bytes())}
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "width_mm": WIDTH_PT / 72 * 25.4,
                      "height_mm": CANVAS[1] * SCALE / 72 * 25.4}, ensure_ascii=True))


if __name__ == "__main__":
    main()
