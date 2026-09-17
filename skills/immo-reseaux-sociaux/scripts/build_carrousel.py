#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur de carrousel et de visuel d'information — immo-reseaux-sociaux.

Texte validé (contenu.json) + identité de l'agent (00_MOI/cadre.md) → fichiers finaux contrôlés :
un PDF 1080 × 1350 pour LinkedIn, une image PNG par diapo pour Instagram et Facebook, et, dans
controle/, la planche contact, la vignette de couverture et le rapport.

Usage :  python3 build_carrousel.py contenu.json DOSSIER_DE_SORTIE [--cadre 00_MOI/cadre.md] [--racine .]
Sortie : lignes OK / MESURE / ATTENTION / BLOQUANT, puis code 0 (rien), 1 (attentions), 2 (bloquant).
Au moindre BLOQUANT, rien de publiable n'est écrit : seul controle/rapport.txt l'est.

Dépendances : Python 3, reportlab et Pillow ; pypdf pour relire le PDF produit (facultatif).
Police : Liberation Sans 2.1.5, SIL Open Font License 1.1, livrée dans assets/polices/.

Il ne décide rien du fond : ni le sujet, ni les mots, ni la source d'un chiffre. Il refuse ce qui
enfreint les règles dures, et il mesure ce qu'il fabrique.
"""
import sys, os, re, json, argparse, unicodedata, pathlib, tempfile

ICI = pathlib.Path(__file__).resolve().parent
POLICES = ICI.parent / "assets" / "polices"
FICHIERS_POLICE = {"reg": POLICES / "LiberationSans-Regular.ttf", "bold": POLICES / "LiberationSans-Bold.ttf"}

NEUTRE = {"dominante": "#14213D", "accent": "#7A2E3B"}
GRIS, TRAIT, BLANC, FOND_PLANCHE = "#5A6678", "#A8B2C0", "#FFFFFF", "#D7DCE3"
INTERLIGNE, ASCENDANT, DESCENDANT = 1.2, 0.905, 0.212          # métriques de Liberation Sans
CORPS_MIN, CORPS_CIBLE = 34, 40                                  # jamais sous 34 px, 40 visés
MX = 90                                                          # marge latérale, en pixels
TYPES = {"couverture", "idee", "etape", "chiffre", "colonnes", "liste", "citation", "photo", "avant_apres", "action"}
CHAMPS = {"couverture": ["titre"], "idee": ["titre"], "etape": ["titre"], "chiffre": ["valeur", "legende", "source"],
          "colonnes": ["gauche_titre", "droite_titre", "lignes"], "liste": ["titre", "elements"],
          "citation": ["texte", "auteur"], "photo": ["fichier", "legende"], "avant_apres": ["avant", "apres", "legende"],
          "action": ["texte"]}
ZONES = {  # tête (ligne de base, jauge), boîte de contenu, pied (filet, ligne de base), zone sûre
    "portrait": {"W": 1080, "H": 1350, "tete": 170, "jauge": 158, "haut": 230, "bas": 990, "filet": 1030, "pied": 1078, "sure": (120, 1100)},
    "carre":    {"W": 1080, "H": 1080, "tete": None, "jauge": None, "haut": 130, "bas": 880, "filet": 940, "pied": 990, "sure": (90, 1000)},
}

OK, MESURES, ATT, BLO = [], [], [], []


def sortir(dossier_controle):
    lignes = ([f"OK        {m}" for m in OK] + [f"MESURE    {m}" for m in MESURES] +
              [f"ATTENTION {m}" for m in ATT] + [f"BLOQUANT  {m}" for m in BLO])
    if dossier_controle:
        dossier_controle.mkdir(parents=True, exist_ok=True)
        (dossier_controle / "rapport.txt").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("\n".join(lignes))
    sys.exit(2 if BLO else (1 if ATT else 0))


try:
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.colors import HexColor
    from PIL import Image, ImageDraw, ImageFont
except ImportError as e:
    BLO.append(f"dépendance absente ({e.name}) : installe reportlab et Pillow si l'environnement le permet ; "
               "sinon, gabarit HTML de secours assets/diapos.template.html")
    sortir(None)


# ── Couleurs ────────────────────────────────────────────────────────
def hexa(c):
    c = c.strip()
    if re.fullmatch(r"#[0-9A-Fa-f]{3}", c):
        c = "#" + "".join(ch * 2 for ch in c[1:])
    return c.upper() if re.fullmatch(r"#[0-9A-Fa-f]{6}", c) else None


def luminance(c):
    def canal(v):
        v = v / 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(c[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)


def contraste(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def rgb(c, alpha=None):
    t = tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))
    return t + (round(alpha * 255),) if alpha is not None else t


# ── Identité : contenu.json, sinon 00_MOI/cadre.md, sinon neutre ─────
def identite_cadre(chemin):
    ident = {}
    if not chemin or not os.path.exists(chemin):
        return ident
    for l in open(chemin, encoding="utf-8"):
        bas = l.lower()
        couleur = re.search(r"#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})\b", l)
        if "couleur dominante" in bas and couleur:
            ident["dominante"] = hexa(couleur.group(0))
        elif re.search(r"couleur d['’]accent", bas) and couleur:
            ident["accent"] = hexa(couleur.group(0))
        elif "bloc de signature" in bas and " : " in l:
            v = l.rsplit(" : ", 1)[1].strip()
            if v and "[" not in v and not v.endswith(":"):
                ident["signature"] = v
        elif "mon logo" in bas:
            m = re.search(r"`([^`]+\.(?:png|jpe?g))`", l, re.I)
            if m:
                ident["logo"] = m.group(1)
    return ident


def theme(contenu, cadre):
    ident = dict(NEUTRE)
    source = "neutre"
    lu = identite_cadre(cadre)
    if lu.get("dominante") and lu.get("accent"):
        ident.update({k: lu[k] for k in ("dominante", "accent")}); source = "cadre.md"
    ident["signature"] = lu.get("signature", "")
    ident["logo"] = lu.get("logo")
    impose = contenu.get("identite") or {}
    for k in ("dominante", "accent"):
        if impose.get(k) and hexa(impose[k]):
            ident[k] = hexa(impose[k]); source = "contenu.json"
    if impose.get("signature"):
        ident["signature"] = impose["signature"].strip()
    if source == "neutre":
        ATT.append("identité à confirmer : couleurs neutres de la mallette, pas les siennes — remarque de rang 7 de livrer.md")
    else:
        OK.append(f"identité lue dans {source} : dominante {ident['dominante']}, accent {ident['accent']}")
    if not ident["signature"]:
        ATT.append("bloc de signature à confirmer : pied des diapos sans nom ni commune")
    # Lisibilité : texte courant sur blanc, blanc sur la dominante (≥ 4,5) ; accent en grand (≥ 3)
    if contraste(ident["dominante"], BLANC) < 4.5:
        ATT.append(f"dominante {ident['dominante']} trop claire (contraste {contraste(ident['dominante'], BLANC):.1f} < 4,5) : dominante neutre utilisée")
        ident["dominante"] = NEUTRE["dominante"]
    if contraste(ident["accent"], BLANC) < 3:
        ATT.append(f"accent {ident['accent']} trop clair (contraste {contraste(ident['accent'], BLANC):.1f} < 3) : la dominante le remplace")
        ident["accent"] = ident["dominante"]
    ident["fond_action"] = ident["accent"] if contraste(ident["accent"], BLANC) >= 4.5 else ident["dominante"]
    MESURES.append(f"contraste texte sur blanc {contraste(ident['dominante'], BLANC):.1f} · blanc sur fond d'action {contraste(ident['fond_action'], BLANC):.1f}")
    return ident


# ── Texte : mesure, coupe, ajustement ───────────────────────────────
def enregistrer_polices():
    for nom, chemin in FICHIERS_POLICE.items():
        if not chemin.exists():
            BLO.append(f"police absente : {chemin}")
            return False
        pdfmetrics.registerFont(TTFont(f"Liberation-{nom}", str(chemin)))
    return True


def largeur(txt, police, taille):
    return pdfmetrics.stringWidth(txt, f"Liberation-{police}", taille)


ESPACE_INSECABLE = "\u00a0"


def typographie(txt):
    """Espaces insécables du français : un guillemet ou une ponctuation haute ne reste jamais seul en bout de ligne."""
    txt = re.sub(r"«\s+", "«" + ESPACE_INSECABLE, txt)
    txt = re.sub(r"\s+([»?!:;])", ESPACE_INSECABLE + r"\1", txt)
    return txt


def couper(txt, police, taille, lmax):
    lignes, cour = [], ""
    for mot in re.split(r"[ \t\n]+", typographie(txt).strip()):
        essai = f"{cour} {mot}".strip()
        if largeur(essai, police, taille) <= lmax:
            cour = essai
        else:
            if largeur(mot, police, taille) > lmax:
                return None
            if cour:
                lignes.append(cour)
            cour = mot
    if cour:
        lignes.append(cour)
    return lignes


def ajuster(txt, police, tmax, tmin, lmax, hmax, lignes_max=None):
    tailles = list(range(tmax, tmin, -2)) + [tmin]
    for t in tailles:
        l = couper(txt, police, t, lmax)
        if l and len(l) * t * INTERLIGNE <= hmax and (lignes_max is None or len(l) <= lignes_max):
            return t, l
    return None, None


class Texte:
    def __init__(self, lignes, police, taille, couleur, x, y0, align="left", courant=False):
        self.lignes, self.police, self.taille, self.couleur = lignes, police, taille, couleur
        self.x, self.align, self.courant = x, align, courant
        self.ys = [y0 + i * taille * INTERLIGNE for i in range(len(lignes))]

    def haut(self):
        return self.ys[0] - self.taille * ASCENDANT

    def bas(self):
        return self.ys[-1] + self.taille * DESCENDANT


class Rect:
    def __init__(self, x, y, w, h, couleur, alpha=1.0):
        self.x, self.y, self.w, self.h, self.couleur, self.alpha = x, y, w, h, couleur, alpha


class Filet:
    def __init__(self, x1, y1, x2, y2, epaisseur, couleur, alpha=1.0):
        self.x1, self.y1, self.x2, self.y2, self.epaisseur, self.couleur, self.alpha = x1, y1, x2, y2, epaisseur, couleur, alpha


class Photo:
    def __init__(self, chemin, x, y, w, h):
        self.chemin, self.x, self.y, self.w, self.h = chemin, x, y, w, h


def empiler(groupes, haut, bas, ecart=36):
    """groupes : (lignes, police, taille, couleur, align, courant, x). Centre le bloc verticalement."""
    total = sum(len(g[0]) * g[2] * INTERLIGNE for g in groupes) + ecart * (len(groupes) - 1)
    y = haut + max(0, (bas - haut - total) / 2)
    sortie = []
    for lignes, police, taille, couleur, align, courant, x in groupes:
        sortie.append(Texte(lignes, police, taille, couleur, x, y + taille * 0.95, align, courant))
        y += len(lignes) * taille * INTERLIGNE + ecart
    return sortie


# ── Composition, diapo par diapo ────────────────────────────────────
def champ(d, k):
    v = d.get(k, "")
    return v.strip() if isinstance(v, str) else v


def composer(d, rang, total, z, ident, carrousel, racine, tmp):
    W, H, L = z["W"], z["H"], z["W"] - 2 * MX
    t = d["type"]
    source_libre = champ(d, "source") if t in ("idee", "etape", "colonnes", "liste", "citation") else ""
    if source_libre:
        z = dict(z, bas=z["bas"] - 100)
    sombre = t in ("couverture", "action")
    fond = ident["dominante"] if t == "couverture" else (ident["fond_action"] if t == "action" else BLANC)
    encre = BLANC if sombre else ident["dominante"]
    discret = BLANC if sombre else GRIS
    el, probleme = [], []

    def fit(txt, police, tmax, tmin, hmax, quoi, lignes_max=None, lmax=L):
        taille, lignes = ajuster(txt, police, tmax, tmin, lmax, hmax, lignes_max)
        if taille is None:
            probleme.append(f"diapo {rang} ({t}) : « {quoi} » ne tient pas, même à {tmin} px — raccourcir")
        return taille, lignes

    if t == "photo":
        src = pathlib.Path(racine) / champ(d, "fichier")
        if not src.exists():
            probleme.append(f"diapo {rang} (photo) : fichier introuvable — {champ(d, 'fichier')}")
        else:
            im = Image.open(src).convert("RGB")
            r = max(W / im.width, H / im.height)
            im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
            g, h = (im.width - W) // 2, (im.height - H) // 2
            recadree = pathlib.Path(tmp) / f"photo-{rang}.jpg"
            im.crop((g, h, g + W, h + H)).save(recadree, quality=90)
            el.append(Photo(str(recadree), 0, 0, W, H))
        taille, lignes = fit(champ(d, "legende"), "reg", 44, CORPS_MIN, 150, "légende", 3)
        if taille:
            hb = len(lignes) * taille * INTERLIGNE + 60
            el.append(Rect(0, z["filet"] - 20 - hb, W, z["sure"][1] - (z["filet"] - 20 - hb), ident["dominante"], 0.92))
            el += empiler([(lignes, "reg", taille, BLANC, "left", True, MX)], z["filet"] - 20 - hb, z["filet"] - 20)
    elif t == "avant_apres":
        moitie = H // 2
        taille, lignes = fit(champ(d, "legende"), "reg", 44, CORPS_MIN, 150, "légende", 3)
        hb = (len(lignes) * taille * INTERLIGNE + 50) if taille else 0
        for rang_photo, cle in enumerate(("avant", "apres")):
            src = pathlib.Path(racine) / champ(d, cle)
            if not src.exists():
                probleme.append(f"diapo {rang} (avant-après) : fichier « {cle} » introuvable — {champ(d, cle)}")
                continue
            im = Image.open(src).convert("RGB")
            r = max(W / im.width, moitie / im.height)
            im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
            g, h = (im.width - W) // 2, (im.height - moitie) // 2
            recadree = pathlib.Path(tmp) / f"photo-{rang}-{cle}.jpg"
            im.crop((g, h, g + W, h + moitie)).save(recadree, quality=90)
            el.append(Photo(str(recadree), 0, rang_photo * moitie, W, moitie))
        if taille:
            # La légende sur la jointure : les deux photos perdent la même hauteur, la comparaison reste juste
            el.append(Rect(0, moitie - hb / 2, W, hb, ident["dominante"], 0.92))
            el += empiler([(lignes, "reg", taille, BLANC, "left", True, MX)], moitie - hb / 2, moitie + hb / 2, 0)
            for etiquette, y_tag in (("AVANT", z["sure"][0] + 170), ("APRÈS", moitie + hb / 2 + 90)):
                el.append(Rect(MX - 24, y_tag - 52, largeur(etiquette, "bold", 40) + 48, 68, ident["dominante"], 0.92))
                el.append(Texte([etiquette], "bold", 40, BLANC, MX, y_tag))
        if ident["signature"]:
            el.append(Rect(0, z["filet"], W, z["sure"][1] - z["filet"], ident["dominante"], 0.92))
    elif t == "couverture":
        groupes = []
        a, la = fit(champ(d, "titre"), "bold", 112, 64, 520, "titre", 5)
        if a: groupes.append((la, "bold", a, BLANC, "left", False, MX))
        if champ(d, "sous_titre"):
            b, lb = fit(champ(d, "sous_titre"), "reg", 52, CORPS_CIBLE, 200, "sous-titre", 3)
            if b: groupes.append((lb, "reg", b, BLANC, "left", True, MX))
        el += empiler(groupes, z["haut"], z["bas"], 44)
    elif t == "idee":
        groupes = []
        a, la = fit(champ(d, "titre"), "bold", 84, 52, 400, "titre", 5)
        if a: groupes.append((la, "bold", a, encre, "left", False, MX))
        if champ(d, "texte"):
            b, lb = fit(champ(d, "texte"), "reg", 50, CORPS_MIN, 330, "texte", 6)
            if b: groupes.append((lb, "reg", b, GRIS, "left", True, MX))
        el += empiler(groupes, z["haut"], z["bas"])
    elif t == "etape":
        groupes = [([f"ÉTAPE {champ(d, 'numero') or max(1, rang - 1)}"], "bold", 40, ident["accent"], "left", False, MX)]
        a, la = fit(champ(d, "titre"), "bold", 78, 50, 380, "titre", 4)
        if a: groupes.append((la, "bold", a, encre, "left", False, MX))
        for cle, quoi in (("duree", "durée"), ("texte", "texte")):
            if champ(d, cle):
                b, lb = fit(champ(d, cle), "reg", 48, CORPS_MIN, 200, quoi, 4)
                if b: groupes.append((lb, "reg", b, ident["accent"] if cle == "duree" else GRIS, "left", True, MX))
        el += empiler(groupes, z["haut"], z["bas"], 30)
    elif t == "chiffre":
        groupes = []
        a, la = fit(champ(d, "valeur"), "bold", 220, 96, 440, "valeur", 2)
        if a: groupes.append((la, "bold", a, ident["accent"], "left", False, MX))
        b, lb = fit(champ(d, "legende"), "reg", 56, CORPS_CIBLE, 260, "légende", 4)
        if b: groupes.append((lb, "reg", b, encre, "left", True, MX))
        c, lc = fit("Source : " + champ(d, "source"), "reg", 36, CORPS_MIN, 100, "source", 2)
        if c: groupes.append((lc, "reg", c, GRIS, "left", False, MX))
        el += empiler(groupes, z["haut"], z["bas"], 28)
    elif t == "colonnes":
        lignes = d.get("lignes") or []
        if not (1 <= len(lignes) <= 4) or any(not isinstance(x, list) or len(x) != 2 for x in lignes):
            probleme.append(f"diapo {rang} (colonnes) : de une à quatre lignes, deux cases chacune")
        else:
            col, gout = (L - 40) / 2, 40
            a1, t1 = fit(champ(d, "gauche_titre"), "bold", 40, CORPS_MIN, 100, "titre gauche", 2, col)
            a2, t2 = fit(champ(d, "droite_titre"), "bold", 40, CORPS_MIN, 100, "titre droit", 2, col)
            tailles = []
            for i, (g, dr) in enumerate(lignes, 1):
                s1, _ = ajuster(g, "reg", 46, CORPS_MIN, col, 170, 3)
                s2, _ = ajuster(dr, "reg", 46, CORPS_MIN, col, 170, 3)
                if not s1 or not s2:
                    probleme.append(f"diapo {rang} (colonnes) : ligne {i} trop longue — raccourcir")
                tailles += [s1 or CORPS_MIN, s2 or CORPS_MIN]
            if a1 and a2 and not probleme:
                s = min(tailles)
                cases = [(couper(g, "reg", s, col), couper(dr, "reg", s, col)) for g, dr in lignes]
                ht = max(len(t1) * a1, len(t2) * a2) * INTERLIGNE
                hrangs = [max(len(c1), len(c2)) * s * INTERLIGNE + 40 for c1, c2 in cases]
                hauteur_bloc = ht + 24 + sum(hrangs)
                y = z["haut"] + max(0, (z["bas"] - z["haut"] - hauteur_bloc) / 2)
                el.append(Texte(t1, "bold", a1, GRIS, MX, y + a1 * 0.95))
                el.append(Texte(t2, "bold", a2, GRIS, MX + col + gout, y + a2 * 0.95))
                y += ht + 12
                el.append(Filet(MX, y, W - MX, y, 3, ident["dominante"]))
                y += 12
                for (c1, c2), hr in zip(cases, hrangs):
                    el.append(Texte(c1, "reg", s, GRIS, MX, y + 20 + s * 0.95, courant=True))
                    el.append(Texte(c2, "reg", s, encre, MX + col + gout, y + 20 + s * 0.95, courant=True))
                    y += hr
                    el.append(Filet(MX, y, W - MX, y, 1.5, TRAIT))
    elif t == "liste":
        elements = d.get("elements") or []
        if not (2 <= len(elements) <= 7):
            probleme.append(f"diapo {rang} (liste) : de deux à sept éléments, pas {len(elements)}")
        else:
            a, la = fit(champ(d, "titre"), "bold", 72, 48, 250, "titre", 3)
            ecart = 22
            dispo = z["bas"] - z["haut"] - (len(la or []) * (a or 44) * INTERLIGNE) - 40 - ecart * (len(elements) - 1)
            s_ok = None
            for s in list(range(50, CORPS_MIN, -2)) + [CORPS_MIN]:
                coupes = [couper(e, "reg", s, L - 80) for e in elements]
                if all(coupes) and sum(len(c) for c in coupes) * s * INTERLIGNE <= dispo:
                    s_ok = s
                    break
            if not a or not s_ok:
                probleme.append(f"diapo {rang} (liste) : trop de texte, même à {CORPS_MIN} px — raccourcir")
            else:
                groupes = [(la, "bold", a, encre, "left", False, MX)]
                coupes = [couper(e, "reg", s_ok, L - 80) for e in elements]
                blocs = empiler(groupes + [(c, "reg", s_ok, encre, "left", True, MX + 80) for c in coupes], z["haut"], z["bas"], ecart)
                el.append(blocs[0])
                for b in blocs[1:]:
                    el.append(b)
                    el.append(Texte(["—"], "bold", s_ok, ident["accent"], MX, b.ys[0]))
    elif t == "citation":
        a, la = fit(f"« {champ(d, 'texte')} »", "bold", 74, 44, 540, "citation", 7)
        b, lb = fit(f"— {champ(d, 'auteur')}", "reg", 40, CORPS_MIN, 100, "auteur", 2)
        if a and b:
            el += empiler([(la, "bold", a, encre, "left", True, MX), (lb, "reg", b, GRIS, "left", False, MX)], z["haut"], z["bas"], 40)
    elif t == "action":
        a, la = fit(champ(d, "texte"), "bold", 90, 56, 540, "texte", 6)
        if a:
            el += empiler([(la, "bold", a, BLANC, "left", False, MX)], z["haut"], z["bas"])

    if source_libre:
        s_src, l_src = ajuster("Source : " + source_libre, "reg", CORPS_MIN, CORPS_MIN, L, 90, 2)
        if s_src:
            el.append(Texte(l_src, "reg", s_src, GRIS, MX, z["bas"] + 100 - 12 - (len(l_src) - 1) * s_src * INTERLIGNE))
        else:
            probleme.append(f"diapo {rang} ({t}) : source trop longue — la raccourcir")
    # Tête : rang et jauge, au même endroit partout, dans la zone sûre
    if carrousel and z["tete"]:
        teinte = BLANC
        if t not in ("couverture", "action", "photo", "avant_apres"):
            teinte = GRIS
        if t in ("photo", "avant_apres"):
            el.append(Rect(0, z["jauge"] - 60, W, 100, "#000000", 0.35))
        el.append(Texte([str(rang)], "reg", CORPS_MIN, teinte, MX, z["tete"]))
        el.append(Texte([str(total)], "reg", CORPS_MIN, teinte, W - MX, z["tete"], "right"))
        x1, x2 = MX + 70, W - MX - 70
        el.append(Filet(x1, z["jauge"] - 12, x2, z["jauge"] - 12, 4, BLANC if sombre or t in ("photo", "avant_apres") else TRAIT, 0.35 if sombre or t in ("photo", "avant_apres") else 1))
        barre = ident["accent"] if not (sombre or t in ("photo", "avant_apres")) else BLANC
        if t == "action" and ident["fond_action"] == ident["accent"]:
            barre = BLANC
        el.append(Filet(x1, z["jauge"] - 12, x1 + (x2 - x1) * rang / total, z["jauge"] - 12, 4, barre))
    # Pied : filet et signature, identiques partout, dans la zone sûre
    if t not in ("photo", "avant_apres"):
        el.append(Filet(MX, z["filet"], W - MX, z["filet"], 2, BLANC if sombre else TRAIT, 0.35 if sombre else 1))
    if ident["signature"]:
        s_sig, l_sig = ajuster(ident["signature"], "reg", CORPS_MIN, CORPS_MIN, L - (140 if ident.get("logo_ok") else 0), 60, 1)
        if s_sig:
            el.append(Texte(l_sig, "reg", s_sig, discret if t not in ("photo", "avant_apres") else BLANC, MX, z["pied"]))
        else:
            probleme.append("bloc de signature trop long pour le pied — raccourcir dans cadre.md")
    if ident.get("logo_ok") and t not in ("photo", "avant_apres"):
        el.append(Photo(ident["logo_ok"], W - MX - 120, z["filet"] + 12, 120, 60))
    return fond, el, probleme


# ── Rendus ──────────────────────────────────────────────────────────
_polices_png = {}


def police_png(nom, taille):
    cle = (nom, taille)
    if cle not in _polices_png:
        _polices_png[cle] = ImageFont.truetype(str(FICHIERS_POLICE[nom]), round(taille), layout_engine=ImageFont.Layout.BASIC)
    return _polices_png[cle]


def rendre_png(fond, elements, W, H, chemin):
    img = Image.new("RGB", (W, H), rgb(fond))
    for e in elements:
        if isinstance(e, Photo):
            p = Image.open(e.chemin).convert("RGBA")
            if (p.width, p.height) != (e.w, e.h):
                p.thumbnail((e.w, e.h))
            img.paste(p, (round(e.x), round(e.y)), p)
    dr = ImageDraw.Draw(img, "RGBA")
    for e in elements:
        if isinstance(e, Rect):
            dr.rectangle([e.x, e.y, e.x + e.w, e.y + e.h], fill=rgb(e.couleur, e.alpha))
        elif isinstance(e, Filet):
            dr.line([e.x1, e.y1, e.x2, e.y2], fill=rgb(e.couleur, e.alpha), width=max(1, round(e.epaisseur)))
        elif isinstance(e, Texte):
            f = police_png(e.police, e.taille)
            ancre = {"left": "ls", "right": "rs", "center": "ms"}[e.align]
            for ligne, y in zip(e.lignes, e.ys):
                dr.text((e.x, y), ligne, font=f, fill=rgb(e.couleur), anchor=ancre)
    img.save(chemin, optimize=True)


def rendre_pdf(pages, W, H, chemin, titre, auteur):
    c = rl_canvas.Canvas(str(chemin), pagesize=(W * 0.75, H * 0.75), initialFontName="Liberation-reg", initialFontSize=34)
    c.setTitle(titre); c.setAuthor(auteur); c.setCreator("immo-reseaux-sociaux — build_carrousel.py")
    for fond, elements in pages:
        c.saveState(); c.scale(0.75, 0.75)
        c.setFillColor(HexColor(fond)); c.rect(0, 0, W, H, stroke=0, fill=1)
        for e in elements:
            if isinstance(e, Photo):
                c.drawImage(e.chemin, e.x, H - e.y - e.h, e.w, e.h, mask="auto", preserveAspectRatio=True, anchor="c")
        for e in elements:
            if isinstance(e, Rect):
                c.setFillColor(HexColor(e.couleur)); c.setFillAlpha(e.alpha)
                c.rect(e.x, H - e.y - e.h, e.w, e.h, stroke=0, fill=1); c.setFillAlpha(1)
            elif isinstance(e, Filet):
                c.setStrokeColor(HexColor(e.couleur)); c.setStrokeAlpha(e.alpha); c.setLineWidth(e.epaisseur)
                c.line(e.x1, H - e.y1, e.x2, H - e.y2); c.setStrokeAlpha(1)
            elif isinstance(e, Texte):
                c.setFont(f"Liberation-{e.police}", e.taille); c.setFillColor(HexColor(e.couleur))
                for ligne, y in zip(e.lignes, e.ys):
                    {"left": c.drawString, "right": c.drawRightString, "center": c.drawCentredString}[e.align](e.x, H - y, ligne)
        c.restoreState(); c.showPage()
    c.save()


def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60].rstrip("-") or "carrousel"


def feuilles(v):
    """Toutes les chaînes d'une valeur JSON, sans la ponctuation de sa structure."""
    if isinstance(v, str):
        return [v]
    if isinstance(v, dict):
        return [s for x in v.values() for s in feuilles(x)]
    if isinstance(v, list):
        return [s for x in v for s in feuilles(x)]
    return []


# ── Programme ───────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description="Fabrique un carrousel ou un visuel d'information contrôlé.")
    ap.add_argument("contenu"); ap.add_argument("sortie")
    ap.add_argument("--cadre", default=None, help="chemin de 00_MOI/cadre.md, pour l'identité")
    ap.add_argument("--racine", default=".", help="dossier de travail, pour les chemins de photos et de logo")
    a = ap.parse_args()
    sortie = pathlib.Path(a.sortie); controle = sortie / "controle"

    try:
        contenu = json.load(open(a.contenu, encoding="utf-8"))
    except Exception as e:
        BLO.append(f"contenu.json illisible : {e}"); sortir(controle)
    if not enregistrer_polices():
        sortir(controle)

    diapos = contenu.get("diapos") or []
    canevas = contenu.get("canevas", "portrait")
    sorties = set(contenu.get("sorties") or ["pdf", "png"])
    carrousel = len(diapos) > 1
    if canevas not in ZONES:
        BLO.append(f"canevas « {canevas} » inconnu : portrait ou carre")
        sortir(controle)
    z = ZONES[canevas]

    # Règles de structure
    if not diapos:
        BLO.append("aucune diapo")
    for i, d in enumerate(diapos, 1):
        t = d.get("type")
        if t not in TYPES:
            BLO.append(f"diapo {i} : type « {t} » inconnu")
            continue
        for k in CHAMPS[t]:
            v = d.get(k)
            if v in (None, "", []):
                BLO.append(f"diapo {i} ({t}) : champ « {k} » vide")
        textes = json.dumps(d, ensure_ascii=False)
        if re.search(r"https?://|www\.", textes, re.I):
            BLO.append(f"diapo {i} : un lien dans le document — le lien va dans le texte du post")
        if re.search(r"\[[^\]]*\]", " ".join(feuilles({k: v for k, v in d.items() if k not in ("fichier", "avant", "apres")}))):
            BLO.append(f"diapo {i} : texte entre crochets, gabarit non rempli ou valeur à confirmer")
        if t == "chiffre" and re.search(r"confirmer|inconnu|\?", str(d.get("source", "")), re.I):
            BLO.append(f"diapo {i} (chiffre) : source à confirmer — le chiffre ne sort pas sans elle")
        if t == "etape" and champ(d, "duree") and not champ(d, "source"):
            BLO.append(f"diapo {i} (etape) : une durée sans source — « source » : ses dossiers, et leur date")
        if t in ("photo", "avant_apres") and d.get("droits_confirmes") is not True:
            BLO.append(f"diapo {i} ({t}) : droits non confirmés — « droits_confirmes »: true, seulement si cadre.md ou lui le disent")
        if t not in ("chiffre",) and re.search(r"\d+(?:[.,]\d+)?\s?(?:%|€|k€|m²|m2|jours?|semaines?|mois|ans|visites?)\b", textes, re.I) and not d.get("source"):
            ATT.append(f"diapo {i} ({t}) : un chiffre sans source dans le texte — vérifier qu'il est à lui, daté, et ajouter « source »")
    if carrousel:
        if canevas != "portrait":
            BLO.append("un carrousel se fabrique en portrait 1080 × 1350")
        if not 5 <= len(diapos) <= 10:
            BLO.append(f"{len(diapos)} diapos : un carrousel en compte de cinq à dix")
        elif len(diapos) > 8:
            ATT.append(f"{len(diapos)} diapos : au-delà de huit, on en demande trop à qui fait défiler")
        if diapos and diapos[0].get("type") != "couverture":
            BLO.append("la première diapo n'est pas la couverture")
        actions = [i for i, d in enumerate(diapos, 1) if d.get("type") == "action"]
        if actions != [len(diapos)]:
            BLO.append(f"une seule action, en dernière diapo — trouvées en : {actions or 'aucune'}")
        corps = {d.get("type") for d in diapos[1:-1]}
        if len(corps) > 3:
            ATT.append(f"{len(corps)} variantes de diapo dans le corps ({', '.join(sorted(corps))}) : trois au plus")
    elif diapos and diapos[0].get("type") in ("couverture", "action", "photo"):
        BLO.append("un visuel unique porte une information : idée, étape, chiffre, colonnes, liste, citation ou avant-après")
    for i, d in enumerate(diapos, 1):
        if d.get("type") not in ("couverture", "action", "photo", "avant_apres", "chiffre", "colonnes"):
            mots = len(re.findall(r"\w+", " ".join(str(v) for k, v in d.items() if k in ("titre", "texte", "elements"))))
            if mots > 15 and d.get("type") != "liste":
                ATT.append(f"diapo {i} ({d.get('type')}) : {mots} mots, une quinzaine au plus sur une diapo de contenu")
    if BLO:
        sortir(controle)

    ident = theme(contenu, a.cadre)
    if ident.get("logo"):
        chemin_logo = pathlib.Path(a.racine) / ident["logo"]
        if chemin_logo.exists():
            ident["logo_ok"] = str(chemin_logo)
        else:
            ATT.append(f"logo indiqué dans cadre.md introuvable : {ident['logo']}")

    with tempfile.TemporaryDirectory() as tmp:
        pages, minimum_courant = [], None
        for i, d in enumerate(diapos, 1):
            fond, elements, probleme = composer(d, i, len(diapos), z, ident, carrousel, a.racine, tmp)
            BLO.extend(probleme)
            for e in elements:
                if isinstance(e, Texte):
                    if carrousel and canevas == "portrait" and (e.haut() < z["sure"][0] or e.bas() > z["sure"][1]):
                        BLO.append(f"diapo {i} : texte hors de la zone sûre ({e.haut():.0f}–{e.bas():.0f} px)")
                    if e.courant:
                        minimum_courant = e.taille if minimum_courant is None else min(minimum_courant, e.taille)
            if carrousel and canevas == "portrait":
                compteurs = [e.lignes[0] for e in elements if isinstance(e, Texte) and abs(e.ys[0] - z["tete"]) < 1]
                if compteurs != [str(i), str(len(diapos))]:
                    BLO.append(f"diapo {i} : compteur de tête incohérent {compteurs} — défaut du moteur")
            pages.append((fond, elements))
        if BLO:
            sortir(controle)
        if minimum_courant is not None:
            MESURES.append(f"corps du texte courant : {minimum_courant:.0f} px au plus petit")
            if minimum_courant < CORPS_CIBLE:
                ATT.append(f"texte courant descendu à {minimum_courant:.0f} px : lisible, mais sous les 40 visés — raccourcir")

        sortie.mkdir(parents=True, exist_ok=True); controle.mkdir(parents=True, exist_ok=True)
        nom = slug(contenu.get("titre_document") or champ(diapos[0], "titre") or "visuel")
        pngs = []
        for i, (fond, elements) in enumerate(pages, 1):
            p = (sortie if "png" in sorties else pathlib.Path(tmp)) / (f"{nom}-{i:02d}.png" if carrousel else f"{nom}.png")
            rendre_png(fond, elements, z["W"], z["H"], p); pngs.append(p)
        if "pdf" in sorties and carrousel:
            pdf = sortie / f"{nom}.pdf"
            rendre_pdf(pages, z["W"], z["H"], pdf, contenu.get("titre_document", nom), ident["signature"])
            poids = pdf.stat().st_size
            MESURES.append(f"PDF : {len(pages)} pages, {poids / 1024:.0f} Ko")
            if poids > 10 * 1024 * 1024:
                ATT.append("PDF de plus de 10 Mo : alléger les photos")
            try:
                from pypdf import PdfReader
                r = PdfReader(str(pdf))
                tailles = {(round(float(pg.mediabox.width), 1), round(float(pg.mediabox.height), 1)) for pg in r.pages}
                vides = [n for n, pg in enumerate(r.pages, 1) if not (pg.extract_text() or "").strip()]
                if len(r.pages) != len(pages) or tailles != {(810.0, 1012.5)}:
                    BLO.append(f"PDF non conforme : {len(r.pages)} pages, format {tailles}")
                else:
                    OK.append("PDF relu : une page par diapo, 1080 × 1350")
                if vides:
                    ATT.append(f"PDF : pas de texte lisible par une machine en page(s) {vides}")
                else:
                    OK.append("PDF : texte lisible par une machine sur chaque page")
            except ImportError:
                ATT.append("pypdf absent : le PDF n'a pas été relu")
        for p in pngs:
            with Image.open(p) as im:
                if im.size != (z["W"], z["H"]):
                    BLO.append(f"{p.name} : {im.size} au lieu de {z['W']} × {z['H']}")
        if "png" in sorties:
            OK.append(f"{len(pngs)} image(s) PNG de {z['W']} × {z['H']}")
        # Planche contact et vignette : ce qu'on regarde avant de livrer
        vign = 270
        hv = round(vign * z["H"] / z["W"])
        cols = min(4, len(pngs)); rangs = (len(pngs) + cols - 1) // cols
        planche = Image.new("RGB", (cols * vign + (cols + 1) * 16, rangs * hv + (rangs + 1) * 16), rgb(FOND_PLANCHE))
        for n, p in enumerate(pngs):
            with Image.open(p) as im:
                planche.paste(im.resize((vign, hv), Image.LANCZOS), (16 + (n % cols) * (vign + 16), 16 + (n // cols) * (hv + 16)))
        planche.save(controle / "planche.png")
        with Image.open(pngs[0]) as im:
            im.resize((360, round(360 * z["H"] / z["W"])), Image.LANCZOS).save(controle / "vignette.png")
        OK.append("controle/planche.png et controle/vignette.png écrites : à regarder avant de livrer")
    sortir(controle)


if __name__ == "__main__":
    main()
