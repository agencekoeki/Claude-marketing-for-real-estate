# La coque des écrans, et le tableau de bord

## Pourquoi une coque

Cinq écrans de livraison sur trois outils, plus un relevé. S'ils n'ont en commun que les
couleurs, l'agent réapprend à lire à chaque outil. **Une coque commune, quatre zones, toujours
dans le même ordre** — et il sait où regarder avant même de lire.

Chaque page reste autonome : aucune ressource externe, aucune police à charger, mode sombre
géré. La coque est recopiée dans chaque fichier, pas partagée.

---

## Les quatre zones, dans cet ordre

**1. Le bandeau d'état.** Le titre de l'écran, une ligne de contexte, et des puces à droite —
quel outil, quel écran, et **combien de choses l'attendent**. La puce d'alerte est en couleur
d'alerte ; s'il n'y a rien, elle n'existe pas.

**2. À faire, dans l'ordre.** Avant tout le reste, en haut, dans un encadré à liseré d'alerte.
Deux lignes au plus, classées par ce qui bloque avant ce qui gêne. C'est le seul endroit de
l'écran qui lui demande quelque chose. **S'il n'y a rien, l'encadré dit « Rien. C'est
prêt. »** en vert — on ne le retire pas, parce que l'absence de tâche est une information.

**3. Le principal.** Ce pour quoi l'écran existe : le texte, le constat, le carnet, l'annonce.
C'est la zone qui peut être longue, et c'est pour ça qu'elle vient après « à faire » : ce qu'il
doit faire se lit sans défiler.

**4. Rangé.** Une ligne en pied : où c'est enregistré à gauche, une information de contexte à
droite — comment recommencer, ce que le texte a de particulier, quand la prochaine récolte.

## La règle de priorité, et elle ne se négocie pas

**Ce qu'il doit faire se lit sans défiler.** Un écran où « à compléter avant de publier » est
tout en bas produit une annonce publiée avec un trou. La zone « à faire » est au-dessus du
principal sur tous les écrans, sans exception, même quand le principal est ce qu'il attend.

**Une seule couleur d'alerte, une seule de validation.** L'alerte pour ce qui bloque, le vert
pour ce qui est en place. Le bordeaux reste réservé au constat et à ce qui distingue. Rien
d'autre n'est coloré : une page à quatre couleurs se lit comme une publicité.

---

## Le tableau de bord

**Un seul fichier à ouvrir pour tout voir** : `tableau-de-bord.html`, à la racine du dossier de
travail.

L'init le crée à l'étape 2 depuis `assets/tableau-de-bord.template.html`, et le remplit à
l'étape 10. **Puis chaque outil de la mallette le réécrit en fin de course**, à partir de ce
qui est sur le disque — jamais de mémoire, jamais d'estimation :

| Zone du tableau | Lue dans |
|---|---|
| À faire | ce que la livraison de l'outil vient de laisser en attente, plus ce qui attendait déjà |
| Annonces | `01_BIENS/*/annonce.md` — le champ `statut` et les dates |
| Publications | `02_PUBLICATIONS/brouillons/`, `publies/`, `carnet.md` |
| Ce qui tourne sans toi | `00_MOI/recurrences.md` |
| Ton profil | l'en-tête d'état de `00_MOI/profil.md` |
| Rangé | le chemin, et le nombre de sous-dossiers de `.claude/skills/` |

## Rien n'est simulé

**Chaque valeur du tableau de bord vient d'une ligne de fichier ou d'un calcul sur une ligne
de fichier.** Si la source est vide, la valeur s'écrit « — » ou la ligne disparaît. Jamais un
chiffre plausible, jamais un chiffre dit en conversation qui n'a pas été écrit dans un fichier
avant. Un tableau de bord qui affiche « 3 visites » sans qu'un champ `visites: 3` existe est
un tableau de bord qui ment — et il ment avec une belle mise en page, ce qui est pire.

La table de dérivation, valeur par valeur :

| Valeur affichée | Source exacte | Si absente |
|---|---|---|
| « [N] choses t'attendent » | le nombre de lignes de la zone À faire | la puce disparaît |
| profil, voix, cadre, clients, récurrences [N] % | **les lignes `MESURE` de `verifier.py`**, recopiées telles quelles — jamais comptées par le modèle | « — » si le script n'a pas tourné |
| [N] outils installés, [N] biens, [N] brouillons | idem, lignes `MESURE` du script | « — » |
| annonces en ligne / à publier | `annonce.md` avec `statut: en ligne` / `statut: brouillon` | « aucune annonce » |
| en ligne depuis [N] j | aujourd'hui − `date_mise_en_ligne` | rien |
| [N] visites | le champ `visites` de `annonce.md` | rien — pas zéro |
| [N] brouillons | fichiers de `02_PUBLICATIONS/brouillons/` | « aucun » |
| attend depuis [N] j | aujourd'hui − `date_ecriture`, sinon date du fichier | rien |
| sujets en réserve, [N] attendent | lignes de la table « À écrire » de `carnet.md` ; celles dont « il te faut » ≠ rien | « pas de carnet » |
| dernière publication il y a [N] j | aujourd'hui − max(`date_publication`) dans `publies/` | « aucune enregistrée » |
| ce qui tourne | table « installées » de `recurrences.md`, colonnes Nom, Cadence, Heure, Depuis, Contrôle | « rien d'installé » |
| mis à jour le, par | écrit par l'outil au moment où il écrit le fichier | jamais absent |
| miroir du projet : [date] | l'en-tête d'état de `profil.md`, ligne « miroir déposé le » | « jamais » |

**Ce qu'on n'affiche pas parce qu'aucun fichier ne le porte :** la prochaine occurrence d'une
tâche, le nombre de vues, le taux de clic, une estimation de quoi que ce soit.

**Le script fait les comptes, le modèle recopie.** `verifier.py` imprime les lignes `MESURE`
— pourcentages par fichier, nombre de biens, de brouillons, d'outils — et le tableau de bord
les recopie telles quelles. Un modèle qui compte des lignes estime ; un script compte.

**Et le gabarit porte cette table en commentaires HTML**, à côté de chaque valeur : c'est là
que le modèle regarde au moment de remplir.

**La zone « à faire » est la seule qui demande un jugement** : classer par ce qui bloque. Une
annonce avec une mention vide passe avant un brouillon qui attend, qui passe avant une tâche à
lire. Trois lignes au plus ; au-delà, on ne lit plus.

**Ce qu'on n'y met pas :** des chiffres de marché, des statistiques de portail, des noms de
tiers. Le tableau de bord est un état de ses fichiers, pas un rapport.

Et **on ne lui montre pas le tableau de bord à chaque fois**. Il est là, à la racine, et le
relevé lui dit où. Il l'ouvrira quand il voudra savoir où il en est — c'est un objet à lui,
pas un écran de séance.
