# Apparier une fiche et des biens

## Ce que c'est

Deux directions, un seul mécanisme.

**Un client, quels biens.** Une personne placée — par `lire.md` ou parce qu'il la décrit —
et la question : dans ce que j'ai, qu'est-ce qui lui va ? C'est le geste quotidien d'un agent
avec un acquéreur, et il le fait de tête. Ici on le fait depuis l'index.

**Un bien, quelle fiche.** Un bien entre — un mandat signé — et la question : à qui il parle ?
C'est ce qu'`immo-annonce` a besoin de savoir pour la première ligne, et ce que
`immo-reseaux-sociaux` a besoin de savoir pour la cible d'un post sur ce bien.

## Ce qu'on lit

**`01_BIENS/index.md`**, une ligne par bien : type, surface, secteur, statut, fiche acquéreur
probable. Créé par l'init depuis son fichier de stock, tenu à jour par `immo-annonce`. **S'il
n'existe pas, on ne fouille pas son ordinateur pour le reconstituer** — on lui demande son
fichier de biens, ou on travaille avec ce qu'il dit.

**Les fiches côté acquéreur** : ce qui le met en route, ce qu'il lui faut, ce qui le bloque.

**Et le parcours acquéreur, étapes 1 à 3** : ce qu'il cherche, ce qui le fait cliquer, ce
qu'il redoute avant de visiter.

## Comment on apparie

**Par ce qui met en route, pas par les critères.** Les critères — surface, budget, pièces —
sont les filtres du portail, et l'acquéreur les a déjà appliqués. Ce qui apparie, c'est
« ce qui le met en route » de la fiche contre le fait distinctif du bien : une famille qui
cherche un jardin contre un bien dont le fait distinctif est le jardin.

**Trois biens au plus par personne, un ou deux par bien.** Au-delà, on liste, on n'apparie
plus.

**Chaque appariement porte sa raison en une ligne**, et la raison est un fait de l'index
contre un champ de la fiche. « Parce qu'il cherche un jardin et que celui-là en a un de
200 m² » ; jamais « parce que ça pourrait lui plaire ».

**Et ce qui le bloque se vérifie sur le bien.** Si la fiche dit « il fuit les travaux » et que
l'index dit « travaux à prévoir », on ne l'apparie pas — ou on le dit.

## Ce qu'on rend

> Pour [fiche] : [bien] — parce que [fait contre champ]. [bien] — parce que [...].
> À écarter malgré les critères : [bien] — parce que [ce qui le bloque].

Ou, pour un bien qui entre :

> Ce bien parle à [fiche], parce que [fait distinctif contre ce qui la met en route]. La
> première ligne de l'annonce et la cible du post en découlent.

## Ce qu'on écrit

**Dans `01_BIENS/index.md`, la colonne « fiche acquéreur probable »** d'un bien qui vient
d'être apparié — proposée, validée, écrite. C'est la seule écriture de ce mode, et elle sert
aux deux autres outils.

**Jamais un nom de client dans l'index.** Un appariement est une fiche contre un bien, pas
une personne contre une adresse.

## Ce qu'on ne fait pas

**On ne propose pas un bien qui n'est pas dans l'index.** Pas de recherche sur les portails
pour trouver ce qu'il n'a pas : c'est son stock, ou rien.

**On n'apparie pas un vendeur à un bien.** Le vendeur choisit un agent ; c'est l'USP, pas
l'index.

**On ne fait pas de tableau croisé fiches × biens** pour tout le stock. On apparie une
personne, ou un bien — pas le marché.
