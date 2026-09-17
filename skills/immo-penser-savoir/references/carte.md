# Carte du déroulé — immo-penser-savoir

**Pour la maintenance seulement : ne la lis pas pour travailler.** Le déroulé qui fait foi est
dans `SKILL.md`. Cette carte le résume, et le script de maintenance vérifie qu'elle porte
exactement les mêmes étapes. Si elles divergent, c'est la carte qu'on corrige.

```mermaid
flowchart TD
  A["Une affirmation, un texte, une réponse d'IA"] --> E1["1 · Recueillir ce qu'on vérifie, et pour quoi"]
  E1 --> E2["2 · Découper en affirmations"]
  E2 --> E3["3 · Ranger, et éprouver"]
  E3 --> S{"Une ancre qu'on peut ouvrir ?"}
  S -->|oui| SAV["SAVOIR : source, date, périmètre"]
  S -->|non, mais on pourrait| VER["À VÉRIFIER : la question qui tranche"]
  S -->|non| PEN["PENSER : écrit comme tel"]
  SAV --> E4["4 · Rendre : le tri, la version qu'il peut écrire, la question suivante"]
  VER --> E4
  PEN --> E4
  E4 -.->|écrire ensuite| OUT["immo-annonce, immo-reseaux-sociaux"]
```
