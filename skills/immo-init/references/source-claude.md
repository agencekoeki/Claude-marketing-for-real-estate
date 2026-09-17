# Fouiller son compte Claude — à sa demande seulement

**Tu ne fouilles ni sa mémoire ni ses conversations passées de ta propre initiative.** Ces deux
gisements ne s'ouvrent que s'il le demande en toutes lettres : « regarde dans nos anciennes
conversations », « pars de ce que ta mémoire sait de moi ». À l'écran des sources, tu peux dire une
fois que c'est possible ; tu ne le proposes pas davantage. Sans sa demande, l'enquête se fait sans
eux.

C'est la source la moins chère et la plus riche quand il utilise déjà Claude — quand il la
demande. Deux gisements distincts, qui ne s'interrogent pas de la même façon.

**Sa mémoire** : des fiches déjà écrites sur lui. S'il le demande, tu les lis ; le protocole
complet est dans `memoire.md` — commence par là.

**Ses conversations passées** : une recherche par mots. S'il le demande, tu dois savoir quoi
chercher.

**Vérifie que la recherche dans les conversations passées est disponible dans le contexte où
tu tournes.** Si elle ne l'est pas, dis-le en une phrase, note-le en section 13, et passe aux
fichiers. Ne fais pas semblant de chercher.

---

## La règle qui décide de tout

La recherche dans les conversations est une **recherche textuelle**. Elle a besoin de mots
qui ont réellement figuré dans les échanges.

Les mots méta ne matchent rien : « mes habitudes », « ce dont on a parlé », « mon style »,
« hier », « mes préférences ». Ils décrivent l'acte de parler, pas ce dont on a parlé.

Les mots de contenu matchent : le vocabulaire de son métier, le nom d'une commune, le nom
d'un logiciel.

Requêtes courtes, deux à quatre mots. Chaque requête doit être différente des précédentes :
reformuler la même idée ne change pas les résultats, il faut changer d'angle.

---

## Les requêtes

**Elles sont dans `metier.md`, section « Batteries de requêtes ».** Cinq passes : métier,
production, outils, correction, temporelle.

Deux méritent un mot ici parce que leur valeur n'est pas évidente.

**La passe correction** est la meilleure pour le style, et personne n'y pense. Chercher
« plus court », « trop long », « ne dis pas », « réécris » ramène des préférences qu'il a
exprimées lui-même. Donc `[dit]`, pas une inférence.

**La passe temporelle** ne cherche pas par sujet mais par fenêtres de dates. Elle sert à voir
à quels moments il sollicite, ce qui alimente directement les récurrences.

---

## Comment lire un résultat

Ouvre une conversation **à l'endroit du résultat**, pas au début. Tu cherches un passage, pas
une lecture intégrale. Une ou deux conversations ouvertes par question, pas dix.

**Distingue toujours qui a dit quoi.** C'est la règle la plus importante de cette source. Une
suggestion que Claude a faite et que l'utilisateur n'a pas commentée n'est pas une décision
de l'utilisateur. Une idée émise dans un brainstorm reste une hypothèse. Un extrait peut
commencer au milieu d'un message : n'attribue pas ce dont tu n'es pas sûr.

Concrètement : tu ne marques `[dit]` que ce qu'il a écrit lui. Ce que Claude a proposé et
qu'il a validé explicitement se marque `[dit]` aussi. Tout le reste est `[à confirmer]`.

---

## Ses messages à lui, comme corpus

**Ses propres messages dans les conversations sont son registre le plus brut** : personne ne
se surveille en parlant à un outil. Copie-les — ses messages seulement, jamais les réponses
de Claude — dans un fichier temporaire, et c'est le corpus du registre « messages à Claude »
pour `scripts/stylo.py`. Voir `stylometrie.md`. Le fichier temporaire se supprime après la
mesure : on ne garde que la carte.

## Le glossaire maison

Passe à faire en lisant les résultats, pas en lançant des requêtes. **Relève les mots qu'il
emploie sans jamais les expliquer** : sigles, noms de dossiers, de secteurs, de résidences,
surnoms de quartiers, abréviations maison. Un terme qu'il n'a jamais défini dans une
conversation est un terme qu'il considère comme évident — c'est exactement la définition de
ce qui doit entrer en section 7.

C'est la case que personne ne pense à écrire et celle qui fait qu'un outil comprend une
demande du premier coup au lieu de demander. Elle se remplit aussi depuis ses comptes rendus
de réunion et ses mails : garde l'œil ouvert sur ces sources-là.

## Ses projets

Leurs noms et leurs instructions sont déjà un profil : ils disent ce qu'il fait assez souvent
pour avoir mérité un espace dédié. Un projet « posts » ou « annonces » est en soi un
candidat-skill, à noter dans `recurrences.md`.

---

## Si tout est vide

Trois causes possibles, dis laquelle tu soupçonnes plutôt que de conclure qu'il n'y a rien :

- il découvre Claude aujourd'hui
- la génération de mémoire depuis les conversations est désactivée dans ses réglages
- la recherche et la référence aux conversations passées est désactivée

Note l'état en section 13 du profil et passe à la source suivante. N'attends pas qu'il les
active.

**Attention au périmètre.** Si tu travailles depuis un projet, seules les conversations de ce
projet sont visibles. Hors projet, seules celles hors projet. Si tu ne trouves rien et qu'il
affirme avoir beaucoup discuté, c'est souvent ça : demande-lui de relancer l'init depuis
l'endroit où il travaille d'habitude.

---

## Plafond

Voir `protocole.md`. Arrête-toi plus tôt si trois requêtes d'affilée ne ramènent rien de neuf.

---

## Rappel de marquage

Avant d'écrire quoi que ce soit tiré de cette source : chaque ligne porte `[dit]`, `[vu]` ou
`[à confirmer]`, **suivi du mois** — `[dit 2026-09]`. Ce qu'il a dit lui-même est `[dit]`. Ce
que tu as constaté ici est `[vu]`, formulé comme un constat vérifiable. Le reste est
`[à confirmer]` et reste vide.

Quand la date est inconnue — une ligne reprise d'ailleurs, un import — on écrit `[dit ?]`
plutôt que d'inventer un mois.

Une occurrence unique reste une occurrence unique. Tu n'inventes jamais une valeur pour
remplir une case.
