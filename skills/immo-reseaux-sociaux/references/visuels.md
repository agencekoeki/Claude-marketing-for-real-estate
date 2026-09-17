# Le visuel

## Ce que ce fichier fait

Il décide **quel objet visuel accompagne la publication**. `mises-en-page.md` dit ensuite
comment il est disposé, `direction-graphique.md` à quoi il ressemble, `outils-image.md`
comment le faire fabriquer, `prise-de-vue.md` quoi cadrer.

**L'inversion à lui dire :** la photo du bien est le visuel le plus attendu et le moins
distinctif. Tout le monde l'a, le portail l'a en mieux, et elle ne dit rien de lui. Ce qui
distingue coûte souvent moins cher — et avec l'outil, presque tout coûte moins de dix
minutes. Les coûts sont dans `rythme.md`.

---

## La typologie — ce qu'une image peut être

Vingt-deux types, classés par **ce que l'image est**, pas par qui la fabrique. Pour chacun :
ce qu'elle sert, qui la fabrique, où elle marche le mieux, et le piège. « Le moteur », c'est
`scripts/build_carrousel.py` : il sort le fichier final, à ses couleurs, contrôlé. Le gabarit HTML
sert pour ce que le moteur ne sait pas faire — la carte annotée, le diagramme, le portrait
annoté —, et en secours quand le moteur ne peut pas tourner.

### Ce qui montre le réel

| Type | Sert à | Qui la fabrique | Piège |
|---|---|---|---|
| **La photo du bien** | le sujet est le bien | lui, téléphone | attendue, indistincte |
| **La photo de détail** | la projection — une poignée, une vue, un carrelage | lui | sans contexte, illisible |
| **La photo de lieu** | l'angle du lieu, le plus rare | lui, depuis la voiture | banale si c'est un monument |
| **La photo de lui au travail** | les coulisses, l'USP en acte | lui ou un collègue | posée, elle sonne faux |
| **Le portrait** | le profil, la carte signature | un collègue, 20 min | jamais sur un tableau |
| **La capture d'écran** | la preuve — un message, un avis, une alerte, anonymisés | lui, 1 min | un nom qui traîne |
| **L'avant-après** | la preuve d'un travail | lui, deux photos au même cadrage — le moteur les assemble | cadrage différent, ça ne prouve rien |
| **Le document photographié** | la preuve — un diagnostic, un plan, une facture, floutés | lui | une donnée de tiers visible |

### Ce qui explique

| Type | Sert à | Qui la fabrique | Piège |
|---|---|---|---|
| **La carte de citation** | une phrase forte, la sienne ou celle d'un client anonymisé | le moteur | une phrase creuse en grand reste creuse |
| **Le chiffre isolé** | la preuve, un seul chiffre avec sa source | le moteur | deux chiffres, zéro retenu |
| **Le tableau comparatif** | l'objection — deux options, deux quartiers | le moteur | des critères différents par colonne |
| **La chronologie** | les étapes, avec leurs durées | le moteur, une étape par diapo, ou générateur | sans durées, c'est une liste |
| **La liste de contrôle** | l'utile, ce qu'on enregistre | le moteur | plus de sept lignes |
| **Le schéma** | un mécanisme — comment marche une clause, un délai | générateur famille OpenAI, ou gabarit | un schéma faux avec l'air vrai |
| **L'infographie** | une explication dense, plusieurs faits liés | générateur famille OpenAI | lisible sur un écran, pas en vignette |
| **La carte annotée** | le lieu, trois repères | gabarit HTML sur un fond neutre — jamais un plan réel généré | trop de repères |
| **Le diagramme** | une répartition, une tendance, avec sa source | gabarit HTML | un chiffre sans source |

### Ce qui donne le ton

| Type | Sert à | Qui la fabrique | Piège |
|---|---|---|---|
| **L'illustration** | une idée abstraite, une ambiance, sans bien réel | générateur, avec la neutralisation du rendu maison | l'effet catalogue, la dominante jaune |
| **L'affiche** | un événement — porte ouverte, permanence | générateur famille OpenAI, texte court | l'affiche de festival pour une porte ouverte |
| **La bande dessinée** | une situation qui revient, en trois ou quatre cases | générateur famille OpenAI, personnage constant | la blague qui vise un client |
| **Le collage** | plusieurs photos réelles assemblées, une visite en un coup d'œil | gabarit ou assemblage | six images faibles ne font pas une forte |
| **Le mème** | jamais — il vise quelqu'un ou rabaisse le métier | personne | c'est le piège |

### Ce qui se déroule

Le carrousel — un PDF pour LinkedIn, des images pour Instagram et Facebook, fabriqués par le
moteur : `carrousels.md`. La
vidéo, clip de huit secondes à partir d'une photo : `outils-image.md`. Le short face caméra,
zéro montage : `short.md`. Et le moteur qui invente une forme depuis un fait de lui, avec
sa galerie :
`formats.md`.

---

## Comment on choisit

Quatre questions, dans cet ordre.

**Que demande l'angle ?** Le lieu appelle une photo de lieu ou une carte annotée. L'objection
appelle un tableau, un schéma, ou une carte de citation. La preuve appelle un chiffre, un
avant-après, une capture, un document. L'utile appelle une liste, une chronologie, une
infographie. La projection appelle une photo de détail. Les coulisses appellent une photo de
lui, une bande dessinée, ou la carte signature.

**Que demande la plateforme ?** Voir la section images de `plateformes.md` : LinkedIn
recouvre le bas de l'image sur mobile, Instagram rogne en carré pour la grille.

**De quoi dispose-t-il déjà ?** Une photo existante, un message reçu, un avant-après. Le
visuel le plus rentable est souvent celui qu'il a déjà sans le savoir.

**A-t-il le droit ?** Photos d'intérieur, visuels imposés, droits du photographe :
`cadre.md`, et rien ne se devine.

**Si l'angle demande une image que personne ne peut prendre**, c'est un type « qui
explique » ou « qui donne le ton » — jamais une photo inventée d'un bien réel, jamais un
lieu réel généré, même si le générateur sait maintenant le rendre fidèlement.

---

## Ce qui rend un visuel inutilisable

Il sera vu en vignette, sur un téléphone. Six lignes de contenu au maximum, texte deux fois
plus gros que raisonnable, contraste franc. Vertical ou carré, jamais paysage. Un filigrane
d'une autre plateforme le disqualifie. Il doit se comprendre seul, sans le texte.

**L'exactitude, plus stricte qu'ailleurs.** Un chiffre sur une image circule sans son
contexte. Aucun chiffre sans sa source visible sur l'image, et aucun qui ne vienne pas de lui.

**Un visuel par publication.** Deux, c'est un carrousel.
