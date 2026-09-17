# Fouiller ses mails envoyés

La meilleure source pour la voix, et la plus sensible. La plupart des gens écrivent bien plus
dans leur messagerie que partout ailleurs, et ils y écrivent sans se surveiller. C'est
exactement ce qu'on cherche.

C'est aussi là que se trouvent des identités, des situations personnelles et des montants.
D'où la règle qui gouverne tout ce fichier.

---

## La règle

**On extrait de la forme, jamais du fond.**

Comment il ouvre, comment il ferme, s'il tutoie, combien de lignes, quelle ponctuation,
à quelle fréquence il relance. Rien sur ce que raconte le message.

Aucun nom, aucune adresse, aucun montant, aucune situation personnelle ou professionnelle
d'un tiers n'est recopié dans un fichier de `00_MOI/`. Pas même comme exemple. Pas même
anonymisé : un mail anonymisé reste reconnaissable par celui qui l'a vécu.

---

## Deux prérequis, et comment les poser

**À qui appartient la boîte.** Avant tout, la question posée en une phrase, parce que la
réponse change ce que tu as le droit de faire : sa messagerie professionnelle appartient
parfois à sa structure et pas à lui. `metier.md` dit si ce cas est fréquent dans ce métier et
comment formuler la question. S'il ne sait pas, ou si la boîte est celle de la structure, tu
proposes la source suivante sans insister et tu notes le point en section 13.

**L'accès.** Sa messagerie par connecteur — Gmail, ou Outlook avec un compte Microsoft 365
professionnel —, sinon l'export de vingt à trente mails envoyés : c'est l'ordre d'accès de
`connecteurs.md`, avec les clics et ce qu'il faut lui dire avant. Jamais sa messagerie web au
navigateur. S'il existe un connecteur pour lui et qu'il n'est pas branché, c'est le moment, et
la formulation compte :

> Tes mails envoyés, c'est là que tu écris le plus et le plus naturellement. Si je peux les
> lire, j'apprends ta façon d'écrire beaucoup mieux qu'avec tes posts, qui sont souvent
> retravaillés. Je ne regarde que ce que tu as envoyé, jamais ce que tu reçois, et je
> n'en retiens que la forme. Tu veux le brancher ?

S'il dit non, tu notes le manque et tu continues. Un refus ici n'empêche rien, et insister
en salle devant ses collègues est le meilleur moyen de perdre toute la journée.

---

## Les requêtes

**Chaque requête est un appel distinct, et chaque appel lui demande son accord.** Une enquête
mail, c'est six à dix requêtes courtes, pas une lecture de la boîte. Préviens-le du nombre
d'autorisations avant la première.

Toujours l'envoyé, jamais la réception : `in:sent` sur Gmail, le dossier des éléments envoyés
sur Outlook.

Les opérateurs de recherche de sa messagerie marchent d'ordinaire. **S'ils ne ramènent rien, reformule
en langage courant** — « mes mails envoyés à des vendeurs ces six derniers mois » — avant de
conclure que la boîte est vide.

**Cadrage temporel.** `in:sent newer_than:6m` — six mois suffisent. Au-delà, tu décris
quelqu'un qui a peut-être changé de structure ou de secteur. Trois mois en mode salle.

**Segmentation par interlocuteur.** C'est la passe qui produit le plus de valeur, parce que
la plupart des gens n'écrivent pas pareil selon à qui ils parlent, et ne le savent pas.
**Les segments et leurs requêtes sont dans `metier.md`.** Repère le type de correspondant par
les mots du fil, pas par l'adresse.

**Longueur utile.** Privilégie les fils où il a vraiment écrit. Un « ok merci » ne dit rien
de son style. Vise les messages d'au moins une centaine de mots.

**Signaux de récurrence.** `in:sent relance` · `in:sent "point"` · `in:sent
récapitulatif` · `in:sent "cette semaine"`. Et surtout : un même objet de message qui
revient à intervalle régulier. C'est un rituel qu'il fait à la main.

---

## Ce qui se mesure plutôt que de se noter

S'il peut exporter ses mails envoyés en texte — beaucoup de messageries le font en deux
clics —, **c'est le corpus idéal pour `scripts/stylo.py profil`** : la couche que la
stylométrie tient pour la plus discriminante, mesurée au lieu d'être estimée. Ce qui suit
reste utile pour ce que le script ne voit pas — l'écart entre interlocuteurs, les relances,
les sigles.

## Ce que tu notes, concrètement

Pour chaque segment d'interlocuteur :

- longueur moyenne, en lignes
- formule d'appel exacte, et si elle varie
- tutoiement ou vouvoiement, et s'il bascule selon l'interlocuteur
- formule de clôture et signature
- présence ou non d'une question finale
- ponctuation : points d'exclamation, points de suspension, majuscules
- emoji : oui, non, lesquels
- délai et ton des relances
- les sigles et abréviations qu'il emploie sans les développer, pour la section 7 du profil

Puis l'écart entre segments, qui est l'information la plus utile de toutes. C'est un constat
qu'il n'a jamais formulé lui-même et qu'il reconnaît immédiatement. `metier.md` te dit quel
écart chercher en priorité dans ce métier. C'est ton meilleur moment de démonstration.

---

## Les échantillons dans voix.md

Tu ne colles jamais un vrai mail. Pour illustrer un trait, **tu reconstitues** une phrase
type qui le porte, et tu signales que c'est une reconstitution :

> Ouverture type vers un vendeur, reconstituée : « Bonjour Monsieur X, comme convenu je
> reviens vers vous concernant votre bien. » — `[vu]`

---

## Plafond

Voir `protocole.md`. Répartis les messages entre les segments plutôt que de prendre les plus
récents, sinon tu décris une seule facette de son écriture.

Si le connecteur est lent ou incomplet après deux tentatives, abandonne la source et dis-le.
Une enquête mail ratée ne bloque rien : les questions de l'étape suivante compensent.

---

## Rappel de marquage

Avant d'écrire quoi que ce soit tiré de cette source : chaque ligne porte `[dit]`, `[vu]` ou
`[à confirmer]`, **suivi du mois** — `[dit 2026-09]`. Ce qu'il a dit lui-même est `[dit]`. Ce
que tu as constaté ici est `[vu]`, formulé comme un constat vérifiable. Le reste est
`[à confirmer]` et reste vide.

Quand la date est inconnue — une ligne reprise d'ailleurs, un import — on écrit `[dit ?]`
plutôt que d'inventer un mois.

Une occurrence unique reste une occurrence unique. Tu n'inventes jamais une valeur pour
remplir une case.
