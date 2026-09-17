# Carte de la mallette — qui écrit, qui lit

**Pour la maintenance seulement : ne la lis pas pour travailler.** La table qui fait foi est
dans `verite.md`. Cette carte le résume, et le script de maintenance vérifie qu'elle porte
exactement les mêmes étapes. Si elles divergent, c'est la carte qu'on corrige.

```mermaid
flowchart LR
  subgraph SK["Les 5 outils, sur le compte"]
    INIT["immo-init 8.1<br/>installe · enquête · écrit la vérité"]
    PAR["immo-parcours 1.10<br/>creuse · montre · lit un mail"]
    ANN["immo-annonce 3.9<br/>annonce portail et site"]
    RS["immo-reseaux-sociaux 10.3<br/>carnet · post du jour · écriture"]
    PS["immo-penser-savoir 1.1<br/>trie su et supposé · n'écrit rien"]
  end
  subgraph DOS["Dossier de son ordinateur : la seule source de vérité"]
    subgraph MOI["00_MOI"]
      PROF["profil.md<br/>en-tête d'état · §4 USP"]
      VOIX["voix.md"]
      CAD["cadre.md"]
      CT["clients-types.md<br/>fiches + parcours"]
      REC["recurrences.md"]
    end
    IDX["01_BIENS/index.md<br/>une ligne par bien"]
    ANMD["01_BIENS/‹bien›/annonce.md<br/>fait distinctif en tête"]
    PUB["02_PUBLICATIONS<br/>carnet · brouillons · publies"]
    CLMD["CLAUDE.md + .claude/skills<br/>pour Claude Code"]
  end
  MIR["Miroir : 5 fichiers datés<br/>connaissance du projet, lue sur web et mobile"]
  MEM["Mémoire du compte<br/>pointeur, jamais le contenu"]
  INIT -->|écrit les 5 fichiers| MOI
  INIT -->|écrit, se copie| CLMD
  INIT -.->|6 lignes validées par lui| MEM
  PAR -->|propose, il valide| CT
  PAR -->|place l'USP| PROF
  PAR -->|propose la fiche probable| IDX
  RS -->|construit l'USP au 1er carnet si à confirmer| PROF
  ANN -->|écrit| ANMD
  ANN -->|tient la ligne du bien| IDX
  RS -->|écrit| PUB
  ANMD -->|fait distinctif, repères| RS
  IDX -->|apparier| PAR
  MOI -.->|lu avant de produire| ANN
  MOI -.->|lu avant de produire| RS
  MOI -.->|copie manuelle datée| MIR
  MEM -.->|sans dossier ni miroir : ne pas relancer l'init| RS
  MOI -.->|périmètre, lecture seule| PS
```
