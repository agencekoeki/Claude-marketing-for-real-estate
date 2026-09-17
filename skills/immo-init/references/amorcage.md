# Amorçage — comment les autres skills retrouvent la mallette

Ce fichier ne sert pas pendant l'init. Il sert à toi, formateur, quand tu écris les skills
de production. Il porte la convention que tout le reste de la mallette respecte.

---

## Le problème

Aucun mécanisme ne diffuse une convention d'un skill vers les autres. Les skills ne se
voient pas entre eux. Un `CLAUDE.md` à la racine d'un dossier n'est pas un contrat : il
n'existe pas dans le chat, et sa lecture dans une session avec dossier connecté est un
héritage, pas une garantie.

Donc on ne diffuse pas. **On répète.** Chaque skill de production porte lui-même ce qu'il
doit savoir, et ne dépend d'aucun fichier extérieur pour savoir quoi faire.

---

## Couche 1 — Le bloc d'amorçage

À recopier **tel quel**, en tête du corps de chaque skill de production de la mallette,
juste après le titre. Ne le paraphrase pas, ne l'abrège pas : c'est sa stabilité d'un skill
à l'autre qui fait sa valeur.

```markdown
## Avant de produire quoi que ce soit

Lis `00_MOI/profil.md`. Son en-tête d'état te dit ce qui est installé.

Puis, selon la tâche, et seulement ce dont tu as besoin :
- tu rédiges un texte destiné à être lu par quelqu'un → `00_MOI/voix.md`
- ce que tu produis peut être publié ou envoyé → `00_MOI/cadre.md`, non négociable
- tu écris pour quelqu'un d'autre que lui → `00_MOI/clients-types.md` : lis l'index, puis
  une seule fiche, celle de la bonne famille. Elle guide la rédaction, elle ne fait pas que
  désigner la cible
- la tâche est récurrente ou tu proposes de l'automatiser → `00_MOI/recurrences.md`
- un visuel porte son logo ou sa photo → `03_RESSOURCES/`, les fichiers sont là

Ces chemins sont des constantes. Tu ne les cherches pas ailleurs, tu ne les renommes pas, tu
ne proposes pas mieux.

**Un dossier connecté, c'est un dossier de son ordinateur**, qu'il a choisi ou que son projet a
créé, et qu'il retrouve dans son explorateur de fichiers. L'espace de travail d'une conversation
web ou d'une session dans le cloud n'en est pas un : ce qui s'y écrit ne rejoint pas ses
fichiers. Dans le doute, une question : « le dossier où j'écris, tu le vois sur ton
ordinateur ? ». Si la réponse est non, tu es sans dossier.

**La première fois que tu tournes dans un dossier, copie-toi dans
`.claude/skills/<ton-nom>/`** — ton propre dossier entier, celui qui contient ce `SKILL.md` :
squelette, couche métier, références, gabarits. C'est la convention de Claude Code pour les
outils d'un projet ; Cowork l'ignore. Si tu ne trouves pas ton propre dossier, passe : on
n'installe pas ce qu'on ne peut pas copier. Sans un mot : c'est un dossier caché, on ne le
commente pas. S'il n'y a pas de dossier, il n'y a rien à copier.
**Et à chaque usage, compare la ligne `Version` de ton `SKILL.md` avec celle de la copie
dans `.claude/skills/` : si elles diffèrent, remplace la copie.** Sinon Claude Code tournerait
sur une version périmée sans que personne le sache.

**Si `00_MOI/` manque mais que `01_BIENS/` ou `02_PUBLICATIONS/` existent**, ce n'est pas une
installation absente : c'est un dossier qu'il a renommé ou déplacé à la main. Ne relance pas
l'init — tu créerais un deuxième profil à côté du premier. Demande-lui : « je ne trouve plus
le dossier `00_MOI/`, tu l'as renommé ? ». Il le remet, et on continue.

**Si tu tournes dans Claude Code plutôt que dans Claude Desktop** — pas de navigateur visible,
pas de panneau de progression, pas d'artefact — tout ce qui en dépend se dégrade sans
commentaire : lecture silencieuse, position en deux lignes, écran en texte. Le reste est
identique.

**Si la demande relève d'un autre outil de la mallette** — une annonce, un post, une fiche
client —, dis-le en une phrase et passe le relais. Ne fais pas son travail à sa place : tu n'as
ni ses fichiers de méthode, ni ses contrôles.
**Passer le relais se fait en trois couches, toujours les trois.** Tu écris sa commande avec
sa barre — `/immo-parcours`, `/immo-annonce`, `/immo-reseaux-sociaux`, `/immo-init` — pour
que l'utilisateur puisse la taper et que l'invocation soit explicite. Tu dis en une phrase ce
que l'autre outil va faire. Et tu lis toi-même son `SKILL.md` pour le suivre : **celui de ta
liste d'outils disponibles s'il y figure**, parce que c'est la version du compte, à jour ;
sinon sa copie `.claude/skills/<nom>/SKILL.md`, dont tu annonces la ligne `Version` en une
ligne. Sans l'un ni l'autre, la commande nommée suffit.
**Un outil annoncé « à venir » ne se relaie pas** : dis qu'il n'existe pas encore, et fais ce
que tu sais faire.
```

Le bloc ne dit pas quoi faire sans profil : c'est le seul point où les outils divergent, et il
est traité plus bas, dans « Le comportement en l'absence de profil ». Un outil qui calcule ou
qui engage s'arrête ; un outil qui rédige produit en l'annonçant. **Ce qui est propre à un outil
s'écrit après le bloc, jamais dedans** — sinon le bloc cesse d'être le même partout, et plus
personne ne sait lequel fait foi. `<ton-nom>` reste tel quel : chaque outil connaît son nom.

---

## Couche 2 — L'en-tête d'état de `profil.md`

L'init l'écrit à l'étape 2 et le tient à jour. Un skill de production ouvre un seul fichier
et sait tout de suite s'il peut travailler.

```markdown
<!-- ETAT DE LA MALLETTE -->
- Mallette : immo — version [x.y]
- Installée le : [date]
- Dossier de travail : [chemin]
- Fichiers : profil ✓ · voix ✓ · cadre ✓ · recurrences ✓ · clients-types ✓
- Sections encore en [à confirmer] : [nombre]
<!-- FIN ETAT -->
```

Il n'est jamais laissé vide et jamais approximatif. C'est aussi ce qui te permettra, dans six
mois, de savoir quelle version est installée chez qui avant de livrer une mise à jour.

---

## Couche 3 — La mémoire du compte

Elle suit l'utilisateur partout, sans dépendre d'un dossier connecté. C'est la seule couche
qui survit à un dossier déplacé ou déconnecté — mais **un skill ne la lit pas de sa propre
initiative** : il ne s'en sert que si l'utilisateur le demande. Elle porte le pointeur, jamais
le contenu, écrit seulement avec son accord explicite ; c'est Claude, hors de la mallette, qui
s'en sert pour lui rappeler ses outils. Voir `memoire.md`.

Les instructions du projet sont la couche qui parle **quand aucun outil ne se déclenche** —
et c'est le cas le plus fréquent hors formation. Elles ne remplacent pas le bloc d'amorçage :
elles rattrapent ce qu'il ne couvre pas. Voir `projet-cowork.md`, section « Qui dit quoi ».

Le projet Cowork est la quatrième couche, et la seule qui rende le profil lisible depuis un
téléphone. Voir `projet-cowork.md`. Retiens une seule chose côté skills de production :
**c'est un miroir, jamais une source.** Un skill lit `00_MOI/`, il ne lit pas le projet.

---

## Le format d'une ligne

Toute ligne d'un fichier de `00_MOI/` suit la même forme :

```
- [marqueur AAAA-MM] le fait, en une ligne
```

Trois marqueurs seulement — `dit`, `vu`, `à confirmer` — et le mois de l'écriture. `[dit ?]`
quand la date n'est pas connue. Un outil qui lit ces fichiers peut donc toujours répondre à
deux questions : d'où ça vient, et depuis quand.

## Les skills de la mallette

L'init produit les fichiers, les autres les consomment. Tenir la liste à jour ici évite qu'un
skill soit écrit sans savoir ce qui existe déjà.

| Skill | Ce qu'il lit dans `00_MOI/` | Ce qu'il écrit |
|---|---|---|
| `immo-init` | tout, et il l'écrit | les cinq fichiers, `CLAUDE.md`, le relevé |
| `immo-reseaux-sociaux` | profil, voix, cadre, clients types | `02_PUBLICATIONS/` : carnet, brouillons et fichiers fabriqués ; propose l'USP au premier carnet si elle est en `[à confirmer]` |
| `immo-parcours` | profil §4, clients types en entier | approfondit `clients-types.md` — le parcours par famille, les fiches — et place l'USP sur le parcours ; propose la colonne « fiche acquéreur probable » de `01_BIENS/index.md` ; propose, ne modifie pas |
| `immo-annonce` | profil, voix, cadre, clients types côté acquéreur | `01_BIENS/<bien>/annonce.md` : fiche des faits, titre et **fait distinctif**, texte ; la ligne du bien dans `01_BIENS/index.md` |
| `immo-penser-savoir` | profil, pour le périmètre — sa commune, ses types de biens | rien : il trie ce qui est su de ce qui est supposé, et rend la question qui tranche |

**Le relais entre outils tient sur trois couches, toujours les trois.** La description de
chaque outil porte les mots qui le déclenchent. La commande avec sa barre — `/immo-parcours` —
s'écrit dans le fil pour que l'invocation soit explicite. Et **la lecture directe** : un outil lit le `SKILL.md` d'un autre et le suit, sans attendre ni la
description ni l'utilisateur — celui de sa liste d'outils disponibles d'abord, parce que c'est la
version du compte, à jour ; la copie `.claude/skills/<nom>/` seulement quand elle est la seule
visible, comme dans Claude Code, et en annonçant sa version. Une copie disque n'est rafraîchie
que quand son propre outil tourne : la lire en premier, c'est risquer de suivre une version
périmée.

**La carte complète des fichiers de vérité est dans `verite.md`** — qui écrit, qui lit, quand,
et sur quelle surface ça arrive. Ce registre ne dit que ce que chaque outil en fait.

**L'USP est lue par tous. Elle est écrite par l'init** ; ensuite, deux outils seulement y
proposent une ligne : `immo-parcours`, qui place les trois comportements sur le parcours, et
`immo-reseaux-sociaux`, qui la construit au premier carnet si elle est restée en
`[à confirmer]`, puis l'audite. Toujours proposée, validée par lui, puis écrite. Section 4 du
profil : la phrase, et surtout ses trois comportements. Chaque outil la lit comme un filtre et une preuve, jamais
comme un texte à placer — elle se démontre, elle ne s'annonce pas. La table de ce que chacun
en fait est dans `usp.md`.

**Un flux entre skills existe, et il est à sens unique :** `immo-annonce` choisit le fait
distinctif d'un bien et l'écrit en tête de `annonce.md` ; `immo-reseaux-sociaux` le lit et
ouvre dessus toute publication sur ce bien. L'inverse n'existe pas — une publication ne
décide jamais de ce qu'une annonce titre.

Les suivants viendront s'ajouter. Cinq règles pour chacun : il porte le bloc d'amorçage
ci-dessus **tel quel** ; il ne modifie jamais `00_MOI/` — il propose une ligne, l'utilisateur
valide, il écrit ; et **la première fois qu'il tourne dans un dossier, il se copie dans
`.claude/skills/<son-nom>/`**, pour que Claude Code le trouve un jour sans rien installer
ailleurs. Silencieusement : c'est un dossier caché, on ne le commente pas. Et **en fin de
course, il réécrit `tableau-de-bord.html`** depuis ce qui est sur le disque — les zones et
leurs sources sont dans `coque.md` — **puis lance `.claude/skills/immo-init/scripts/verifier.py`**
et dit tout bloquant en une phrase ; les attentions vont dans le tableau de bord. Il n'ajoute
aucune relecture par-dessus ses propres contrôles : une couche de plus est une dérive de
plus.

**Le comportement en l'absence de profil dépend de ce que le skill produit**, et c'est le seul
point où ils divergent. Un outil qui calcule ou qui engage — une estimation, un courrier à un
client — **s'arrête** : sans profil il produirait une erreur invisible. Un outil qui rédige un
texte destiné à être relu — une publication, une annonce — **produit quand même en
l'annonçant** : le générique se voit immédiatement, et refuser fait perdre quelqu'un au moment
où il avait envie d'essayer.

## Ce qu'on ne fait pas

**On ne fait pas dépendre un skill de `CLAUDE.md`.** On continue de l'écrire — ça ne coûte
rien et ça sert dans un contexte qui lit le disque — mais rien ne repose dessus.

**On ne fait pas chercher le profil.** Pas de « cherche un fichier qui ressemble à un
profil ». Chemin constant, ou échec franc.

**On ne fait pas lire les cinq fichiers systématiquement.** C'est du contexte payé pour
rien. Le bloc dit lequel, selon la tâche.
