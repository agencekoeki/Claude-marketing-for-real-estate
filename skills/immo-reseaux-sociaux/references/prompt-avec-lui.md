# Quand le visuel le montre, lui

## Ce que ce fichier décide

Une forme qui exige sa photo — le personnage dessiné, le portrait annoté, la bande dessinée
où il apparaît, une scène — passe par ici avant que le prompt s'écrive. Parce que sa photo
n'est pas une image comme une autre : **la confier à un générateur, c'est la confier à un
tiers**, et un visage se reconnaît même mal rendu.

## Deux consentements, pas un

`cadre.md` porte deux lignes, et elles ne disent pas la même chose :

- **« Ma photo apparaît sur mes visuels »** — oui, non, seulement quand je parle de moi. Ça
  autorise un gabarit HTML par-dessus sa photo : le fichier reste chez lui.
- **« Ma photo peut servir de référence à un générateur »** — oui, non. Ça autorise le
  téléversement dans ChatGPT ou Gemini. **Sans ce oui, aucun prompt ne contient sa photo**,
  et la forme se rabat sur le gabarit ou change.

Si la seconde ligne est vide, on pose la question — une fois, avec ce qu'elle implique : « ta
photo partirait dans l'outil de génération, comme référence ; tu es d'accord ? » Un non n'est
pas un manque. C'est une décision qu'on ne rediscute pas à chaque post.

## Quelle photo

**Celle de `03_RESSOURCES/`, et aucune autre.** Nommée dans le prompt par son nom de fichier,
pour qu'il sache laquelle joindre. Pas une photo prise par un client, pas une capture de son
profil, pas une photo où quelqu'un d'autre apparaît. S'il n'y en a pas dans `03_RESSOURCES/`,
la forme attend qu'il l'y pose — on ne va pas la chercher ailleurs.

**Une seule photo de référence pour le personnage dessiné**, toujours la même, pour que le
personnage soit le même. Plusieurs — jusqu'à quatorze côté Google — seulement pour une série
où il faut tenir l'identité sous plusieurs angles.

## Trois usages, trois prompts

**1. Le personnage dessiné, une fois pour toutes.** On le fabrique une fois, on garde
l'image obtenue dans `03_RESSOURCES/personnage.png`, et **c'est elle qui sert de référence
ensuite**, plus la photo. Famille Google — l'identité se conserve mieux. Le prompt dit :

> Utilise la photo jointe comme référence d'identité. Dessine cette personne en [trait simple /
> aplats, deux couleurs : les siennes]. Ne change ni les traits du visage, ni la morphologie,
> ni la coiffure, ni les lunettes. Fond uni neutre, pas de décor. Buste, de face, expression
> neutre. Aucun texte, aucun logo. Le même personnage devra être reproduit à l'identique
> ensuite.

Puis on vérifie : **il se reconnaît**, et ses proches le reconnaîtraient. Sinon on refait ; on
ne publie pas un personnage qui le flatte ou le vieillit.

**2. Le portrait annoté — l'agent en pièces détachées.** Le gabarit HTML par-dessus sa photo
d'abord : c'est le plus sûr, rien ne sort de chez lui. Si un générateur, famille OpenAI pour
la précision des légendes, avec cette contrainte en tête du prompt :

> Ne modifie pas la photo jointe : ni le visage, ni la lumière, ni le cadrage. Ajoute
> uniquement, par-dessus, des traits fins et des points depuis [la main, la poche, les
> chaussures] vers des légendes courtes, texte exact entre guillemets : « … », « … », « … ».
> Fond de la photo inchangé. Style de schéma technique, une couleur de trait.

Et on vérifie que le visage n'a pas bougé — la famille OpenAI restructure parfois légèrement
un visage, c'est connu.

**3. Une scène.** Lui dans une situation — la minute d'avant, la table de la cuisine. **Jamais
en photoréalisme** : une photo réaliste de lui dans un lieu où il n'était pas est une image
fausse, et depuis août 2026 elle doit être signalée. Donc toujours son personnage dessiné, en
référence, dans une scène dessinée, avec la neutralisation du rendu maison :

> Utilise l'image jointe comme référence : c'est le personnage, à reproduire à l'identique.
> Scène dessinée, même style que le personnage. [La scène, en une phrase, sans lieu réel ni
> bien réel.] Aucun texte sauf : « … ». Pas de logo. Lumière neutre, pas d'effet.

## Le geste, pour lui — la seule chose à faire

Deux temps, dans cet ordre, écrits tels quels dans la livraison :

> 1. Ouvre [Gemini / ChatGPT], joins `03_RESSOURCES/[fichier]`.
> 2. Colle ceci : [le prompt].

Puis ce qu'il vérifie sur le résultat, en trois points : **il se reconnaît**, les mains et le
texte sont justes, aucun logo ni décor n'a été ajouté. S'il ne se reconnaît pas, il refait —
on ne corrige pas un visage au montage.

## Ce qu'on signale, et où

Un dessin de lui est un dessin : la mention vient de `cadre.md` et va dans le texte du post,
pas dans l'image. Une photo retouchée au-delà de la lumière et du cadrage se signale de même.
Le portrait annoté — la photo intacte, des traits par-dessus — n'est pas une image modifiée
au sens de l'obligation, mais dans le doute on signale.

## Ce qu'on ne fait jamais

**La photo d'un client, d'un vendeur, d'un collègue** — même avec accord oral. **Une
génération réaliste de lui** dans un lieu, une visite, une signature qu'il n'a pas vécus.
**Un personnage qui change** d'un post à l'autre : c'est l'image de `03_RESSOURCES/` qui sert
de référence, toujours la même. **Un prompt qui nomme un lieu réel** — la famille Google le
rendrait fidèlement, et ce serait une image fausse d'un vrai lieu.

## Ce qu'on garde

Dans `03_RESSOURCES/` : sa photo, son personnage, et **le prompt qui a produit le personnage**
— dans `cadre.md`, compositions récurrentes — pour pouvoir le refaire à l'identique si le
fichier se perd.
