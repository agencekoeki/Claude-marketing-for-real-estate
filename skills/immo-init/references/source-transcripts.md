# Fouiller ses comptes rendus de réunion

## Contents
- Pourquoi c'est la meilleure source pour les clients types
- Détecter l'outil
- Le verrou de confidentialité
- Ce qu'on en tire, et ce qu'on n'en tire pas
- Les transcripts et la voix
- Plafond

---

## Pourquoi c'est la meilleure source pour les clients types

Un compte rendu de rendez-vous d'estimation ou de débriefing de visite contient **le client
qui parle avec ses mots à lui**. C'est exactement ce que l'entretien des trois derniers
dossiers cherche à reconstituer de mémoire, sauf que là c'est enregistré et daté.

Deux choses en sortent que rien d'autre ne donne aussi bien : les objections telles qu'elles
sont formulées, et la durée réelle des allers-retours quand plusieurs rendez-vous sont
espacés dans le temps.

C'est aussi la seule source où l'utilisateur **parle** au lieu d'écrire. Voir plus bas : ça
change ce qu'on a le droit d'en tirer.

---

## Détecter l'outil

Beaucoup de gens en ont un sans y penser, parce qu'il a été activé par défaut dans leur
visio. Pose la question simplement :

> Est-ce que tu as un truc qui prend tes réunions en note tout seul ? Un assistant qui
> t'envoie un compte rendu après un rendez-vous en visio ?

S'il ne sait pas, deux indices qui tranchent vite : un compte rendu automatique reçu par mail
après une visio, ou un document « Notes » attaché à un événement de son agenda.

Familles d'outils à reconnaître : les assistants dédiés qui rejoignent la réunion, les
fonctions intégrées aux visioconférences, et les enregistreurs de poche qui transcrivent.
Ne cherche pas à cataloguer. Ce qui compte est **où les comptes rendus atterrissent** :

- dans l'application de l'outil, sans rien sur son disque → il faut qu'il exporte, et en
  salle c'est souvent trop long : note la source et passe
- dans son stockage en ligne, sa messagerie ou un dossier local → exploitable tout de suite
- nulle part, il ne les relit jamais → c'est une information en soi, note-la

Note l'outil et l'emplacement en section 13 du profil, même si tu n'exploites pas la source.

---

## Le verrou de confidentialité

C'est la source la plus sensible de la mallette, et de loin. Un compte rendu de rendez-vous
vendeur contient un nom, une adresse, un motif de vente personnel, parfois une capacité de
financement ou une situation familiale. Et il contient la voix d'un tiers qui a consenti à
l'enregistrement pour le compte rendu de son interlocuteur, pas pour alimenter un profil.

**Demande le feu vert explicitement, et dis ce que tu ne feras pas :**

> Tes comptes rendus de rendez-vous, c'est la meilleure source pour comprendre comment tes
> clients parlent. Je n'en retiens que des tournures — la façon dont les gens formulent leurs
> questions et leurs objections. Aucun nom, aucune adresse, aucun montant, aucune situation
> ne sort de là. Je peux regarder ?

Un refus n'arrête rien. Note le manque et passe à l'entretien, qui donne la même chose en
moins précis.

**La règle forme-pas-fond ne suffit pas ici. La règle est lexicale :** on extrait des
tournures, jamais des situations. « Ma situation est compliquée en ce moment » est une
situation, on ne l'écrit pas. « De toute façon je ne suis pas pressé » est une tournure, on
l'écrit.

Si tu hésites sur une phrase, c'est qu'elle est du fond. Passe.

---

## Ce qu'on en tire, et ce qu'on n'en tire pas

**On en tire :**

- **Les objections, mot pour mot.** Une objection est une formule, pas une confidence.
  « Je veux voir ce que ça donne avant de m'engager » est réutilisable telle quelle.
- **Son vocabulaire à lui.** Les sigles, abréviations et noms de dossiers qu'il emploie sans
  les expliquer à son interlocuteur. C'est le gisement le plus riche pour la section 7 du
  profil : à l'oral, personne ne développe ses acronymes.
- **Le vocabulaire des clients.** Comment ils nomment les pièces, le prix, le mandat, le
  délai. C'est leur langue, pas celle du métier, et c'est ce qui rend un texte reconnaissable.
- **Les questions qui reviennent.** Une question posée dans trois rendez-vous différents est
  un sujet de publication, et un candidat pour `recurrences.md`.
- **Qui parle dans la pièce.** Combien de personnes, qui pose les questions, qui tranche à la
  fin, qui reste silencieux puis bloque. Alimente directement les rôles dans la décision des
  fiches clients types.
- **La durée.** Si plusieurs comptes rendus concernent le même dossier, l'écart entre les
  dates donne le rythme réel des allers-retours.

**On n'en tire pas :** aucun nom, aucune adresse, aucun bien identifiable, aucun montant,
aucun motif de vente, aucune situation personnelle ou professionnelle. Pas même anonymisé :
un compte rendu anonymisé reste reconnaissable par celui qui l'a vécu, et souvent par la
personne dont il parle.

Et rien sur la santé, la situation familiale ou financière de qui que ce soit, même si ça
occupe la moitié du rendez-vous. C'est fréquent dans ce métier, et c'est exactement ce qu'on
laisse derrière.

---

## Les transcripts et la voix

**Ils ne vont dans `voix.md` que dans un seul bloc : le registre « oral » de la signature
mesurée.** C'est la seule source où l'utilisateur parle au lieu d'écrire, et son registre oral
n'est pas son registre écrit. Une voix écrite calibrée sur de l'oral produit des textes
bavards — mais un script de short calibré sur de l'écrit produit quelqu'un qui lit. Donc :
**ses mots à lui seulement**, extraits des comptes rendus, mesurés par `scripts/stylo.py
profil --registre oral`, et collés dans le bloc « oral ». Jamais les mots des clients, jamais
une situation. Ce bloc ne sert qu'au short face caméra.

Ils alimentent `clients-types.md` et la section 3 du profil. Si un trait oral est vraiment
frappant — une formule de reformulation qu'il emploie systématiquement, par exemple — tu peux
l'écrire dans `voix.md` sur une ligne isolée marquée « à l'oral », jamais dans les règles
générales.

---

## Plafond

Dix comptes rendus au maximum, les plus récents, répartis entre types de rendez-vous plutôt
que pris à la file — sinon tu décris une seule phase du métier.

**En mode salle, cette source ne s'ouvre que si elle est déjà accessible sans manipulation.**
Un export à faire pendant la séance coûte plus que ce qu'il rapporte.

Si l'outil existe mais que les comptes rendus ne sont pas atteignables, note-le en section 13
comme un branchement à faire plus tard : c'est le meilleur candidat pour enrichir les fiches
clients types après la formation.

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
