# Fabriquer un carrousel

## La chaîne, dans l'ordre

Sept étapes, et **aucune ne se saute** : le fichier final vient en dernier, jamais avant le
texte.

**1. Cadrer.** La fiche client, la promesse en une phrase, le modèle retenu parmi les sept plus
bas. Tu les as déjà si les étapes du `SKILL.md` sont faites.

**2. Écrire avant de fabriquer.** Le texte intégral de chaque diapo, dans la conversation, une
diapo par bloc. **Il le valide avant toute fabrication** — c'est la seule validation que la
chaîne lui demande, et elle tient en une question.

**3. La couverture.** Du texte seul par défaut. Une de ses photos si ses droits sont confirmés.
Une image générée seulement si elle ne représente aucun bien réel : le prompt vient de
`outils-image.md`, et c'est lui qui la fabrique.

**4. Structurer.** Le texte validé devient un `contenu.json`, rangé dans le dossier du kit pour
pouvoir refabriquer, qui suit `assets/carrousel.exemple.json` : une entrée par diapo, les champs
de son type, rien d'autre.
Chaque crochet de l'exemple se remplace — le moteur refuse un crochet oublié.

**5. Fabriquer.** `python3 scripts/build_carrousel.py contenu.json <dossier de sortie> --cadre
00_MOI/cadre.md --racine <dossier de travail>`. Le script est dans le dossier `scripts/` de cet
outil ; dans un dossier de travail, sa copie `.claude/skills/immo-reseaux-sociaux/scripts/`. Il
lui faut Python 3, reportlab et Pillow — l'en-tête d'état de son profil dit ce que l'installation a
trouvé : s'ils manquent, installe-les si l'environnement le
permet, sinon le gabarit de secours plus bas.

**6. Contrôler.** Lis `controle/rapport.txt`. **Un BLOQUANT se corrige dans le texte, puis on
refabrique** — rien de publiable n'a été écrit. Puis regarde `controle/planche.png` et
`controle/vignette.png` avec la liste fermée « Avant de livrer » : oui ou non à chaque ligne, pas
une relecture ouverte qui cherche ce qui pourrait être mieux.

**7. Livrer.** Le PDF pour LinkedIn, les images dans l'ordre pour Instagram et Facebook, le texte
du post, et le titre du document que LinkedIn demande au téléversement. Chaque fichier
séparément, jamais dans une archive. Avec un dossier : `02_PUBLICATIONS/brouillons/`, un dossier
au nom du kit, à côté de lui.

## Ce que le moteur impose, et pourquoi

| Règle | Pourquoi, et ce qui arrive sinon |
|---|---|
| Texte courant à 40 px, jamais sous 34 | un téléphone affiche une diapo de 1 080 px à un peu plus d'un tiers de sa taille : 22 px y deviennent illisibles |
| Rien d'informatif au-dessus de 120 px ni sous 1 100 px | règle de prudence de la mallette : les boutons et les barres des applications recouvrent le haut et le bas |
| Cinq à dix diapos, la couverture en tête, une seule action en dernier | BLOQUANT ; neuf ou dix sont signalées |
| Aucun lien dans le document | BLOQUANT — le lien va dans le texte du post |
| Un chiffre porte sa source, sur sa diapo | BLOQUANT si la source est à confirmer ; un chiffre glissé dans un texte sans source est signalé |
| Une photo ou un avant-après, seulement si ses droits sont confirmés | BLOQUANT — c'est `cadre.md` ou lui qui le disent, jamais toi |
| Ses couleurs et sa signature, lues dans `cadre.md` | sinon couleurs neutres de la mallette : la remarque de rang 7 de `livrer.md` |
| Des couleurs lisibles sur leur fond | une dominante ou un accent trop clairs sont remplacés, et le rapport le dit |

## Ce qui compte en plus du sujet

Un carrousel n'est pas un texte découpé en pages. C'est **une suite d'écrans qui doivent
chacun mériter le glissement suivant**, et c'est ça qu'on travaille.

Cinq choses décident du résultat, aucune n'est le sujet.

**La promesse de la couverture.** Elle est vue en vignette, dans le fil, avant tout le reste.
Si elle explique, elle a raté ; si elle promet quelque chose de précis, on glisse.

**La progression.** Chaque diapo livre une partie de la promesse et en garde. Une diapo qui
n'apporte rien de neuf est l'endroit exact où on décroche.

**La cohérence de grille.** Marges identiques, éléments à la même place, pied identique. Un
titre qui saute de trois centimètres d'une diapo à l'autre se voit immédiatement quand on
défile vite — c'est ce qui sépare un carrousel fait maison d'un carrousel tenu.

**La densité.** Une idée par diapo, et une quinzaine de mots au maximum sur une diapo de
contenu. Tout le reste va dans le texte du post.

**La sortie.** La dernière diapo est celle où le doigt s'arrête — principe de la mallette, sans
chiffre faute de source référencée ici. Une seule action, et elle doit être faisable depuis l'endroit où il lit.

---

## Le nombre, et où ça décroche

**Six à huit diapos, cinq pour les plus courts.** En dessous de cinq, l'effort ne vaut pas la
peine et le format ne produit rien. Au-delà de dix, on en demande trop à quelqu'un qui fait défiler — règle de métier de la mallette,
sans chiffre faute de source.

**La jauge d'avancement en tête de chaque diapo n'est pas décorative :** savoir qu'il reste
deux écrans fait finir, ne pas savoir fait abandonner.

---

## Les variantes du moteur

Le moteur en porte dix, sur une grille commune ; le champ `type` de chaque diapo les nomme.
**Ne mélange pas plus de trois variantes dans le corps d'un même carrousel** : au-delà, la série
perd son unité, et le rapport le signale.

| Variante (`type`) | Sert à | Place habituelle |
|---|---|---|
| Couverture (`couverture`) | promettre | toujours la première, toujours seule |
| Idée (`idee`) | une affirmation et son explication | le corps |
| Étape (`etape`) | une chronologie, une étape par diapo, avec sa durée | tout le corps si c'est le sujet |
| Chiffre (`chiffre`) | un chiffre isolé avec sa source | un par diapo ; trois au plus, dans le bilan chiffré |
| Deux colonnes (`colonnes`) | idée reçue contre réalité, avant contre après | une seule fois |
| Liste (`liste`) | ce qu'on vérifie, de deux à sept lignes | une seule fois |
| Citation (`citation`) | une phrase d'un client, anonymisée | une seule fois |
| Photo (`photo`) | une de ses photos, légende courte | à retirer s'il n'en a pas |
| Avant-après (`avant_apres`) | deux photos au même cadrage, la légende sur la jointure | le corps de l'avant-après |
| Action (`action`) | une seule chose à faire | toujours la dernière |

Une durée d'étape ou un chiffre dans un texte portent leur source : champ `source` sur la
diapo, affiché en bas du contenu.

---

## Sept carrousels qui marchent dans ce métier

Pour chacun : le nombre de diapos, ce qu'il faut avoir, et ce qu'on met en couverture.

**Les étapes d'une vente.** Sept diapos : couverture, cinq étapes, action. Ce qu'il faut : les
durées réelles, pas théoriques — c'est ce qui intéresse et c'est ce qu'il est seul à savoir.
Couverture : le temps total, ou l'étape que personne n'anticipe.

**Ce qui fait rater une vente.** Six : couverture, quatre erreurs, action. Ce qu'il faut :
quatre dossiers réels, anonymisés. Couverture : l'erreur la plus contre-intuitive, pas la plus
grave.

**Le bilan chiffré d'une vente.** Six : couverture, trois chiffres, une photo, action. Ce
qu'il faut : ses chiffres avec leur source — nombre de visites, délai ; l'écart au prix affiché
seulement si `00_MOI/cadre.md` l'autorise, parce qu'il dit ce qu'une vente identifiable a rapporté.
Couverture : le chiffre le plus surprenant. **C'est le carrousel qui rentre des mandats**,
parce qu'il s'adresse aux vendeurs.

**Une idée reçue démontée.** Cinq : couverture, deux colonnes, deux idées, action. Ce qu'il
faut : un fait qui contredit, sinon on n'en fait pas.

**Le quartier en cinq repères.** Sept : couverture, cinq photos légendées, action. Ce qu'il
faut : cinq photos prises par lui, et les noms des lieux. Le plus simple à produire et le plus
rare.

**La préparation d'un bien, avant-après.** Cinq : couverture, deux avant-après, une idée,
action. Ce qu'il faut : des photos au même cadrage — sinon ça ne prouve rien.

**Vendre maintenant ou attendre.** Cinq : couverture, deux colonnes, deux idées, action. Ce
qu'il faut : des critères identiques des deux côtés, et aucune donnée de marché inventée.

**Aucun de ces sept ne demande de photo professionnelle**, sauf le quartier et l'avant-après —
et un téléphone suffit.

---

## Ce qui va dans le texte du post

**Pas ce qui est sur les diapos.** Le texte pose le contexte et donne une raison de faire
glisser ; il ne répète jamais le contenu.

Trois à cinq lignes suffisent, avec l'accroche qui tient avant la coupe — voir `apercu.md`.

---

## Le coût, et quand ne pas le proposer

Le moteur lui épargne la mise en page et l'export : il lui reste à valider le texte et à
téléverser. **Le temps d'un carrousel reste celui de son texte**, et c'est toujours le format le
plus long à écrire.

**Pas plus d'un par semaine — et pas plus d'un par mois s'il ne tient pas déjà trois
publications par semaine.** Un carrousel isolé dans un fil de textes n'installe rien.

**Et propose-le en priorité pour ce qui se garde :** les étapes, les erreurs, le bilan chiffré.
Ce sont les seuls qu'on enregistre et qu'on ressort.

---

## Si le moteur ne peut pas tourner

Pas de Python, ou ni reportlab ni Pillow, et pas moyen de les installer :
`assets/diapos.template.html`. Même grille, mêmes tailles, même zone sûre, mais sept variantes
seulement — ni liste, ni citation, ni avant-après. Il s'exporte en PDF : la page est réglée à
1 080 × 1 350, sans marge, ne pas choisir A4. Pour Instagram, chaque diapo se capture. **Dis-le en
livrant** : ce fichier n'a pas été contrôlé par le moteur, et la liste ci-dessous se fait à la
main.

## Avant de livrer

- `controle/rapport.txt` : aucun BLOQUANT, et chaque ATTENTION a été lue et tranchée
- la couverture promet, elle n'explique pas, et elle se lit à la taille de `controle/vignette.png`
- cinq à huit diapos, pas plus de trois variantes dans le corps
- aucune diapo ne se retire sans que la promesse y perde
- une idée par diapo, une quinzaine de mots au maximum
- la jauge avance correctement du premier au dernier écran
- le pied est identique partout
- la dernière porte une seule action, et aucun lien n'est dans le document
- chaque chiffre porte sa source sur la diapo où il apparaît
- chaque photo a ses droits confirmés, et aucune image générée ne représente un bien réel
- les couleurs et la signature sont les siennes — sinon c'est dit en livrant
- le texte du post ne répète pas les diapos
