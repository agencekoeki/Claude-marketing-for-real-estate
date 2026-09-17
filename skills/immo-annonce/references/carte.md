# Carte du déroulé — immo-annonce

**Pour la maintenance seulement : ne la lis pas pour travailler.** Le déroulé qui fait foi est
dans `SKILL.md`. Cette carte le résume, et le script de maintenance vérifie qu'elle porte
exactement les mêmes étapes. Si elles divergent, c'est la carte qu'on corrige.

```mermaid
flowchart TD
  A(["/immo-annonce"]) --> B["Bloc d'amorçage commun · niveau lu sur disque"]
  B --> C{"Profil et dossier ?"}
  C -->|sans profil| D["Descriptif + mentions en blancs visibles, puis /immo-init"]
  C -->|web ou téléphone| E["Miroir, sinon mémoire : installée → ne pas relancer l'init<br/>sortie : stockage en ligne qui sait écrire, sinon téléchargement"]
  C -->|profil présent| S1
  D --> S1
  E --> S1
  S1["1 · Fiche des faits · 3 repères à distance mesurée"] --> S1b
  S1b["1 bis · À côté : 5 annonces au plus · prix signalé, jamais décidé"] --> S2
  S2["2 · Trois lecteurs · 1 fiche acquéreur · USP incarnée · 1 question vendeur"] --> S3
  S3["3 · Écrire : textes à lui · canal de dépôt · titre à 5 places · mentions depuis cadre.md"] --> S4
  S4["4 · Ordre des photos · contrôle fait par fait · livraison"] --> W["01_BIENS/‹bien›/annonce.md"]
  W --> IX["01_BIENS/index.md : ligne du bien créée ou mise à jour<br/>sans adresse ni propriétaire"]
  W --> RS["lu par immo-reseaux-sociaux : fait distinctif"]
  IX --> PA["lu par immo-parcours pour apparier"]
  W --> F["Tableau de bord + verifier.py"]
```
