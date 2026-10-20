"""Source-grounded vector overview. Draws SVG objects; never edits raster drafts."""
from pathlib import Path
from html import escape
import math
import random

ROOT = Path(__file__).resolve().parent
W, H = 2400, 1120
INK = '#27384A'
BLUE = '#4D89B9'
ORANGE = '#E5A15B'
GRAY = '#D5DCE3'
VIOLET = '#A59ABA'
parts = []
random.seed(7)


def add(s):
    parts.append(s)


def rect(x, y, w, h, fill='white', stroke=INK, radius=5, sw=1.6, extra=''):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')


def text(x, y, value, size=25, weight=400, color=INK, anchor='start'):
    size = max(size, 34)  # ~7.1 pt at a final width of 178 mm.
    lines = value.split('\n')
    add(f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">')
    for i, line in enumerate(lines):
        add(f'<tspan x="{x}" dy="{0 if i == 0 else size * 1.19}">{escape(line)}</tspan>')
    add('</text>')


def path(d, color=INK, width=2.3, arrow=True, dashed=False, under=False):
    if under:
        add(f'<path d="{d}" fill="none" stroke="white" stroke-width="{width + 5}" stroke-linejoin="round"/>')
    dash = 'stroke-dasharray="7 5"' if dashed else ''
    marker = f'marker-end="url(#{"blueArrow" if color == BLUE else "arrow"})"' if arrow else ''
    add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" {dash} {marker}/>')


def ellipse(x, y, rx, ry, fill=BLUE, opacity=1, stroke='none', angle=0):
    add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" transform="rotate({angle} {x} {y})"/>')


def axis(x, y, scale=1):
    path(f'M {x} {y} l {28*scale} {12*scale}', width=1.5)
    path(f'M {x} {y} l {-22*scale} {13*scale}', width=1.5)
    path(f'M {x} {y} l 0 {-32*scale}', width=1.5)


def camera(x, y, s=1):
    add(f'<path d="M {x} {y} l {38*s} {-21*s} v {42*s} Z" fill="#EAF1F8" stroke="{INK}" stroke-width="1.8"/>')
    rect(x-8*s, y-7*s, 10*s, 14*s, '#D5E4F1', sw=1.5, radius=1)


def car(x, y, s=1, completed=False, query=False, rotation=0, surface=True):
    add(f'<g transform="translate({x} {y}) rotate({rotation}) scale({s})">')
    add(f'<path d="M 0 42 L 25 23 L 88 20 L 114 35 L 146 47 L 145 72 L 12 77 L 0 66 Z" fill="#E8F0F8" stroke="{INK}" stroke-width="2"/>')
    add(f'<path d="M 26 26 L 42 3 L 92 1 L 114 35 L 79 42 Z" fill="#BCD5E9" stroke="{INK}" stroke-width="2"/>')
    add(f'<path d="M 43 8 L 55 33 L 30 26 Z M 49 7 L 88 6 L 105 31 L 62 34 Z" fill="#ECF5FB" stroke="{INK}" stroke-width="1.6"/>')
    ellipse(29, 70, 13, 18, '#36485A', stroke=INK)
    ellipse(119, 65, 13, 18, '#36485A', stroke=INK)
    ellipse(29, 70, 6, 10, '#D1DCE7')
    ellipse(119, 65, 6, 10, '#D1DCE7')
    for i in range(31 if surface else 0):
        px, py = 8 + (i * 23 % 130), 42 + (i * 13 % 26)
        color = ORANGE if completed and px > 91 else BLUE
        ellipse(px, py, 5.2, 2.8, color if completed or px < 95 else GRAY, .85, angle=-10)
    if query:
        rect(-8, -10, 164, 102, 'none', '#9BA8B5', sw=1, extra='stroke-dasharray="4 4"')
    add('</g>')


def human(x, y, s=1, completed=False, posed=False, query=False, surface=True):
    add(f'<g transform="translate({x} {y}) scale({s})">')
    # Exactly one head and one skeleton, with observed/completed surface ownership.
    ellipse(0, 8, 11, 13, '#DCEAF5', stroke=INK)
    joints = {'neck': (0, 26), 'hip': (0, 76), 'ls': (-19, 34), 'rs': (19, 34),
              'le': (-30, 58), 're': (35, 50 if posed else 58),
              'lh': (-35, 79), 'rh': (48 if posed else 35, 32 if posed else 79),
              'lk': (-15, 112), 'rk': (25 if posed else 15, 111),
              'lf': (-25 if posed else -18, 148), 'rf': (40 if posed else 18, 148)}
    bones = [('neck', 'hip'), ('neck', 'ls'), ('neck', 'rs'), ('ls', 'le'), ('le', 'lh'),
             ('rs', 're'), ('re', 'rh'), ('hip', 'lk'), ('lk', 'lf'), ('hip', 'rk'), ('rk', 'rf')]
    for a, b in bones:
        p, q = joints[a], joints[b]
        path(f'M {p[0]} {p[1]} L {q[0]} {q[1]}', '#62778B', 3, False)
        for j in range(1, 5 if surface else 1):
            u = j / 5
            px, py = p[0] * (1-u) + q[0]*u, p[1]*(1-u)+q[1]*u
            color = ORANGE if completed and px > 3 else BLUE
            ellipse(px, py, 7 if a in ('neck', 'hip') else 4.5, 7.8, color, .7, angle=12)
    for px, py in joints.values():
        ellipse(px, py, 3, 3, INK)
    if query:
        rect(-45, -13, 98, 174, 'none', '#9BA8B5', sw=1, extra='stroke-dasharray="4 4"')
    add('</g>')


def road(x, y, w=210, h=105, complete=False, actors=False):
    add(f'<g transform="translate({x} {y})">')
    add(f'<path d="M 0 {h} L {w*.30} 0 L {w*.90} 0 L {w} {h} Z" fill="#F4F6F8" stroke="#8FA0AE" stroke-width="1.4"/>')
    for i in range(1, 6):
        yy = h * i / 6
        path(f'M {w*.30*(1-yy/h)} {yy} H {w*.90+w*.1*yy/h}', '#CBD3DA', 1, False)
    for j in range(1, 7):
        xx = w*j/7
        path(f'M {w*.30+xx*.60} 0 L {xx} {h}', '#CBD3DA', 1, False)
    for i in range(56):
        u, v = random.random(), random.random()
        px = w*.30*(1-v) + u*(w*.60+w*.40*v)
        py = h*v
        color = BLUE if u < .52 else ORANGE if complete else GRAY
        ellipse(px, py, 3.3+2*v, 1.7+v, color, .83, angle=-20)
    if actors:
        car(w*.24, h*.20, .55, complete)
        human(w*.82, h*.04, .48, complete, True)
    add('</g>')


def view(x, y, w=215, h=125, variant=0, completed=True):
    rect(x, y, w, h, '#F6F8FA', '#A7B3BE', radius=4)
    add(f'<path d="M {x+8} {y+h-5} L {x+w*.44} {y+30} L {x+w*.68} {y+30} L {x+w-8} {y+h-5} Z" fill="#E3E8ED"/>')
    for yy in (y+54, y+84, y+114):
        path(f'M {x+w*.55} {yy} l 0 10', 'white', 3, False)
    rect(x+8, y+24, 32, 42, '#E7ECEF', '#BEC9D2', radius=1, sw=1)
    rect(x+w-40, y+17, 30, 49, '#E7ECEF', '#BEC9D2', radius=1, sw=1)
    car(x+58+variant*4, y+64, .53, completed, rotation=-5 if variant == 1 else 0)
    human(x+w-46, y+61, .32, completed, posed=variant == 2)


def tokens(x, y, completed=False, size=21):
    states = [BLUE, BLUE, ORANGE if completed else GRAY, ORANGE if completed else GRAY, 'url(#hatch)', ORANGE if completed else GRAY]
    for i, fill in enumerate(states):
        rect(x+i*(size+4), y, size, size, fill, '#768A9D', radius=0, sw=1)


def lock(x, y, s=1):
    path(f'M {x+5*s} {y+12*s} v {-5*s} a {7*s} {7*s} 0 0 1 {14*s} 0 v {5*s}', INK, 2, False)
    rect(x, y+12*s, 24*s, 20*s, INK, INK, radius=3)
    ellipse(x+12*s, y+21*s, 2*s, 3*s, 'white')


add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">')
add('<title id="title">DriveCompose: observation-anchored joint completion of composable Gaussian driving worlds</title>')
add('<desc id="desc">A source-grounded mechanism illustration. Multi-camera evidence forms typed canonical queries, which are jointly completed using parallel local attention and global memory. Observed codes and free space are constrained. Decoded candidates are checked before acceptance as fixed world content. Only the accepted world and current state enter the renderer. External dynamics update state only.</desc>')
add(f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 Z" fill="{INK}"/></marker><marker id="blueArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 Z" fill="{BLUE}"/></marker><pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="white"/><path d="M -2 2 L 2 -2 M 0 7 L 7 0 M 5 9 L 9 5" stroke="#98A5B2" stroke-width="1"/></pattern></defs>')
add('<rect width="2400" height="1120" fill="white"/><g font-family="Arial, Helvetica, sans-serif">')

# Scope and hierarchy. Only the focal computation receives a tinted enclosure.
for x in (310, 675, 1450, 1920):
    path(f'M {x} 20 V 1090', '#D9E0E7', 1.2, False)
rect(697, 80, 730, 840, '#FBFAFD', '#DDD6E7', radius=14, sw=1.5)
for x, label in ((25, '(a) Observations'), (335, '(b) Canonical queries'),
                 (720, '(c) Joint Completion DiT'),
                 (1475, '(d) Fixed Gaussian world'), (1942, '(e) State-driven reuse')):
    text(x, 50, label, 29, 600)

# A. Input -> encoder -> evidence. Camera images are explanatory diagrams.
text(155, 103, 'Multi-camera logs', 25, 600, anchor='middle')
view(46, 125, 235, 135, completed=False)
view(46, 285, 235, 135, 1, completed=False)
text(165, 454, 'RGB · K · T · time', 21, anchor='middle')
camera(60, 500, .75); camera(145, 500, .75); camera(230, 500, .75)
path('M 279 352 H 295 V 573 H 165 V 594', width=2.8)
rect(62, 595, 208, 94, '#EDF3F9', '#748DA4', radius=7)
text(166, 631, 'Driving Log\nEncoder', 28, 500, anchor='middle')
path('M 166 689 V 730', width=2.8)
text(165, 765, 'Geometry + IDs\nconfidence + state', 24, anchor='middle')
path('M 272 768 H 324 V 185', width=2.7, arrow=False)
for yy in (185, 395, 640):
    ellipse(324, yy, 3.6, 3.6, INK)
    path(f'M 324 {yy} H 347', width=2.7)

# B. Canonical representations and an explicit typed-encoding interface.
text(356, 107, 'Background / world', 25, 600)
road(356, 135, 225, 115)
axis(384, 274, .65)
text(610, 330, 'Sky', 22, anchor='middle')
ellipse(610, 267, 19, 19, 'none', stroke='#A3B2C0')
for a in range(0, 360, 60):
    r = math.radians(a)
    path(f'M 610 267 L {610+30*math.cos(r)} {267+30*math.sin(r)}', '#6F879C', 1.4)
text(356, 370, 'Vehicle local', 25, 600)
car(366, 400, 1.23, False, True)
axis(592, 491, .6)
text(356, 573, 'Human\ntemplate', 25, 600)
human(457, 635, 1.15, False, False, True)
axis(588, 801, .6)
rect(617, 392, 40, 416, '#F4F1F8', '#9C8DAF', radius=4)
add('<text transform="translate(643 600) rotate(-90)" text-anchor="middle" fill="#384A5C" font-size="34">Typed latent encoding</text>')
path('M 578 219 H 664 V 370 H 636 V 392', width=2.5)
path('M 640 267 H 650 V 392', width=1.8, dashed=True)
path('M 550 453 H 617', width=2.5)
path('M 513 742 H 617', width=2.5)
path('M 657 600 H 683', width=2.8, arrow=False)
path('M 683 340 V 640', width=2.8, arrow=False)

# C. Three independent local groups and one common memory. Connections first,
# then representation/operation objects; white bridges mean no false junctions.
text(1062, 119, 'Canonical + world-reference coordinates', 24, 500, anchor='middle')
text(1062, 161, 'Type · visibility · confidence · scene context', 22, anchor='middle')
path('M 1402 171 V 234 H 1284', '#8E819E', 1.7, dashed=True)
rect(854, 218, 430, 48, '#EEE9F5', '#9D91AF', radius=4)
for i in range(14):
    rect(862+i*29, 228, 23, 27, '#C4BAD4', '#9B8FAF', radius=0, sw=.8)
text(1068, 203, 'Global memory', 25, 600, anchor='middle')
row_y = [340, 490, 640]
for i, yy in enumerate(row_y):
    gx = 730-i*12
    bx = 1180+i*10
    path(f'M 980 {yy-17} H {gx} V {230+i*12} H 854', '#6D647D', 1.8, dashed=False)
    path(f'M {1195+i*25} 266 H {bx} V {yy+17} H 1140', '#6D647D', 1.8, dashed=True)
for yy, label in zip(row_y, ('BG + sky', 'Vehicle', 'Human')):
    text(753, yy-37, label, 23, 500)
    tokens(751, yy-12, False, 25)
    rect(980, yy-36, 160, 72, 'white', '#8B7C9B', radius=6)
    text(1060, yy-5, 'Local\nattention', 24, 500, anchor='middle')
    tokens(1210, yy-12, True, 25)
    path(f'M 921 {yy} H 980', width=2.7, under=True)
    path(f'M 1140 {yy} H 1210', width=2.7, under=True)
    path(f'M 683 {yy} H 751', width=2.8, under=True)
text(758, 730, 'Conditional flow', 26, 600)
text(1230, 730, 'τ: 0 → 1', 26, 500)
rect(754, 751, 648, 159, 'white', '#C7BECE', radius=7)
tokens(774, 790, False, 21)
path('M 928 801 H 970', width=2.4)
rect(970, 765, 234, 82, '#EDF3FA', '#819AB4', radius=5)
text(1087, 797, 'Keep observed', 22, 500, anchor='middle')
text(1087, 835, 'free code = 0', 22, anchor='middle')
path('M 1204 801 H 1235', width=2.4)
tokens(1235, 790, True, 21)
text(1104, 891, 'Every step', 21, anchor='middle')
# Observation bypass and free-opacity consumer remain distinct.
path('M 775 353 H 741 V 939 H 993 V 847', BLUE, 2.3, under=True)
for yy in (353, 503, 653):
    ellipse(775, yy, 3, 3, BLUE)
    if yy != 353:
        path(f'M 775 {yy} H 741', BLUE, 2.3, False, under=True)
text(802, 976, 'Observed-code bypass', 22, color=BLUE)
path('M 1345 811 V 968 H 1440 V 300', '#77889A', 1.8, False, dashed=True)
for yy in row_y:
    path(f'M 1440 {yy-22} H 1470', '#77889A', 1.8, dashed=True)
text(1402, 1022, 'Free support: opacity = 0', 22, anchor='end')
text(758, 1060, 'Solid: data / gather', 21)
text(758, 1097, 'Dashed: condition / broadcast', 21)

# D. Completed representation -> typed decoder -> candidate -> checker -> world.
text(1678, 105, 'Gaussian decoders', 25, 600, anchor='middle')
for yy, name in zip(row_y, ('BG + sky', 'Vehicle', 'Human')):
    path(f'M 1380 {yy} H 1470', width=2.7, under=True)
    rect(1470, yy-45, 180, 90, '#F2F5F8', '#7C91A6', radius=4)
    text(1560, yy-14 if '\n' in name else yy+11, name, 23, 500, anchor='middle')
    path(f'M 1650 {yy} H {1725 if yy == 640 else 1660}', width=2.5)
road(1660, 284, 207, 99, True)
car(1670, 450, 1.18, True)
human(1767, 570, .83, True, False)
for xx, yy in ((1868, 360), (1846, 510), (1803, 640)):
    path(f'M {xx} {yy} H 1890', width=1.8, arrow=False)
path('M 1890 360 V 698 H 1745 V 728', width=2.3)
text(1695, 724, 'Candidate', 23, 500, anchor='end')
rect(1555, 750, 303, 94, 'white', '#8E9EAC', radius=7)
text(1706, 787, 'Observed-view\ncheck', 25, 600, anchor='middle')
path('M 1745 728 V 750', width=2.5)
text(1464, 778, 'Ref.', 17)
camera(1490, 813, .4)
path('M 1510 813 H 1555', width=1.8)
path('M 1706 844 V 874', width=2.6)
rect(1524, 876, 365, 185, '#FAFCFD', '#C4D1DB', radius=7)
road(1558, 882, 291, 122, True, True)
lock(1537, 902, .85)
text(1705, 1040, 'Checked fixed world', 25, 600, anchor='middle')
# This is the sole persistent-content input to rendering. Candidate has no bypass.
path('M 1889 964 H 1937 V 346 H 1985', width=3.3, under=True)

# E. State and checked world are separate renderer inputs; only state is updated.
text(2169, 111, 'Current state', 27, 600, anchor='middle')
rect(1974, 125, 373, 138, '#FAFCFD', '#B6C5D2', radius=6)
camera(2006, 181, .85)
car(2093, 150, .72, rotation=-12, surface=False)
human(2290, 138, .55, posed=True, surface=False)
path('M 2170 263 V 303', width=2.8)
rect(1985, 305, 360, 84, '#EDF3FA', '#7D97B1', radius=7)
text(2165, 354, 'Compose & render', 29, 600, anchor='middle')
path('M 2020 389 V 417 H 1966 V 898', width=2.5, arrow=False)
for yy, title, v in ((471, 'New camera view', 0), (657, 'Vehicle state', 1), (843, 'Human pose', 2)):
    path(f'M 1966 {yy+55} H 2005', width=2.5)
    view(2005, yy, 235, 130, v)
    text(2122, yy-10, title, 22, anchor='middle')
text(2240, 422, 'Shared world', 22, anchor='end')
rect(2027, 1008, 293, 76, 'white', '#7F91A2', radius=6, extra='stroke-dasharray="6 5"')
text(2174, 1039, 'External policy\n/ dynamics', 23, 500, anchor='middle')
path('M 2240 536 H 2285 V 986 H 2174 V 1008', width=2.3)
for yy in (722, 908):
    path(f'M 2240 {yy} H 2285', width=2.3, arrow=False)
path('M 2320 1045 H 2372 V 180 H 2348', width=2.7)

# Compact legend. Shapes and hatching complement color.
rect(24, 870, 260, 235, 'white', '#CED7DF', radius=6)
for xx, yy, fill, label in ((43, 917, BLUE, 'Observed'), (43, 962, ORANGE, 'Completed'),
                            (43, 1007, GRAY, 'Unknown'), (43, 1052, 'url(#hatch)', 'Free')):
    rect(xx, yy-24, 24, 24, fill, '#8091A0', radius=0, sw=1)
    text(xx+36, yy, label, 19)
add('</g></svg>')
output = ROOT / 'drivecompose-overview-native.svg'
output.write_text('\n'.join(parts), encoding='utf-8')
print(output)
