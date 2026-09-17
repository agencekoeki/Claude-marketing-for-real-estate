# Contrôler avant de livrer

Une passe, fait par fait, dans cet ordre. Elle est entière à tous les niveaux : le niveau
décide de ce qu'on demande et de ce qu'on prescrit sur la forme, jamais de ce qu'on vérifie.

---

## 0. Retourne tes propres affirmations

Avant tout, reprends chaque phrase qui n'est pas un chiffre et déplie-la avec `eprouver.md` :
sur quoi repose-t-elle, et l'affirmation contraire tient-elle aussi bien ?

« Calme », « lumineux », « proche de », « en bon état », « recherché » : chacun tombe ou se
remplace par le fait qui le fonde. **Une annonce qui passe ce test est une annonce qu'un
assistant reprend** — c'est le même critère.

## 1. Le titre

Quatre places fixes présentes, une cinquième avec un seul fait distinctif, aucun adjectif,
pas de prix, soixante-dix caractères au plus. Le fait distinctif passe les trois filtres de
`titre.md`, et la première ligne tient sa promesse. Si le portail compose le titre lui-même,
le fait distinctif est en première ligne.

## 1 bis. Les versions disent les mêmes faits

Si plusieurs versions sont livrées, une par canal : surface, prix, exposition, état,
distances identiques dans toutes. Ce qui diffère est la longueur, le titre à sa longueur, la
première ligne. Un fait qui diverge entre deux versions est rédhibitoire.

## 2. Chaque fait a sa ligne dans la fiche

Reprends le texte fait par fait : surface, pièces, étage, exposition, année, état, distances,
prix, charges. **Chacun doit correspondre à une ligne de la fiche des faits**, marquée `[dit]`
ou `[vu]` avec sa source. Un fait dans le texte qui n'est pas dans la fiche est une invention,
et il sort.

## 3. Rien de deviné

Et en particulier **aucune distance estimée** : chaque distance de l'annonce est dans la fiche
avec « itinéraire » ou « dit » comme source. Une distance à vol d'oiseau, ou une distance que
personne n'a mesurée ni confirmée, sort.

Une exposition tirée d'une photo, un « calme » tiré d'un jardin, un « refait » tiré d'un
carrelage neuf : non. Voir `faits.md`. Si tu hésites sur l'origine d'un fait, il n'a pas
d'origine.

## 4. Le bloc réglementaire

Chaque mention que `cadre.md` désigne est présente, **avec le texte qu'il fournit, pas le
tien**. Chaque case en `[à confirmer]` est une ligne vide et nommée dans l'annonce, signalée à
la livraison. Aucune mention n'est rédigée de ta propre initiative.

## 5. Les tiers

Aucun nom de propriétaire, aucune adresse au-delà de ce que `cadre.md` autorise, aucun motif de
vente, aucune situation personnelle. Et sur les photos : rien qui identifie les occupants, la
plaque, le voisin.

## 6. Les trois lecteurs

**L'acquéreur** : la première ligne répond-elle à ce que sa fiche met en premier ? Chaque
« ce qui le bloque » de la fiche a-t-il sa réponse dans le texte ?

**Le vendeur** : ce qu'il tient à voir y est-il, au bon endroit, pas ajouté à la fin ? Et
l'annonce incarne-t-elle les trois comportements de l'USP — ou en contredit-elle un ? Une
USP de franchise avec des travaux tus, une USP de sérieux avec la taxe foncière absente :
c'est ce que le vendeur retiendra.

**Le moteur** : tous les champs structurés sont-ils remplis ? Les mots qu'on cherche — le
quartier, « jardin », « garage » — sont-ils dans le texte tels qu'on les tape ?

## 7. Le voisinage

La première ligne dit-elle autre chose que ce que les comparables disent tous en premier ?
Les faits qu'ils omettent tous sont-ils donnés ? La première photo est-elle différente de celle
qu'ils ont tous mise ? Et si le même bien est ailleurs à un autre prix, l'agent le sait-il ?

Rien de ce qui a été vu chez un confrère n'est entré dans la fiche sans confirmation. Aucune
agence n'est nommée. Voir `a-cote.md`.

## 8. L'ordre

Titre, première ligne, la vie dedans, ce qui se filtre mal, l'environnement en distances, ce
qui coûte, le bloc réglementaire. Ce qui fait décider en premier. Et **le titre tient en
soixante-dix caractères, la première ligne en une centaine** — au-delà, le portail coupe.

## 9. Sa voix

Contre ses annonces passées d'abord, contre `voix.md` ensuite. Les interdits — les siens et
les formules saturées de `metier.md`. Et aucune phrase qu'il a écrite ou corrigée n'a été
relissée.

## 10. La signature de l'outil

**Puis la mesure, si `voix.md` porte une signature mesurée :** écris le brouillon dans un
fichier temporaire et lance `.claude/skills/immo-init/scripts/stylo.py compare <brouillon>
00_MOI/voix.md --registre annonces` — sinon `--registre publications`, sinon sans registre.
Ce qu'il rend est un signal externe — la seule chose qui ne dérive pas quand
on juge la voix. Une phrase trop régulière, un tiret cadratin qu'il ne met jamais, un mot
qu'il emploie sans arrêt et que le brouillon n'a pas : tu corriges avant de livrer — sauf
dans le bloc réglementaire, qui n'est pas dans sa voix. Si
`voix.md` n'a pas de signature, le script le dit et tu passes.


Aucun tiret cadratin, aucune parallélisme négative, aucun triplet, aucune espace insécable
ajoutée. Aucune tournure de la liste : « il est important de noter », « n'hésitez pas », « ce
bien conviendra parfaitement ». Les annonces sont le genre où ces tics se voient le plus,
parce que tout le monde en lit vingt d'affilée.

## 11. Les photos

La première répond-elle à la fiche client et pas au bien ? L'ordre est-il celui de la visite ?
Rien qui identifie, rien qui date, rien qui n'est pas rangé ? Les droits sont-ils dans
`cadre.md` ?

## 12. Le doublon

Si le bien a déjà eu une annonce — ancien mandat, autre agence — celle-ci n'en reprend aucune
phrase. On ne recopie pas, même son propre texte d'il y a six mois — c'est la règle de toute la
mallette sur ce qui vient d'une page.

---

## Ce qui est rédhibitoire

Quatre choses. Si l'une est présente, **tu ne livres pas** — tu dis ce qui manque et tu
attends.

- un fait qui n'est pas dans la fiche
- une mention obligatoire rédigée par toi, ou absente alors que `cadre.md` la désigne
- une donnée qui identifie un tiers
- une photo dont les droits ne sont pas établis, si la ligne de `cadre.md` est vide

Le reste se corrige avec lui.

---

## Quand il dit « c'est nul, refais »

Propose deux hypothèses tirées du texte : « c'est l'ordre, ou c'est le ton ? » S'il ne
désigne rien, réécris une fois en changeant **une seule chose** — presque toujours la première
ligne. S'il rejette la deuxième, arrête : une annonce rejetée deux fois dit que la fiche client
est fausse, pas que l'écriture est mauvaise.

---

## Comment tu livres

**Pas ici.** `livrer.md` possède la sortie.
