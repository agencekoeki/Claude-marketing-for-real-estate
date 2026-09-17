# Les portails, et le canal de dépôt

## Ce que ce fichier est

La couche générique et périssable sur les portails d'annonces français. Relevé en septembre
2026, à revérifier tous les six mois. Si l'utilisateur décrit autre chose que ce qui est écrit
ici, **c'est lui qui a raison** : il a le formulaire sous les yeux.

## La première question, et elle décide de tout

**Comment dépose-t-il ?** Deux cas, et ils ne produisent pas la même chose.

**Par son logiciel de transaction ou une passerelle** — c'est le cas de la plupart des
professionnels. Il saisit une fois, le logiciel pousse sur ses portails. Alors **il n'y a
qu'une version** : celle du logiciel, avec sa correspondance de champs — titre, description,
les cases structurées. Les longueurs qui comptent sont celles du logiciel, et ce sont les
portails qui tronquent ensuite. On lui livre une version, et on lui dit où chaque portail
coupera.

**Directement sur chaque portail** — un agent indépendant sans logiciel, ou un portail hors
passerelle. Alors **une version par portail**, chacune dans les longueurs et les champs du
portail, et la première ligne penchée vers son public.

La réponse est dans `00_MOI/cadre.md`, section « Mes portails et mon canal de dépôt ». Si elle
est vide, c'est la première question de l'étape 3 — pas la fiche des faits, pas le titre :
comment il dépose.

## La règle qui remplace « un seul texte partout »

**Une seule source, une version par canal de dépôt.** La fiche des faits, le fait distinctif
et la première ligne sont uniques. Ce qui change d'une version à l'autre : la longueur, la
correspondance des champs, et **la première ligne penchée vers le public du portail** — sans
qu'un seul fait change. Les faits qui divergent entre deux portails sont une faute, pas une
adaptation.

## Les portails, leur public, et ce qu'on sait de leurs contraintes

| Portail | Son public | Ce qu'on sait — septembre 2026 |
|---|---|---|
| Leboncoin | tout le monde, le plus consulté de France | titre ~70 caractères, description ~4 000, jusqu'à 20 photos en offre pro, JPEG obligatoire — le HEIC est refusé |
| SeLoger | le volume, les familles, quasi que des agences | photos sans limite, minimum 4 pour le référencement, HEIC accepté, 800 × 600 minimum |
| Bien'ici | mobile, primo-accédants 25-40 ans, moins de volume mais des contacts mieux qualifiés | JPEG |
| Logic-Immo | les investisseurs locatifs | JPEG ; fait partie du même groupe que SeLoger |
| Belles Demeures, Figaro Immobilier | le premium | à relever sur son formulaire |
| Green-Acres | la campagne, les acheteurs étrangers | à relever |
| MeilleursAgents | des acheteurs informés, qui comparent les prix | à relever |
| Un portail régional | l'ancrage local | à relever |
| **Son site** | ses visiteurs directs, et Google | aucune limite : la version la plus complète, une page par bien à adresse stable |

Leboncoin, SeLoger et Bien'ici sont les trois généralistes de référence ; une passerelle en
alimente souvent huit à quinze. **Aucune part d'audience ne se cite sans source datée** — le
pourcentage qui figurait ici n'en avait pas.

**Tout ce qui n'est pas dans cette table se relève sur le formulaire du portail**, au
navigateur, une fois, et se note dans `cadre.md` : la longueur du titre, celle de la
description, si le titre est composé par le portail, le nombre de photos. C'est le travail de
l'init ou du premier passage de cet outil, pas de chaque annonce.

## Ce qui change d'une version à l'autre

**Le titre.** Sa longueur, et s'il est composé par le portail à partir des champs — alors le
fait distinctif descend en première ligne, règle de `titre.md`.

**La première ligne.** Elle penche vers le public du portail sans changer de fait : sur
Bien'ici, ce qui parle à un primo-accédant — l'état, ce qui est refait ; sur Logic-Immo, ce
qui parle à un investisseur — le loyer possible, les charges ; sur Leboncoin, le fait le plus
concret. Sur son site, la première ligne de la fiche acquéreur retenue.

**La longueur du corps.** Complète sur son site et SeLoger, tenue dans 4 000 sur Leboncoin,
et ce que le formulaire impose ailleurs. On coupe par blocs entiers de `structure.md`, jamais
au milieu d'un bloc : l'environnement saute avant ce qui coûte, jamais l'inverse.

**Les photos.** Le nombre et l'ordre restent ceux de `photos.md` ; le format se convertit en
JPEG pour tout ce qui n'est pas SeLoger.

**Le bloc réglementaire ne change jamais**, portail ou pas.

## Ce qu'on ne fait pas

**On ne réécrit pas les faits pour un portail.** Une surface, une exposition, un prix
identiques partout, ou c'est une faute.

**On ne produit pas dix versions.** Trois canaux au plus se livrent en entier : son logiciel
ou ses trois portails principaux, plus son site. Les autres portent une ligne — « même
version que Leboncoin, tronquée à N » — ou rien.

**On ne pousse aucune annonce.** Il dépose. Même quand un logiciel le permettrait, on ne s'y
connecte pas : c'est un espace à identifiant.
