# Carte du déroulé — immo-parcours

**Pour la maintenance seulement : ne la lis pas pour travailler.** Le déroulé qui fait foi est
dans `SKILL.md`. Cette carte le résume, et le script de maintenance vérifie qu'elle porte
exactement les mêmes étapes. Si elles divergent, c'est la carte qu'on corrige.

```mermaid
flowchart TD
  A(["/immo-parcours"]) --> B["Bloc d'amorçage commun<br/>exception : lit tout clients-types.md"]
  B --> C{"Dossier de son ordinateur ?"}
  C -->|non| MI["Miroir en lecture seule<br/>sinon mémoire : installée → ne pas relancer l'init"]
  C -->|oui| N["Niveau lu sur le remplissage de clients-types.md"]
  MI --> U{"Quel usage ?"}
  N --> U
  U -->|montre-moi| MO["MONTRER · « Ta fiche client type », frise, USP<br/>passerelle une fois s'il a dit persona"]
  U -->|mail, note, avis collé| L["LIRE · fiche · étape · ce qu'il lui faut<br/>4 lignes, rien écrit"]
  L --> AP["APPARIER via 01_BIENS/index.md"]
  U -->|formation, installation| P1
  subgraph APP["APPROFONDIR"]
    P1["1 · Parcours par famille, 4 cases marquées par étape"] --> P2
    P2["2 · Chaque fiche : 2 ou 3 étapes où elle s'attarde"] --> P3
    P3["3 · USP placée sur la frise"] --> P4
    P4["4 · 3 écrans + contrôle"]
  end
  P4 --> V{"Il valide la ligne ?"}
  V -->|oui| W["Écrit clients-types.md · §4 · colonne d'index.md<br/>« remplace le fichier dans ton projet »"]
  V -->|non| K["Rien n'est écrit"]
  W --> F["Tableau de bord + verifier.py, qui lit les tableaux"]
```
