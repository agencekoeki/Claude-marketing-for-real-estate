# Récolter des sujets

## Ce qu'on cherche, et ce qu'on ne cherche pas

**On ne cherche pas des idées, on cherche des traces d'activité réelle.**

Une idée inventée est générique par construction : elle pourrait être écrite par n'importe
lequel de ses confrères. Une trace est datée, précise, et il la reconnaît — c'est elle qui
donne un texte que personne d'autre ne pouvait produire.

Quatre familles de traces, et rien d'autre :

- **ce qu'il a fait** — rendez-vous, visites, signatures, déplacements
- **ce qu'on lui a demandé** — les questions qu'il a répondues, souvent plusieurs fois
- **ce qui a changé** — un bien rentré, un prix ajusté, une vente conclue, un avis déposé
- **ce qui arrive** — une date, une échéance, une saison

---

## Six sources, et ce que chacune donne

### Son agenda

**La plus rentable, et la moins utilisée.** C'est un journal daté de son activité réelle, qu'il
tient déjà sans y penser.

**Ce qu'on y lit :** les quinze derniers jours pour ce qu'il a fait — visites, estimations,
signatures, rendez-vous vendeur. Les quinze prochains pour ce qui arrive — portes ouvertes,
remises de clés, réunions. Et les créneaux qui reviennent, qui sont des rituels.

**Ce qu'on en tire :** l'angle des coulisses et l'angle de la preuve, presque sans effort.
« Trois estimations cette semaine » est un sujet ; « j'ai fait des estimations » n'en est pas
un.

**Ce qu'on n'en tire pas :** aucun nom, aucune adresse. Un rendez-vous devient « une visite »,
pas « la visite chez X ».

### Ses mails envoyés

**La meilleure source pour les objections**, et elle est déjà exploitée par l'init pour la
voix — ici on cherche autre chose.

**Ce qu'on y lit :** les questions auxquelles il a répondu dans le mois. Une question à
laquelle il a répondu trois fois est une publication qui lui rendra du temps tous les mois.
C'est la mission « se faciliter la vie ».

**Requêtes utiles :** les messages les plus longs qu'il a écrits, ceux qui commencent par une
reformulation de question, et ceux envoyés plusieurs fois à des destinataires différents.

**Ce qu'on n'en tire pas :** le contenu d'un dossier, une situation, un montant. On retient la
question, jamais qui l'a posée.

### Ses comptes rendus de rendez-vous

S'il a un preneur de notes automatique. **Ce qu'on y cherche ici n'est pas sa voix mais les
questions posées en face à face** — celles qu'on ne pose jamais par écrit.

Verrou lexical identique à celui de l'init : on extrait des tournures, jamais des situations.

### Son dossier de travail

**Ce qu'on y lit :** les fichiers récents. Des photos ajoutées la semaine dernière veulent dire
un bien fraîchement pris en photo. Un document créé veut dire un dossier qui avance.

**Attention :** cette source est locale : une récolte qui la lit ne se planifie qu'en local,
Claude Desktop ouvert. Voir plus bas.

### Ses avis récents

Un avis déposé depuis la dernière récolte est un sujet immédiat : la preuve, avec ses mots à
lui. Et s'il contient une objection qu'il n'avait pas identifiée, elle remonte aussi dans
`clients-types.md`.

### Son outil métier

Biens rentrés, prix ajustés, ventes conclues, relances en attente. **Il n'y a généralement pas
de connecteur** : demande-lui un export, ou pose-lui simplement la question — trois minutes et
il te donne tout.

Ne cherche pas à t'y connecter, et **n'ouvre jamais un espace qui demande un identifiant**.

---

## Ce que les connecteurs permettent, et ce qu'ils imposent

La section 13 de son profil dit quels connecteurs sont branchés — l'init l'a consigné. **Tu
ne récoltes que dans ce qui est branché**, et tu ne lui fais pas brancher quoi que ce soit au
milieu d'une récolte : si la messagerie ou l'agenda manquent, tu le notes comme une remarque et tu
récoltes ailleurs.

**Chaque requête sur un connecteur est un appel distinct qui lui demande son accord.** Une
récolte, c'est cinq à huit requêtes ciblées, pas une lecture de la boîte. Préviens-le du
nombre avant la première. Et si un connecteur ne répond pas après deux tentatives, tu
abandonnes cette source sans diagnostic — c'est la règle de l'init, elle vaut ici.

**Ses fichiers ne sont visibles que si son dossier de travail est ajouté à la séance.** Le
dossier de la mallette est celui de la séance ; ses autres dossiers ne le sont pas. C'est
pour ça que la récolte planifiée ne les lit pas.

## Comment on récolte

**On annonce avant d'ouvrir**, source par source, comme dans l'init. Pas de recherche
silencieuse.

**On extrait de la forme, pas du fond.** Ce qu'il a fait, ce qu'on lui a demandé, ce qui a
changé. Jamais un nom, une adresse, un montant, une situation.

**Plafonds :** quinze jours en arrière et quinze en avant sur l'agenda, une trentaine de mails
envoyés sur le mois, dix comptes rendus, les fichiers modifiés depuis la dernière récolte.

**Deux tentatives par source.** Une source qui ne donne rien est une information, pas un échec.

---

## Ce qu'une trace devient

**Jamais un post directement.** Chaque trace devient **une ligne du carnet**, avec sa famille
de sujet et ce qu'il faut avoir sous la main. C'est `plan.md` qui reprend la main.

| La trace | Ce qu'elle devient |
|---|---|
| Trois rendez-vous du même type dans la semaine | un sujet de coulisses, ou une question qui revient |
| Une question répondue plusieurs fois par écrit | une publication qui lui rendra du temps |
| Un bien rentré, ajusté, vendu | un des huit moments d'un bien |
| Un avis déposé | une preuve, avec les mots du client |
| Une date qui approche | un sujet daté, à préparer trois semaines avant |
| Un créneau qui revient chaque semaine | un candidat pour `00_MOI/recurrences.md` |

**Et une trace qui ne rentre nulle part n'est pas un sujet.** On la laisse.

---

## La récolte est planifiable, sous une condition

C'est ce qui rend la mallette auto-alimentée, et la contrainte est connue : **une tâche planifiée à distance ne lit pas son dossier local** — seule une tâche liée à un
dossier le lit, et elle ne tourne qu'en local, Claude Desktop ouvert.

Donc la récolte se planifie à distance si elle se limite à **son agenda et sa messagerie
branchés par connecteur, et ses avis publics** — tout ce qui se lit sans son ordinateur. Dès
qu'elle a besoin de son dossier de travail, elle se lance à la demande.

**La bonne cadence est celle du carnet** : une fois par mois, quelques jours avant qu'il s'y
mette, pour qu'il arrive avec la matière déjà rassemblée plutôt qu'une page blanche.

**Mais une tâche planifiée à distance ne peut pas écrire dans son dossier.** Sa liste de traces reste
dans la conversation de la tâche. Donc le carnet commence par une ligne : « colle-moi ce que
la tâche t'a préparé » — et s'il ne l'a pas, on refait la récolte en séance, dix minutes. La
tâche prépare ; elle ne remplit pas le carnet toute seule, et on ne le lui promet pas.

Et la règle de l'init s'applique : **une tâche prépare, elle ne publie pas.** La récolte
produit une liste de traces, pas des publications.

---

## Ce qu'on ne fait jamais

**On ne cherche pas d'idées sur internet.** Les listes de sujets pour agents immobiliers
produisent exactement ce que `metier.md` interdit — citations, jeux-concours, rebonds
d'actualité — et ça le fait ressembler à tout le monde.

**On ne lit aucun espace connecté** : ni son outil métier, ni un groupe privé, ni une
messagerie autre que la sienne.

**On ne récolte pas chez les confrères.** Le paysage local a été regardé une fois pendant
l'init, et un agent qui surveille ses concurrents arrête d'écrire.

---

## Rappel de marquage

Une trace est `[vu]` : datée, vérifiable, formulée comme un constat. Ce qu'il confirme en te
répondant est `[dit]`. Et rien de ce qui touche un tiers n'entre nulle part — ni son nom, ni
sa situation, ni son adresse.
