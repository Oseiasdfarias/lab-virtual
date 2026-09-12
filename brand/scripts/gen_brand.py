#!/usr/bin/env python3
"""Gera o pacote de marca do Laboratorio Virtual (SVG + PNG).

GEOMETRIA: copia exata da opcao 1 ("Subida") aprovada no preview, normalizada para
L_ARM = 100. Nao alterar sem pedido explicito -- foi o desenho validado.

Preview original (viewBox 120, pivo em 38,24):
  repouso  (38,24)->(38,80)          largura 2.0  tracejado 4 4  opacidade 0.30
  arco     r=26, de 8deg a 44deg     largura 2.5                 opacidade 0.70
  seta     0,-3.6 8,0 0,3.6          rotate(-46)                 opacidade 0.70
  haste    (38,24)->(80.9,60)        largura 5.0  ponta redonda
  motor    (80.9,60)->(91.2,47.7)    largura 9.0  ponta redonda
  helice   (78.9,37.4)->(103.5,58)   largura 4.0  ponta redonda
  pivo     circulo r=6

Fisica: a helice levanta a haste a partir do repouso (vertical). O motor sai
perpendicular a haste e a helice fica paralela a ela (empuxo perpendicular = torque).
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from text2path import text_to_path

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "/usr/share/fonts/truetype/ibm-plex/IBMPlexSans-SemiBold.ttf"

INK = "#1D1D1F"        # cor do preview (--text-primary, tema claro)
PAPER = "#F5F5F7"      # cor do preview (--text-primary, tema escuro)
LEGACY_CORAL = "#FF5757"

K = 100.0 / 56.0       # preview: haste media 56 unidades -> normaliza para 100

# ---------------------------------------------------- geometria (do preview)
THETA = 50.0
L_ARM = 100.0
L_MOTOR = 16.0 * K
L_PROP = 16.0 * K
R_ARC = 26.0 * K
L_REST = 56.0 * K
TH_A, TH_B = 8.0, 44.0

W_ARM = 5.0 * K
W_MOTOR = 9.0 * K
W_PROP = 4.0 * K
R_PIVOT = 6.0 * K
W_ARC = 2.5 * K
W_REST = 2.0 * K
DASH = 4.0 * K
ARROW_L, ARROW_H = 8.0 * K, 3.6 * K

OP_REST, OP_ARC = 0.30, 0.70


def rad(d):
    return math.radians(d)


def blend(fg, bg, alpha):
    """Cor solida equivalente a 'fg' com opacidade 'alpha' sobre 'bg'.

    Usada no arco e na seta: eles ficam POR CIMA da haste, e com opacidade real
    sobre o preto da haste virariam cinza-escuro ilegivel.
    """
    f = [int(fg[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(bg[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02X%02X%02X" % tuple(round(f[i] * alpha + b[i] * (1 - alpha)) for i in range(3))


def geometry(l_arm):
    f = l_arm / L_ARM
    u = (math.sin(rad(THETA)), math.cos(rad(THETA)))
    v = (math.cos(rad(THETA)), -math.sin(rad(THETA)))
    A = (l_arm * u[0], l_arm * u[1])
    M = (A[0] + L_MOTOR * f * v[0], A[1] + L_MOTOR * f * v[1])
    P1 = (M[0] + L_PROP * f * u[0], M[1] + L_PROP * f * u[1])
    P2 = (M[0] - L_PROP * f * u[0], M[1] - L_PROP * f * u[1])
    return u, v, A, M, P1, P2


def arc_pt(r, a):
    return (r * math.sin(rad(a)), r * math.cos(rad(a)))


def bbox(items):
    xs, ys = [], []
    for (x, y), rr in items:
        xs += [x - rr, x + rr]
        ys += [y - rr, y + rr]
    return min(xs), min(ys), max(xs), max(ys)


def icon_parts(full=True, l_arm=L_ARM, weight=1.0, c_rest=None, c_arc=None):
    u, v, A, M, P1, P2 = geometry(l_arm)
    f = l_arm / L_ARM
    wa, wm, wp = W_ARM * f * weight, W_MOTOR * f * weight, W_PROP * f * weight
    rp = R_PIVOT * f * weight
    r_arc, l_rest = R_ARC * f, L_REST * f
    w_arc, w_rest, dash = W_ARC * f, W_REST * f, DASH * f
    al, ah = ARROW_L * f, ARROW_H * f

    pts = [((0, 0), rp), (A, wa / 2), (M, wm / 2), (P1, wp / 2), (P2, wp / 2)]
    if full:
        pts.append(((0, l_rest), w_rest / 2))
        pts += [(arc_pt(r_arc, a), w_arc / 2 + al * 0.5)
                for a in (TH_A, (TH_A + TH_B) / 2, TH_B)]
    bb = bbox(pts)

    def elements(T, ox, oy, c, inflate=0.0, opaque=False):
        """Ordem de empilhamento: repouso, haste, motor, helice, pivo, arco, seta.
        O arco e a seta ficam por ULTIMO para nao serem cortados pela haste."""
        # com cor solida (c_rest/c_arc) nao precisa de opacidade; sem ela
        # (variante currentColor) cai de volta na opacidade do preview
        cr = c if opaque or not c_rest else c_rest
        ca = c if opaque or not c_arc else c_arc
        op_r = 1.0 if (opaque or c_rest) else OP_REST
        op_a = 1.0 if (opaque or c_arc) else OP_ARC
        s = []
        if full:
            s.append(f'<line x1="{ox:.2f}" y1="{oy:.2f}" x2="{ox:.2f}" y2="{oy + l_rest:.2f}" '
                     f'stroke="{cr}" stroke-width="{w_rest + inflate:.2f}" '
                     f'stroke-dasharray="{dash:.2f} {dash:.2f}" stroke-linecap="butt" '
                     f'opacity="{op_r}"/>')
        s.append(f'<line x1="{ox:.2f}" y1="{oy:.2f}" x2="{T(A)[0]:.2f}" y2="{T(A)[1]:.2f}" '
                 f'stroke="{c}" stroke-width="{wa + inflate:.2f}" stroke-linecap="round"/>')
        s.append(f'<line x1="{T(A)[0]:.2f}" y1="{T(A)[1]:.2f}" x2="{T(M)[0]:.2f}" '
                 f'y2="{T(M)[1]:.2f}" stroke="{c}" stroke-width="{wm + inflate:.2f}" '
                 f'stroke-linecap="round"/>')
        s.append(f'<line x1="{T(P2)[0]:.2f}" y1="{T(P2)[1]:.2f}" x2="{T(P1)[0]:.2f}" '
                 f'y2="{T(P1)[1]:.2f}" stroke="{c}" stroke-width="{wp + inflate:.2f}" '
                 f'stroke-linecap="round"/>')
        s.append(f'<circle cx="{ox:.2f}" cy="{oy:.2f}" r="{rp + inflate / 2:.2f}" fill="{c}"/>')
        if full:
            a0, a1 = arc_pt(r_arc, TH_A), arc_pt(r_arc, TH_B)
            s.append(f'<path d="M {T(a0)[0]:.2f} {T(a0)[1]:.2f} A {r_arc:.2f} {r_arc:.2f} '
                     f'0 0 0 {T(a1)[0]:.2f} {T(a1)[1]:.2f}" fill="none" stroke="{ca}" '
                     f'stroke-width="{w_arc + inflate:.2f}" stroke-linecap="round" '
                     f'opacity="{op_a}"/>')
            s.append(f'<polygon points="0,{-ah:.2f} {al:.2f},0 0,{ah:.2f}" fill="{ca}" '
                     f'opacity="{op_a}" stroke="{ca}" stroke-width="{inflate:.2f}" '
                     f'stroke-linejoin="round" transform="translate({T(a1)[0]:.2f} '
                     f'{T(a1)[1]:.2f}) rotate({TH_B - 90:.2f})"/>')
        return s

    def render(ox, oy, c, outline=None, ob=0.0):
        def T(p):
            return (p[0] + ox, p[1] + oy)
        fills = elements(T, ox, oy, c)
        if not outline:
            return "\n  ".join(fills)
        # intercala contorno+preenchimento por elemento, para cada peca manter
        # a borda visivel sobre as anteriores
        outs = elements(T, ox, oy, outline, inflate=2 * ob, opaque=True)
        return "\n  ".join(x for pair in zip(outs, fills) for x in pair)

    return render, bb


def aux_colors(c, bg_ref=None):
    """Cores solidas do repouso e do arco. None para currentColor (mantem opacidade)."""
    if c == "currentColor":
        return None, None
    bg_ref = bg_ref or ("#1D1D1F" if c == PAPER else "#FFFFFF")
    return blend(c, bg_ref, OP_REST), blend(c, bg_ref, OP_ARC)


def wrap(body, vw, vh, bg=None):
    rect = f'<rect width="{vw:.2f}" height="{vh:.2f}" fill="{bg}"/>\n  ' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw:.2f} {vh:.2f}" '
            f'width="{vw:.0f}" height="{vh:.0f}" role="img" '
            f'aria-label="Laboratório Virtual">\n  {rect}{body}\n</svg>\n')


def svg_icon(full=True, pad=16, c=INK, l_arm=L_ARM, weight=1.0, bg=None, outline=None,
             bg_ref=None):
    cr, ca = aux_colors(c, bg_ref)
    render, (x0, y0, x1, y1) = icon_parts(full, l_arm, weight, cr, ca)
    ob = (W_ARM * 0.42 * l_arm / L_ARM * weight) if outline else 0.0
    x0, y0, x1, y1 = x0 - ob, y0 - ob, x1 + ob, y1 + ob
    w, h = x1 - x0, y1 - y0
    side = max(w, h) + 2 * pad
    ox, oy = -x0 + (side - w) / 2, -y0 + (side - h) / 2
    return wrap(render(ox, oy, c, outline, ob), side, side, bg), side, side


def svg_lockup(vertical=False, c=INK, bg=None, outline=None, bg_ref=None):
    cr, ca = aux_colors(c, bg_ref)
    render, (x0, y0, x1, y1) = icon_parts(full=True, c_rest=cr, c_arc=ca)
    ob = W_ARM * 0.42 if outline else 0.0
    x0, y0, x1, y1 = x0 - ob, y0 - ob, x1 + ob, y1 + ob
    iw, ih = x1 - x0, y1 - y0
    pad = 18.0

    def txt(d, tx, ty, fs):
        out = ""
        if outline:
            # contorno do texto e proporcional ao CORPO da fonte (~5%), nao a
            # espessura da haste -- senao as letras ficam estufadas
            tob = fs * 0.05
            out = (f'\n  <path d="{d}" fill="{outline}" stroke="{outline}" '
                   f'stroke-width="{tob:.2f}" stroke-linejoin="round" '
                   f'transform="translate({tx:.2f} {ty:.2f})"/>')
        return out + (f'\n  <path d="{d}" fill="{c}" '
                      f'transform="translate({tx:.2f} {ty:.2f})"/>')

    if not vertical:
        fs, gap = 62.0, 34.0
        d, tw, _, _, cap = text_to_path(FONT, "Laboratório Virtual", fs)
        vh = max(ih, cap) + 2 * pad
        vw = iw + gap + tw + 2 * pad
        body = render(pad - x0, (vh - ih) / 2 - y0, c, outline, ob)
        body += txt(d, pad + iw + gap, vh / 2 + cap / 2, fs)
    else:
        fs, gap = 54.0, 30.0
        d1, tw1, _, _, cap = text_to_path(FONT, "Laboratório", fs)
        d2, tw2, _, _, _ = text_to_path(FONT, "Virtual", fs)
        lh = fs * 1.12
        vw = max(iw, max(tw1, tw2)) + 2 * pad
        vh = ih + gap + cap + lh + 2 * pad
        body = render((vw - iw) / 2 - x0, pad - y0, c, outline, ob)
        base = pad + ih + gap + cap
        body += txt(d1, (vw - tw1) / 2, base, fs)
        body += txt(d2, (vw - tw2) / 2, base + lh, fs)

    return wrap(body, vw, vh, bg), vw, vh


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ->", os.path.relpath(path, OUT))


def main():
    """PADRAO = versao com contorno (preenchimento claro + contorno escuro).

    Ela funciona sobre qualquer fundo, entao dispensa manter uma variante por tema.
    As versoes solidas ficam como alternativa para impressao em 1 cor e tamanhos
    muito pequenos, onde o contorno empasta.
    """
    print("SVG (padrao = com contorno):")
    write(f"{OUT}/svg/icone.svg", svg_icon(c=PAPER, outline=INK)[0])
    write(f"{OUT}/svg/icone-reduzido.svg",
          svg_icon(full=False, pad=14, c=PAPER, outline=INK)[0])
    write(f"{OUT}/svg/logo-horizontal.svg", svg_lockup(c=PAPER, outline=INK)[0])
    write(f"{OUT}/svg/logo-vertical.svg", svg_lockup(vertical=True, c=PAPER, outline=INK)[0])

    print("SVG (alternativas solidas):")
    write(f"{OUT}/svg/icone-solido.svg", svg_icon()[0])
    write(f"{OUT}/svg/icone-solido-branco.svg", svg_icon(c=PAPER)[0])
    write(f"{OUT}/svg/icone-mono.svg", svg_icon(c="currentColor")[0])
    write(f"{OUT}/svg/logo-horizontal-solido.svg", svg_lockup()[0])
    write(f"{OUT}/svg/logo-horizontal-mono.svg", svg_lockup(c="currentColor")[0])
    write(f"{OUT}/svg/logo-vertical-solido.svg", svg_lockup(vertical=True)[0])
    write(f"{OUT}/svg/icone-coral.svg", svg_icon(c=LEGACY_CORAL)[0])

    # favicon: solido de proposito -- abaixo de ~32px o contorno fecha os vaos
    print("SVG (favicon):")
    write(f"{OUT}/svg/favicon.svg", svg_icon(full=False, pad=8, weight=1.35)[0])
    write(f"{OUT}/svg/favicon-branco.svg",
          svg_icon(full=False, pad=8, weight=1.35, c=PAPER)[0])
    write(f"{OUT}/svg/favicon-contorno.svg",
          svg_icon(full=False, pad=8, weight=1.35, c=PAPER, outline=INK)[0])


if __name__ == "__main__":
    main()
