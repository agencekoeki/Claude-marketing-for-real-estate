# Le post du jour

## Ce que c'est

Le mode inverse de l'écriture : **il ne demande rien, il propose.** Chaque jour où il
publie, un paquet complet, prêt à relire et coller :

1. **Le texte**, décliné pour chaque plateforme de sa section 8 — pas un texte copié trois
   fois, trois versions qui respectent chacune sa coupe et son ton
2. **Le visuel** : le type choisi dans `visuels.md`, et selon le type, la page gabarit
   remplie, le plan de prise de vue, ou le prompt exact à coller dans son générateur — avec
   le rapport d'image et les contraintes de la plateforme
3. **La justification**, en trois lignes : quelle mission, pour quelle fiche, pourquoi
   aujourd'hui

Il relit, il publie. Dix minutes.

## D'où vient le post du jour

**Du carnet, d'abord.** La table « À écrire » est la réserve ; le post du jour en prend une
ligne. Pas la première : celle que **les trois filtres** désignent.

**Le rythme** — `rythme.md` : pas deux jours de suite sur le même sujet, pas deux jours de
suite le même type de visuel, et le format qui dépasse quinze minutes une fois par semaine au
plus.

**L'équilibre des missions** — sur la semaine, les quatre missions qui rentrent des mandats
en prennent au moins deux. Le post du jour regarde ce qui est déjà sorti cette semaine dans
`publies/` et prend la mission qui manque.

**Ce qui arrive** — une échéance du carnet dans les dix jours passe devant. Une trace fraîche
de la récolte — un mail reçu trois fois cette semaine — aussi.

**S'il n'y a pas de carnet**, le post du jour ne s'improvise pas : il faut le carnet d'abord.
Une ligne : « je te fais ton carnet, vingt minutes, et demain tu auras ton post ».

## La créativité, bornée

**Pas la façade et « maison à vendre ».** Mais pas n'importe quoi non plus : un agent
immobilier n'est pas un influenceur, et chaque post sert une des huit missions.

La créativité, c'est **le quoi montrer et le comment dire**, à l'intérieur du sujet. Pour un
sujet donné, huit traitements — on en essaie trois mentalement, on garde celui que la fiche
client et l'USP désignent :

| Traitement | Ce que ça donne |
|---|---|
| **Le détail plutôt que l'ensemble** | pas la maison, la poignée de la porte de 1920 |
| **Le contre-pied** | « ce que je ne ferai pas pour vendre votre maison » |
| **Le chiffre** | un seul, avec sa source, en grand |
| **La scène** | ce qui s'est passé mardi à 16 h, sans nom |
| **La question** | celle qu'on lui pose trois fois par semaine, et sa réponse |
| **L'avant-après** | ce qu'il a fait, montré |
| **Le pas de côté** | le quartier, le boulanger, la rue — pas le bien |
| **La liste courte** | trois choses à vérifier avant de |

**Les bornes, non négociables :** les faits de ses fichiers — rien d'inventé ; `cadre.md` ;
l'USP — le traitement montre un comportement ou n'en contredit aucun ; et le test de
`eprouver.md` sur ce qui n'est pas un chiffre. Un traitement créatif qui échoue au test de la
négation est une formule, pas une idée.

**Et une chose que l'outil ne décide pas : le ton.** Sa voix, ses échantillons, sa ligne
« jamais ». Un traitement audacieux dans une voix sobre reste sobre.

## La forme, sortie du moteur — pas d'une liste

Un traitement et un type d'image font un post correct. **Une forme sortie d'un fait de lui en
fait un qu'on ne peut pas prévoir** — `formats.md` : cinq questions posées au fait du jour,
renverser, rétrécir, compter, déplacer, dater ; on élimine par le cadre, les faits, l'USP, le
test du confrère sérieux ; il en reste une. La galerie — `galerie.md` — montre soixante
sorties du moteur avec le fait que chacune exige ; on y pioche quand le fait du jour y
rentre, et on la dépasse quand il n'y rentre pas. Au niveau 2, c'est à lui qu'on pose la question,
et la forme sort de sa réponse.

**Un jour sur deux, la forme est une des siennes** — celles qui reviennent, dans `cadre.md`.
L'autre jour, le moteur. C'est ce qui fait qu'on le reconnaît sans qu'il tourne en rond.

Les formats longs — roman-photo, bande dessinée, infographie, comparatif, short — sont ceux de
la semaine, pas du jour : un par semaine au plus.

## La déclinaison par plateforme

Une plateforme décide, les autres suivent — mais **chaque version se réécrit**, elle ne se
copie pas :

| Plateforme | Ce qui change |
|---|---|
| LinkedIn | l'accroche avant ~140 caractères, pas de lien dans le corps, image carrée ou portrait, le bas de l'image libre |
| Instagram | l'accroche avant ~125, l'image porte le message, portrait 4:5 avec le message dans le carré central |
| Facebook, groupes locaux | le ton du groupe, la règle du groupe dans `cadre.md`, la photo réelle avant tout |
| Sa page d'établissement | court, factuel, pas d'accroche |

**Jamais le même texte le même jour sur LinkedIn et une autre plateforme** — on décale d'un
jour. Voir `rythme.md`.

## Le visuel du jour, et ses contraintes

Selon le type retenu dans `visuels.md` :

- **une photo à prendre** → le plan de prise de vue de `prise-de-vue.md`, en une ligne :
  quoi, d'où, à quelle heure
- **un visuel fabriqué** → l'image du moteur, `scripts/build_carrousel.py` ; la carte signature,
  `carte-signature.template.html` ; le gabarit de secours seulement si le moteur ne peut pas tourner
- **un générateur, et la forme le montre, lui** → `prompt-avec-lui.md` d'abord : le second
  consentement de `cadre.md`, la photo ou le personnage de `03_RESSOURCES/` nommé par son
  fichier, et le geste en deux temps — « joins, puis colle »
- **un générateur** → **le prompt exact à coller**, avec la neutralisation du rendu maison,
  le rapport d'image, la famille à viser — `outils-image.md` — et ce qu'il doit vérifier sur
  le résultat
- **un carrousel** → `carrousels.md`, et c'est le format de la semaine, pas du jour

Toujours avec **les contraintes de la plateforme sur l'image** — section images de
`plateformes.md` : rien d'important dans le quart bas sur LinkedIn, le message dans le carré
central sur Instagram, PNG pour un visuel avec du texte, JPG pour une photo.

## La justification, en trois lignes

> Mission : [laquelle des huit]. Pour : [la fiche]. Pourquoi aujourd'hui : [l'échéance, la
> trace, ou la mission qui manquait cette semaine].

C'est ce qui le convainc de publier au lieu de reporter. Et c'est ce qui se note dans
`publication.template.md` — pour que, dans trois mois, on sache pourquoi ce post existait.

## La livraison

Sur la coque, avec `assets/ecran-post-du-jour.html` si un écran rendu est possible : le
texte principal entre ses deux traits, les déclinaisons, le visuel ou son prompt, la
justification, et **une seule chose à faire** — prendre la photo, coller le prompt, ou
rien. Plafond de `livrer.md`. Question finale : « ça part comme ça ? ».

## Sans dossier

Le post du jour tourne aussi depuis le téléphone, sur le miroir — et le paquet devient un
fichier dans son stockage en ligne ou à télécharger, jamais un texte perdu dans une conversation. Mais il
ne sait pas ce qui est sorti hier depuis le téléphone tant que rien n'est rapatrié : il le dit
en une ligne. Voir `sans-dossier.md`.

## Le lendemain

Le post d'aujourd'hui va dans `brouillons/` jusqu'à ce qu'il dise qu'il a publié — alors il
passe dans `publies/` avec sa date, et le post de demain sait qu'il existe. **S'il ne dit
rien pendant trois jours, le post du jour le lui demande** : « celui de lundi, il est parti ? »
Un brouillon qui s'entasse est le signal d'échec du système ; on ne produit pas le suivant
par-dessus sans savoir.

## Ce qu'on ne fait pas

**On ne produit pas cinq jours d'avance.** Un post par jour, le jour même, parce que la trace
fraîche de la récolte et ce qui est sorti hier changent le choix.

**On ne remplit pas.** S'il n'y a rien dans le carnet qui serve une mission aujourd'hui, on
le dit — « rien qui vaille aujourd'hui, on reprend demain » — plutôt que de publier pour
publier. La clarté thématique vaut plus que le volume.

**On ne décide pas du ton.** Sa voix décide.
