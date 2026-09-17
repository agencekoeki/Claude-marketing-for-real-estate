# Le projet Cowork — ancrer la mallette au niveau du compte

## Pourquoi ça compte pour ce métier

Un agent immobilier n'est pas à son bureau. Il est en voiture entre deux visites, avec son
téléphone. Le dossier local ne le suit pas là. Un projet, si — à une condition, expliquée
plus bas, qui se joue au moment de la création et ne se rattrape pas après.

## À quoi il sert vraiment

Cinq fonctions, et le stagiaire n'en soupçonne qu'une. Dis-les-lui, parce qu'un projet dont on
ne comprend pas l'usage est un projet qu'on n'ouvre pas.

**Il contient le dossier.** C'est l'atelier : le dossier de travail vit dedans, et c'est là
que les outils écrivent.

**Il porte ce qui est vrai de toutes les séances.** Ses instructions s'appliquent à chaque
tâche du projet, y compris quand aucun outil ne se déclenche. C'est son seul filet dans ce
cas-là.

**Il met son profil dans sa poche.** Les fichiers déposés se lisent depuis son téléphone,
là où le dossier de son ordinateur n'existe pas.

**Il cloisonne la mémoire.** Ce que Claude apprend ici ne se mélange pas à ses autres usages,
et ce qu'il apprend ailleurs ne vient pas polluer son travail.

**Il porte ses tâches planifiées.** Une tâche installée dans le projet hérite de ses
instructions et de son contexte.

Et une chose qu'il faut dire aussi : **un seul projet, pas un par outil.** Un projet est lié à
un dossier ; en créer un second le couperait de `00_MOI/` ou du compte. Le projet est
l'atelier, les outils sont ce qu'on y prend.

## Le nom, et ce qui l'accompagne

Le nom est ce qu'il verra dans son panneau de gauche pendant des mois. **Tu n'en proposes
aucun** : un nom qu'il a choisi est un objet qui est à lui, et un nom qu'on lui a donné reste
l'outil de quelqu'un d'autre. Deux garde-fous seulement — pas « assistant », pas « Claude »,
c'est son dossier, pas un outil.

Les champs que je connais d'un projet sont ses instructions, ses tâches planifiées, son
contexte et sa mémoire. **Si son application propose en plus une description ou un résumé,
traite-la comme la première ligne des instructions** — une phrase qui dit qui il est et à quoi
sert cet espace — et n'y mets rien d'autre. Si le champ n'existe pas, n'en parle pas.

## Ce qu'un projet porte

Quatre choses, et c'est ce qui en fait le bon contenant pour la mallette :

- **des instructions**, appliquées à toutes les tâches du projet
- **des tâches planifiées** propres au projet
- **un contexte** : un dossier local, un projet de chat lié, ou une URL
- **une mémoire**, cloisonnée au projet

Les projets n'existent pas dans Claude Code. Ils demandent un plan payant — Pro, Max, Team ou
Enterprise — et une version récente de l'application. Sur une partie des comptes Pro et Max,
le chat et Cowork ne font plus qu'une conversation depuis septembre 2026 : les projets y
marchent partout, mais les écrans décrits ici peuvent différer.

---

## La règle qui décide de tout

**Le mode de création décide si le projet suit le stagiaire sur son téléphone.**

Un projet créé dans Cowork est enregistré sur le compte et récupérable depuis les autres
appareils. Un projet créé **à partir d'un dossier déjà existant** sur l'ordinateur reste sur
cet ordinateur et n'est pas enregistré sur le compte.

Conséquence pratique, et c'est le piège : si le stagiaire crée d'abord son dossier puis
choisit « Utiliser un dossier existant », il perd le mobile. Et ça ne se rattrape pas sans
tout refaire.

**Le bon chemin, et le seul à recommander en formation : « Partir de zéro ».** Il crée le
dossier lui-même, avec ses instructions et ses fichiers, et il est enregistré sur le compte.
Un seul geste au lieu de deux, et rien à rattraper.

Si le stagiaire arrive avec un projet déjà créé depuis un dossier existant, ne le fais pas
tout refaire séance tenante : l'init fonctionne quand même, tout le local marche. Note en
section 13 que le projet n'est pas synchronisé, dis-lui en une phrase ce que ça lui coûte —
pas d'accès depuis son téléphone — et propose de le refaire plus tard, à froid.

---

## Le protocole, dans l'ordre

### Avant l'init — la création

C'est lui qui clique, pas toi. Tu dictes, il fait. Quatre étapes :

1. Ouvrir Claude Desktop, panneau de gauche, **Projects**, bouton « + » — dans l'onglet
   **Cowork** si la zone de saisie affiche encore « Chat » et « Cowork »
2. Choisir **« Start from scratch » / « Partir de zéro »** — surtout pas « dossier existant »
3. Nommer le projet. Il choisit, tu ne proposes rien
4. Choisir où le dossier est créé sur son ordinateur. Dans ses documents, à côté de ses
   autres dossiers de travail — pas le bureau, pas les téléchargements. Trois raisons : il le
   gardera des années, il doit être là où il range ce qui compte, et **c'est aussi un
   répertoire de projet Claude Code** dont le `CLAUDE.md` sera lu automatiquement s'il
   l'ouvre là un jour. Fais-lui noter le chemin

S'il ne trouve pas ces entrées, trois causes, dans cet ordre : **la nouvelle interface** — plus
de « Chat » ni de « Cowork » dans la zone de saisie : les écrans diffèrent, ce n'est pas une
panne ; **un compte gratuit**, qui n'a pas de projet ; puis **une version d'application trop
ancienne**. Ne devine pas un chemin de menu que tu ne vois pas : fais-lui décrire son écran.

### Pendant l'init — rien de spécial

L'init travaille dans le dossier du projet comme dans n'importe quel dossier connecté. Elle
crée `00_MOI/` et le reste de l'arborescence.

## Qui dit quoi : quatre endroits, quatre portées

À ce stade, quatre choses portent des instructions. Elles ne sont pas interchangeables, et
les confondre produit soit de la contradiction, soit du texte mort.

| Où | Lu quand | Porte | Ne porte jamais |
|---|---|---|---|
| Le `SKILL.md` d'un outil | l'outil se déclenche | la procédure de cet outil | son profil, ses données |
| Les instructions du projet | **toute séance du projet**, même sans outil, y compris sur mobile | qui il est, comment il veut travailler, ce qui ne part jamais sans lui | des chemins de dossier, son style, du détail |
| `CLAUDE.md` | une séance qui travaille dans le dossier | l'ordre de lecture des fichiers, les règles de rangement et de suppression | ce qui n'a pas de sens hors du dossier |
| `00_MOI/` | à la demande d'un outil | **des données, jamais des instructions** | des consignes de comportement |

### La cinquième portée : Claude Code, et la convention `.claude`

Claude Code lit ses outils et ses réglages à deux endroits. **`~/.claude/`**, dans le répertoire
personnel, vaut pour tous ses projets. **`<projet>/.claude/`**, dans le dossier de travail,
vaut pour ce projet — et c'est là que vont les skills du projet, dans `.claude/skills/`,
au même format que ce qu'on téléverse sur le compte.

**Cowork n'a pas de skills à l'échelle du projet** — ce n'est pas documenté par Anthropic, mais
signalé par des utilisateurs en 2026, et à revérifier. Un dossier `.claude/skills/` dans le
dossier de travail est donc invisible pour lui, et lisible par Claude Code, comme sa
documentation le prévoit. C'est exactement ce qu'on
veut : la mallette s'installe dans le dossier, et le dossier devient autonome.

**Ce que l'init crée, et pourquoi.**

`<dossier>/CLAUDE.md`, à la racine : le contrat, lu par Cowork comme par Claude Code, qui le
charge automatiquement en ouvrant le dossier.

`<dossier>/.claude/skills/immo-init/` : l'init s'y copie lui-même à l'étape 2 — squelette,
couche métier, références, gabarits. Chaque outil de la mallette fait pareil la première fois
qu'il tourne dans ce dossier. Résultat : Claude Code ouvert dans le dossier trouve
`/immo-init`, `/immo-reseaux-sociaux` et les suivants sans qu'on ait rien installé ailleurs.

**Ce que l'init ne crée pas.** Ni `.claude/rules/`, ni `.claude/agents/` : réglages de
développeur sans objet ici. **Une exception** : s'il utilise Claude Code, `.claude/settings.json`
avec le seul *hook* d'arrêt qui lance `verifier.py` — voir `audit.md`. C'est la seule chose
réellement forcée du système, et elle ne coûte rien à quelqu'un qui ne s'en sert pas.

**Et le cas où il travaille ailleurs**, dans un autre projet Claude Code : là, seul
`~/.claude/CLAUDE.md` — sa mémoire personnelle, chargée partout — peut dire où est son profil.
C'est le quatrième dépôt de l'étape 9, et il ne s'écrit que s'il utilise Claude Code.

**Claude Code lit ses mémoires en remontant depuis le répertoire où il est ouvert** jusqu'à la
racine, et charge tout `CLAUDE.md` rencontré au passage. Conséquence directe et gratuite :
**le `CLAUDE.md` que tu écris à la racine de son dossier est déjà lu par Claude Code** dès
qu'il l'ouvre là. Rien à faire.

Pour ce cas-là, trois lignes suffisent :

> Je suis [métier, secteur]. Mon profil de travail est dans `[chemin complet]/00_MOI/`.
> Lis-le avant de produire quoi que ce soit pour moi.
> Rien ne part vers l'extérieur sans moi.

**Et on ne déplace jamais `00_MOI/` dans `~/.claude/`.** Trois raisons, la première suffit :
c'est un dossier caché que l'utilisateur ne trouvera jamais, alors que toute la mallette
repose sur le fait que ces fichiers sont à lui et qu'il peut les corriger à la main. Ensuite,
c'est le territoire de l'outil, qui y range et y balaie ses propres données. Enfin, Cowork
connecte un dossier choisi par l'utilisateur, pas un répertoire de configuration.

| Où | Lu quand | Porte |
|---|---|---|
| Le `SKILL.md` d'un outil | l'outil se déclenche | la procédure de cet outil |
| Les instructions du projet | toute séance du projet, y compris sur mobile | qui il est, comment il veut travailler |
| `CLAUDE.md` du dossier | une séance dans le dossier — **Cowork comme Claude Code** | le rangement des fichiers |
| `.claude/skills/` du dossier | Claude Code ouvert dans le dossier — Cowork l'ignore | les outils de la mallette, auto-installés |
| `~/.claude/CLAUDE.md` | tout projet Claude Code, partout | où est son profil, et rien de plus |
| `00_MOI/` | à la demande d'un outil | des données, jamais des instructions |

**La règle de non-recouvrement, et elle n'est pas « ne jamais répéter ».** Une règle qui doit
tenir dans les deux contextes se répète légitimement : « rien ne part sans moi » vaut dans le
dossier comme sur son téléphone. Ce qui ne doit jamais fuir d'un endroit à l'autre, c'est ce
qui est **propre à un contexte**.

Concrètement : **aucun chemin de dossier dans les instructions du projet.** Sur son téléphone,
`00_MOI/profil.md` n'existe pas — seuls les fichiers déposés existent. Une instruction qui
renvoie à un chemin local y est au mieux inutile, au pire elle fait chercher Claude et échouer
la réponse. Les instructions du projet parlent **des fichiers de ce projet**, jamais du
dossier.

Et inversement : le protocole d'interaction — produire d'abord ou questionner d'abord — n'a
rien à faire dans `CLAUDE.md`. Il vaut partout, donc il vit dans les instructions.

### Après l'init — l'ancrage, en trois dépôts

C'est l'étape 9 de la skill. Trois emplacements, trois contenus différents. Ne mets jamais
la même chose à deux endroits sans le décider exprès.

**1. Les instructions du projet.** Trois à cinq points, pas plus : au-delà, ça devient
contre-productif. Elles portent le protocole d'interaction, pas le style. Ce qui entre ici
vient de la section 6 du profil.

**Aucun chemin de dossier ici.** Ces instructions s'appliquent aussi depuis son téléphone, où
le dossier n'existe pas. On parle des fichiers du projet, jamais de `00_MOI/`.

Gabarit à proposer, à adapter avec ses mots à lui :

> Je suis [métier, secteur]. Mon profil, ma façon d'écrire et mes contraintes sont dans les
> fichiers de ce projet : lis-les avant de produire quoi que ce soit, et dis-moi si tu ne les
> trouves pas.
> Tu produis d'abord et je corrige, plutôt que de m'interroger longuement. [ou l'inverse,
> selon sa section 6]
> Rien ne part vers l'extérieur sans moi.
> Si tu ne sais pas, dis-le et laisse la place vide. N'invente jamais un chiffre, une surface
> ni une date.

Quand la section 4 de son profil porte une phrase de positionnement, **elle a sa place ici**,
en tête : c'est ce qui est vrai de toutes ses séances, et c'est ce qui évite qu'un outil
produise quelque chose de hors sujet. Elle s'ajoute quand elle existe, pas à l'installation.

La dernière ligne est la plus rentable et celle qu'on oublie : c'est la seule règle de
marquage qui survive hors du dossier, là où aucun outil ne se déclenche.

**2. Les fichiers du projet — le miroir.** Les cinq fichiers de `00_MOI/` y sont déposés,
et c'est ce qui les rend lisibles depuis son téléphone.

**D'abord vérifier, trente secondes** : il ouvre son projet sur le web ou son téléphone et
regarde le panneau de connaissance du projet. Si les cinq fichiers y sont déjà, la
synchronisation les y a portés — rien à faire, on consigne. Sinon, **le bouton « + » de la
connaissance du projet, puis choisir le fichier**, cinq fois. C'est tout. La procédure entière
et la règle de rafraîchissement sont dans `verite.md`.

Deux règles, non négociables, parce que le double dépôt est ce qui pourrit une installation
en trois mois :

- **Le dossier local est la source de vérité. Le projet est un miroir.** Si les deux
  divergent, le local gagne, sans discussion. Un skill ne lit jamais le miroir pour décider,
  il ne fait que le rafraîchir.
- **Chaque copie porte sa date dans son nom.** `profil-2026-09-15.md`. Un document déposé
  est un instantané qui ne se met pas à jour tout seul : sans date visible, il donnera dans
  six mois des réponses périmées et confiantes.

Et une limite technique qui impose le geste manuel : **Cowork ne modifie pas le contenu d'un
projet.** Ce qu'on veut y garder, on l'y ajoute soi-même. Donc tu ne peux pas rafraîchir le
miroir à sa place. Tu peux préparer les fichiers datés dans le dossier, lui dire lesquels
déposer, et lui indiquer quand recommencer : à chaque fois qu'il modifie son profil ou sa
voix à la main, et sinon tous les trimestres.

La capacité n'est pas un souci : sur les plans payants, quand la connaissance approche la
limite de contexte, le mode retrieval s'active seul et multiplie la capacité par dix. Mais
une base restreinte reste plus précise qu'une grosse : cinq fichiers datés, pas son
disque dur.

**3. La mémoire du compte.** Voir `memoire.md`.

**Attention au cloisonnement** : la mémoire est scopée au projet, ce que Claude apprend dans
un projet ne se transmet pas aux autres. Les six lignes de pointeur ne sont utiles que si
elles sont disponibles partout : fais-les écrire **depuis une conversation hors projet**.
Dis-le-lui en une phrase, c'est contre-intuitif et il ne le devinera pas.

---

## Quand mettre à jour les instructions

Elles se figent vite et personne n'y revient. Trois déclencheurs, et un seul suffit :

- **sa section 6 change** — il découvre qu'il préfère être questionné plutôt que corrigé
- **un outil s'ajoute** à sa mallette et change ce qu'il attend d'une séance
- **le miroir est rafraîchi**, parce que c'est le moment où il rouvre l'écran du projet

Dans les trois cas, tu lui montres la ligne à changer, il valide, il la colle. Tu ne modifies
pas ses instructions toi-même : elles vivent dans son compte, pas dans le dossier.

Et une règle de volume : **si les instructions dépassent cinq points, quelque chose devrait
être ailleurs.** Le détail va dans `00_MOI/`, la procédure va dans un outil. Des instructions
qui grossissent sont des instructions qu'on cesse de suivre.

## Consigner

Rien de ce que tu dictes ici ne laisse de trace dans les fichiers. Dès qu'une action est
faite — ou refusée — consigne-la dans l'en-tête d'état de `profil.md` : projet créé et par
quel chemin, miroir déposé et à quelle date. « Non fait » est un résultat valable. Une case
vide ne l'est pas : personne ne saura jamais si l'action a eu lieu.

## Ce que tu ne fais pas

**Tu ne crées pas le projet à sa place.** Tu dictes, il clique. C'est trois clics, et c'est
le moment où il comprend que la mallette est à lui.

**Tu ne déposes pas ses fichiers de biens ou de clients dans le projet.** Le miroir, c'est
`00_MOI/` et rien d'autre.

**Tu ne mets pas sa voix dans les instructions du projet.** Elle change, elle vit dans
`voix.md`, et une instruction figée qui contredit un fichier à jour est pire que pas
d'instruction.
