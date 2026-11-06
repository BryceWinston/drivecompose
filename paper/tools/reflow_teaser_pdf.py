"""Compact the selected original teaser without altering its image resources.

This edits the PDF only. The separate draw.io design variants are not inputs.
All crops remove inspected outer white margins; no source pixels are resampled.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math

import pymupdf as fitz

BASELINE_SHA256 = "6183604dca2eae5cfa7a65e7e65c64599ee84be00640159bc7f0b3ac487326a5"
W, H = 1350, 640
INK = (.0627, .110, .196)
MUTED = (.435, .478, .537)
RULE = (.796, .824, .863)
FRAME = (.57, .64, .73)
BLUE_FILL = (.671, .788, .925)
BLUE_RULE = (.557, .682, .824)
CROPS = {
    6: (22, 24, 656, 334),
    30: (44, 8, 656, 359),
    31: (168, 12, 1813, 802),
    32: (24, 1, 303, 198),
    33: (25, 1, 304, 198),
    34: (40, 24, 728, 307),
    35: (60, 0, 711, 280),
    36: (60, 0, 711, 280),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--evidence-dir", required=True, type=Path)
    args = ap.parse_args()
    if sha(args.source) != BASELINE_SHA256:
        raise ValueError("Expected the explicitly selected original PDF baseline.")
    args.evidence_dir.mkdir(parents=True, exist_ok=True)
    source = fitz.open(args.source)
    original_images = {item[0]: item for item in source[0].get_images(full=True)}
    doc = fitz.open()
    doc.insert_pdf(source)
    remap = {old[0]: new[0] for old, new in zip(
        source[0].get_images(full=True), doc[0].get_images(full=True))}
    p = doc.new_page(width=W, height=H)
    fonts = {"regular": "C:/Windows/Fonts/times.ttf", "bold": "C:/Windows/Fonts/timesbd.ttf",
             "symbol": "C:/Windows/Fonts/cambria.ttc"}
    font_names = {"regular": "TNR", "bold": "TNRB", "symbol": "CAMS"}
    measures = {key: fitz.Font(fontfile=path) for key, path in fonts.items()}
    for key, path in fonts.items():
        p.insert_font(fontname=font_names[key], fontfile=path)
    labels, images, lines, boxes = [], [], [], []

    def text(value, x, y, size=18, weight="regular", color=INK, align="left", name=None):
        width = measures[weight].text_length(value, fontsize=size)
        if align == "center":
            x -= width / 2
        elif align == "right":
            x -= width
        missing = [ch for ch in value if not measures[weight].has_glyph(ord(ch))]
        if missing:
            raise ValueError(f"Missing glyphs in {weight}: {missing!r}")
        p.insert_text((x, y), value, fontsize=size, fontname=font_names[weight], color=color)
        labels.append(dict(id=name or value, text=value, baseline=y, x=x, width=width,
                           size=size, weight=weight))

    def line(a, b, width=1.5, color=INK, dashed=False, name=None):
        p.draw_line(a, b, width=width, color=color, dashes="[5 4] 0" if dashed else None)
        lines.append(dict(id=name, start=a, end=b, width=width))

    def arrow(a, b, width=1.5, color=INK, head=6, dashed=False, name=None):
        line(a, b, width, color, dashed, name)
        theta = math.atan2(b[1]-a[1], b[0]-a[0])
        q1 = (b[0]-head*math.cos(theta)+head*.43*math.sin(theta),
              b[1]-head*math.sin(theta)-head*.43*math.cos(theta))
        q2 = (b[0]-head*math.cos(theta)-head*.43*math.sin(theta),
              b[1]-head*math.sin(theta)+head*.43*math.cos(theta))
        s = p.new_shape()
        s.draw_polyline([q1, b, q2, q1])
        s.finish(color=color, fill=color, width=.3, closePath=True)
        s.commit()

    def box(bounds, name, fill=None, color=FRAME, width=1.1, radius=None):
        p.draw_rect(bounds, color=color, fill=fill, width=width, radius=radius)
        boxes.append(dict(id=name, bounds=list(bounds), color=color, width=width))

    def picture(xref, field, name):
        raw = original_images[xref]
        iw, ih = raw[2:4]
        crop = fitz.Rect(CROPS.get(xref, (0, 0, iw, ih)))
        field = fitz.Rect(field)
        scale = min(field.width/crop.width, field.height/crop.height)
        x = field.x0+(field.width-crop.width*scale)/2
        y = field.y0+(field.height-crop.height*scale)/2
        visible = fitz.Rect(x, y, x+crop.width*scale, y+crop.height*scale)
        full = fitz.Rect(x-crop.x0*scale, y-crop.y0*scale,
                         x+(iw-crop.x0)*scale, y+(ih-crop.y0)*scale)
        p.insert_image(full, xref=remap[xref], keep_proportion=True)
        content_id = p.get_contents()[-1]
        clip = (f"q {visible.x0:.7f} {H-visible.y1:.7f} "
                f"{visible.width:.7f} {visible.height:.7f} re W n\n").encode()
        doc.update_stream(content_id, clip+doc.xref_stream(content_id)+b"\nQ")
        images.append(dict(id=name, source_xref=xref, crop_px=list(crop),
                           visible_bounds=list(visible), scale=scale,
                           image_resource_sha256=hashlib.sha256(source.xref_stream(xref)).hexdigest()))
        return visible

    def operator(bounds, words, name, weight="regular"):
        box(bounds, name, BLUE_FILL, BLUE_RULE, 1.08, .12)
        x0, y0, x1, y1 = bounds
        cy = (y0+y1)/2
        for j, word in enumerate(words):
            text(word, (x0+x1)/2, cy-7+j*27, 23.28, weight, align="center")

    # Two equal-width scope frames replace the lone separating rule.
    box((280, 10, 1340, 196), "upper-observation-frame")
    box((280, 208, 1340, 630), "lower-completion-frame")

    # Shared source sequence retains the original 6 photographs and ordering.
    text("Multi-view sequence", 138, 143, 23.304, "bold", align="center")
    for row, pair in enumerate([(10, 13), (11, 14), (12, 15)]):
        y = 166+82*row
        text(["t₀", "t₁", "t₂"][row], 20, y+39, 17.28)
        for col, xr in enumerate(pair):
            r = picture(xr, (40+104*col, y, 135+104*col, y+63.092), f"input-{row}-{col}")
            box(r, f"input-frame-{row}-{col}", color=RULE, width=.8)
    # Ellipses remain true text (the same two source characters).
    for x in [87.5, 191.5]:
        text("⋮", x, 428, 18.72, weight="symbol", color=MUTED, align="center")
    arrow((6, 166), (6, 442), .8, MUTED, head=5, name="time-arrow")
    text("Time", 1.7, 464, 15, color=MUTED)
    text("Example frames", 138, 464, 17.28, align="center")
    line((245, 166), (253, 166), 1, MUTED)
    line((253, 166), (253, 442), 1, MUTED)
    line((245, 442), (253, 442), 1, MUTED)
    line((253, 300), (264, 300), 1.5)
    port_y = 248+(450-12)*560/1645
    line((264, 114), (264, port_y), 1.5)
    arrow((264, 114), (315, 114), name="input-to-observation")
    arrow((264, port_y), (315, port_y), name="input-to-completion")

    # Upper branch: compact operators, cropped source fields, matched centerline.
    operator((315, 81, 520, 147), ["Observation-only", "reconstruction"],
             "observation-operator", "bold")
    text("Aggregated observed surfaces", 677.5, 38, 18, "bold", align="center")
    picture(30, (545, 45, 810, 177), "aggregated-observed-scene")
    operator((850, 81, 1010, 147), ["State-driven", "rendering"], "rendering-operator")
    picture(28, (851, 24, 878, 45), "source-camera-icon")
    text("Camera", 889, 36, 17.28, color=MUTED)
    text("change", 889, 56, 17.28, color=MUTED)
    text("Unseen regions exposed", 1180, 38, 18, "bold", align="center")
    picture(6, (1040, 45, 1320, 177), "unseen-regions-scene")
    arrow((520, 114), (560, 114), name="reconstruction-to-observed")
    arrow((797, 114), (850, 114), dashed=True, name="observed-to-state-rendering")
    arrow((1010, 114), (1041, 114), name="rendering-to-unseen")
    text("(a) Observation-only reconstruction", 810, 187, 18, "bold", align="center")

    # Lower branch keeps the same completed scene, with no retouching.
    text("Joint completion", 315, 238, 23.28, "bold")
    text("Reuse the same assets", 1150, 238, 23.28, "bold", align="center")
    picture(31, (315, 248, 875, 248+790*560/1645), "joint-completion-main")
    # Legend occupies the inherited empty corner, releasing the lower strip.
    for y, value, fill, stroke in [
        (265, "Observed", (.863, .89, .922), (.659, .702, .765)),
        (291, "Completed", (1, .941, .824), (.894, .627, .173)),
    ]:
        box((813, y, 828, y+15), f"legend-{value}", fill, stroke, .9)
        text(value, 836, y+14, 16.56, "bold")

    # Reuse alternatives stay aligned and are reached by one explicit input.
    line((980, 310), (980, 554), 1.2)
    arrow((886, port_y), (980, port_y), name="completion-to-reuse")
    for cy, xr, words in zip([310, 432, 554], [34, 35, 36],
                             [("Camera", "view"), ("Vehicle", "rotation"), ("Human", "pose")]):
        picture(xr, (1004, cy-56, 1260, cy+56), f"reuse-{xr}")
        arrow((980, cy), (1003, cy), head=5, width=1.2, name=f"reuse-arrow-{xr}")
        for j, word in enumerate(words):
            text(word, 1274, cy-4+j*20, 16.56, "bold")

    # Compact comparison: labels beside cars avoid an extra caption-height row.
    line((315, 522), (950, 522), .65, RULE)
    picture(32, (330, 529, 420, 593), "all-inputs-aggregated-car")
    text("After aggregating", 434, 553, 17.28)
    text("all inputs", 434, 575, 17.28)
    arrow((580, 561), (631, 561), name="auxiliary-completion")
    picture(33, (645, 529, 735, 593), "completed-car")
    text("After joint", 750, 553, 17.28)
    text("completion", 750, 575, 17.28)
    text("Also: rotation and articulation", 1137, 620, 16.56, color=MUTED, align="center")
    text("(b) DriveCompose: joint completion and asset reuse", 810, 620, 18, "bold", align="center")

    doc.delete_page(0)
    doc.set_metadata({"title": "DriveCompose teaser", "creator": "DriveCompose compact PDF layout",
                      "producer": "PyMuPDF; original image resources retained"})
    doc.subset_fonts()
    # Avoid subset-font space/hyphen extraction aliases in Times New Roman.
    for entry in doc[0].get_fonts():
        kind, pointer = doc.xref_get_key(entry[0], "ToUnicode")
        if kind != "xref":
            continue
        cmap_id = int(pointer.split()[0])
        repaired = []
        for ln in doc.xref_stream(cmap_id).decode("ascii").splitlines():
            parts = ln.split()
            if (len(parts) in (2, 3) and parts[-1].lower() in ("<00a0>", "<00ad>")
                    and (len(parts) == 2 or parts[0] == parts[1])):
                parts[-1] = "<0020>" if parts[-1].lower() == "<00a0>" else "<002d>"
                ln = " ".join(parts)
            repaired.append(ln)
        doc.update_stream(cmap_id, ("\n".join(repaired)+"\n").encode("ascii"))
    doc.save(args.output, garbage=4, deflate=True)
    doc.close()
    render = fitz.open(args.output)
    render[0].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False).save(args.evidence_dir/"candidate.png")
    render[0].get_pixmap(matrix=fitz.Matrix(.85, .85), colorspace=fitz.csGRAY,
                         alpha=False).save(args.evidence_dir/"candidate-gray.png")
    inventory = dict(canvas=[W, H], source_sha256=BASELINE_SHA256, labels=labels, images=images,
                     lines=lines, boxes=boxes)
    (args.evidence_dir/"object-inventory.json").write_text(json.dumps(inventory, ensure_ascii=False,
                                                                    indent=2), encoding="utf-8")
    spec = dict(scope="PDF layout and two scope frames; no scientific content edits",
                canvas_before=list(source[0].rect), canvas_after=[W, H],
                height_reduction_percent=(1-H/source[0].rect.height)*100,
                correction_plan=[
                    dict(id="L01", objects=["upper-observation-frame", "lower-completion-frame"],
                         operation="Add equal-width 1.1 pt neutral frames at recorded bounds.",
                         preserve="All image content, source palette and original panel captions."),
                    dict(id="L02", objects=["observation-operator", "rendering-operator"],
                         operation="Reduce height from 89.28 to 66 pt, preserving text size and blue palette."),
                    dict(id="L03", objects=["joint-completion-main", "all-inputs-aggregated-car",
                                             "completed-car", "Observed", "Completed"],
                         operation="Crop outer white image margins, move legend to empty upper corner,"
                                   " place comparison captions beside vehicles, and reduce page height to 640 pt."),
                ],
                visual_grammar_receipt=dict(
                    claim_in_one_sentence="Completion supplies unseen surfaces, with the same assets reused under changed states.",
                    primary_reading_spine="Shared input at left; observation branch above and completion/reuse below.",
                    entry_and_exit="Six original photos; exposed unseen surfaces and three original reuse alternatives.",
                    dominant_focal_zone="Original central joint-completion scene.",
                    hierarchy_levels="Two original branches, scene fields, auxiliary vehicle comparison.",
                    role_to_shape_mapping="Blue operators, original scene fields, two neutral branch scope outlines.",
                    connector_prominence_levels="1.5 pt primary flow, 1.2 pt reuse branches, 0.65 pt comparison separator.",
                    typography_roles="Original Times New Roman hierarchy; no blanket type reduction.",
                    semantic_palette="Original blue operators and observed/completed surface colors.",
                    grayscale_plan="Panel scope and scene scale carry the layout hierarchy without hue.",
                    meaningful_content_hull=[1.7, 10, 1340, 630],
                    whitespace_functions="Frame padding, short connector lanes and protection of source scene silhouettes.",
                    evidence_role="Original concept figure; no empirical results added or image content synthesized.",
                    expressive_layer_if_any="None.", forbidden_motifs="No new module cards or generated artwork.",
                    reference_firewall="Only the user-selected PDF defines content and styling.",
                    review_sizes=["1.5x PDF render", "174.625 mm publication width", "grayscale whole figure"]),
                source_limitations="The original central raster contains its original baked labels/curves;"
                                   " retained as inherited, not claimed as fully native vector artwork.")
    (args.evidence_dir/"layout-spec.json").write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output":str(args.output), "sha256":sha(args.output), "images":len(images),
                      "page_size":[W,H], "height_reduction_percent":spec["height_reduction_percent"]}, indent=2))


if __name__ == "__main__":
    main()
