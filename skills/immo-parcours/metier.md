# Couche métier — le parcours d'un client d'agent immobilier

**Le seul fichier à réécrire pour décliner ce skill sur un autre métier.** Les autres outils
lisent les étapes par leur numéro : on ne les renomme pas, on n'en ajoute pas.

---

## Le parcours vendeur — neuf étapes

C'est là que se joue le mandat, et donc l'USP. On le remplit en premier.

| # | Étape | Ce qu'on y regarde |
|---|---|---|
| 1 | Il y pense | l'événement de vie qui déclenche, ce qu'il tape, à qui il en parle |
| 2 | L'estimation | ce qu'il attend, le prix qu'il a en tête, ce qui le fait douter de l'agent |
| 3 | Le choix de l'agent | contre qui, sur quoi il compare, ce dont il se souvient — **c'est l'étape de l'USP** |
| 4 | Le mandat | simple ou exclusif, ce qu'il craint en signant, ce qu'il demande |
| 5 | La mise en vente | ce qu'il veut voir dans son annonce, à quelle vitesse, ce qu'il juge |
| 6 | Les visites | ce qu'il attend après chaque visite, ce qu'il ne supporte pas |
| 7 | L'offre | comment il réagit à une offre basse, qui il consulte |
| 8 | Le compromis et l'acte | ce qui l'inquiète, les délais qu'il ne comprend pas |
| 9 | Après | s'il recommande, à qui, et ce qui l'en empêcherait |

**Où on le perd, typiquement :** à l'étape 3 au profit d'un confrère, à l'étape 4 sur
l'exclusivité, à l'étape 6 sur le silence entre deux visites, à l'étape 7 sur une offre qu'il
prend pour une insulte.

## Le parcours acquéreur — sept étapes

| # | Étape | Ce qu'on y regarde |
|---|---|---|
| 1 | Il cherche | ses filtres, ses alertes, depuis combien de temps, ce qui l'a déjà déçu |
| 2 | Il voit l'annonce | ce qu'il lit en premier, ce qui le fait cliquer, ce qui le fait passer |
| 3 | Il visite | ce qu'il vérifie, ce qu'il redoute, la question qu'il pose au téléphone avant |
| 4 | Il fait une offre | ce qui le décide, qui il consulte, combien de temps il hésite |
| 5 | Il finance | ce qu'il ne sait pas, ce qui le bloque |
| 6 | Le compromis et l'acte | les délais, les conditions, ce qui l'inquiète |
| 7 | Il emménage | s'il en parle, à qui |

**Les étapes 2 et 3 sont celles de l'annonce** : `immo-annonce` les lit pour savoir ce que
l'acquéreur redoute avant de visiter, et donc ce que l'annonce doit répondre.

---

## Ce qui rend une case vraie

Une case du parcours ne se remplit qu'avec **une chose qu'un client a dite ou faite**, dans un
dossier réel. « Il veut être rassuré » est une supposition ; « il m'a demandé trois fois si le
prix était le bon » est un fait. Les mots des clients viennent de la section 3 du profil, des
fiches, et des comptes rendus si l'init les a lus.

La case « où je le perds » vient des dossiers perdus, en bas de `clients-types.md`. Si cette
table est vide, c'est la première chose à remplir : sans dossier perdu, on ne sait pas où le
parcours casse.

---

## Ce que les autres outils en font

**`immo-reseaux-sociaux`** lit la colonne « ce qu'il se demande » : chaque question est un
sujet, à l'étape où elle se pose. C'est la mission « se faciliter la vie » alimentée par le
parcours au lieu de la mémoire.

**`immo-annonce`** lit les étapes 2 et 3 de l'acquéreur, et l'étape 5 du vendeur — ce qu'il
veut voir dans son annonce.

**`immo-suivi`**, à venir, lira les étapes 5 à 8 du vendeur : c'est le point vendeur.

**L'USP** se pose sur le parcours vendeur, un comportement par étape où il se voit. Une étape
sans comportement est une étape où il est un agent comme les autres.
