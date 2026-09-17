# Banc d'essai de verifier.py : mêmes dossiers synthétiques, version d'origine contre version 7.5
import subprocess, shutil, pathlib, re
import sys
# Usage : python3 banc-verifier.py <ancien verifier.py> <nouveau verifier.py> <dossier assets d'immo-init>
V1, V2, A = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
BASE = pathlib.Path("/tmp/banc")

def installation(nom):
    d = BASE / nom
    shutil.rmtree(d, ignore_errors=True)
    for s in ["00_MOI", "01_BIENS", "02_PUBLICATIONS/brouillons", "02_PUBLICATIONS/publies", "03_RESSOURCES", ".claude/skills"]:
        (d / s).mkdir(parents=True, exist_ok=True)
    for g in ["profil", "voix", "cadre", "recurrences", "clients-types"]:
        shutil.copy(A / f"{g}.template.md", d / "00_MOI" / f"{g}.md")
    shutil.copy(A / "CLAUDE.template.md", d / "CLAUDE.md")
    return d

def remplace(d, fichier, old, new):
    p = d / "00_MOI" / fichier
    t = p.read_text(encoding="utf-8"); assert old in t, (fichier, old); p.write_text(t.replace(old, new, 1), encoding="utf-8")

def ajoute(d, fichier, texte):
    p = d / "00_MOI" / fichier
    p.write_text(p.read_text(encoding="utf-8") + texte, encoding="utf-8")

ETAPE3 = "| 3. Le choix de l'agent | | | | |"
cas = {}
d = installation("S1"); cas["S1 gabarit frais"] = d
d = installation("S2"); remplace(d, "clients-types.md", ETAPE3, "| 3. Le choix de l'agent | [dit 2026-09] plus cher que l'autre — M. Exemple 06 12 34 56 78, test@exemple.fr | [dit 2026-09] rappel le soir même | [dit 2026-09] estimation écrite | [dit 2026-09] confrère moins cher |"); cas["S2 tel+mail dans une case"] = d
d = installation("S3"); ajoute(d, "clients-types.md", "\n- M. Exemple 06 12 34 56 78\n"); cas["S3 tel en ligne NON marquée"] = d
d = installation("S4"); ajoute(d, "clients-types.md", "\n- [dit 2026-09] M. Exemple 06 12 34 56 78\n"); cas["S4 tel en ligne marquée"] = d
d = installation("S5"); remplace(d, "clients-types.md", ETAPE3, "| 3. Le choix de l'agent | [dit 2026-09] vous êtes plus cher | [dit 2026-09] rappel le soir même | [dit 2026-09] estimation écrite | [dit 2026-09] confrère moins cher |"); cas["S5 parcours propre (témoin)"] = d
d = installation("S6"); remplace(d, "clients-types.md", ETAPE3, "| 3. Le choix de l'agent | vous êtes plus cher | | | |"); cas["S6 case remplie sans marqueur"] = d
d = installation("S7"); (d / "01_BIENS" / "t3-centre-2026-09").mkdir(); cas["S7 bien sans index.md"] = d

def run(v, d):
    r = subprocess.run(["python3", v, str(d)], capture_output=True, text=True)
    o = r.stdout
    mes = re.findall(r"MESURE    clients-types[^\n]*", o)
    return r.returncode, o.count("BLOQUANT"), o.count("ATTENTION"), " | ".join(m.replace("MESURE    ", "") for m in mes), o

print(f"{'scénario':34} {'v1 code/BLOQ/ATT':18} {'v2 code/BLOQ/ATT':18}")
details = {}
for nom, d in cas.items():
    c1, b1, a1, m1, o1 = run(V1, d)
    c2, b2, a2, m2, o2 = run(V2, d)
    print(f"{nom:34} {c1}/{b1}/{a1:<14} {c2}/{b2}/{a2}")
    print(f"{'':34} v1 · {m1}")
    print(f"{'':34} v2 · {m2}")
    details[nom] = (o1, o2)
print("\n--- S1 : ATTENTION restantes en v2 (gabarit frais) ---")
print("\n".join(l for l in details["S1 gabarit frais"][1].splitlines() if l.startswith("ATTENTION")))
print("\n--- S6 v2 / S7 v2 : lignes nouvelles ---")
print("\n".join(l for l in details["S6 case remplie sans marqueur"][1].splitlines() if "case sans marqueur" in l))
print("\n".join(l for l in details["S7 bien sans index.md"][1].splitlines() if "index.md" in l))
print("\n--- S2/S3 v2 : BLOQUANT ---")
print("\n".join(l for l in details["S2 tel+mail dans une case"][1].splitlines() if l.startswith("BLOQUANT")))
print("\n".join(l for l in details["S3 tel en ligne NON marquée"][1].splitlines() if l.startswith("BLOQUANT")))
