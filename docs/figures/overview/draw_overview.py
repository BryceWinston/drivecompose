"""Reproducible vector overview. All spatial marks are mechanism schematics.

Run with ReportLab; render the exported PDF with Poppler for the PNG preview.
SVG preserves text, paths, token cells and illustration as separate objects.
"""
from pathlib import Path
import base64
import html
import json
import math
import random
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'paper/fig'
ARCHIVE = ROOT.parent / '_archive/drivecompose/20261023-overview-redraw'
W, H = 1200, 730
S = 495 / W
INK = '#243241'
MUTED = '#536271'
LINE = '#A8B4BE'
BLUE = '#2878B8'
GRAY = '#DAE0E6'
ORANGE = '#E99739'
PURPLE = '#8261AC'
pdfmetrics.registerFont(TTFont('ArialDC', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialDC-Bold', 'C:/Windows/Fonts/arialbd.ttf'))


class Drawing:
    def __init__(self, path, hidden=()):
        self.path = Path(path)
        self.hidden = set(hidden)
        self.c = canvas.Canvas(str(self.path.with_suffix('.pdf')), pagesize=(W*S, H*S))
        self.c.setTitle('DriveCompose: observation-anchored joint completion and state-driven reuse')
        self.c.scale(S, S)
        self.c.translate(0, H)
        self.c.scale(1, -1)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="174.625mm" height="{H*S/72*25.4}mm" viewBox="0 0 {W} {H}">']
        self.text_bounds = []
        self.rect(0, 0, W, H, '#FFFFFF', None)

    def style(self, fill, stroke, lw=1):
        self.c.setLineWidth(lw)
        if fill:
            self.c.setFillColor(HexColor(fill))
        if stroke:
            self.c.setStrokeColor(HexColor(stroke))
        return f'fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{lw}"'

    def rect(self, x, y, w, h, fill='white', stroke=LINE, lw=1, r=0):
        a = self.style(fill, stroke, lw)
        self.c.roundRect(x, y, w, h, r, fill=bool(fill), stroke=bool(stroke))
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" {a}/>')

    def ellipse(self, x, y, rx, ry, fill, stroke=None, lw=1):
        a = self.style(fill, stroke, lw)
        self.c.ellipse(x-rx, y-ry, x+rx, y+ry, fill=bool(fill), stroke=bool(stroke))
        self.svg.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" {a}/>')

    def poly(self, pts, fill=None, stroke=INK, lw=1, close=True):
        a = self.style(fill, stroke, lw)
        p = self.c.beginPath()
        p.moveTo(*pts[0])
        for xy in pts[1:]:
            p.lineTo(*xy)
        if close:
            p.close()
        self.c.drawPath(p, stroke=bool(stroke), fill=bool(fill))
        tag = 'polygon' if close else 'polyline'
        self.svg.append(f'<{tag} points="'+ ' '.join(f'{x},{y}' for x,y in pts) + f'" {a}/>')

    def line(self, pts, color=INK, lw=1.6, arrow=False, dash=False):
        if dash:
            self.c.setDash(5, 4)
        self.poly(pts, None, color, lw, False)
        if dash:
            self.c.setDash()
            self.svg[-1] = self.svg[-1].replace('/>', ' stroke-dasharray="5 4"/>')
        if arrow:
            x,y = pts[-1]
            a,b = pts[-2]
            t = math.atan2(y-b, x-a)
            size = 7
            self.poly([(x,y), (x-size*math.cos(t)+3*math.sin(t),y-size*math.sin(t)-3*math.cos(t)),
                       (x-size*math.cos(t)-3*math.sin(t),y-size*math.sin(t)+3*math.cos(t))],color,None)

    def text(self, x, y, text, size=20, bold=False, color=INK, anchor='start', role='label'):
        if role in self.hidden:
            return
        font = 'ArialDC-Bold' if bold else 'ArialDC'
        tw = pdfmetrics.stringWidth(text, font, size)
        xx = x - (tw/2 if anchor=='middle' else tw if anchor=='end' else 0)
        self.c.saveState()
        self.c.translate(xx, y)
        self.c.scale(1,-1)
        self.c.setFont(font, size)
        self.c.setFillColor(HexColor(color))
        self.c.drawString(0,0,text)
        self.c.restoreState()
        self.svg.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}" fill="{color}" data-role="{role}">{html.escape(text)}</text>')
        self.text_bounds.append({'text':text,'x':round(xx,2),'y':y,'w':round(tw,2),'font_px':size,'font_pt':round(size*S,3),'role':role})

    def label(self, x, y, lines, size=20, bold=False, color=INK, anchor='middle', leading=23):
        for i,s in enumerate(lines):
            self.text(x,y+i*leading,s,size,bold,color,anchor)

    def op(self, x,y,w,h,lines,fill='#FFFFFF',stroke=INK,size=21):
        self.rect(x,y,w,h,fill,stroke,1.3,4)
        if isinstance(lines,str):
            lines=[lines]
        self.label(x+w/2,y+h/2-(len(lines)-1)*11.5+size*.33,lines,size,True)

    def image(self, path, x,y,w,h):
        self.c.saveState()
        self.c.translate(x,y+h)
        self.c.scale(1,-1)
        self.c.drawImage(str(path),0,0,w,h,mask='auto')
        self.c.restoreState()
        data=base64.b64encode(Path(path).read_bytes()).decode()
        self.svg.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" xlink:href="data:image/png;base64,{data}"/>')

    def finish(self):
        self.c.showPage()
        self.c.save()
        self.svg.append('</svg>')
        self.path.with_suffix('.svg').write_text('\n'.join(self.svg),encoding='utf-8')
        return self.text_bounds


def tokens(d,x,y,states,cell=17,h=22,gap=3):
    colors={'o':BLUE,'u':GRAY,'g':ORANGE,'n':'#BBA8CF','f':'#FFFFFF'}
    for i,s in enumerate(states):
        xx=x+i*(cell+gap)
        d.rect(xx,y,cell,h,colors[s],MUTED,.8,1)
        if s=='f':
            for z in range(-int(h),int(cell),6):
                a=max(0,z); b=min(cell,z+h)
                if b>a:
                    d.line([(xx+a,y+h-(a-z)),(xx+b,y+h-(b-z))],LINE,.7)
        elif s=='n':
            for j in range(4):
                d.ellipse(xx+3+(j*5)%max(4,int(cell-4)),y+4+(j*7)%int(h-6),1,1,PURPLE)


def car(d,x,y,scale=1,complete=False,turn=False):
    """The same canonical identity; color means evidence state, not asset class."""
    pts=[(-39,7),(-25,-10),(17,-14),(38,-1),(38,16),(-29,23),(-39,17)]
    def tr(p):
        a,b=p
        if turn:
            a,b=.9*a-.3*b,.3*a+.9*b
        return x+scale*a,y+scale*b
    d.poly([tr(p) for p in pts],'#EEF4F8',MUTED,1)
    d.poly([tr(p) for p in [(-24,-9),(-10,-22),(11,-23),(24,-12),(17,-7)]],'#EEF4F8',MUTED,1)
    d.poly([tr(p) for p in [(-8,-20),(9,-21),(19,-12),(-10,-10)]],'#D8E8F4',BLUE,.8)
    for a,b in [(-23,19),(25,11)]:
        xx,yy=tr((a,b)); d.ellipse(xx,yy,6*scale,8*scale,INK)
    rng=random.Random(19)
    for j in range(65):
        a=rng.uniform(-33,33); b=rng.uniform(-5,15)
        xx,yy=tr((a,b)); col=BLUE if a<3 else ORANGE if complete else GRAY
        d.ellipse(xx,yy,2.1*scale,1.4*scale,col)


def human(d,x,y,scale=1,complete=False,pose=False):
    # Root/binding remains; only joint pose differs in the reuse illustration.
    nodes=[(0,-32),(0,-19),(-13,-8),(13,-8),(-17,10),(17,10),(0,0),(-8,23),(8,23),(-12,43),(13,43)]
    if pose:
        nodes[2]=(-12,-25); nodes[4]=(-24,-34); nodes[7]=(-14,20); nodes[9]=(-24,36)
    bones=[(0,1),(1,2),(2,4),(1,3),(3,5),(1,6),(6,7),(7,9),(6,8),(8,10)]
    for a,b in bones:
        ax,ay=nodes[a]; bx,by=nodes[b]
        for j in range(7):
            t=j/6; xx=ax*(1-t)+bx*t; yy=ay*(1-t)+by*t
            col=BLUE if xx<=0 else ORANGE if complete else GRAY
            d.ellipse(x+scale*xx,y+scale*yy,4.5*scale,4.8*scale,col)
        d.line([(x+scale*ax,y+scale*ay),(x+scale*bx,y+scale*by)],INK,.7)
    d.ellipse(x,y-42*scale,8*scale,10*scale,BLUE)
    for xx,yy in nodes:
        d.ellipse(x+xx*scale,y+yy*scale,1.8*scale,1.8*scale,'#FFFFFF',INK,.5)


def ground(d,x,y,w=85,h=40,complete=False):
    corners=[(x-w/2,y),(x,y-h/2),(x+w/2,y),(x,y+h/2)]
    d.poly(corners,'#F4F7F9',LINE,.8)
    for t in [.25,.5,.75]:
        d.line([(x-w/2+w*t/2,y-h*t/2),(x+w*t/2,y+h/2-h*t/2)],LINE,.6)
        d.line([(x-w/2+w*t/2,y+h*t/2),(x+w*t/2,y-h/2+h*t/2)],LINE,.6)
    rng=random.Random(7)
    for i in range(55):
        u=rng.uniform(-1,1); v=rng.uniform(-1,1)
        xx=x+(u-v)*w/4; yy=y+(u+v)*h/4
        col=BLUE if u<.25 else ORANGE if complete else GRAY
        d.ellipse(xx,yy,1.8,1,col)


def world(d,x,y,scale=1,kind=None):
    ground(d,x,y,158*scale,56*scale,True)
    # Repeated background and actor marks preserve identity across state branches.
    d.poly([(x-60*scale,y-12*scale),(x-60*scale,y-47*scale),(x-41*scale,y-54*scale),(x-24*scale,y-43*scale),(x-24*scale,y-1*scale)],'#E2EEF7',BLUE,.7)
    for j in range(4):
        d.line([(x-56*scale,y-(20+7*j)*scale),(x-44*scale,y-(25+7*j)*scale)],BLUE,.8)
    car(d,x+(12 if kind=='vehicle' else -3)*scale,y-1*scale,.59*scale,True,kind=='vehicle')
    human(d,x+47*scale,y-15*scale,.40*scale,True,kind=='human')
    # Camera frustum distinguishes a changed view from a changed asset state.
    cx=x+(-63 if kind=='camera' else -45)*scale
    cy=y+(28 if kind=='camera' else 38)*scale
    d.poly([(cx,cy),(cx+11*scale,cy-17*scale),(cx+22*scale,cy-5*scale)],None,MUTED,.9)
    d.rect(cx-5*scale,cy-1*scale,8*scale,6*scale,'#FFFFFF',MUTED,.8)


def draw(path,hidden=()):
    d=Drawing(path,hidden)
    # Large-scale grouping: plain left/right fields, one tinted scientific core.
    d.rect(338,45,480,433,'#F7F4FB',None,r=8)
    d.line([(325,45),(325,473)],'#D4DBE2',.8)
    d.line([(830,45),(830,473)],'#D4DBE2',.8)
    for x,title in [(8,'(a) Canonical evidence'),(348,'(b) Joint completion'),(846,'(c) Decode and check')]:
        d.text(x,28,title,25,True,role='title')
    d.text(12,554,'Offline construction',20,True,MUTED)

    # A: a compact recovery path, a three-type canonical support, and latent encoding.
    d.rect(15,59,127,85,'#F2F5F7',LINE)
    d.rect(21,53,127,85,'#F2F5F7',LINE)
    d.image(OUT/'overview-assets/input-street-schematic.png',27,47,127,85)
    d.rect(27,47,127,85,None,LINE,.8)
    d.label(172,77,['Calibrated','driving log'],21,True,anchor='start')
    d.text(172,126,'Views · time',20,color=MUTED)
    d.line([(91,146),(91,158),(161,158),(161,174)],arrow=True)
    d.op(18,174,288,41,'Shared visual encoder',fill='#F3F8FC')
    d.text(162,242,'Features · geometry · tracks',20,anchor='middle')
    d.line([(162,215),(162,222)],arrow=True)
    d.line([(162,249),(162,262)],arrow=True)
    d.op(18,262,288,42,'Motion-aware aggregation',fill='#F3F8FC')
    d.line([(162,304),(162,318)],arrow=True)
    ground(d,58,352,86,41,False)
    car(d,160,350,.88,False)
    human(d,266,350,.63,False)
    d.label(58,397,['BG + sky','World'],20)
    d.label(160,397,['Vehicle i','Local'],20)
    d.label(266,397,['Human j','Rest pose'],20)
    d.line([(58,425),(58,437),(266,437),(266,425)],color=LINE,lw=1)
    d.line([(160,437),(160,447)],arrow=True)
    d.op(47,447,226,35,'Typed encoders',size=20)
    tokens(d,57,505,'oouuf',17,21)
    d.text(174,522,'zobs + slots',20)
    d.line([(298,516),(332,516),(332,240),(354,240)],arrow=True)
    d.line([(160,482),(160,495)],arrow=True)

    # B: evidence conditions, local groups, read/write memory and an explicit sampler.
    d.label(355,72,['Canonical + reference','world coordinates'],20,anchor='start')
    d.label(701,72,['Pooled log','features'],20)
    d.line([(701,101),(701,127)],PURPLE,1.2,True)
    d.line([(373,103),(348,103),(348,197),(369,197)],MUTED,1.1,True)
    d.op(391,127,388,39,'Shared memory: read / write',fill='#EBE3F4',stroke=PURPLE,size=22)
    d.rect(355,199,446,95,None,'#B7A4CF',.9,3)
    groups=[(367,'BG regions'),(518,'Vehicle i'),(669,'Human j')]
    for x,label in groups:
        d.text(x+58,215,label,20,True,anchor='middle')
        tokens(d,x+5,229,'oouuf',18,24,3)
        d.line([(x+40,197),(x+40,166)],PURPLE,1.3,True)
        d.line([(x+74,166),(x+74,197)],PURPLE,1.3,True)
    d.text(585,286,'Local attention within each group',20,anchor='middle')
    d.line([(425,262),(425,298),(727,298),(727,262)],MUTED,1.2)
    d.line([(576,298),(576,316)],arrow=True)
    # Sampler is a bounded repeat; the output is decoded after the final projection.
    d.op(359,320,204,51,['Flow step','unknown codes only'],fill='#FFFFFF',stroke=PURPLE,size=20)
    d.op(594,320,204,51,['Restore observed','Clear free'],fill='#FFFFFF',stroke=BLUE,size=20)
    d.line([(576,316),(576,311),(461,311),(461,320)],arrow=True)
    d.line([(563,345),(594,345)],arrow=True)
    d.line([(798,345),(807,345),(807,307),(352,307),(352,229),(367,229)],PURPLE,1,True,dash=True)
    d.text(583,397,'Every integration step',20,True,anchor='middle')
    tokens(d,362,420,'oonnf',18,23,3)
    d.line([(470,431),(505,431)],arrow=True)
    tokens(d,515,420,'oongf',18,23,3)
    d.line([(623,431),(658,431)],arrow=True)
    tokens(d,668,420,'ooggf',18,23,3)
    d.text(581,467,'Noise → completed unknown codes',20,anchor='middle')
    # The completed-code output leaves the composite only after projection.
    d.line([(776,432),(822,432),(822,113),(849,113)],arrow=True)

    # C: shared typed decode, candidate and observed-only reference, original-state gate.
    d.op(849,91,337,43,'Typed Gaussian decoders',size=21)
    d.text(1017,70,'Free-space opacity = 0',20,anchor='middle')
    ground(d,900,168,75,32,True)
    car(d,1007,166,.72,True)
    human(d,1118,167,.47,True)
    d.text(900,202,'BG + sky',20,anchor='middle')
    d.text(1007,202,'Vehicle',20,anchor='middle')
    d.text(1118,202,'Human',20,anchor='middle')
    for x in [900,1007,1118]:
        d.line([(x,134),(x,145)],MUTED,1,True)
    # Reference is decoded from the same observed codes using the same codec.
    tokens(d,856,225,'oo',16,19,3)
    d.text(900,241,'zobs',20)
    d.text(955,241,'same codec',20,color=MUTED)
    d.line([(875,249),(875,260)],MUTED,1.1,True)
    d.op(847,260,161,51,['Observed-only','reference'],size=20)
    d.op(1027,260,160,51,['Completed','candidate'],size=20)
    d.line([(900,209),(900,216),(1118,216),(1118,209)],MUTED,1.1)
    d.line([(1007,209),(1007,216)],MUTED,1.1)
    d.line([(1107,216),(1107,260)],arrow=True)
    d.line([(928,311),(928,327),(1015,327),(1015,340)],arrow=True)
    d.line([(1107,311),(1107,340)],arrow=True)
    d.op(970,340,217,53,['Render & compare','at recorded states'],fill='#F5F8FA',size=20)
    d.rect(850,339,83,55,'#FFFFFF',LINE)
    d.image(OUT/'overview-assets/input-street-schematic.png',851,340,81,54)
    d.line([(933,366),(970,366)],MUTED,1.1,True)
    d.label(892,418,['Recorded','views'],20,color=MUTED)
    d.line([(1077,393),(1077,410)],arrow=True)
    d.text(1123,414,'pass',20,color=MUTED)
    d.line([(970,381),(955,381),(955,463)],MUTED,1.1)
    d.line([(949,463),(961,463)],MUTED,1.2)
    d.text(951,487,'reject',20,color=MUTED,anchor='middle')
    world(d,1084,457,.84)
    d.text(1085,503,'Fixed world W',22,True,anchor='middle')

    # D: a shared immutable world branches into clearly different external states.
    d.line([(346,520),(1055,520)],LINE,1,dash=True)
    d.text(348,554,'(d) State-driven reuse',25,True,role='title')
    d.text(1187,554,'Same W · different states',21,True,anchor='end')
    d.text(349,593,'Camera / actor states',20)
    d.line([(545,587),(583,587)],arrow=True)
    d.op(583,566,230,42,'Compose & render',fill='#F3F8FC',size=21)
    d.line([(1085,512),(1085,526),(1194,526),(1194,587),(813,587)],arrow=True)
    # Three output views of the SAME content, under different supplied states.
    d.line([(698,608),(698,620)],MUTED,1.2)
    d.line([(457,620),(1060,620)],MUTED,1.2)
    for x,k,label in [(457,'camera','New camera'),(758,'vehicle','Vehicle SE(3)'),(1060,'human','Human joints')]:
        d.line([(x,620),(x,632)],MUTED,1.2,True)
        d.rect(x-99,634,198,63,'#FFFFFF','#D3DCE3',.8,2)
        world(d,x,676,.70,k)
        d.text(x,723,label,21,True,anchor='middle')
    d.text(345,650,'',20)
    # Compact semantic legend: evidence state is never used for asset type.
    d.text(12,600,'Evidence state',21,True)
    for x,y,s,label in [(12,619,'o','Observed'),(170,619,'u','Unknown'),(12,668,'g','Generated'),(170,668,'f','Free')]:
        tokens(d,x,y,s,19,23)
        d.text(x+28,y+19,label,20)
    bounds=d.finish()
    return bounds


if __name__=='__main__':
    OUT.mkdir(exist_ok=True,parents=True)
    ARCHIVE.mkdir(exist_ok=True,parents=True)
    name=OUT/'drivecompose-overview-20261023'
    bounds=draw(name)
    draw(ARCHIVE/'title-hidden',('title',))
    draw(ARCHIVE/'title-and-detail-hidden',('title','detail'))
    audit={'canvas':[W,H],'publication_width_pt':495,'minimum_font_pt':min(t['font_pt'] for t in bounds),
           'out_of_canvas_text':[t for t in bounds if t['x']<0 or t['x']+t['w']>W or t['y']>H],
           'text':bounds,'evidence':'schematic only; generated input image, deterministic vector spatial motifs'}
    (ARCHIVE/'vector-audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in audit.items() if k!='text'}))
