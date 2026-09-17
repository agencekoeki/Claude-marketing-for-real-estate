# Livrer

## Ce fichier possède la sortie

Douze choses réclament d'être dites au moment de livrer, réparties dans tout le package.
**Aucune ne se déclenche seule : elles passent toutes par ici, elles sont classées, et elles
sont plafonnées.**

Sans ça, elles s'additionnent — et elles s'additionnent le plus chez le débutant, qui n'a ni
échantillons, ni fiche, ni couleurs réglées. Celui qui est le moins armé recevrait le plus
gros mur. C'est l'inverse de ce que les niveaux promettent.

---

## La forme, et elle ne varie jamais

Trois blocs, dans cet ordre, et rien d'autre.

```
[une phrase, maximum, avant le texte — ou rien]

───────────────────────────────

Le texte de la publication, tel qu'il sera publié.

Rien d'autre entre les deux traits.

───────────────────────────────

[ce qu'il doit faire, s'il y a quelque chose à faire]
[une ou deux remarques, pas plus]
[une question]
```

**Les deux traits ne sont pas décoratifs.** Ils délimitent ce qu'il doit sélectionner pour
copier. Sans eux, le post est de la prose au milieu de ta prose, et il doit deviner où
commencer — sur un téléphone, entre deux visites, c'est la friction qui fait qu'on ne publie
pas.

**Jamais de bloc de code pour le texte.** Il doit le juger comme un lecteur, pas comme un
développeur. Le trait fait le travail du délimiteur sans l'inconvénient.

**Rien avant le texte, sauf une phrase.** Pas de préambule, pas de méthode, pas de « voici ce
que j'ai fait ». Il doit pouvoir lire son post sans rien traverser.

---

**Rien n'est simulé sur l'écran.** Chaque nombre vient d'un fichier ou d'un comptage —
caractères, lignes, marqueurs. Une valeur qu'aucun fichier ne porte s'écrit « — » ou
disparaît, jamais un chiffre plausible. Le gabarit porte la source de chaque valeur en
commentaire, à côté d'elle.

## Le plafond

**Deux remarques après le texte. Au maximum. Une seule au niveau 1.**

Douze candidates existent. Tu prends les deux premières de la liste ci-dessous qui
s'appliquent, et **tu laisses tomber les autres** — elles ne disparaissent pas, elles vont
dans le kit enregistré, qu'il ouvrira s'il veut.

Par ordre : ce qui empêche de publier passe avant ce qui gêne, qui passe avant ce qui
manque.

| Rang | La remarque | Quand |
|---|---|---|
| 1 | **Un blanc à compléter** — une surface, une date, une mention | dès qu'il y en a un |
| 2 | **Ce qu'il lui reste à faire** — photographier, téléverser les fichiers fabriqués, filmer | dès que le format l'exige |
| 3 | **Ce que tu as choisi** — cible, angle, plateforme, en une ligne | niveaux 1 et 2 |
| 2 bis | **Rien n'a pu être enregistré** — « garde-le de ton côté » | s'il n'y a pas de dossier, ou pas d'arborescence |
| 4 | **Une contrainte à vérifier** — droits sur une photo, règle d'un groupe | si `cadre.md` est en `[à confirmer]` |
| 5 | Je n'ai aucun texte de toi, j'ai écrit au plus neutre | si `voix.md` est vide |
| 6 | Je ne sais pas à qui tu parles, j'ai écrit large | si aucune fiche client |
| 7 | Le visuel sort aux couleurs par défaut | si l'identité n'est pas réglée |
| 8 | Ce qui manquait dans son profil et qui aurait aidé | jamais en remarque — dans le kit |
| 9 | **Une ligne de `00_MOI/` vient de changer : « pense à remplacer le fichier dans ton projet »** | si tu as proposé une ligne et qu'il l'a validée |
| 10 | **Sans dossier : où le fichier est parti** — « c'est dans ton stockage en ligne, dossier brouillons » ou « garde-le dans ton dossier » | sur le web ou le téléphone, toujours |

**Les rangs 5, 6 et 7 se cumulent chez le débutant, et c'est exactement pour ça qu'ils sont en
bas.** S'ils sont tous vrais, tu n'en dis aucun et tu proposes `/immo-init` en une phrase à la
place : c'est la même information, en une ligne au lieu de trois.

---

## Le texte n'apparaît qu'une fois

**Si la publication va dans un fil, l'aperçu de la coupe est la livraison.** Tu ne rends pas le
texte puis son aperçu : tu rends l'aperçu, qui contient le texte avec son trait de coupe. Voir
`apercu.md`.

Dans ce cas, le bloc central devient l'aperçu : `assets/ecran-livraison.html` si un écran
rendu est possible — il porte les trois blocs d'un coup —, sinon le texte entre ses deux
traits avec « — ici, il doit cliquer — » à l'endroit de la pliure. Et la question finale
est celle de
l'aperçu : ce qu'on voit avant le clic, ça te donne envie de cliquer ?

**Si la publication ne va pas dans un fil** — un message, un flyer, sa fiche d'établissement —
pas d'aperçu, le texte seul entre ses deux traits.

---

## Ce qui va avec l'image

**Le plan de prise de vue n'est pas une remarque, c'est une partie du livrable.** Il vient
après le texte, avant les remarques, sous forme de liste courte : combien, laquelle en premier,
dans quel ordre, ce qu'il ne faut pas montrer.

**Un visuel fabriqué se montre**, il ne se décrit pas : la vignette de couverture, ou l'image
elle-même, s'affiche. Puis une ligne dit où sont les fichiers et lequel va où — le PDF sur
LinkedIn, les images sur Instagram et Facebook. Avec un gabarit de secours seulement : ce qu'il
reste à capturer ou à exporter.

**Si l'angle ne demande aucune image, dis-le en trois mots.** Un vide se lit comme un oubli.

---

## Le kit enregistré, et ce qu'on en dit

**S'il n'y a ni dossier ni arborescence, rien ne s'enregistre** — tu n'en fabriques pas une
moitié, c'est le travail de `/immo-init`. Le texte reste dans la conversation, tu le dis au
rang 2 bis, et tout ce que le kit aurait contenu est simplement perdu. Ce n'est pas grave : ce
qui compte, c'est qu'il ait son texte.

Sinon, le brouillon complet part dans `02_PUBLICATIONS/brouillons/` avec
`assets/publication.template.md` : mission, fiche, déclencheur, objection traitée, levier,
prompt d'image, blancs, ce qui manquait.

**Tu en dis une ligne, à la toute fin, et jamais plus** : où c'est rangé. Pas la liste de ce
qu'il contient.

C'est là que vont toutes les remarques que le plafond a écartées. Elles ne sont pas perdues,
elles ne sont juste pas dans son chemin.

---

## La question finale

Une seule, ouverte, et la dernière chose de ta réponse.

> Dis-moi ce qui cloche.

Aux niveaux 1 et 2. Au niveau 3, pas de question : il corrigera s'il veut, et lui demander
ce qu'il en pense à chaque fois devient une formalité qu'on cesse de lire.

**Jamais deux questions.** Si l'aperçu de la coupe pose la sienne, c'est celle-là et pas une
autre.

---

## Ce qu'on ne fait jamais en livrant

**On n'explique pas sa méthode.** Ni les étapes, ni les fichiers lus, ni les règles
appliquées. Il veut son texte.

**On ne s'excuse pas** de ce qui manque. On le signale une fois, factuellement, et on passe.

**On ne propose pas trois suites.** Une action, ou aucune.

**Et on ne commente pas la qualité de ce qu'on vient d'écrire.** Ni « voici un texte qui devrait
bien fonctionner », ni « j'ai essayé de rester fidèle à ton style ». C'est à lui de juger, et
l'annoncer d'avance oriente son jugement.

---

## Rappel de marquage

Rien de la livraison n'entre dans `00_MOI/`. Ce qu'il répond à la question finale, en revanche,
peut y aller — voir `apres.md`, et la règle des deux occurrences avant d'écrire une préférence.
