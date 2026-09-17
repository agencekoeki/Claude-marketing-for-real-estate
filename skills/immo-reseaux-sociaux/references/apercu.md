# Montrer où le texte sera coupé

## Pourquoi ça change tout

Un agent écrit son post dans une zone de saisie qui affiche tout. Puis il publie, et le feed
n'en montre que les premières lignes derrière un « voir plus ». Il ne le découvre jamais,
parce qu'en relisant sa propre publication il voit le texte entier — il l'a écrit.

**Résultat : l'essentiel est presque toujours sous la pliure.** C'est l'erreur la plus
fréquente et la plus coûteuse, et elle ne se corrige pas par un conseil. Elle se corrige en
la montrant.

D'où l'aperçu : la même publication, avec un trait à l'endroit où le lecteur devra décider de
cliquer.

## Les repères de coupe

| Plateforme | Limite dure | Visible avant « voir plus » |
|---|---|---|
| LinkedIn | 3 000 | ~210 sur ordinateur, ~140 sur mobile |
| Instagram | 2 200 | ~125 |
| Facebook | très haute | variable, compte sur ~125 |
| X | 280 en compte gratuit | tout |

**Ces nombres sont des ordres de grandeur, pas des constantes.** Ils dépendent de l'appareil,
de la largeur de l'écran et de la version de l'application, et ils bougent à chaque
redessin d'interface. Dis-le au stagiaire au lieu de lui vendre une précision qui n'existe
pas.

**Règle qui en découle : on calibre toujours sur la valeur la plus serrée.** Cent quarante
caractères pour LinkedIn, pas deux cent dix. Un texte qui tient sur mobile tient partout ;
l'inverse est faux, et la majorité de son audience locale lit sur téléphone.

Deux choses déplacent la coupe et personne n'y pense : **un saut de ligne compte**, et il peut
avancer la pliure de plusieurs lignes ; et **les emoji comptent souvent double**.

## Ce qu'on en fait

Trois vérifications, dans cet ordre.

**L'accroche tient-elle entièrement avant la coupe ?** Si la phrase se casse au milieu, le
lecteur voit une demi-idée et ne clique pas. Une accroche coupée est pire qu'une accroche
courte.

**Y a-t-il une raison de cliquer ?** Ce qui est visible doit ouvrir quelque chose : une
tension, une question, un début d'histoire. Une première ligne qui se suffit à elle-même
n'appelle aucun clic.

**L'appel à l'action est-il sous la pliure ?** C'est normal et ce n'est pas un problème : il
s'adresse à ceux qui ont déjà décidé de lire. En revanche, **rien d'essentiel ne doit être
au-dessous** — ni une information pratique, ni une date, ni une mention obligatoire.

## C'est la livraison, pas un supplément

**Quand la publication va dans un fil, cet aperçu remplace la remise du texte.** Tu ne rends
pas le texte puis son aperçu : le texte n'apparaît qu'une fois, ici, avec son trait de coupe.

Et la question finale de la séance est celle de ce fichier, pas une autre — voir `livrer.md`,
qui interdit d'en poser deux.

## Comment tu le montres

Remplis `assets/ecran-livraison.html` : le texte tel qu'il sera publié, le trait de coupe à
l'endroit calculé pour la plateforme visée, le décompte, et le plan de prise de vue à côté.
C'est la même page que la livraison — le texte n'apparaît qu'une fois.

**Si l'écran rendu n'est pas disponible**, ne renonce pas à la démonstration : recopie dans le
fil la partie visible seule, puis écris « — ici, il doit cliquer — », puis le reste. Le trait
compte plus que la mise en forme.

Et une fois la coupe montrée, **ne reformule pas tout seul.** Demande :

> Ce qu'on voit avant le clic, ça te donne envie de cliquer ?

C'est sa réponse qui décide, et c'est le moment où il comprend la contrainte pour toutes ses
publications futures, pas seulement pour celle-là.

---

## Rappel de marquage

Rien de ce qui est mesuré ici n'entre dans `00_MOI/`. Les seuils de coupe sont des faits de
plateforme, pas des faits sur lui, et ils périment.
