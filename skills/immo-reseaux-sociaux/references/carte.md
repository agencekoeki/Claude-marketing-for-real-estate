# Carte du déroulé — immo-reseaux-sociaux

**Pour la maintenance seulement : ne la lis pas pour travailler.** Le déroulé qui fait foi est
dans `SKILL.md`. Cette carte le résume, et le script de maintenance vérifie qu'elle porte
exactement les mêmes étapes. Si elles divergent, c'est la carte qu'on corrige.

```mermaid
flowchart TD
  A(["/immo-reseaux-sociaux"]) --> B["Bloc d'amorçage commun · niveau lu sur disque"]
  B --> L{"Lien collé ?"}
  L -->|oui| URL["depuis-une-page d'abord, au navigateur visible"]
  L -->|non| MODE{"Quel mode ?"}
  URL --> MODE
  MODE -->|quoi dire ce mois-ci| CAR
  MODE -->|mon post du jour| PDJ
  MODE -->|écris un post| E1
  subgraph CARNET["CARNET · planifiable à distance si messagerie et agenda par connecteur"]
    CAR["Récolte de traces réelles"] --> CU["USP auditée, construite si à confirmer"]
    CU --> CS["6 à 8 sujets"]
    CS --> CW["02_PUBLICATIONS/carnet.md"]
  end
  subgraph POST["POST DU JOUR"]
    PDJ{"Carnet existant ?"} -->|oui| PF["3 filtres : rythme · missions · échéances"]
    PF --> PK["Paquet : textes, visuel ou prompt, 3 lignes"]
  end
  PDJ -->|non : carnet d'abord| CAR
  subgraph ECR["ÉCRITURE"]
    E1["1 · Mission → sujet → 1 fiche client"] --> E2["2 · Ce qui est déjà publié"]
    E2 --> E3["3 · Angle · plateforme et format"]
    E3 --> E4["4 · Écrire depuis ses textes · kit : visuel fabriqué par le moteur, ou prompt"]
    E4 --> E4b["4 bis · Aperçu avec le trait de coupe"]
    E4b --> E5["5 · Contrôle → livrer → brouillons/ ou stockage en ligne"]
  end
  E5 --> F["Tableau de bord + verifier.py"]
  CW --> F
```
