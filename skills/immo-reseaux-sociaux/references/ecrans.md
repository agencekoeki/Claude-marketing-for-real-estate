# Les écrans

Même dispositif que `immo-init`, en plus court. Deux suites d'écrans, une par mode : le carnet
en trois, l'écriture en cinq. **On ne mélange pas les deux dans une même séance.**

---

## Le panneau de progression porte la position

**Le geste est précis :** dans ta toute première réponse, avant d'écrire quoi que ce soit à
l'écran, tu poses ton plan avec les écrans du mode retenu — trois pour le carnet, cinq pour
l'écriture — une ligne par écran, dans l'ordre, avec leurs titres mot pour mot. Puis tu marques
chaque écran terminé au moment où il l'est.

Si le panneau ne se remplit pas, tu ne le mentionnes pas et tu n'insistes pas. **Seul le
titre s'affiche**, donc les titres sont ceux des
écrans, courts. Il ne rend que les tâches touchées dans l'échange en cours, et c'est une vue
qu'on alimente sans l'éditer.

## La forme d'un écran, dans le fil

**Deux lignes de markdown.** Pas de caractères de cadre, pas de bloc de code, pas de chasse
fixe : l'application a sa propre typographie, plus lisible que tout ce qu'on dessinerait, et
elle s'adapte à la largeur de l'écran.

```
### 3 · L'angle et l'endroit
> Deux directions, tu choisis.
```

**Le compteur ne va pas dans le titre** : la position est dans le panneau de progression.

## Les écrans du mode carnet

| # | Titre | Ligne d'intention |
|---|---|---|
| 1 | Ce qui arrive | Tes biens, tes rendez-vous de l'année. |
| 2 | Ce qu'ils demandent | Leurs objections deviennent des sujets. |
| 3 | Ton carnet | Six à huit sujets, tu rayes le reste. |

L'écran 3 est le livrable. Les deux premiers se font en quelques échanges.

## Le mode post du jour — un seul écran

Pas de tunnel : une tâche déclarée, « Ton post du jour », et l'écran de livraison
`assets/ecran-post-du-jour.html`. Le texte reste dans le fil, entre ses deux traits.

## Les écrans du mode écriture

| # | Titre | Ligne d'intention |
|---|---|---|
| 1 | De quoi on parle | Sur quoi, et pour qui. |
| 2 | Ce que tu as déjà dit | Je regarde ce qui est déjà sorti. |
| 3 | L'angle et l'endroit | Deux directions, tu choisis. |
| 4 | Le texte et les photos | Voilà, à toi de corriger. |
| 5 | Rangé | Où il est, ce qu'il reste à faire. |

Les écrans 2 et 5 sont souvent muets : s'il n'y a rien de publié et rien à compléter, une
ligne suffit et on enchaîne. Ne fabrique pas de contenu pour remplir un écran.

**L'écran 4 est le seul qui compte vraiment.** Si la séance doit être courte, ce sont le 2 et
le 3 qui se compressent, jamais le 4.

## Ce qui va dans le corps

**Rien de ce qu'il doit lire attentivement, copier ou corriger ne va dans un bloc de code.**
Surtout pas le texte de la publication : un bloc de code se lit comme du technique, et il doit
le juger comme un lecteur, pas comme un développeur. La forme de la livraison — les deux
traits qui encadrent le texte — est dans `livrer.md`.

En revanche, dès que le contenu est comparatif — deux angles à comparer, les photos à prendre
dans l'ordre, les sujets du carnet — **un tableau markdown** vaut mieux qu'un paragraphe.

---

## Trois registres, du plus riche au plus sûr

Un écran rendu dans un panneau si c'est possible, le panneau de progression sinon, et les deux
lignes de markdown dans tous les cas. Tu prends la plus riche disponible et tu redescends sans
commentaire. **L'écran affiche, la conversation demande** — la question reste toujours dans le
fil.

**Mais le panneau est une ressource unique** : un écran rendu remplace l'affichage de la
progression et rétrécit la conversation. Il ne se justifie que là où il y a quelque chose à
regarder.

**Un seul écran rendu se justifie ici : à l'étape 4.** `assets/ecran-livraison.html` porte tout
ce que `livrer.md` prescrit au même endroit — le texte avec son trait de coupe, le plan de
prise de vue à côté, les remarques en dessous. Voir la publication et ce qu'il faut
photographier côte à côte est ce qui fait comprendre qu'un post n'est pas un texte.

**Et pour le carnet**, `assets/ecran-carnet.html` : c'est le seul livrable de la séance et il
sert trois mois, donc il mérite d'être un objet, comme le relevé de l'installation.

Une exception absolue : **le texte de la publication reste aussi dans le fil**, en clair. Il
doit pouvoir le copier, le corriger, le coller ailleurs. Un texte qui n'existe que dans un
panneau est un texte qu'il ne publiera pas.

**Comment on affiche un écran rendu :** tu lis le fichier, tu remplaces les crochets, tu crées
un artefact. Un seul par réponse. Si ça échoue, tu passes au texte sans commenter — on ne
décrit jamais un écran qu'on n'a pas réussi à montrer.

Les deux pages suivent la coque commune de la mallette — bandeau d'état, **à faire avant tout
le reste**, le principal, rangé — la même que l'init et l'annonce. Ce qu'il doit faire se lit
sans défiler. Tu remplaces les crochets, tu ne les fabriques pas. Elles portent
les couleurs du relevé de l'installation, et c'est délibéré — le stagiaire reconnaît l'objet,
c'est la même mallette.

---

## Les réponses possibles

Affichées sous chaque écran qui attend quelque chose.

> répondre · « je ne sais pas » · « écris, on verra après » · « où on en est ? »

**Répondre.** Le cas normal.

**« Je ne sais pas ».** Tu prends la valeur la plus probable, tu le dis, tu avances.
Contrairement à l'init, tu ne laisses pas vide : un texte a besoin d'une cible et d'un angle
pour exister. Tu décides, tu annonces ta décision, il corrigera sur le texte.

**« Écris, on verra après ».** La plus fréquente, et elle est légitime. Tu sautes les écrans 1
à 3, tu décides seul, et **tu dis en une ligne ce que tu as choisi** — « j'ai visé tes
vendeurs, sous l'angle du quartier » — au rang 3 du classement de `livrer.md`. Corriger un
texte est plus facile que répondre à trois questions, et beaucoup de gens travaillent comme ça.

**« Où on en est ? »** Tu redis l'écran courant et ce qui reste.

Face à une réponse absurde ou agressive, tu ne relèves pas : tu traites comme un « je ne sais
pas », tu décides, et tu écris. Un texte livré vaut mieux qu'une discussion.

## Le niveau change ce qu'on affiche

**Au niveau 1, on n'affiche pas les réponses possibles.** Un menu de quatre options à quelqu'un
qui ne sait pas quoi répondre est une question de plus, pas une aide. Tu décides, tu livres, tu
poses une seule question ouverte à la fin.

Aux niveaux 2 et 3, elles s'affichent normalement. Voir `niveau.md`.
