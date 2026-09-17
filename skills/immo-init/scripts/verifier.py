#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vérification mécanique des fichiers de vérité de la mallette.

Ne dérive pas : c'est un script. Il ne vérifie que ce qui casse réellement un lecteur —
pas la qualité, pas le style, pas le sens. Il rapporte, il ne corrige jamais.

Usage :  python3 verifier.py <dossier de travail>
Sortie : lignes « MESURE » (les chiffres que le tableau de bord recopie tels quels),
         « OK », « ATTENTION », « BLOQUANT », puis un code de retour :
         0 rien à signaler · 1 attentions · 2 au moins un bloquant

Mallette 7.5 : lit aussi les tableaux (parcours, index, SONCAS, leviers), cherche les
coordonnées sur toutes les lignes, et ne signale plus les lignes du gabarit laissées vides.
"""
import re, sys, os, datetime

DOSSIER = sys.argv[1] if len(sys.argv) > 1 else "."
MOI = os.path.join(DOSSIER, "00_MOI")
FICHIERS = ["profil.md", "voix.md", "cadre.md", "clients-types.md", "recurrences.md"]
AUJOURDHUI = datetime.date.today()

MARQUEUR = re.compile(r"^- \[(dit|vu|à confirmer)( (\d{4}-\d{2}|\?))?\]")
MARQUEUR_CASE = re.compile(r"^\[(dit|vu|à confirmer)( (\d{4}-\d{2}|\?))?\]")
MAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
TEL = re.compile(r"(?<!\d)(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}(?!\d)")
SEPARATEUR = re.compile(r"^\|(\s*:?-{3,}:?\s*\|)+\s*$")
# Ligne de gabarit laissée vide : « Libellé : », « Libellé : [date] », « Libellé : oui / non »
GABARIT = re.compile(r":\s*$|:\s*\[[^\]]*\]\s*$|:\s*[^:\[\]]*\S\s/\s\S[^:\[\]]*$")
CHOIX = re.compile(r"\S\s/\s\S")
CROCHETS = re.compile(r"^\[[^\]]*\]$")
ANCIEN_MOIS = 6

attentions, bloquants = [], []
def att(m): attentions.append(m)
def blo(m):
    if m not in bloquants: bloquants.append(m)

def age_mois(aaaamm):
    an, mo = map(int, aaaamm.split("-"))
    return (AUJOURDHUI.year - an) * 12 + (AUJOURDHUI.month - mo)

def cellules(ligne):
    s = ligne.strip()
    if len(s) < 2 or not s.startswith("|") or not s.endswith("|"): return None
    return [c.strip() for c in s[1:-1].split("|")]

# ── 1. Le dossier est-il celui de la mallette ?
if not os.path.isdir(MOI):
    numerotes = [d for d in os.listdir(DOSSIER) if re.match(r"^0[1-9]_", d)] if os.path.isdir(DOSSIER) else []
    if numerotes:
        blo(f"00_MOI/ absent mais {', '.join(numerotes)} présents : dossier renommé ou déplacé — ne pas réinstaller, demander.")
    else:
        blo("00_MOI/ absent : aucune installation dans ce dossier.")
    print("\n".join(f"BLOQUANT  {m}" for m in bloquants)); sys.exit(2)

# ── 2. Chaque fichier existe et a une taille non nulle
for f in FICHIERS:
    p = os.path.join(MOI, f)
    if not os.path.exists(p): blo(f"{f} manquant.")
    elif os.path.getsize(p) == 0: blo(f"{f} vide.")

# ── 3. L'en-tête d'état du profil est intact
profil = os.path.join(MOI, "profil.md")
t = ""
if os.path.exists(profil):
    t = open(profil, encoding="utf-8").read()
    if "<!-- ETAT DE LA MALLETTE -->" not in t or "<!-- FIN ETAT -->" not in t:
        blo("profil.md : en-tête d'état absent ou cassé — la reprise après coupure ne marchera pas.")
    if not re.search(r"^## 4\.", t, re.M): att("profil.md : section 4 (USP) introuvable.")
    if not re.search(r"^## 6\.", t, re.M): att("profil.md : section 6 (comment je travaille) introuvable.")

# ── 4. Lignes et cases : un marqueur et un mois ; rien qui identifie un tiers ; rien de trop vieux
lignes_mesure, cases_mesure = {}, {}
for f in FICHIERS:
    p = os.path.join(MOI, f)
    if not os.path.exists(p): continue
    lignes = open(p, encoding="utf-8").read().split("\n")
    dans_etat, dans_tableau = False, False
    n_l = ac_l = 0
    c_marq = c_ac = c_vides = c_sans = 0
    for i, l in enumerate(lignes):
        n = i + 1
        # coordonnées : sur toutes les lignes, marquées ou non, tableaux compris
        if MAIL.search(l): blo(f"{f}:{n} adresse mail dans un fichier de 00_MOI/ — donnée de tiers ?")
        if TEL.search(l): blo(f"{f}:{n} numéro de téléphone dans un fichier de 00_MOI/ — donnée de tiers ?")
        if "<!-- ETAT DE LA MALLETTE -->" in l: dans_etat = True
        if "<!-- FIN ETAT -->" in l: dans_etat = False; continue
        if dans_etat: continue
        c = cellules(l)
        if c is not None:
            if SEPARATEUR.match(l.strip()): dans_tableau = True; continue
            suivante = lignes[i + 1].strip() if i + 1 < len(lignes) else ""
            if SEPARATEUR.match(suivante) or not dans_tableau: continue   # ligne d'en-tête
            for j, case in enumerate(c):
                if j == 0: continue                                        # libellé de la ligne
                m = MARQUEUR_CASE.match(case)
                if m:
                    c_marq += 1
                    if m.group(1) == "à confirmer": c_ac += 1
                    if m.group(1) != "à confirmer" and not m.group(2):
                        att(f"{f}:{n} case sans mois, colonne {j + 1} : « {case[:58]} »")
                    if m.group(3) and m.group(3) != "?" and age_mois(m.group(3)) > ANCIEN_MOIS:
                        att(f"{f}:{n} case de {age_mois(m.group(3))} mois — à revoir : « {case[:58]} »")
                elif not case or CROCHETS.match(case) or CHOIX.search(case):
                    c_vides += 1                                           # case du gabarit
                else:
                    c_sans += 1
                    att(f"{f}:{n} case sans marqueur [dit/vu/à confirmer], colonne {j + 1} : « {case[:58]} »")
            continue
        dans_tableau = False
        if not l.startswith("- "): continue
        m = MARQUEUR.match(l)
        if not m:
            contenu = l[2:].strip()
            k = i + 1                          # une puce du gabarit peut continuer sur les lignes indentées
            while k < len(lignes) and lignes[k].startswith("  ") and lignes[k].strip() and not lignes[k].lstrip().startswith(("- ", "|")):
                contenu += " " + lignes[k].strip(); k += 1
            if contenu and not GABARIT.search(contenu):
                att(f"{f}:{n} ligne sans marqueur [dit/vu/à confirmer] : « {contenu[:58]} »")
            continue
        n_l += 1
        if m.group(1) == "à confirmer": ac_l += 1
        if m.group(1) != "à confirmer" and not m.group(2):
            att(f"{f}:{n} marqueur sans mois : « {l[2:60].strip()} »")
        if m.group(3) and m.group(3) != "?":
            age = age_mois(m.group(3))
            if age > ANCIEN_MOIS:
                att(f"{f}:{n} ligne de {age} mois — à revoir : « {l[2:60].strip()} »")
    lignes_mesure[f] = (n_l, ac_l)
    if c_marq + c_vides + c_sans:
        cases_mesure[f] = (c_marq - c_ac, c_marq + c_vides + c_sans)

# ── 4 bis. Les mesures que le tableau de bord recopie — jamais estimées par le modèle
for f in FICHIERS:
    if f not in lignes_mesure: continue
    n, ac = lignes_mesure[f]
    pct = round(100 * (n - ac) / n) if n else 0
    print(f"MESURE    {f.replace('.md','')} : {pct} % — {n - ac} lignes remplies sur {n} marquées")
    if f in cases_mesure:
        r, tot = cases_mesure[f]
        print(f"MESURE    {f.replace('.md','')} (tableaux) : {round(100 * r / tot) if tot else 0} % — {r} cases remplies sur {tot}")
biens_dir = os.path.join(DOSSIER, "01_BIENS")
if os.path.isdir(biens_dir):
    biens = [d for d in os.listdir(biens_dir) if os.path.isdir(os.path.join(biens_dir, d))]
    print(f"MESURE    biens : {len(biens)} dossier(s) dans 01_BIENS/")
    idx = os.path.join(biens_dir, "index.md")
    if biens and not os.path.exists(idx):
        att("01_BIENS/index.md absent alors que des biens existent — immo-parcours n'appariera rien.")
pub = os.path.join(DOSSIER, "02_PUBLICATIONS")
if os.path.isdir(pub):
    for sub in ("brouillons", "publies"):
        q = os.path.join(pub, sub)
        if os.path.isdir(q): print(f"MESURE    {sub} : {len([x for x in os.listdir(q) if x.endswith('.md')])} fichier(s)")
sk = os.path.join(DOSSIER, ".claude", "skills")
if os.path.isdir(sk): print(f"MESURE    outils installés : {len([d for d in os.listdir(sk) if os.path.isdir(os.path.join(sk, d))])}")

# ── 5. Les dossiers du domaine existent
for d in ["01_BIENS", "02_PUBLICATIONS", "03_RESSOURCES"]:
    if not os.path.isdir(os.path.join(DOSSIER, d)): att(f"{d}/ absent.")

# ── 6. CLAUDE.md et les outils
if not os.path.exists(os.path.join(DOSSIER, "CLAUDE.md")): att("CLAUDE.md absent à la racine — Claude Code sera aveugle.")
if not os.path.isdir(sk): att(".claude/skills/ absent — aucun outil auto-installé.")

# ── 7. Le miroir
if t:
    m = re.search(r"Miroir déposé dans le projet le : ([^\n]+)", t)
    if m:
        v = m.group(1).strip()
        d = re.search(r"(\d{4})-(\d{2})", v)
        if d:
            age = (AUJOURDHUI.year - int(d.group(1))) * 12 + (AUJOURDHUI.month - int(d.group(2)))
            if age > 3: att(f"miroir du projet déposé il y a {age} mois — à rafraîchir.")
        elif "[" in v or not v: att("miroir du projet : jamais déposé — il ne lira rien depuis son téléphone.")

# ── Sortie
for m in bloquants: print(f"BLOQUANT  {m}")
for m in attentions: print(f"ATTENTION {m}")
if not bloquants and not attentions: print("OK        rien à signaler.")
sys.exit(2 if bloquants else (1 if attentions else 0))
