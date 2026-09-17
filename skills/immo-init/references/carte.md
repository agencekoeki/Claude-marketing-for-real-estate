# Carte du déroulé — immo-init

**Pour la maintenance seulement : ne la lis pas pour travailler.** Le déroulé qui fait foi est
dans `SKILL.md`. Cette carte le résume, et le script de maintenance vérifie qu'elle porte
exactement les mêmes étapes. Si elles divergent, c'est la carte qu'on corrige.

```mermaid
flowchart TD
  A(["/immo-init"]) --> B{"Surface, test fonctionnel<br/>dossier de son ordinateur ? navigateur ? recherche dans les conversations ?"}
  B -->|pas de dossier| Q{"« Ta zone de saisie affiche Chat et Cowork ? »<br/>et plan payant ?"}
  Q -->|compte gratuit| XF["Noter §13 · produire sans dossier en attendant"]:::stop
  Q -->|payant| X1["STOP : dicter un projet « Partir de zéro »<br/>onglet Cowork ou nouvelle interface · chemin réel noté §13"]:::stop
  B -->|dossier sans navigateur ni projets| X2["STOP : relancer depuis Claude Desktop<br/>cas Claude Code"]:::stop
  B -->|OK, manques notés en §13| C{"00_MOI/profil.md ?"}
  C -->|absent mais 01_BIENS ou 02_PUBLICATIONS| X3["Demander : dossier renommé ?"]:::stop
  C -->|installation interrompue| R["Reprise par l'en-tête d'état"]
  C -->|installation terminée| U["Mise à jour : ne toucher qu'à ce qu'il corrige"]
  C -->|absent| M{"Mode ?"}
  M -->|salle 60 à 90 min| S1
  M -->|complet 2 à 3 h| S1
  R --> E3
  S1["1 · Énoncer 3 règles puis lire metier.md"] --> S2
  S2["2 · Arborescence · gabarits · en-tête d'état · CLAUDE.md · copie · tableau de bord"] --> E3
  E3["3 · Enquête, écrite source par source<br/>public d'abord · puis privé par l'ordre d'accès : connecteur, dossier synchronisé, export, questions"] --> S4
  S4["4 · Montrer le profil, compter les trous"] --> S5
  S5["5 · Questions : 8 au plus, une passe"] --> S6
  S6["6 · Voix : choix forcés → textes réels → texte-test corrigé"] --> S7
  S7["7 · Fiches clients types → USP dérivée"] --> S8
  S8["8 · Récurrences → 1 tâche : à distance sans dossier, en local avec"] --> S9
  S9["9 · Ancrage : instructions · miroir daté · mémoire sans chemin ni client"] --> S10
  S10["10 · Contrôle 6 points → relevé → tableau de bord → verifier.py"] --> Z(["Clôture"])
  classDef stop fill:#fde2e1,stroke:#c0392b,color:#111
```
