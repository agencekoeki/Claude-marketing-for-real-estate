# Le titre

## Pourquoi il a son propre fichier

Le titre est la seule ligne lue par les trois lecteurs à la fois, dans la liste de résultats,
à côté de dix-neuf autres. Sur les portails de type Leboncoin, **c'est le champ que la
recherche interroge** : si le mot que tape l'acquéreur n'y est pas, l'annonce ne sort pas.
Et c'est ce que l'assistant extrait en premier.

Un titre se construit, il ne s'écrit pas. Et ce qu'il contient de plus précieux — **le fait
distinctif** — sert ensuite à toute la mallette.

---

## Ce qu'il mange

Cinq entrées, toutes déjà produites avant lui. Il ne demande rien de nouveau.

| Entrée | D'où | Ce qu'il en prend |
|---|---|---|
| La fiche des faits | `faits.md`, étape 1 | le type, la surface, les pièces, le lieu, et les faits candidats |
| La fiche client | `00_MOI/clients-types.md`, étape 2 | ce qu'elle veut lire en premier |
| Le voisinage | `a-cote.md`, étape 1 bis | ce que les comparables titrent tous, à ne pas titrer |
| Le portail | `00_MOI/cadre.md` | sa longueur, et s'il compose le titre lui-même |
| La voix | `00_MOI/voix.md` | ses interdits, ses mots |

---

## Les quatre places, et la cinquième

Un titre a quatre places fixes et une place libre. Les quatre fixes sont ce que l'acquéreur a
filtré et ce qu'il tape : elles y sont toujours.

**Le type.** Maison, appartement, terrain, local. Le mot exact qu'on cherche.

**Le lieu.** La commune, ou le quartier si c'est ce qu'on tape. Un seul.

**La surface.** En m², le chiffre.

**Les pièces.** Le nombre, en chiffre.

**Et la cinquième place : un seul fait distinctif.** C'est là que le titre se gagne, et c'est
la seule place où on réfléchit.

> Maison 4 pièces, 96 m², Tarascon centre, jardin clos de 200 m²

**Aucun adjectif nulle part.** Personne ne tape « lumineux », un assistant écarte « rare », un
acquéreur ne croit pas « idéal », et le vendeur trouve « coup de cœur » creux. Le titre n'a
pas la place pour un mot qu'aucun des trois lecteurs n'utilise.

**Pas de prix.** Il a son propre champ et il s'affiche à côté. Le mettre dans le titre coûte
quinze caractères pour rien.

---

## Choisir le fait distinctif

Trois filtres, dans cet ordre, et le premier tranche presque toujours.

**1. Ce que la fiche client veut lire en premier.** Une famille lit le jardin ou les chambres.
Un investisseur lit le loyer ou l'état locatif. Un primo-accédant lit ce qui a été refait, avec
sa date. Le champ « ce qui le met en route » de la fiche désigne le fait.

**2. Ce que les comparables ne titrent pas.** Si quatre annonces sur cinq dans la liste
titrent sur le jardin, le nôtre ne se distingue pas par le jardin — il prend le fait suivant de
la fiche. À faits égaux, on prend celui que personne ne met en avant. Voir `a-cote.md`.

**3. Un fait qu'on tape et qu'on vérifie.** « Garage » se tape et se vérifie en visite.
« Toiture 2022 » se vérifie sur facture. « Calme » ne se tape pas et ne se vérifie pas — il ne
va jamais dans un titre.

**Si aucun fait ne passe les trois filtres**, on titre avec les quatre places seules. Un titre
sans cinquième place est un titre honnête ; un titre avec un adjectif à la place est un titre
qu'on saute.

---

## L'ordre des mots

**Le mot le plus cherché en premier**, parce que les titres se coupent — à la fin, sur un
téléphone, dans une liste étroite. Le type et le lieu d'abord, le fait distinctif ensuite, la
surface et les pièces là où il reste de la place.

Sauf quand le fait distinctif **est** ce qu'on cherche : « Garage » ou « Terrain constructible »
en tête si c'est ce que la fiche tape.

**Soixante-dix caractères**, espaces comprises, pour tenir partout. Si le portail en affiche
moins, c'est lui qui a raison et c'est dans `cadre.md`.

---

## Si le portail compose le titre lui-même

Certains portails assemblent le titre à partir des champs — type, pièces, surface, ville — et
le titre de l'agent n'est qu'un champ secondaire ou n'apparaît pas. **Tu ne le devines pas :
c'est dans `cadre.md`, ou tu lui demandes.**

Dans ce cas, deux choses changent. Le fait distinctif descend en **première ligne**, qui
devient ce que l'acquéreur lit après le titre automatique. Et les champs structurés doivent
être remplis avec le mot exact — c'est eux qui feront le titre.

Le fait distinctif, lui, ne change pas : il a été choisi, il reste.

---

## Le test, avant de retenir

**Écris-le dans la liste, mentalement, à côté de quatre titres de comparables.** Il doit se
distinguer par un fait, pas par un ton. Si les cinq titres se ressemblent, le fait distinctif
est mal choisi. Si le nôtre est le seul avec un adjectif, il est mal écrit.

Puis **la promesse** : ce que le titre annonce, la première ligne doit le tenir. Un titre qui
dit « jardin clos de 200 m² » appelle une première ligne qui dit ce qu'on y fait — pas une
première ligne sur la cuisine.

---

## Ce qu'il produit, et qui s'en sert

**Un titre, un fait distinctif, une raison.** Les trois s'enregistrent dans
`01_BIENS/<bien>/annonce.md`, en tête :

```
titre: Maison 4 pièces, 96 m², Tarascon centre, jardin clos de 200 m²
fait_distinctif: jardin clos de 200 m²
pourquoi: la fiche famille lit le jardin en premier, et aucun comparable ne le chiffre
```

**Le fait distinctif est ce qui sert ensuite.** La première ligne le tient. La première photo
le montre — voir `photos.md`. Et `immo-reseaux-sociaux` le reprend : quand il publie sur ce
bien — mandat signé, toujours disponible, bilan de vente — il ouvre sur le même fait, pas sur
un autre. C'est ce qui fait qu'un acquéreur qui voit le post puis l'annonce reconnaît le bien.

Au niveau 2, deux titres sont proposés — deux faits distinctifs différents, et il tranche. Aux
niveaux 1 et 3, tu tranches et tu annonces.

---

## Ce qu'on ne fait pas

**Pas de majuscules de cri, pas de point d'exclamation, pas de « URGENT », « RARE »,
« EXCLUSIVITÉ ».** Ils se voient et ils font passer.

**Pas deux faits distinctifs.** Un titre avec « jardin, garage, vue » ne distingue rien : il
liste. Un seul, celui de la fiche.

**Pas de mot que le vendeur contesterait.** Il lit le titre le premier, et « à rénover » dans
le titre d'un bien qu'il a entretenu trente ans coûte le mandat. Ce qui coûte se dit dans le
corps, pas dans le titre.

**Un seul fait distinctif, quel que soit le portail.** Le titre s'ajuste à la longueur de
chaque canal et descend en première ligne là où le portail le compose lui-même — mais le fait
distinctif ne change pas d'un portail à l'autre. Voir `portails.md`.
