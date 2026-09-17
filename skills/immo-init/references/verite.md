# Les fichiers de vérité

## Ce que l'init est vraiment

Une enquête dont la seule sortie durable est **un jeu de fichiers**. Tout le reste de la
mallette n'est que des lecteurs de ces fichiers. Si un outil produit quelque chose de faux
alors que les fichiers sont justes, c'est l'outil qui est en cause ; si les fichiers sont
faux, tous les outils le sont — et c'est pour ça que l'init est le seul à y écrire.

Ce fichier est le modèle unique : **qui écrit quoi, qui lit quoi, quand, pour quoi, et sur
quelle surface ça arrive.** Tout outil de la mallette doit pouvoir s'y vérifier.

---

## La table

| Fichier | Écrit par | Lu par | Quand | Pour |
|---|---|---|---|---|
| `00_MOI/profil.md` | init ; `immo-parcours` place l'USP ; `immo-reseaux-sociaux` la construit au premier carnet si elle est restée en `[à confirmer]` ; les autres proposent une ligne — toujours validée par lui | tous, à chaque production | avant tout | l'en-tête d'état, la zone, l'USP (§4) **placée sur le parcours**, la façon de travailler (§6), le glossaire (§7), où il publie (§8), ce qui a marché (§10), les outils (§13) |
| `00_MOI/voix.md` | init ; les autres proposent | tout outil qui rédige | avant d'écrire | les échantillons d'abord, les arbitrages, les interdits, le journal des corrections |
| `00_MOI/cadre.md` | init ; lui à la main | tout outil qui publie ou envoie | avant tout ce qui sort | ce qu'il a le droit de faire, les mentions qu'il publie déjà, l'identité visuelle, les portails et leurs contraintes |
| `00_MOI/clients-types.md` | init ; `immo-parcours` approfondit ; les autres proposent | tout outil qui écrit pour un tiers | avant d'écrire | l'index, une seule fiche — déclencheur, objection, levier, qui tranche — et **le parcours** par famille : les étapes, et à chacune ce que le client se demande, ce qui le fait avancer, ce que l'agent fait |
| `00_MOI/recurrences.md` | init ; les autres proposent | tout outil qui automatise ou récolte | quand une tâche revient | ce qui tourne, ce qui a été écarté, les candidats |
| `CLAUDE.md` | init | Cowork et Claude Code, automatiquement | à l'ouverture du dossier | le rangement, les outils, le pointeur vers `00_MOI/` — la seule instruction que Claude Code voit |
| `.claude/skills/<outil>/` | chaque outil, lui-même | Claude Code | à l'ouverture du dossier | les outils, disponibles sans installation ailleurs |
| `tableau-de-bord.html` | init, puis chaque outil en fin de course | lui | quand il veut savoir où il en est | l'état de ses fichiers, jamais un rapport |
| `01_BIENS/index.md` | init depuis son stock ; `immo-annonce` tient la ligne de chaque bien ; `immo-parcours` propose la colonne « fiche acquéreur probable » | `immo-parcours` pour apparier, `immo-annonce` | quand un client est placé, quand un bien entre ou sort | une ligne par bien : type, surface, secteur, statut, fiche acquéreur probable — jamais l'adresse ni le propriétaire |
| `01_BIENS/<bien>/annonce.md` | `immo-annonce` | `immo-reseaux-sociaux` | quand il publie sur ce bien | le fait distinctif, les repères mesurés, le statut, le bilan |
| `02_PUBLICATIONS/carnet.md`, `brouillons/` — les kits, et à côté de chacun les fichiers fabriqués —, `publies/` | `immo-reseaux-sociaux` | lui-même, et le tableau de bord | à chaque carnet, à chaque écriture | la réserve, ce qui attend, ce qui est sorti et son effet |
| `03_RESSOURCES/` | lui, et l'init qui lui dit quoi y mettre | tout outil qui fabrique un visuel | quand un visuel se fabrique | son logo, sa photo, tels quels — des fichiers, pas des faits |

**Trois choses ne sont dans aucun fichier, et c'est voulu :** les chiffres de marché, les
données de tiers, et ce qu'un outil a lu sur une page. Le premier périme, le deuxième est
interdit, le troisième est de la matière du jour.

---

## Les trois surfaces, et comment la vérité y arrive

**Claude Desktop, avec un dossier connecté** — l'onglet Cowork, ou la conversation unique qui
le remplace par vagues depuis septembre 2026. Le dossier est connecté à la séance : tout est lu
directement, tout s'écrit directement. C'est la surface de référence, et la seule où l'init
tourne. Plans payants seulement.

**Claude Code.** Ouvert dans le dossier, il charge `CLAUDE.md` automatiquement et trouve les
outils dans `.claude/skills/`. Il lit `00_MOI/` parce que `CLAUDE.md` et le bloc d'amorçage de
chaque outil le lui disent. Pas de projet, pas d'instructions de projet : **`CLAUDE.md` est
sa seule porte**, et il doit porter le pointeur vers l'USP et la façon de travailler.

**Claude web et mobile.** Pas de dossier de son ordinateur — même quand la session a un espace
de travail ou tourne dans le cloud : ce qui s'y écrit ne rejoint pas ses fichiers. La vérité n'y arrive que par **la connaissance du
projet** — les fichiers ajoutés au projet avec le bouton « + » — et par les instructions du
projet. C'est le miroir : un instantané daté, en lecture seule, qui ne se met pas à jour tout
seul.

**Le web produit dans une boîte de dépôt.** Ce qu'un outil fabrique sans dossier — un post,
une annonce — devient un vrai fichier, le même que celui du dossier, déposé dans son stockage en ligne par le connecteur s'il est branché et sait écrire — Google
Drive, ou OneDrive si Microsoft 365 a l'écriture activée —, sinon téléchargé. Puis rapatrié dans
le dossier à la prochaine séance sur l'ordinateur, et effacé du stockage. La boîte de dépôt est en écriture
seule et temporaire, comme le miroir est en lecture seule et daté : **ni l'un ni l'autre n'est
la vérité.**

**Les tâches planifiées.** À distance, elles lisent ses connecteurs et les fichiers de son compte,
jamais son dossier. Une tâche liée à un dossier ne tourne qu'en local, Claude Desktop ouvert.
Le détail est dans `tri-recurrences.md`.

**La règle qui découle des trois :** le dossier est la source, le reste des copies. Depuis
son téléphone il lit et il produit avec ce qu'il y a ; il ne modifie `00_MOI/` que depuis son
ordinateur. Et **chaque fois qu'un fichier de `00_MOI/` change, le miroir est périmé** — un
outil qui vient de proposer une ligne le dit en une phrase : « pense à remplacer le fichier
dans ton projet ».

---

## Le miroir, procédure exacte

**D'abord vérifier en trente secondes, parce qu'on ne sait pas d'avance :** il ouvre son
projet sur le web ou son téléphone et regarde le panneau de connaissance du projet. Si ses
cinq fichiers de `00_MOI/` y sont déjà — la synchronisation du projet créé « de zéro » les y
a portés —, il n'y a rien à faire, on consigne, on passe.

**Sinon, deux clics par fichier :** dans le projet, le bouton **« + »** de la connaissance du
projet, puis choisir le fichier. Cinq fois. Les fichiers portent leur date dans leur nom —
`profil-2026-09.md` — pour que dans six mois on sache qu'ils sont un instantané.

**Ce qui va dans le miroir :** les cinq fichiers de `00_MOI/`. Rien d'autre. Ni ses biens, ni
ses brouillons, ni ses ressources : le miroir sert à ce qu'il puisse produire depuis son
téléphone avec sa voix et son cadre, pas à répliquer son disque.

**Quand le rafraîchir :** chaque fois qu'il modifie un fichier de `00_MOI/` à la main ou
qu'un outil y a proposé une ligne, et sinon tous les trimestres. Le tableau de bord porte la
date du dernier miroir.

---

## Ce que chaque outil doit savoir, et où il l'apprend

**Le bloc d'amorçage** en tête de chaque `SKILL.md` de production : la liste de `00_MOI/`, quand
ouvrir chaque fichier, ce qu'est un dossier connecté, l'auto-installation, le dossier renommé,
Claude Code, le relais. Il est identique dans tous les outils, mot pour mot ; `amorcage.md` en
porte la version de référence, et un script de maintenance le contrôle avant chaque livraison.
Ce qui est propre à un outil s'écrit après le bloc, jamais dedans. Un outil qui ne le porte pas
n'est pas un outil de la mallette.

**`CLAUDE.md`** pour ce qui vaut dans le dossier quel que soit l'outil.

**Ce fichier** pour le modèle entier — et il vit dans l'init seulement, parce que l'init est
le seul à écrire la vérité et donc le seul à devoir en connaître la carte.

---

## Ce qui n'est pas encore un fichier, et devra l'être

Quand un outil futur aura besoin d'une vérité que la table ne porte pas, **on l'ajoute ici
d'abord**, avec son écrivain et ses lecteurs, avant d'écrire l'outil. C'est la règle qui
empêche la dérive : un fichier de vérité n'apparaît jamais par nécessité locale d'un skill.

**Un cas d'école de cette règle : le parcours client.** Il aurait pu devenir un sixième fichier.
Il ne l'est pas : c'est la dimension du temps de `clients-types.md`, et l'USP s'y place plutôt
que de flotter. `immo-parcours` est le seul outil autorisé à approfondir ces deux fichiers —
sous la même règle que tous : il propose la ligne, l'utilisateur valide, il écrit.

Ce qu'on voit venir : `immo-suivi` aura besoin d'un journal par client — un fichier par
dossier en cours, dans un `04_DOSSIERS/` qui n'existe pas encore. `immo-avis-valeur`, à venir aussi,
aura besoin de ses références de prix — et c'est le seul cas où un chiffre de marché entrera dans
un fichier, daté, dans le dossier du bien, jamais dans `00_MOI/`.
