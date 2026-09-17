# La stylométrie de la mallette

## Ce que c'est, et pourquoi on mesure

La stylométrie est la mesure de ce qui, dans une façon d'écrire, **ne dépend pas du sujet et
échappe à la volonté de l'auteur**. Elle est née pour attribuer des textes anonymes ; elle
sert ici à l'inverse — reproduire quelqu'un sans le trahir, et **détecter quand on le
trahit**.

Un modèle qui lit trente mails et « sent » qu'il écrit court dérive : il estime, et son
estimation hérite du contexte. Un script qui compte ne dérive pas. C'est pour ça que la voix
de la mallette a deux couches : **les échantillons**, qui portent la voix et servent à écrire,
et **la signature mesurée**, qui sert à contrôler.

## Les cinq niveaux, et ce qu'on en mesure

| Niveau | Ce qui discrimine | Ce que `stylo.py` mesure |
|---|---|---|
| Lexical | les mots-outils et leurs taux, la longueur des phrases et **sa variance**, la richesse | vingt mots-outils pour mille, ceux qui sont sur-représentés par rapport au français courant, moyenne et écart des phrases, part de courtes et de longues, richesse sur mille mots |
| Caractère | la ponctuation, les guillemets, les espaces, les majuscules, les accents | onze signes pour mille caractères, espace avant ponctuation, « ça » sans cédille, majuscules accentuées ou non |
| Structurel | l'appel, la clôture, la signature, les paragraphes | ouvertures, clôtures, longueur des paragraphes, débuts de phrase |
| Idiosyncrasique | ce qu'il fait et que presque personne ne fait — et **ce qu'il ne fait jamais** | la ligne « sur-représentés », et la ligne **« jamais »** |
| Syntaxique | les structures de phrase | approximé par les débuts de phrase ; on ne fait pas d'analyse syntaxique |

**La ligne « jamais » est la plus utile de toutes.** Un homme qui ne met jamais de point
d'exclamation et à qui un outil en écrit trois se reconnaît immédiatement — et ses lecteurs
aussi. C'est une contrainte dure pour l'écriture et un test binaire pour le contrôle.

## Personne n'a un style : les registres

Ses mails aux vendeurs, ses mails aux acquéreurs, ses publications, ses annonces, ses messages
à Claude ne se ressemblent pas. **Un profil global moyenne des choses qui ne se moyennent
pas.** On mesure donc **un registre à la fois**, chacun sur son corpus homogène, et un outil
de production compare son brouillon au registre le plus proche de ce qu'il produit.

Les registres de ce métier, et leur corpus :

| Registre | Corpus | Qui s'en sert |
|---|---|---|
| mails aux vendeurs | ses mails envoyés, segment vendeurs | le suivi à venir, le point vendeur |
| mails aux acquéreurs | ses mails envoyés, segment acquéreurs | les réponses à une demande de visite |
| publications | `02_PUBLICATIONS/publies/`, ou ses pages publiques relevées | `immo-reseaux-sociaux` |
| annonces | ses annonces passées — `01_BIENS/`, son site | `immo-annonce` |
| messages à Claude | ses propres messages dans ses conversations passées — seulement s'il le demande | le registre le plus brut : sert de référence pour l'informel |
| oral | ses comptes rendus de réunion, **ses mots à lui seulement**, jamais ceux des clients | **le short face caméra**, et rien d'autre — un script se dit, il ne se lit pas |

**Sous deux mille mots par registre, le script le dit, et la signature est fragile.** On la
colle quand même, avec l'avertissement : un outil qui la lit saura qu'elle est mince.

## D'où viennent les corpus — taper large

Tout ce que l'init ouvre déjà, réparti par registre :

- **Sa messagerie** — Gmail, Outlook ou autre —, mails envoyés, segmentés par interlocuteur — `source-mail.md`. Exportés en texte
  si possible : c'est le meilleur corpus.
- **Ses conversations passées**, seulement s'il demande qu'on s'en serve — ses messages à lui,
  jamais les réponses de Claude, `source-claude.md`. Le registre le plus brut, celui où personne ne se surveille.
- **Ses publications**, sur ses pages relevées au navigateur — `source-presence-en-ligne.md`
  — puis, avec le temps, `publies/`.
- **Ses annonces**, sur son site et les portails — même source.
- **Ses fichiers**, ses productions écrites — `source-fichiers.md`.

**Les comptes rendus de réunion ne nourrissent que le registre oral**, et seulement ses mots
à lui — jamais ceux des clients, jamais une situation. Une signature écrite calibrée sur de
l'oral produit des textes bavards ; mais un script de short calibré sur de l'écrit produit
quelqu'un qui lit. Les deux registres existent et ne se mélangent pas. Jamais l'agenda : des
titres ne font pas un style.

**Le corpus ne se stocke pas.** Il sert à mesurer, puis on ne garde que la carte. Aucun mail,
aucun message n'est recopié — la mesure ne retient que des taux.

## Où ça se stocke, précisément

`00_MOI/voix.md`, section **« Ma signature mesurée »**, un bloc `### Registre : …` par
registre, collé tel que le script le rend. Chaque ligne `[vu]` avec son compte et son mois.
La section reste `[à confirmer]` tant qu'aucun corpus n'a été mesuré.

**On ne l'écrit jamais à la main.** Une ligne écrite à la main dans cette section est une
estimation déguisée en mesure — et c'est exactement ce que la section existe pour empêcher.

## Qui s'en sert, quand, comment

**À l'écriture**, dans tout outil qui rédige : les échantillons passent devant, comme
toujours ; et **la ligne « jamais » du bon registre devient une contrainte dure** — on
n'écrit pas ce qu'il n'écrit jamais.

**Au contrôle** : `stylo.py compare <brouillon> 00_MOI/voix.md --registre <nom>`. Ce qu'il
rend est un signal externe. On corrige avant de livrer, sauf ce qui n'est pas dans sa voix par
nature — le bloc réglementaire d'une annonce.

**À l'audit mensuel** : si `publies/` a grandi, on remesure le registre publications. Un écart
entre la nouvelle carte et l'ancienne dit soit qu'il a changé, soit qu'un outil a dérivé et
que ses publications portent la signature de l'outil. Les deux se disent.

**Le choix du registre est une règle, pas un jugement :**

| Outil | Registre à comparer | Sinon |
|---|---|---|
| `immo-reseaux-sociaux` | publications | messages à Claude, puis global |
| `immo-annonce` | annonces | publications, puis global |
| `immo-suivi`, à venir | mails aux vendeurs | global |
| `immo-parcours`, réponses proposées | mails aux vendeurs ou aux acquéreurs selon la fiche | global |
| `immo-reseaux-sociaux`, short face caméra | **oral** | aucun — on écrit plus court et il redit avec ses mots |

## Ce que la mesure ne dit pas

Elle ne dit pas si un texte est bon. Elle ne dit pas si un texte lui ressemble au sens où lui
le sentirait — c'est aux échantillons et à sa relecture de le dire. Elle dit qu'un texte
s'éloigne de ses habitudes mesurables, ou qu'il ne s'en éloigne pas. **C'est un garde-fou, pas
un juge.** Un texte qui passe la mesure et qu'il rejette a raison d'être rejeté.
