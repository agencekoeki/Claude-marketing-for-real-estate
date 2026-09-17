#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Versions de la mallette. Une seule source : la ligne « Version » de chaque SKILL.md.

  python3 .github/scripts/versions.py --verifier [--etiquette v2.4.0]
  python3 .github/scripts/versions.py --ecrire --mallette 2.5.0

--verifier : versions.json, plugin.json et le catalogue disent-ils la même chose que les SKILL.md ?
--ecrire   : réécrit versions.json et les numéros de plugin.json et du catalogue depuis les SKILL.md.
"""
import argparse, json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parents[2]
OUTILS = ["immo-init", "immo-parcours", "immo-annonce", "immo-reseaux-sociaux", "immo-penser-savoir"]
DEPOT = "https://github.com/agencekoeki/Claude-marketing-for-real-estate"
CATALOGUE, PLUGIN, VERSIONS = RACINE / ".claude-plugin" / "marketplace.json", RACINE / ".claude-plugin" / "plugin.json", RACINE / "versions.json"


def lues():
    out = {}
    for o in OUTILS:
        m = re.search(r"^\*\*Version (\d+\.\d+)", (RACINE / "skills" / o / "SKILL.md").read_text(encoding="utf-8"), re.M)
        if not m:
            sys.exit(f"BLOQUANT  {o} : ligne « Version » introuvable")
        out[o] = m.group(1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", action="store_true"); ap.add_argument("--ecrire", action="store_true")
    ap.add_argument("--mallette"); ap.add_argument("--etiquette")
    a = ap.parse_args()
    outils = lues()
    catalogue = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    plugin = next(p for p in catalogue["plugins"] if p["name"] == "mallette-immo")
    manifeste = json.loads(PLUGIN.read_text(encoding="utf-8"))
    if a.ecrire:
        mallette = a.mallette or json.loads(VERSIONS.read_text(encoding="utf-8"))["mallette"]
        VERSIONS.write_text(json.dumps({"mallette": mallette, "outils": outils, "depot": DEPOT,
                                        "telechargements": DEPOT + "/releases/latest"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        plugin["version"] = catalogue["metadata"]["version"] = manifeste["version"] = mallette
        CATALOGUE.write_text(json.dumps(catalogue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        PLUGIN.write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK        versions.json et catalogue écrits : mallette {mallette}, {outils}")
        return
    v = json.loads(VERSIONS.read_text(encoding="utf-8"))
    ecarts = []
    if v.get("outils") != outils:
        ecarts.append(f"versions.json {v.get('outils')} ≠ SKILL.md {outils}")
    if not (v.get("mallette") == plugin.get("version") == catalogue["metadata"].get("version") == manifeste.get("version")):
        ecarts.append("numéro de la mallette différent entre versions.json, plugin.json et le catalogue")
    if a.etiquette and a.etiquette != "v" + str(v.get("mallette")):
        ecarts.append(f"l'étiquette {a.etiquette} ne correspond pas à la mallette {v.get('mallette')}")
    for e in ecarts:
        print(f"BLOQUANT  {e}")
    if ecarts:
        sys.exit(1)
    print(f"OK        versions conformes : mallette {v['mallette']}, {len(outils)} outils")


if __name__ == "__main__":
    main()
