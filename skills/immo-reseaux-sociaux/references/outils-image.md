# Faire fabriquer l'image par un autre outil

## Ce que tu produis, et ce que tu ne produis pas

Tu ne génères pas d'image. **Mais tu écris le prompt exact, tu dis quel matériau fournir et
dans quel format attendre le résultat.** C'est l'essentiel du travail : un agent sait cliquer,
il ne sait pas quoi demander.

**Ce que tu rends :** le matériau à fournir, le prompt à coller, le rapport d'image attendu,
et ce qu'il faut vérifier sur le résultat.

**Ce qu'il fait :** il colle, il attend, il télécharge, il vérifie.

Ce fichier est daté de septembre 2026. Les noms de modèles et les quotas changent vite : si le
stagiaire décrit autre chose que ce qui est écrit ici, **c'est lui qui a raison**, il a l'outil
sous les yeux.

---

## Choisir la famille d'outil

Deux familles dominent, et elles échouent à des endroits différents. Le choix se fait sur le
besoin, pas sur ce qu'il a déjà installé.

| Le besoin | La famille à viser |
|---|---|
| Du texte lisible sur l'image, un tableau, un schéma, des panneaux ordonnés | celle qui excelle en rendu de texte et en contrôle de mise en page — l'offre OpenAI |
| Une photo réaliste, une lumière, une matière, une retouche de photo existante | celle qui excelle en photoréalisme et en édition — l'offre Google |
| Une retouche locale, en désignant une zone de l'image | l'offre OpenAI, dont la boucle de correction est la plus simple |
| Un clip de quelques secondes à partir d'une photo | l'offre Google, côté vidéo |

**Demande-lui ce dont il dispose avant de recommander.** S'il n'a qu'un des deux, on travaille
avec celui-là : la différence de résultat est bien moindre que la différence entre publier et
ne pas publier.

**Et pour les visuels d'information, le moteur de la mallette reste préférable :** il est
gratuit, immédiat, à ses couleurs, contrôlé, et il ne dépend d'aucun quota. Ne va vers un
générateur que pour ce que le moteur ne sait pas faire — une illustration, une ambiance, une
retouche.

---

## La règle qui prime sur tout, en immobilier

**Une image générée ne représente jamais un bien réel.** Jamais. Ni la façade, ni une pièce,
ni la vue depuis la fenêtre.

**Une photo réelle ne se retouche que sur ce qui ne change pas ce qu'on achète.**

| Autorisé | Interdit |
|---|---|
| Redresser, recadrer, ajuster la luminosité | Supprimer un défaut, une fissure, une humidité |
| Flouter un visage, une plaque, un nom | Changer ce qu'on voit par la fenêtre |
| Retirer un objet personnel — une photo de famille, un courrier | Ajouter ou retirer un élément du bâti |
| Ajouter un meuble dans une pièce vide, **si c'est annoncé** | Remplacer un ciel gris par un ciel bleu |

La ligne est simple : **si la retouche modifie ce que l'acquéreur croit acheter, c'est une
tromperie.** Un agent engage sa responsabilité professionnelle, pas son goût.

L'ameublement virtuel d'une pièce vide est une pratique répandue et acceptable **à condition
d'être annoncé sur l'image elle-même**, pas dans une mention en bas du texte.

Et si le stagiaire insiste pour retirer quelque chose qui le gêne : tu ne le fais pas, tu dis
pourquoi en une phrase, et tu proposes autre chose — un autre cadrage, une autre pièce, un
visuel d'information.

---

## Ce que chaque famille sait fabriquer, type par type — septembre 2026

Les deux familles se sont spécialisées, et la typologie de `visuels.md` en dépend.

**La famille OpenAI est devenue un assistant de mise en page.** Infographies denses, schémas
légendés, étapes numérotées, bandes dessinées en plusieurs cases avec un personnage constant,
placement exact des objets, texte long et multilingue rendu fidèlement sur les
étiquettes. Un mode qui réfléchit avant de dessiner, et **plusieurs images cohérentes en un
seul appel** — une série de visuels qui se ressemblent. Elle sait rendre un vrai plan, un vrai
schéma, pas un à-peu-près qui a l'air vrai. Ce qui est ouvert aux comptes gratuits change : à
vérifier sur le sien. Aucun chiffre ici — nombre d'images par appel, taux de rendu du texte —,
faute de source vérifiée.

**La famille Google est devenue le photographe.** Réalisme, peau, lumière, matières, jusqu'à
la 4K, et plus rapide que la génération précédente. **Jusqu'à quatorze images de référence**
pour tenir une identité — un personnage, un produit, une charte — sur toute une série. Le texte
court passe, le texte long moins. Source : lancement de Nano Banana 2, Gemini 3.1 Flash Image,
par Google le 26 février 2026.

**Une capacité qui est un danger pour ce métier :** la famille Google a la recherche web
activée par défaut, et un lieu réel nommé se rend fidèlement. **Ça ne change rien à la
règle** : une rue réelle générée reste une image fausse, et on n'en publie pas. C'est une
raison de plus de ne jamais nommer un lieu réel dans un prompt.

**Ce qui reste vrai pour les deux :** tout texte se relit lettre par lettre, et dans une
scène on compte les objets — les deux se trompent sur le nombre.

| Type ou format | Famille | Ce qu'on met dans le prompt |
|---|---|---|
| infographie, schéma, chronologie, affiche, liste illustrée | OpenAI | le texte exact entre guillemets, l'ordre des éléments, « fond blanc, pas d'effet » |
| bande dessinée, série de visuels cohérents | OpenAI, huit en un appel | le personnage décrit une fois, le nombre de cases, le texte de chaque case |
| illustration, ambiance, matière, photo retouchée | Google | la neutralisation du rendu maison, jamais un lieu ni un bien réel |
| série aux couleurs de sa charte | Google, avec ses références | son logo et sa photo de `03_RESSOURCES/` en référence, ses deux couleurs |
| son personnage dessiné, constant — procédure dans `prompt-avec-lui.md` | Google, sa photo en référence, une fois | « dessin, style simple, le même personnage à chaque fois » — puis on réutilise l'image obtenue en référence |
| son portrait annoté — pièces détachées | gabarit HTML par-dessus sa photo, ou OpenAI avec sa photo en référence | les légendes exactes entre guillemets, « traits et points depuis le personnage vers les légendes, fond neutre » |

## Le rendu par défaut, et comment s'en débarrasser

Chaque outil a un rendu maison qu'il applique même quand personne ne l'a demandé. Si tu ne le
neutralises pas dans le prompt, toutes ses images se ressembleront — et ressembleront à celles
de tout le monde.

### La dominante jaune

**Le défaut le plus documenté, et il touche les deux familles.** Les images sortent tirées
vers le jaune, le sépia, l'ambre. Un mécanisme plausible : la demande est réécrite en amont et
enrichie de formules du genre « lumière cinématographique chaude » ou « heure dorée », d'où
une dominante que personne n'a réclamée.

**La parade est dans le prompt, pas après.** Trois formulations qui marchent, à cumuler :

- **« balance des blancs neutre, pas de dominante chaude, couleurs fidèles »**
- décrire la lumière en termes factuels — **« lumière de midi »**, « lumière du nord »,
  « ciel couvert » — plutôt qu'en termes d'ambiance, qui déclenchent justement le réchauffement
- si l'outil accepte les températures : **« environ 6 000 à 6 500 kelvins »**

Et un réflexe à lui donner : **ne jamais écrire « cinématographique », « chaleureux »,
« lumière dorée », « ambiance cosy »** dans un prompt immobilier. Ce sont exactement les mots
qui produisent la teinte dont il se plaindra.

### Le rendu « catalogue »

Le second défaut, moins visible et plus grave pour ce métier. Par défaut, une image générée
sort **trop propre** : tout est neuf, rien n'est usé, la composition est centrée et
symétrique, l'arrière-plan est flou, l'éclairage est parfait et il n'y a aucun objet qui
traîne.

Un intérieur réel ne ressemble pas à ça, et un lecteur local le sent immédiatement.

**Les contrepoids à mettre dans le prompt :**

- **« photographié au téléphone »**, pas « photographie professionnelle »
- **« lumière naturelle disponible, pas d'éclairage ajouté »**
- **« cadrage légèrement décentré »**, plutôt que centré et symétrique
- **« profondeur de champ normale »**, sinon tout l'arrière-plan part en flou
- **« aucun étalonnage, aucun filtre »**

### Ce que chaque famille fait mieux

| Besoin | Où l'envoyer |
|---|---|
| Garder un visage identique — sa photo professionnelle retouchée | **Google** : l'identité se conserve mieux |
| Restaurer une photo ancienne ou abîmée | **Google** |
| Du texte lisible sur l'image, une consigne en plusieurs étapes | **OpenAI** |
| Un rendu propre et net sur un fond, un arrière-plan remplacé | **OpenAI** |

**Attention à sa photo de profil** : la famille OpenAI a tendance à restructurer légèrement un
visage. Si le résultat ne lui ressemble plus tout à fait, c'est ça — relance en ajoutant
**« ne modifie aucun trait du visage »**, ou passe à l'autre famille.

### Le cas particulier de l'immobilier

Un intérieur généré sort en grand angle, meublé neuf, désencombré, éclairé de partout. Il
ressemble à un catalogue de cuisiniste, pas à une maison.

Ça n'a aucune importance **tant qu'on ne prétend pas que c'est un bien réel** — et c'est
interdit, voir plus haut. Pour une illustration abstraite, c'est même souvent ce qu'on veut.
Mais si le rendu doit paraître vrai, il faut le dégrader volontairement : lumière d'une seule
fenêtre, ombres marquées, un objet du quotidien dans le cadre.

## Écrire un prompt d'image

Six éléments, dans cet ordre. Un prompt sans le sixième produit une image inutilisable sur
les réseaux.

1. **Le sujet**, en une phrase concrète
2. **Le cadrage** : plan large, moyen, gros plan, et l'angle
3. **La lumière** : heure du jour, direction, ambiance
4. **Le style** : photographie, illustration, schéma — et surtout ce qu'on ne veut pas. Si sa
   direction graphique est réglée, donne ses deux couleurs dans le prompt : c'est ce qui rend
   une image générée cohérente avec ses gabarits
5. **Le texte à afficher**, entre guillemets et mot pour mot s'il y en a
6. **Le rapport d'image** : vertical plein écran, portrait ou carré. Voir `plateformes.md`

Gabarit à lui donner tel quel :

> [Sujet en une phrase]. [Cadrage et angle]. [Lumière]. Style [photographie / illustration],
> pas de [ce qu'on ne veut pas]. Texte affiché exactement : « [le texte] ». Format [rapport],
> sans marge blanche.

Et **commence toujours le prompt par la neutralisation du rendu maison** — balance des blancs
neutre, lumière factuelle, pas d'étalonnage. C'est la ligne qu'on oublie et qui explique la
moitié des déceptions.

**Trois choses qui ratent systématiquement**, à lui annoncer avant qu'il essaie : un texte
long sur l'image, plus de deux ou trois éléments à placer précisément, et la ressemblance
d'une personne réelle.

**Et deux interdits :** aucun visage de personne réelle, aucune marque ou enseigne visible.

---

## Faire une vidéo à partir d'une photo

C'est possible, et c'est très limité. Dis les limites avant qu'il s'enthousiasme.

**Des clips d'environ huit secondes**, et un nombre restreint par jour — quelques-uns sur un
plan payant, les chiffres varient selon le plan et l'outil. Ce n'est pas une visite filmée,
c'est un plan d'ambiance.

**Ce que ça sert vraiment :** animer une photo de quartier pour une story, faire un plan
d'ouverture de trois secondes, donner du mouvement à une image fixe. Rien de plus.

**Ce que ça ne remplace pas :** une visite, une présentation face caméra, un avant-après. Pour
ça, il filme — voir `visuels.md`.

Structure du prompt : la photo de départ, puis un seul mouvement décrit simplement — un
travelling lent vers l'avant, une lumière qui change, une caméra qui monte. **Un seul
mouvement.** Deux instructions de mouvement donnent un résultat instable.

Et la même règle dure s'applique : **on n'anime pas la photo d'un bien réel** si le mouvement
invente ce qu'on ne voyait pas. Un travelling qui révèle une pièce que la photo ne montrait
pas est une image fausse.

---

## Une obligation, pas seulement une règle

Depuis le 2 août 2026, un professionnel de l'immobilier doit signaler un contenu réaliste
créé ou modifié par l'IA quand il peut passer pour authentique. **Le texte exact de la mention
vient de `cadre.md`**, jamais de toi. Ce que ça change ici : un dessin de lui se déclare comme
un dessin, une photo retouchée se signale, et un visuel d'information — un tableau, une
frise — n'est pas concerné parce que personne ne le prend pour une photo. Dans le doute, on
signale.

## Le marquage des images générées

**Les images produites par les générateurs des deux grandes familles portent une marque
invisible**, et des applications grand public savent la lire : il suffit de téléverser l'image
et de poser la question. Certaines indiquent même quelle portion de l'image est marquée.

Trois conséquences.

**Sur un visuel d'information, ce n'est pas un problème.** Personne ne croit qu'un tableau
comparatif a été photographié.

**Sur quoi que ce soit qui ressemble à une photo de bien, c'en est un.** Une raison de plus de
ne jamais en générer.

**Et une retouche partielle se repère sur la zone retouchée.** C'est l'argument à donner
quand il insiste pour effacer quelque chose : ce n'est pas seulement interdit, c'est visible.
Il porte mieux qu'un rappel à la déontologie. Voir `signature-ia.md`.

---

## Ce que tu vérifies sur le résultat

Il revient avec son image. Quatre questions, dans cet ordre :

- le texte affiché est-il **exactement** celui demandé, sans faute ? C'est ce qui rate le plus
- le rapport d'image est-il le bon, ou va-t-il être recadré à la publication ?
- y a-t-il un détail aberrant — une main, une perspective, un mot inventé ?
- est-ce lisible en vignette, sur un téléphone ?

S'il y a un défaut, **ne lui fais pas tout recommencer** : donne la correction à demander en
une phrase. C'est ce que font les boucles d'édition, et c'est plus rapide qu'un nouveau
prompt.

---

## Rappel de marquage

Rien de ce fichier n'entre dans `00_MOI/`. En revanche, **quels outils il possède** est une
information sur lui : elle va en section 13 du profil, marquée `[dit]`.
