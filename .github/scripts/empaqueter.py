#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fabrique les fichiers d'une version : un fichier par outil, en .zip et en .skill — le même contenu,
dossier de l'outil à la racine, licence jointe —, et les notes tirées du journal des versions.

  python3 .github/scripts/empaqueter.py dist
"""
import pathlib, re, shutil, sys, zipfile

RACINE = pathlib.Path(__file__).resolve().parents[2]
OUTILS = ["immo-init", "immo-parcours", "immo-annonce", "immo-reseaux-sociaux", "immo-penser-savoir"]
DEPOT = "https://github.com/agencekoeki/Claude-marketing-for-real-estate"
IGNORES = {"__pycache__", ".DS_Store"}


def main():
    sortie = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "dist"); sortie.mkdir(parents=True, exist_ok=True)
    for o in OUTILS:
        dossier = RACINE / "skills" / o
        if not (dossier / "SKILL.md").exists():
            sys.exit(f"BLOQUANT  {o} : SKILL.md absent")
        chemin = sortie / f"{o}.zip"
        with zipfile.ZipFile(chemin, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(dossier.rglob("*")):
                if f.is_file() and not IGNORES & set(f.parts):
                    z.write(f, pathlib.Path(o) / f.relative_to(dossier))
            z.write(RACINE / "LICENSE", pathlib.Path(o) / "LICENSE")
        shutil.copyfile(chemin, sortie / f"{o}.skill")
        print(f"OK        {o}.zip et {o}.skill")
    journal = (RACINE / "skills" / "immo-init" / "CHANGELOG.md").read_text(encoding="utf-8")
    entree = re.search(r"^\*\*\d+\.\d+ — .*?(?=\n\n\*\*\d+\.\d+ — |\Z)", journal, re.M | re.S)
    liens = "\n".join(f"- {o} : [.zip]({DEPOT}/releases/latest/download/{o}.zip) · [.skill]({DEPOT}/releases/latest/download/{o}.skill)" for o in OUTILS)
    (sortie / "notes.md").write_text(
        "## Ce qui change\n\n" + (entree.group(0).strip() if entree else "Voir le journal des versions.") +
        "\n\n## Installer ou mettre à jour\n\n" +
        "Par le catalogue de plugins : vérifier les mises à jour. Par fichiers : réimporter un fichier par outil, en .zip ou en .skill — le même contenu.\n\n" + liens + "\n",
        encoding="utf-8")
    print("OK        notes.md")


if __name__ == "__main__":
    main()
