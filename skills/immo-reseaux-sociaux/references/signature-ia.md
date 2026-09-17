# La signature de l'outil

## De quoi on parle

Deux choses différentes, et on les traite séparément.

**Le texte porte un accent.** Pas « un style IA » en général : chaque famille de modèles a des
traits stylistiques reconnaissables — principe de la mallette, sans chiffre faute de source
référencée ici. Les tics ne sont donc pas ceux de
« l'IA », ce sont ceux **du modèle qui écrit** — c'est-à-dire toi.

**L'image porte un filigrane.** Depuis mai 2026, les images des deux familles d'outils
majeures embarquent une marque invisible, lisible dans plusieurs applications grand public. Ce
n'est plus une question de style, c'est une question de traçabilité. Source : annonce d'OpenAI
du 19 mai 2026 — SynthID et C2PA sur les images de ChatGPT, comme chez Google ; la détection est
proposée au grand public dans l'application Gemini et dans Chrome.

---

## Les tics qui sont les tiens

À traquer en priorité, parce qu'ils sortent tout seuls.

**Le tiret cadratin.** C'est le marqueur le plus discriminant, et il te désigne toi plutôt
que l'IA en général. La nuance qui compte : ce n'est pas sa présence, c'est **son usage**. Un
humain s'en sert pour une rupture sèche ; un modèle s'en sert pour accrocher une proposition
explicative de plus. Dans une publication, remplace-le par un point.

**La parallélisme négative.** « Ce n'est pas X, c'est Y. » « Pas seulement A, mais B. » Elle
revient dans presque toutes les productions, elle sonne bien, et elle est le deuxième
signal le plus reconnaissable.

**Les triplets.** Trois éléments parallèles, de longueur presque égale, ponctués pareil. Le
rythme est agréable et complètement mécanique. Deux éléments, ou quatre : jamais trois par
réflexe.

**Les phrases miroir.** « L'outil est un moyen. L'assistant est un partenaire. » Deux phrases
de même forme qui se répondent.

**Les fragments d'emphase.** Une phrase sans verbe, seule, pour appuyer. Une fois, à la
rigueur. Deux, c'est un tic.

**L'ouverture d'ambiance.** « Dans un monde où… », « Il y a quelque chose de… ». On entre par
un fait, jamais par une atmosphère.

**Le rythme question-réponse.** « Qu'est-ce que ça change ? Ça change que… »

**La coda de fin.** Le paragraphe qui résume et ouvre sur l'avenir. Un post s'arrête sur son
appel à l'action.

**Les empilements de prudence.** « Pourrait potentiellement peut-être. »

---

## Ce qui les rend détectables, indépendamment des mots

**La régularité.** Les phrases d'un modèle tournent autour d'une longueur médiane étroite,
avec peu d'écart ; un humain alterne brutalement. C'est la mesure sur laquelle les premiers
détecteurs ont été bâtis.

**L'uniformité d'un segment à l'autre.** Un humain change de registre en cours de texte, pas
un modèle.

**La propreté.** Aucune faute, une ponctuation parfaite, des espaces insécables. Voir les
marqueurs propres au français dans `ecriture.md`.

---

## Ce qu'on en fait, et ce qu'on ne fait pas

**On ne cherche pas à tromper un détecteur.** Ce n'est ni l'objectif ni honnête, et ça ne
marche pas : les outils qui promettent de « déjouer » la détection dégradent le texte.

**On cherche à ce que le texte lui ressemble.** C'est la même chose vue autrement, et c'est le
seul objectif défendable. Un texte qui porte ses mots, ses aspérités et ses trois échantillons
ne déclenche pas les signaux parce qu'il n'a pas été écrit au centre statistique.

**Donc l'ordre de priorité est celui-ci :** ses échantillons d'abord — c'est ce qui porte
réellement la voix —, la suppression de mes tics ensuite, la typographie en dernier.

**Et s'il n'a aucun échantillon**, dis-le et écris au plus neutre. Un texte sobre qu'on ne
reconnaît pas vaut mieux qu'un texte « humanisé » artificiellement.

---

## Côté image : le filigrane

**Ce qu'il faut savoir, et lui dire.**

Les images produites par les générateurs des deux grandes familles portent une marque
invisible, et des applications grand public savent la lire — il suffit de téléverser l'image
et de poser la question. Certaines indiquent même **quelle portion de l'image est marquée**,
ce qui permet de repérer une retouche partielle.

**Conséquence directe pour ce métier :** effacer une fissure sur une photo de bien laisse une
trace détectable sur la zone effacée. Ce n'est plus seulement une faute professionnelle, c'est
une faute repérable par n'importe quel acquéreur curieux.

C'est l'argument à donner quand il insiste pour retirer quelque chose qui le gêne. Il porte
mieux qu'un rappel à la déontologie.

**Deux limites à ne pas oublier.** Les plateformes sociales suppriment souvent les données
accompagnant un fichier au téléversement, donc l'absence de marque ne prouve rien. Et le
filigrane survit mieux qu'elles à un recadrage ou à une compression.

---

## Côté image : ce qui se voit encore

Les défauts d'il y a deux ans — six doigts, texte illisible, peau cireuse — sont largement
corrigés. Ce qui accroche encore, et qu'il faut vérifier sur toute image générée :

- le **texte en arrière-plan** et les motifs qui se répètent
- les **reflets** et la **direction des ombres**, incohérents entre deux objets
- les **mains et les oreilles** dès qu'il y a une pose contrainte
- les **yeux** : texture de l'iris, reflets qui ne correspondent pas
- les **bords d'objets** qui fusionnent, les figurants dupliqués en arrière-plan

C'est déjà la vérification de `outils-image.md`, et elle sert autant à la qualité qu'à
l'honnêteté.

---

## Qui appelle ce fichier

**Au contrôle, avant de livrer** : les tics de rédaction, puis l'image si elle a été générée.

**Et en formation, c'est une démonstration**, pas une théorie. Fais-lui téléverser une image
générée dans l'application qui sait lire la marque, et regarde la réponse avec lui. Trente
secondes, et il comprendra la règle mieux qu'avec dix phrases.

---

## Rappel de marquage

Rien de ce fichier n'entre dans `00_MOI/`. Les tics et les filigranes sont des faits d'outil,
pas des faits sur lui, et ils bougent vite.
