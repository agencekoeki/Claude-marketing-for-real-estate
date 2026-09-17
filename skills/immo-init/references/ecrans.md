# Les écrans

Un cadre fixe, répété, qui dit où on en est et ce que le stagiaire peut faire. Il n'est pas
décoratif : sans repère, une heure de questions ressemble à un interrogatoire sans fin, et toi
tu dérives — la conformité à un protocole long se dégrade à mesure qu'on produit.

---

## Le panneau de progression porte la position

**C'est l'indicateur principal, et il est natif.** Le panneau de droite affiche la liste des
tâches déclarées pendant l'échange. Déclare les onze étapes en tâches dès ta première réponse,
coche-les au fur et à mesure, et il porte la position sans qu'on dessine quoi que ce soit.

Trois contraintes, qui viennent de sa façon de fonctionner :

- **Seul le titre s'affiche.** Le champ description n'est jamais montré : tout ce qui doit se
  lire tient dans le titre, court.
- **Il ne rend que les tâches touchées dans l'échange en cours.** À la réouverture d'une
  conversation il peut être vide — c'est normal, ne t'en étonne pas devant lui.
- **C'est une vue, pas un formulaire.** On l'alimente en déclarant des tâches, on ne l'édite
  pas à la main.

---

## La forme d'un écran, dans le fil

**Deux lignes de markdown, et rien d'autre.** Pas de caractères de cadre, pas de bloc de code,
pas de chasse fixe : l'application a sa propre typographie, elle est plus lisible que tout ce
qu'on pourrait dessiner, et elle s'adapte à la largeur de l'écran.

```
### 3 · L'enquête
> Je regarde ce qui existe déjà sur toi.
```

Le titre de niveau trois porte le numéro et le nom. La citation porte la ligne d'intention, et
la barre verticale que l'application dessine à sa gauche fait le travail du cadre, en mieux.

**Le compteur ne va pas dans le titre.** La position est dans le panneau de progression. L'y
écrire deux fois est du bruit.

## Les onze écrans

| # | Titre | Ligne d'intention |
|---|---|---|
| 0 | Avant de commencer | On vérifie, puis on choisit la durée. |
| 1 | Les règles du jeu | Comment je note, et ce que je tais. |
| 2 | Ton espace | Je crée ton dossier et tes fichiers. |
| 3 | L'enquête | Je regarde ce qui existe déjà sur toi. |
| 4 | Ce que j'ai trouvé | Je te montre, tu corriges. |
| 5 | Ce que je ne devine pas | Les quelques questions qui restent. |
| 6 | Ta façon d'écrire | Tu choisis, puis tu corriges un texte. |
| 7 | À qui tu parles | Tes trois derniers dossiers, et un raté. |
| 8 | Ce qui tournerait seul | On en installe un, pas trois. |
| 9 | T'y retrouver partout | Ton projet, tes fichiers, ta mémoire. |
| 10 | Ce que tu emportes | Le contrôle, puis ton relevé. |

Titres et lignes d'intention sont fixes. **Ce sont aussi les titres des onze tâches déclarées
au panneau** : mêmes mots, un seul vocabulaire.

**L'écran 0 compte double.** Il porte le contrôle de surface, le choix du mode et la création
du dossier — la partie la plus technique de la séance, et celle où il décroche le plus vite.
Trois choses le sauvent : annoncer d'emblée qu'il y aura dix étapes et combien de temps ça
prend, ne jamais expliquer pourquoi tu vérifies quelque chose, et poser une seule question à
la fin. Et une quatrième avant le temps 2 de l'enquête : le prévenir qu'il va cliquer
« autoriser » plusieurs fois, et que c'est normal — voir `connecteurs.md`. Tout le reste
se fait en silence.

**Les écrans 4 et 6 sont les deux moments où il se reconnaît.** S'il faut raccourcir,
raccourcis ailleurs.

## Ce qui va dans le corps

Le titre et sa citation, puis le corps en texte normal.

**Rien de ce qu'il doit lire attentivement, copier ou corriger ne va dans un bloc de code.**
Un bloc de code donne un bouton « copier », se lit comme du technique, et c'est exactement
l'impression qu'on cherche à éviter.

En revanche, dès que le contenu est comparatif — des axes à choisir, des candidats à classer,
des fiches à survoler — **un tableau markdown** rend mieux qu'un paragraphe, et il est stylé
par l'application.

---

## Trois registres, du plus riche au plus sûr

**1. L'écran rendu.** Une vraie page mise en forme, dans un panneau à côté de la conversation.

**Mais le panneau est une ressource unique.** Un écran rendu remplace l'affichage de la
progression et rétrécit la conversation. C'est un échange, pas un gain gratuit : il ne se
justifie que là où il y a quelque chose à **regarder**, pas là où il y a une position à
connaître.

**Il affiche, il ne demande rien.** La question reste dans le fil : un panneau ne te renvoie
pas ce qu'on y fait, et tu n'as pas besoin qu'il le fasse.

**2. Le panneau de progression**, qui porte la position sans rien fabriquer.

**3. Les deux lignes de markdown** ci-dessus. Aucune dépendance, ça rend partout.

Tu prends la plus riche disponible et tu redescends **sans commentaire**. Ne demande jamais au
stagiaire quel registre utiliser : il n'en sait rien et la question casse le rythme.

## Quand un écran rendu se justifie

**Deux fois, pas dix.**

**Pas l'écran 0.** Les dix étapes sont exactement ce que le panneau de progression affiche
nativement : ouvrir un artefact pour les redessiner coûte le panneau et n'apporte rien.

**L'écran 4**, parce que c'est là qu'il se reconnaît. Le constat en grand, les taux de
remplissage, les sources ouvertes et celles qui manquent. Si tu ne dois en faire qu'un, fais
celui-là.

**L'écran 10**, qui est déjà une page : le relevé d'installation, voir `rapport.md`.

## Comment on affiche un écran rendu

**C'est la consigne qui manquait**, et sans elle tu retombes toujours sur le texte.

Les pages de `assets/` ne s'affichent pas toutes seules. Le geste est : **tu lis le fichier,
tu remplaces les crochets, et tu crées un artefact avec le résultat.**

- **Un artefact par écran rendu, jamais deux dans la même réponse.**
- **La conversation continue en dessous** : la question, les remarques et ce qu'il doit faire
  restent dans le fil.
- **Si l'artefact échoue ou n'est pas disponible, tu passes au texte sans commenter.** On ne
  décrit jamais un écran qu'on n'a pas réussi à montrer.

## Ce qu'on met dans un écran rendu

Les mêmes informations que le titre, plus ce qui **se regarde mieux qu'il ne se lit** : des
taux, un état, une comparaison, un avant-après.

Jamais de prose. Jamais la question. Jamais quelque chose qu'il doit copier ou corriger.

Et **rien qui ne soit vrai** : un taux de remplissage est une donnée, une barre qui avance est
une donnée. Un panneau qui décore est un panneau qui ment sur le sérieux de ce qu'on installe.

Les deux pages partagent les couleurs du relevé, et c'est délibéré : **les écrans du parcours
et la page de fin appartiennent au même monde.** Chacune est autonome — aucune ressource
externe, aucune police à charger, mode sombre géré.

- **Écran 4** → `assets/ecran-4.html`. Les barres se règlent sur `width:[N]%`.
- **Écran 10** → `assets/rapport.template.html`, voir `rapport.md`.

Les deux suivent la coque commune de `coque.md` : bandeau d'état, à faire, le principal,
rangé. **Ce qu'il doit faire se lit sans défiler**, sur tous les écrans de la mallette.

---

## Les quatre réponses

C'est le cœur du dispositif, et son effet est contre-intuitif.

Un stagiaire qui veut faire échouer la séance — ça existe, et ça se manifeste par des réponses
absurdes, du hors-sujet volontaire, ou un « je comprends rien, c'est nul » — tire son pouvoir
d'une seule chose : **faire quelque chose qui n'était pas prévu.**

Alors on prévoit tout. Les quatre réponses sont affichées sous chaque écran qui attend quelque
chose, et les quatre sont légitimes :

> répondre · « je ne sais pas » · « on passe » · « où on en est ? »

**Répondre.** Le cas normal.

**« Je ne sais pas ».** La case reste vide, marquée `[à confirmer]`, et on avance. Ne relance
pas, ne reformule pas, ne culpabilise pas : « d'accord, je laisse vide, tu compléteras si tu
veux ».

**« On passe ».** L'étape entière est sautée et consignée comme sautée. Tu ne négocies pas et
tu ne demandes pas pourquoi.

**« Où on en est ? ».** Tu redis l'étape courante, ce qui est fait, ce qui reste, ce qui a été
sauté. Rien d'autre.

Face à une réponse absurde ou agressive, tu ne relèves pas et tu ne te justifies pas. Tu
traites comme un « je ne sais pas » et tu passes :

> D'accord, je note ça comme non renseigné. On continue.

Il n'y a rien à casser. Au pire le profil finit à 20 %, et le relevé final le dira honnêtement
avec la liste de ce qui manque. C'est un résultat, pas un échec.

## Le niveau change ce qu'on affiche

**Au niveau 1, on n'affiche pas les réponses possibles.** Un menu de quatre options à quelqu'un
qui ne sait pas quoi répondre est une question de plus, pas une aide. Tu décides, tu livres, tu
poses une seule question ouverte à la fin.

Aux niveaux 2 et 3, elles s'affichent normalement.

## L'écran 0 suit une séquence fixe

Donnée en tête du SKILL.md : vérifier la surface en silence, vérifier le dossier, lire
l'en-tête d'état s'il existe, demander le mode. **La question du mode est la dernière et la
seule visible des quatre** — les trois autres ne s'affichent que si elles échouent.

## Reprendre après une coupure

Quota atteint, application fermée, stagiaire parti déjeuner : un tunnel qui ne survit pas à
une interruption n'est pas un tunnel.

**Il n'y a rien de nouveau à construire : l'en-tête d'état de `profil.md` est la sauvegarde.**

Quand `/immo-init` est relancé sur un dossier qui contient déjà `00_MOI/profil.md`, tu ne
repars pas de zéro et tu ne redemandes pas le mode. Tu lis l'en-tête, tu redéclares les tâches
restantes au panneau, et tu affiches :

```
### On reprend · étape 6
> Ton profil et tes clients types sont déjà là.
```

Puis, en texte : ce qui reste, combien de sections sont encore vides, et une question — on
reprend là, ou tu veux revoir quelque chose d'abord ?

Pour que la reprise fonctionne, **l'en-tête d'état se met à jour au fil des étapes**, pas
seulement à la fin. Une étape terminée est une étape écrite.

## Ce qui rend le tunnel solide

Trois choses, et aucune n'est graphique.

**On sait toujours où on est.** Le panneau le dit.

**Tout ce qu'on peut faire est écrit.** Un processus dont les sorties sont prévues ne se casse
pas : il n'y a plus de coup à jouer en dehors.

**Une interruption ne détruit rien.** Ce qui est écrit est écrit, et la reprise le lit.
