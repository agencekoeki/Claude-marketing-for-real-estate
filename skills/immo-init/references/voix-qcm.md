# Calibrer la voix : mesurer d'abord, choisir ensuite

## Ce qui se mesure ne se demande pas

La stylométrie tient pour discriminants — et indépendants de la volonté de l'auteur — les
**mots-outils**, la longueur des phrases et **sa variance**, les taux de ponctuation, les
ouvertures et clôtures. C'est la couche qu'il ne contrôle pas, donc celle qu'un texte écrit à
sa place doit reproduire pour lui ressembler. Et **elle se mesure, elle ne s'estime pas** : un
modèle qui lit trente mails et « sent » qu'il écrit court dérive ; un script qui compte ne
dérive pas.

**Si un corpus existe** — ses mails envoyés exportés en texte, ses publications, ses annonces
passées, ses propres messages à Claude —, lance `scripts/stylo.py profil <corpus> --registre
<nom>` **un registre à la fois**, et colle chaque carte rendue dans `voix.md`, section « Ma
signature mesurée », dans le bloc de son registre. La méthode entière — niveaux, registres,
sources, qui s'en sert — est dans `stylometrie.md`. Chaque ligne est `[vu]` avec son
compte : c'est le `[vu]`
le plus solide de toute la mallette.

**En dessous de 1 500 mots, le script le dit et la carte est du bruit.** On la colle quand
même, avec l'avertissement. En mode salle, si le corpus n'est pas déjà sous la main, on
passe : le choix forcé suffit pour une première voix.

**Ce que la mesure ne remplace pas :** les échantillons. Trois à cinq textes réels portent sa
voix mieux qu'une carte de chiffres. La carte sert à **contrôler** ce qu'un outil produit —
`stylo.py compare` — pas à l'écrire.

---

## Le choix forcé

Une passe courte, trois minutes, avant l'échantillon long de l'étape 6.

Elle sert dans les deux cas. Quand l'enquête a trouvé quelque chose, elle **vérifie une
hypothèse** et fait passer une ligne de `[vu]` à `[dit]`. Quand elle n'a rien trouvé, elle
**amorce**. Même outil, deux fonctions.

---

## Ce qu'on ne fait pas

**On ne propose pas de styles nommés.** « L'expert factuel », « le voisin sympa », « le
conteur » : un archétype fait choisir une identité, pas une préférence. Les gens désignent
celui qu'ils aimeraient être, pas celui qu'ils sont. Tu obtiens un profil flatteur et faux.

**On ne demande pas de décrire.** Personne ne sait décrire son propre style.

---

## Ce qu'on fait

Des **paires**. Deux versions du même texte court, qui ne diffèrent que sur **une seule
variable**, et il désigne. Il ne décrit rien, il pointe. Et parce qu'il a pointé, c'est du
`[dit]`.

Cinq à six paires maximum, une variable par paire :

1. **Longueur** — deux lignes contre huit
2. **Adresse** — tutoiement contre vouvoiement
3. **Ouverture** — droit au fait contre mise en situation
4. **Ponctuation** — sobre contre exclamative
5. **Emoji** — aucun contre quelques-uns
6. **Clôture** — appel à l'action explicite contre fin sèche

---

## Les deux règles qui font la différence

**Les paires se génèrent à partir de l'enquête, sur un sujet de son métier à lui.** Jamais un
texte générique. Si l'enquête a trouvé qu'il écrit court et sans emoji, formule-le comme une
vérification :

> J'ai cru voir que tu écris plutôt court et sans emoji. Voilà deux versions de la même
> annonce. Laquelle est la tienne ?

Si l'enquête n'a rien donné, prends un sujet qu'il vient de citer et présente les deux
versions sans hypothèse.

**Chaque paire offre une troisième sortie : « ni l'un ni l'autre ».** C'est la réponse la
plus informative des trois, parce qu'elle révèle un axe que tu n'avais pas vu. Sans elle, tu
forces une préférence qui n'existe pas et tu l'écris comme un fait. Quand elle sort, demande
en une question ce qui cloche, et note l'axe découvert.

---

## Ce que tu écris

Dans `voix.md`, section « Arbitrages ». Une ligne par paire :

```
| Axe | Retenu | Écarté | Marqueur |
|---|---|---|---|
| Longueur | court, 3 lignes | version longue | [dit] |
| Emoji | aucun | 2 emoji | [dit] |
| Ouverture | ni l'un ni l'autre → préfère ouvrir par le quartier | — | [dit] |
```

Garder l'option écartée a une valeur : ça permet de rejouer le test dans six mois et de voir
si ça a bougé.

---

## Nommer, mais après

Une fois les six paires faites, tu peux résumer :

> Ce que tu as choisi, ça donne un ton direct, phrases courtes, sans emoji, qui ouvre sur le
> quartier plutôt que sur le bien.

Nommer après, c'est une synthèse tirée de ses choix. Nommer avant, c'est une suggestion qui
oriente la réponse. L'ordre n'est pas cosmétique.

---

## Ce que le choix forcé ne fait pas

Il produit des **arbitrages**, c'est-à-dire une description. Et une description de style est un
mauvais guide pour écrire à la place de quelqu'un : ce sont des textes réels qui portent une
voix, pas des règles.

Les six paires servent donc à trancher ce que les échantillons laissent ambigu, et à lui faire
comprendre qu'il a des préférences. **Elles ne dispensent jamais de collecter trois à cinq
textes qu'il a écrits lui-même** — c'est l'objet de la section « échantillons de référence » de
`voix.md`, et c'est elle qui compte le plus.

Si l'enquête n'a produit aucun échantillon, dis-le franchement en clôturant : les outils de la
mallette écriront au plus neutre tant qu'il n'aura pas déposé trois textes à lui.

## L'enchaînement

Le QCM calibre, l'échantillon de l'étape 6 valide. Ne saute jamais l'ordre : produire un
texte long avant d'avoir calibré, c'est brûler le meilleur moment de la séance sur un essai
au hasard.
