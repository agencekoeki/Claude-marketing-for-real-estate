#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier-mallette.py — contrôle mécanique de la MALLETTE elle-même, avant chaque livraison.

verifier.py contrôle le dossier d'un stagiaire. Celui-ci contrôle les skills : les contrats que
la carte de vérité promet et qu'une relecture humaine laisse dériver. Il ne corrige rien, et il
ne juge ni le style ni la méthode. Il sert au formateur ; la procédure est dans
references/maintenance.md.

Usage :  python3 verifier-mallette.py [dossier contenant les 4 skills] [--moteur]
         Sans dossier : celui qui contient immo-init, deux niveaux au-dessus de ce script —
         .claude/skills/ dans un dossier de travail.
         --moteur : fabrique aussi un carrousel d'essai, et vérifie qu'un contenu fautif est refusé.
Sortie : OK / ATTENTION / BLOQUANT, puis code 0 (rien), 1 (attentions), 2 (au moins un bloquant).
"""
import re, sys, pathlib, hashlib, json, subprocess, tempfile

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
MOTEUR = "--moteur" in sys.argv[1:]
RACINE = pathlib.Path(ARGS[0]) if ARGS else pathlib.Path(__file__).resolve().parents[2]
OUTILS = ["immo-init", "immo-parcours", "immo-annonce", "immo-reseaux-sociaux", "immo-penser-savoir"]
PRODUCTION = ["immo-parcours", "immo-annonce", "immo-reseaux-sociaux"]
EPROUVER = PRODUCTION + ["immo-penser-savoir"]
DEPOT = "https://github.com/agencekoeki/Claude-marketing-for-real-estate"
bloq, att, ok = [], [], []


def lire(p):
    return p.read_text(encoding="utf-8")


def md(outil):
    return sorted(p for p in (RACINE / outil).rglob("*.md") if p.name not in ("CHANGELOG.md", "maintenance.md"))


def rel(p):
    return str(p.relative_to(RACINE))


def section(texte, titre):
    lignes = texte.split("\n")
    d = next((i for i, l in enumerate(lignes) if l.strip() == titre), None)
    if d is None:
        return None
    f = next((i for i in range(d + 1, len(lignes)) if lignes[i].startswith("## ")), len(lignes))
    return "\n".join(lignes[d:f]).strip()


def frontmatter(texte):
    m = re.match(r"^---\n(.*?)\n---\n", texte, re.S)
    fm = {}
    for l in (m.group(1).split("\n") if m else []):
        if ":" in l:
            k, v = l.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


# 1. Nom = dossier (sinon le téléversement échoue), ligne Version (sinon l'auto-copie ne se rafraîchit pas)
versions = {}
for o in OUTILS:
    s = RACINE / o / "SKILL.md"
    if not s.exists():
        bloq.append(f"{o} : SKILL.md absent")
        continue
    t = lire(s)
    fm = frontmatter(t)
    try:
        import yaml
        m_fm = re.match(r"^---\n(.*?)\n---", t, re.S)
        yaml.safe_load(m_fm.group(1) if m_fm else "")
    except ImportError:
        att.append("PyYAML absent : validité de l'en-tête YAML non contrôlée")
    except Exception as e:
        bloq.append(f"{o} : en-tête YAML invalide ({str(e).splitlines()[0]}) — le validateur officiel de skills le refuse")
    if fm.get("name") != o:
        bloq.append(f"{o} : name « {fm.get('name')} » différent du nom du dossier")
    m = re.search(r"^\*\*Version (\d+\.\d+) — [^*]+\.\*\*", t, re.M)
    if m:
        versions[o] = m.group(1)
    else:
        bloq.append(f"{o} : ligne Version introuvable")
    ok.append(f"{o} {versions.get(o, '?')} : description de {len(fm.get('description', ''))} caractères")

# 2. Bloc d'amorçage identique dans les outils de production et dans la référence d'amorcage.md
empreintes = {}
for o in PRODUCTION:
    s = RACINE / o / "SKILL.md"
    b = section(lire(s), "## Avant de produire quoi que ce soit") if s.exists() else None
    if b is None:
        bloq.append(f"{o} : bloc d'amorçage absent")
    else:
        empreintes[o] = hashlib.md5(b.encode()).hexdigest()[:8]
am = RACINE / "immo-init/references/amorcage.md"
if am.exists():
    t = lire(am)
    d = t.find("```markdown\n")
    f = t.find("\n```", d + 12)
    if d >= 0 and f >= 0:
        empreintes["amorcage.md"] = hashlib.md5(t[d + 12:f].strip().encode()).hexdigest()[:8]
if empreintes and len(set(empreintes.values())) == 1:
    ok.append(f"bloc d'amorçage identique dans {len(empreintes)} emplacements")
else:
    bloq.append("bloc d'amorçage divergent : " + ", ".join(f"{k}={v}" for k, v in empreintes.items()))

# 3. Renvois internes : chaque references/, assets/, scripts/ cité existe (y compris via .claude/skills/<outil>/)
for o in OUTILS:
    for p in md(o):
        for m in re.finditer(r"(\.claude/skills/([a-z-]+)/)?((?:references|assets|scripts)/[\w.-]*\w)", lire(p)):
            if not (RACINE / (m.group(2) or o) / m.group(3)).exists():
                bloq.append(f"{rel(p)} : renvoi vers {m.group(0)} introuvable")

# 4. Contrats de verite.md : un outil déclaré écrivain d'un fichier en parle vraiment dans ses fichiers
ve = RACINE / "immo-init/references/verite.md"
if ve.exists():
    contrats = 0
    for l in lire(ve).split("\n"):
        if not l.startswith("| `"):
            continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) < 3:
            continue
        ecrivains = set(re.findall(r"immo-[a-z]+(?:-[a-z]+)*", c[1]))
        if re.search(r"\binit\b", c[1]):
            ecrivains.add("immo-init")
        for e in sorted(ecrivains & set(OUTILS)):
            corpus = "\n".join(lire(p) for p in md(e))
            for ch in re.findall(r"`([^`]+)`", c[0]):
                segs = [s for s in ch.strip("/").split("/") if s and "<" not in s]
                contrats += 1
                if segs and segs[-1] not in corpus:
                    bloq.append(f"verite.md déclare {e} écrivain de {ch}, mais {e} n'en parle nulle part")
    ok.append(f"carte de vérité : {contrats} contrats écrivain → fichier contrôlés")

    # 5. L'USP a les mêmes écrivains dans verite.md et dans amorcage.md
    ligne = next((l for l in lire(ve).split("\n") if l.startswith("| `00_MOI/profil.md`")), "")
    cellule = ligne.split("|")[2] if ligne.count("|") > 3 else ""
    usp_verite = set(re.findall(r"immo-[a-z]+(?:-[a-z]+)*", cellule))
    para = re.search(r"\*\*L['’]USP est lue par tous.*?(?:\n\n|\Z)", lire(am), re.S) if am.exists() else None
    usp_amorcage = set(re.findall(r"immo-[a-z]+(?:-[a-z]+)*", para.group(0))) if para else set()
    if usp_verite == usp_amorcage:
        ok.append(f"USP : mêmes écrivains dans verite.md et amorcage.md (init + {', '.join(sorted(usp_verite)) or 'personne'})")
    else:
        bloq.append(f"USP : verite.md dit init + {sorted(usp_verite)}, amorcage.md dit init + {sorted(usp_amorcage)}")

# 6. Un outil cité qui n'existe pas doit être dit « à venir » sur la même ligne
for o in OUTILS:
    for p in md(o):
        for n, l in enumerate(lire(p).split("\n"), 1):
            for nom in sorted(set(re.findall(r"immo-[a-z]+(?:-[a-z]+)*", l)) - set(OUTILS)):
                if not re.search(r"à venir|voit venir", l):
                    att.append(f"{rel(p)}:{n} outil {nom} cité comme s'il existait")

# 7. Une étude ou « les données » sans source nommée, dans le paragraphe ou le suivant
ETUDE = re.compile(r"\b(?:une|des|deux|trois|cette|la même|l['’])\s*études?\b(?!\s+de\s+marché)|disent les données|les données (?:disent|montrent)", re.I)
SOURCE = re.compile(r"\bsources?\b|\bet al\.|publiée?s? en (?:19|20)\d{2}", re.I)
for o in OUTILS:
    for p in md(o):
        paras = re.split(r"\n\s*\n", lire(p))
        for k, para in enumerate(paras):
            m = ETUDE.search(para)
            suite = paras[k + 1] if k + 1 < len(paras) else ""
            if m and not SOURCE.search(para + "\n" + suite):
                att.append(f"{rel(p)} : « {' '.join(para[max(0, m.start() - 30):m.end() + 40].split())} » — aucune source nommée")

# 7 bis. Une marque seule (Drive, Gmail) là où la mallette raisonne par fonction
MARQUE = re.compile(r"\b(?:Drive|Gmail)\b")
TOLERE = re.compile(r"Outlook|OneDrive|Microsoft|stockage|\*\*Google\*\* — Gmail|connecteur Gmail de Claude|`in:sent` sur Gmail|Gmail, Outlook")
for o in OUTILS:
    for p in md(o):
        lignes_p = lire(p).split("\n")
        for n, l in enumerate(lignes_p, 1):
            contexte = l + " " + (lignes_p[n] if n < len(lignes_p) else "")   # une phrase coupée continue à la ligne suivante
            if MARQUE.search(l) and not TOLERE.search(contexte):
                att.append(f"{rel(p)}:{n} « {l.strip()[:70]} » — marque seule, la mallette raisonne par fonction")

# 8. Vocabulaire interdit par clients-types.md dans ce que l'agent voit : titres et phrases affichés, écrans rendus
INTERDITS = re.compile(r"\b(?:personas?|personæ|parcours client|tunnel|entonnoir|TOFU|MOFU|BOFU|messy middle|biais cognitifs?|leads?|nurturing|segmentation|funnel|insights?)\b", re.I)
for o in OUTILS:
    for nom in ("ecrans.md", "montrer.md"):
        p = RACINE / o / "references" / nom
        if not p.exists():
            continue
        texte = lire(p)
        affiche = re.compile(r"tâches? déclarées?|s['’]appelle|titre|affiche|première ligne", re.I)
        for para in re.split(r"\n\s*\n", texte):
            if not affiche.search(para):
                continue                                   # une phrase de l'utilisateur citée n'est pas affichée
            for m in re.finditer(r"«\s*(.*?)\s*»", para, re.S):
                q = " ".join(m.group(1).split())
                if INTERDITS.search(q) and not INTERDITS.fullmatch(q) and "ce que ta formation appelle" not in q:
                    att.append(f"{rel(p)} : « {q[:70]} » affiché à l'agent — vocabulaire interdit par clients-types.md")
        if nom == "ecrans.md":
            for l in texte.split("\n"):
                if l.startswith("|") and not re.match(r"^\|[\s:|-]+\|$", l.strip()):
                    for mot in sorted(set(x.lower() for x in INTERDITS.findall(l))):
                        att.append(f"{rel(p)} : « {mot} » dans un titre d'écran")
    for p in sorted((RACINE / o / "assets").glob("*.html")):
        visible = re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", lire(p), flags=re.S)
        for m in sorted(set(x.lower() for x in INTERDITS.findall(visible))):
            att.append(f"{rel(p)} : « {m} » visible dans un écran rendu")

# 9. Les fichiers de méthode recopiés d'un outil de production à l'autre restent identiques
for nom in ("eprouver.md",):
    e = {o: hashlib.md5((RACINE / o / "references" / nom).read_bytes()).hexdigest()[:8]
         for o in EPROUVER if (RACINE / o / "references" / nom).exists()}
    if len(set(e.values())) > 1:
        att.append(f"{nom} diverge entre outils de production : {e}")
    else:
        ok.append(f"{nom} identique dans {len(e)} outils")

# 10. L'entrée la plus récente du CHANGELOG correspond aux lignes Version
cl = RACINE / "immo-init/CHANGELOG.md"
if cl.exists():
    haut = re.search(r"^\*\*(\d+\.\d+) — [^*]+\.\*\*(.*?)(?=^\*\*\d+\.\d+ — |\Z)", lire(cl), re.S | re.M)
    if haut and versions.get("immo-init") != haut.group(1):
        bloq.append(f"CHANGELOG en {haut.group(1)}, SKILL.md d'immo-init en {versions.get('immo-init')}")
    for o, v in (re.findall(r"`(immo-[a-z-]+)` (\d+\.\d+)", haut.group(2)) if haut else []):
        if versions.get(o) != v:
            bloq.append(f"CHANGELOG annonce {o} {v}, SKILL.md dit {versions.get(o)}")

# 11. Chaque outil emporte sa carte (references/carte.md), qui porte exactement les étapes de son SKILL.md
for o in OUTILS:
    c = RACINE / o / "references" / "carte.md"
    if not c.exists():
        att.append(f"{o} : references/carte.md absente")
        continue
    es = set(re.findall(r"^## Étape (\d+(?: bis)?) —", lire(RACINE / o / "SKILL.md"), re.M))
    ec = set(re.findall(r'\["(\d+(?: bis)?) ·', lire(c)))
    if "```mermaid" not in lire(c):
        bloq.append(f"{o} : references/carte.md sans bloc mermaid")
    elif es == ec:
        ok.append(f"carte {o} : {len(es)} étapes, conformes au SKILL.md")
    else:
        bloq.append(f"carte {o} : étapes du SKILL.md {sorted(es)} ≠ étapes de la carte {sorted(ec)}")
cm = RACINE / "immo-init" / "references" / "carte-mallette.md"
if cm.exists():
    for o, v in re.findall(r"(immo-[a-z]+(?:-[a-z]+)*) (\d+\.\d+)", lire(cm)):
        if o in versions and versions[o] != v:
            bloq.append(f"carte-mallette.md affiche {o} {v}, SKILL.md dit {versions[o]}")
    ok.append("carte de la mallette : versions affichées conformes")
else:
    att.append("immo-init : references/carte-mallette.md absente")

# 12. Le moteur de visuels : ses fichiers, sa police et sa licence, et un contrat d'exemple qui couvre chaque type
RS = RACINE / "immo-reseaux-sociaux"
moteur = RS / "scripts" / "build_carrousel.py"
requis = [moteur, RS / "assets" / "carrousel.exemple.json", RS / "assets" / "polices" / "LiberationSans-Regular.ttf",
          RS / "assets" / "polices" / "LiberationSans-Bold.ttf", RS / "assets" / "polices" / "OFL.txt"]
manquants = [rel(p) for p in requis if not p.exists()]
if manquants:
    bloq.append(f"moteur de visuels incomplet : {manquants}")
else:
    types_moteur = set(re.findall(r'"([a-z_]+)"', re.search(r"TYPES = \{([^}]*)\}", lire(moteur)).group(1)))
    try:
        types_exemple = {d.get("type") for d in json.loads(lire(RS / "assets" / "carrousel.exemple.json"))["diapos"]}
        if types_exemple == types_moteur:
            ok.append(f"moteur de visuels : fichiers, police et licence présents ; l'exemple couvre les {len(types_moteur)} types")
        else:
            bloq.append(f"carrousel.exemple.json ne couvre pas les types du moteur : manque {sorted(types_moteur - types_exemple)}, en trop {sorted(types_exemple - types_moteur)}")
    except Exception as e:
        bloq.append(f"carrousel.exemple.json illisible : {e}")
    if "SIL OPEN FONT LICENSE Version 1.1" not in lire(RS / "assets" / "polices" / "OFL.txt"):
        bloq.append("assets/polices/OFL.txt ne porte pas la licence SIL OFL 1.1")

# 13. Sur demande : le moteur fabrique, et il refuse ce qu'il doit refuser
if MOTEUR and not manquants:
    essai = {"titre_document": "Essai de maintenance", "diapos": [
        {"type": "couverture", "titre": "Essai du moteur de la mallette"},
        {"type": "idee", "titre": "Une idée par diapo", "texte": "Une quinzaine de mots au plus."},
        {"type": "colonnes", "gauche_titre": "Ce qu'on croit", "droite_titre": "Ce qui est vrai", "lignes": [["Première case", "Deuxième case"]]},
        {"type": "liste", "titre": "Ce qu'on vérifie", "elements": ["Le rapport", "La planche", "La vignette"]},
        {"type": "idee", "titre": "Une autre idée", "texte": "Sans chiffre ni lien."},
        {"type": "action", "texte": "Une seule chose à faire."}]}
    with tempfile.TemporaryDirectory() as tmp:
        t = pathlib.Path(tmp)
        (t / "essai.json").write_text(json.dumps(essai, ensure_ascii=False), encoding="utf-8")
        r = subprocess.run([sys.executable, str(moteur), str(t / "essai.json"), str(t / "sortie")], capture_output=True, text=True)
        pdfs = list((t / "sortie").glob("*.pdf")); pngs = list((t / "sortie").glob("*.png"))
        if r.returncode in (0, 1) and len(pdfs) == 1 and len(pngs) == 6:
            ok.append(f"moteur : carrousel d'essai fabriqué — 1 PDF, 6 PNG, code {r.returncode}")
        else:
            bloq.append(f"moteur : carrousel d'essai non fabriqué (code {r.returncode}) — {(r.stdout + r.stderr).strip()[-200:]}")
        fautif = json.loads(json.dumps(essai)); fautif["diapos"][1]["texte"] = "Voir https://exemple.fr"
        (t / "fautif.json").write_text(json.dumps(fautif, ensure_ascii=False), encoding="utf-8")
        r = subprocess.run([sys.executable, str(moteur), str(t / "fautif.json"), str(t / "refus")], capture_output=True, text=True)
        if r.returncode == 2 and not list((t / "refus").glob("*.pdf")):
            ok.append("moteur : un lien dans une diapo est refusé, et rien de publiable n'est écrit")
        else:
            bloq.append(f"moteur : le contenu fautif n'a pas été refusé (code {r.returncode})")

# 14. Le paragraphe de mise à jour : identique dans les cinq outils, et il porte l'adresse du dépôt
paras = {}
for o in OUTILS:
    m = re.search(r"\*\*Mises à jour et installation\.\*\*.*?(?=\n\n)", lire(RACINE / o / "SKILL.md"), re.S)
    if not m:
        bloq.append(f"{o} : paragraphe « Mises à jour et installation » absent")
    else:
        paras[o] = m.group(0)
if len(paras) == len(OUTILS):
    if len(set(paras.values())) == 1 and DEPOT in next(iter(paras.values())):
        ok.append(f"paragraphe de mise à jour identique dans {len(OUTILS)} outils, adresse du dépôt comprise")
    else:
        bloq.append("paragraphe de mise à jour : versions différentes entre outils, ou adresse du dépôt absente")

# 15. Dans le dépôt : catalogue, manifeste du plugin et versions.json disent la même chose que les SKILL.md
DR = RACINE.resolve().parent
cat, plug_f, vj = DR / ".claude-plugin" / "marketplace.json", DR / ".claude-plugin" / "plugin.json", DR / "versions.json"
if cat.exists() or plug_f.exists() or vj.exists():
    try:
        c = json.loads(lire(cat)); pj = json.loads(lire(plug_f)); v = json.loads(lire(vj))
        entree = [p for p in c.get("plugins", []) if p.get("name") == "mallette-immo"]
        dossiers = sorted(p.name for p in RACINE.iterdir() if (p / "SKILL.md").exists())
        noms = [c.get("name"), pj.get("name")] + [p.get("name") for p in c.get("plugins", [])]
        if not entree or entree[0].get("source") != "./":
            bloq.append("catalogue : le plugin « mallette-immo » doit exister, avec la source « ./ »")
        elif pj.get("name") != "mallette-immo":
            bloq.append("plugin.json : le nom doit être « mallette-immo »")
        elif dossiers != sorted(OUTILS):
            bloq.append(f"skills/ contient {dossiers}, attendu {sorted(OUTILS)}")
        elif any(str(n).startswith("claude-") for n in noms):
            bloq.append("catalogue ou plugin : un nom commence par « claude- »")
        elif v.get("outils") != versions:
            bloq.append(f"versions.json {v.get('outils')} ≠ SKILL.md {versions}")
        elif not (v.get("mallette") == pj.get("version") == entree[0].get("version") == c.get("metadata", {}).get("version")):
            bloq.append("numéro de la mallette différent entre versions.json, plugin.json et le catalogue")
        else:
            ok.append(f"dépôt : catalogue, plugin.json et versions.json conformes aux SKILL.md — mallette {v.get('mallette')}")
    except Exception as e:
        bloq.append(f"dépôt : catalogue, plugin.json ou versions.json illisible — {e}")

# 16. En-têtes YAML : aucune clé en double — l'import de claude.ai refuse ce qu'un analyseur permissif accepte
doubles_trouves = False
for o in OUTILS:
    m = re.match(r"^---\n(.*?)\n---\n", lire(RACINE / o / "SKILL.md"), re.S)
    if not m:
        bloq.append(f"{o} : en-tête YAML introuvable")
        continue
    cles = re.findall(r"^([A-Za-z][\w-]*)\s*:", m.group(1), re.M)
    doubles = sorted({k for k in cles if cles.count(k) > 1})
    if doubles:
        doubles_trouves = True
        bloq.append(f"{o} : clé en double dans l'en-tête — {', '.join(doubles)} ; l'import de claude.ai refusera le fichier")
if not doubles_trouves:
    ok.append(f"en-têtes : aucune clé en double dans {len(OUTILS)} outils")

for m in ok:
    print(f"OK        {m}")
for m in att:
    print(f"ATTENTION {m}")
for m in bloq:
    print(f"BLOQUANT  {m}")
print(f"— {len(bloq)} bloquant(s), {len(att)} attention(s)")
sys.exit(2 if bloq else (1 if att else 0))
