# Les mises en page

## De quoi on parle

**La disposition des éléments sur l'image**, indépendamment de ce qu'elle contient. Une même
information — un chiffre, une comparaison, une photo — se dispose de plusieurs façons, et le
choix change ce qu'on retient.

Trois fichiers se suivent, et il ne faut pas les confondre : `visuels.md` décide **quel objet**
on fabrique, celui-ci décide **comment il est disposé**, `direction-graphique.md` décide **à
quoi il ressemble** — ses couleurs, sa signature, son visage.

---

## Le catalogue

Quatorze dispositions couvrent tout ce qu'un professionnel de terrain a besoin de publier.
Pour chacune : ce qu'elle porte le mieux, et le piège.

### Quand l'image domine

**Photo pleine page.** Rien d'autre, ou un mot. Porte l'émotion et le lieu.
*Piège :* sans texte, elle ne dit rien à qui ne connaît pas déjà le sujet.

**Photo pleine page avec texte incrusté.** Le texte en bas, sur un bandeau ou un dégradé
sombre. La plus universelle.
*Piège :* le texte sur une zone chargée devient illisible. Choisis la photo en fonction de
l'endroit où le texte ira, pas l'inverse.

**Photo avec bandeau.** Une bande de couleur en haut ou en bas qui porte une phrase. Plus
lisible que l'incrustation et plus reconnaissable d'une fois sur l'autre.
*Piège :* le bandeau mange l'image ; au-delà d'un cinquième de la hauteur, autant mettre le
texte à côté.

**Photo et texte côte à côte.** Moitié image, moitié fond uni. Bon compromis quand la photo
est moyenne.
*Piège :* en vignette, chaque moitié devient minuscule.

**Diptyque avant-après.** Deux images, une séparation nette, toujours du même côté.
*Piège :* sans cadrage identique, la comparaison ne prouve rien.

**Mosaïque.** Quatre à six images sur une grille. Porte un ensemble — un quartier, une visite,
une sélection.
*Piège :* au-delà de six, on ne voit plus rien. Et une seule image faible fait chuter
l'ensemble.

### Quand le texte domine

**Carte de citation.** Une phrase, en grand, sur fond uni. La plus simple et la plus sous-
estimée : aucune photo nécessaire.
*Piège :* une phrase creuse en grand reste creuse, et ça se voit davantage.

**Carte signature.** Une phrase, sa photo en petit, ses couleurs. C'est sa composition
personnelle — voir `direction-graphique.md`.
*Piège :* son visage sur tout finit par lasser.

**Question et réponse.** La question en haut, la réponse en bas, séparées par un filet. Porte
les objections qui reviennent.
*Piège :* si la réponse tient en une ligne, ce n'est pas un visuel, c'est un post texte.

**Liste.** Trois à sept éléments, un par ligne, à l'impératif. S'enregistre et se ressort.
*Piège :* au-delà de sept, personne ne lit et personne n'enregistre.

### Quand la donnée domine

**Chiffre isolé.** Un seul chiffre, énorme, avec dessous ce qu'il signifie et sa source.
*Piège :* deux chiffres sur la même image, c'est zéro chiffre retenu.

**Deux colonnes.** Idée reçue contre réalité, avant contre après, option A contre option B.
Trois à cinq lignes, les mêmes critères des deux côtés.
*Piège :* des critères différents d'une colonne à l'autre, et ce n'est plus une comparaison.

**Chronologie.** Quatre à six étapes, avec une durée à chacune, verticale de préférence.
*Piège :* sans les durées, c'est une liste déguisée.

**Carte annotée.** Un plan du secteur avec trois ou quatre repères nommés. La plus rare et la
plus forte pour un métier de terrain.
*Piège :* trop de repères, et elle devient un plan touristique illisible.

---

**Au niveau 3, ce catalogue ne se récite pas.** Ses publications passées disent déjà quelles
dispositions il emploie : on reprend les siennes plutôt que d'en proposer d'autres. Voir
`niveau.md`.

## Choisir, en trois questions

**Qu'est-ce qui porte le message ?** Une image, une phrase, ou une donnée. La réponse élimine
les deux tiers du catalogue.

**Est-ce lisible en vignette ?** À la taille d'une carte de visite. Les mosaïques, les
chronologies longues et les colonnes chargées échouent ici, toujours.

**Est-ce une de ses compositions récurrentes ?** À qualité égale, **on reprend celle qu'il
utilise déjà** — c'est la répétition qui construit la reconnaissance, et changer de
disposition à chaque publication n'installe rien.

---

## Ce que le moteur et les gabarits couvrent, et ce qu'ils ne couvrent pas

**Fabricables directement** : avec le moteur `scripts/build_carrousel.py`, la carte de citation,
la question-réponse, la liste, le chiffre isolé, les deux colonnes, la chronologie,
l'avant-après ; avec `carte-signature.template.html`, la carte signature.

**Fabricables en diapos**, avec le moteur : tout ce qui se déroule en plusieurs écrans. Les
gabarits `visuel.template.html` et `diapos.template.html` ne servent qu'en secours.

**Nécessitent une image**, donc une photo de lui ou un passage par un générateur — voir
`outils-image.md` : la photo pleine page, l'incrustation, le bandeau, le côte à côte, le
diptyque, la mosaïque, la carte annotée.

**Dis-lui laquelle des trois catégories s'applique** au moment de livrer : ça détermine s'il
n'a qu'à téléverser, s'il photographie, ou s'il assemble.

---

## Trois règles qui valent pour toutes

**Une seule idée par image.** Si deux idées cohabitent, ce sont deux images, ou un carrousel.

**Le message en haut.** C'est ce qui reste visible quand l'image est rognée dans un fil.

**Une marge généreuse.** Tout ce qui approche les bords est mangé par l'interface, coupé par
un recadrage, ou masqué par les boutons sur une story. Voir les zones masquées dans
`plateformes.md`.

---

## Rappel de marquage

Rien de ce fichier n'entre dans `00_MOI/`. En revanche, **les deux ou trois dispositions qu'il
choisit de garder** sont une décision de sa part : elles vont dans `cadre.md`, avec ses
couleurs, marquées `[dit]`.
