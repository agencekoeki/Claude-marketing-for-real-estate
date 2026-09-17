# Ce qu'il y a autour du bien

## Pourquoi c'est un fait, et pas un ajout

L'environnement est ce que l'acquéreur ne peut pas lire dans les champs du portail, et c'est
souvent ce qui décide : l'école pour une famille, la gare pour quelqu'un qui travaille
ailleurs, les commerces pour quelqu'un qui ne conduit plus. **C'est une partie de la fiche des
faits**, pas un paragraphe qu'on ajoute au texte.

Et c'est le fait le plus facile à rater, parce que « proche de tout » ne coûte rien à écrire
et ne veut rien dire. On ne l'écrit jamais. On écrit une distance.

---

## Ce que ça mange

**La position du bien.** L'adresse, ou à défaut la rue et la commune. **Pour regarder, jamais
pour écrire** : ce qui se publie de l'adresse est décidé par `00_MOI/cadre.md`, et ce qu'on
utilise pour mesurer ne va nulle part. Dis-le en une phrase quand tu la demandes : « je te
demande l'adresse pour regarder autour, elle ne va pas dans l'annonce ».

**Les repères de sa zone.** Section 2 du profil : les lieux que ses clients citent, ceux qui
ancrent un texte. Ils disent lesquels comptent ici ; ils ne disent pas à quelle distance de ce
bien.

**La fiche client.** Elle dit **quels** repères comptent pour cet acquéreur. Trois, pas dix :
ceux qui répondent à « ce qui le met en route » et à « ce qui le bloque ».

---

## Comment on obtient une distance

Deux voies, et **jamais une estimation silencieuse**.

**La voie du navigateur.** Un plan, un itinéraire à pied ou en voiture depuis la position du
bien vers chaque repère. Au navigateur visible, en annonçant avant :

> Je regarde à combien sont l'école, la gare et la boulangerie depuis la maison. Regarde le
> panneau de droite.

Ce que tu relèves est `[vu]`, avec sa source : `- [vu 2026-09] école primaire à 4 min à pied
(itinéraire)`. **À pied ou en voiture, jamais à vol d'oiseau** — un acquéreur qui compte quatre
minutes et en fait douze ne revient pas.

**La voie de l'agent.** Il connaît son secteur : il sait que la boulangerie est à deux cents
mètres. Mais on ne lui pose pas une question ouverte — on lui propose : « la gare, je dirais
douze minutes à pied, c'est ça ? » Il confirme, il corrige, et la ligne est `[dit]`.

**S'il n'y a ni navigateur ni réponse**, le bloc environnement reste vide dans la fiche, et
vide dans l'annonce. Pas de « proche de » pour combler. Un environnement absent est une
information ; un environnement approximatif est une faute.

---

## Ce qu'on regarde, et ce qu'on ne regarde pas

**Trois repères, choisis pour la fiche client**, parmi ceux de sa section 2 et ce que le plan
montre. Pas la liste complète des commerces de la commune : trois distances qu'on retient
valent mieux que dix qu'on saute.

**Ce qui s'entend et se voit depuis le bien.** Ça ne se lit pas sur un plan, et c'est ce qui
fait une visite déçue : la route, la voie ferrée, la cloche, le bar d'en bas. Une question à
l'agent, une seule — **qu'est-ce qu'on entend depuis le séjour, fenêtres ouvertes ?** Et la
règle des travaux s'applique : **on ne cache pas une nuisance, on la dit.** Une annonce qui la
tait produit une visite perdue ; une annonce qui la dit produit la visite de quelqu'un qui a
déjà décidé que ça ne le gênait pas.

**Ce qu'on ne regarde pas :** les risques réglementaires — inondation, sol, bruit — qui
relèvent d'un diagnostic, pas de l'annonce. Ni les prix du secteur, qui relèvent de l'avis de
valeur. Ni l'ambiance du quartier en général, qui est un jugement.

---

## Ce que ça donne, et à qui

**Trois lignes dans la fiche des faits**, chacune avec sa source et sa date, plus une ligne
sur ce qui s'entend s'il y a quelque chose.

**Le bloc environnement de l'annonce**, dans `structure.md` : trois distances, une phrase
chacune, dans l'ordre de la fiche client.

**Et la publication sur ce bien**, dans `immo-reseaux-sociaux` : l'angle du lieu, quand il
publie sur ce bien, s'appuie sur ces mêmes repères. C'est écrit dans `01_BIENS/<bien>/`, il
n'a qu'à lire.

---

## Rappel de marquage

Une distance mesurée sur un plan est `[vu]` avec « itinéraire » comme source. Une distance
qu'il confirme est `[dit]`. Une distance à vol d'oiseau n'est rien et ne s'écrit pas.
L'adresse ne va dans aucun fichier au-delà de ce que `cadre.md` autorise — et jamais dans
`00_MOI/`.
