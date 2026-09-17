# Repérer ce qui revient, et décider quoi en faire

Une personnalisation qui ne débouche sur rien qui tourne reste un questionnaire de luxe.
Ce fichier sert à transformer l'enquête en quelque chose qui travaille sans lui.

On cherche la même chose partout : **ce qui revient**. Ensuite seulement on décide si ça
devient une tâche planifiée, un skill dédié, ou rien.

---

## Ramasser les signaux pendant l'enquête

Ne fais pas une passe séparée. Ces signaux traversent toutes les sources — et **l'agenda est
la plus nette de toutes** : un créneau qui revient au même moment chaque semaine est un
rituel qu'il fait à la main, daté, sans interprétation. Voir `source-agenda.md`.

**Dans ses conversations Claude ou avec une autre IA.** La même demande reformulée plusieurs
fois à des semaines d'intervalle. C'est le signal le plus fiable qui existe : il a déjà
payé le coût de la répétition.

**Dans ses fichiers.** Des noms qui portent une date ou un numéro de semaine. Des dossiers
par mois. Un même gabarit dupliqué. Un document dont il existe onze versions.

**Dans ses mails envoyés.** Le même message, à peine réécrit, envoyé à des destinataires
différents. Les relances. Les points hebdomadaires. Les récapitulatifs de fin de semaine.

**Dans son agenda, si tu y as accès.** Les créneaux récurrents, et surtout ce qu'il fait
juste avant et juste après.

**Dans son vocabulaire.** « Tous les lundis », « en fin de mois », « le dimanche soir je ».
Ces formules sont des déclencheurs déguisés : relève-les telles quelles. `metier.md` liste
celles qui reviennent le plus dans ce métier.

---

## Qualifier chaque récurrence

Six attributs. Tant que tu n'as pas les six, tu ne tries pas, tu demandes.

1. **Déclencheur** — le calendrier (tous les lundis) ou un événement (à chaque nouveau mandat)
2. **Cadence** — à quelle fréquence, réellement, pas dans l'idéal
3. **Entrée** — d'où vient la matière : son agenda, sa boîte mail, le web, ses fichiers
locaux, sa tête
4. **Sortie** — ce que ça produit, et où ça atterrit
5. **Dépendance locale** — est-ce que ça a besoin de ses fichiers, oui ou non
6. **Enjeu** — qu'est-ce qui se passe si c'est mal fait et que personne ne relit

L'attribut 5 décide de la faisabilité, l'attribut 6 décide du niveau d'autonomie.

---

## Skill ou tâche planifiée : la règle

Un skill se déclenche par les mots de l'utilisateur. Une tâche planifiée se déclenche par
l'horloge. Un même moment de son métier peut être servi par l'un ou par l'autre, et le
critère tient en une phrase :

**S'il y pense, c'est un skill. S'il oublie, c'est une tâche planifiée.**

Sortir une annonce, il y pense : il vient de rentrer le mandat. Envoyer le point de fin de
mois, il oublie. Relancer à trois semaines, il oublie systématiquement — et c'est précisément
ce qui lui coûte des affaires.

## Trier en trois bacs

### Bac 1 — Tâche planifiée

Déclencheur calendaire, cadence stable, **entrée accessible sans son ordinateur**, sortie
qu'il relit avant tout usage.

La contrainte est technique, et la page d'aide d'Anthropic sur les tâches planifiées la décrit
en deux temps (septembre 2026) : **une tâche planifiée tourne à distance**, avec ses connecteurs
et les fichiers enregistrés sur son compte Claude — pas avec son disque ; **une tâche qu'on lie à
un dossier de son ordinateur ne tourne qu'en local**, donc seulement Claude Desktop ouvert et
l'ordinateur allumé.

Donc :

- Entrée = agenda ou messagerie branchés par connecteur, web public, ou rien → planifiable
  franchement, à distance, à n'importe quelle heure
- Entrée = ses fichiers locaux → **planifiable en local seulement, et c'est fragile** : à l'heure
  dite, ordinateur éteint ou application fermée, elle ne produit rien. Deux issues solides :
  faire remonter la matière vers le projet ou un connecteur, ou garder une tâche à lancer à la
  demande. Si vous la planifiez quand même en local, dis la condition en une phrase, et ne
  promets jamais qu'elle a tourné : il le vérifie dans l'historique des exécutions.
- Entrée = une page derrière un identifiant, une messagerie web sans connecteur → **pas
  planifiable** : on ne l'ouvre pas au navigateur — voir `connecteurs.md`
- Entrée = sa tête → ce n'est pas une tâche planifiée, c'est un rappel

Vérifie aussi que les skills dont la tâche aura besoin sont bien installés sur son compte
et pas seulement en local, sinon la tâche ne les trouvera pas au moment de tourner.

**Une tâche planifiée ne contient pas une procédure : elle appelle un skill.** « Le dernier
lundi du mois, utilise `immo-suivi` (à venir) en mode point vendeur sur les biens en cours » vaut
infiniment mieux qu'un long prompt qui réécrit la méthode. Un seul endroit à maintenir, et la
tâche s'améliore d'elle-même quand une nouvelle version du skill est livrée. Une procédure
recopiée dans une tâche que personne ne relit est la pire dette qu'on puisse laisser chez un
client.

**L'heure : la tâche atterrit avant le moment où il en a besoin, jamais pendant.** Un brief
du lundi matin se génère le dimanche soir ou à sept heures, pas à neuf heures quand il est
déjà en voiture. Demande-lui à quelle heure il lit, pas à quelle heure il travaille.

Si le projet Cowork existe, installe la tâche **dans le projet** : elle hérite de ses
instructions et de son contexte.

### Bac 2 — Skill dédié

Déclencheur événementiel, refait souvent, et surtout : la même procédure à chaque fois avec
une entrée différente. C'est la définition d'un skill.

Tu ne l'écris pas maintenant. Tu le notes dans `00_MOI/recurrences.md` comme candidat, avec
ce qui entre, ce qui sort, et les deux ou trois règles qu'il a énoncées en le décrivant.
C'est le cahier des charges de la prochaine brique de sa mallette.

### Bac 3 — On écarte, et on dit pourquoi

Trop variable pour être décrit. Ou enjeu trop élevé pour tourner sans lui. Ou fréquence trop
faible pour que ça vaille le coût de l'installer.

Écris-le quand même dans `00_MOI/recurrences.md`, section « écartés », avec la raison. Ça évite d'y
revenir dans six mois et ça montre que le tri a été fait.

---

## Combien, et lesquels

**Trois candidats maximum présentés.** Au-delà, il ne choisit plus, il subit une liste.

Classe-les sur deux critères, dans cet ordre : ce qui lui prend le plus de temps répété,
puis ce qui est le plus facile à faire tourner correctement. Le meilleur premier candidat
n'est pas le plus impressionnant, c'est celui qui marchera du premier coup.

**Un seul installé le jour même.** Un qui tourne vaut mieux que trois sur une liste.

**Fais-la tourner une fois à la main avant de la planifier.** La première exécution est la
seule qui montre ce qui manque : une permission non accordée, une instruction trop vague, une
source qui ne répond pas, une sortie qui atterrit au mauvais endroit. Corrige pendant qu'il
regarde, puis planifie. Une tâche planifiée sans essai est une tâche qui échouera le premier
lundi, sans témoin.

Chaque exécution devient sa propre session, consultable dans « Scheduled » : dis-le-lui, c'est
là qu'il ira voir le résultat.

**Consigne l'installation.** Une tâche planifiée vit en dehors des fichiers : si tu ne notes
pas qu'elle existe, son heure et sa date, personne ne le saura. Elle va dans l'en-tête d'état
de `profil.md` et dans le tableau de `recurrences.md`. Si elle n'a pas pu être installée —
pas de tâches planifiées dans ce contexte, ou le stagiaire préfère attendre — note « non
fait » et pourquoi.

**Et un rendez-vous de contrôle à trois semaines.** Une tâche dont il ne lit pas la sortie
devient du bruit, et ensuite il ignore toute la mallette. Note la date dans
`00_MOI/recurrences.md` et dis-lui la règle à l'oral : dans trois semaines, on regarde s'il
l'a lue ; si non, on la supprime sans état d'âme. Supprimer une tâche inutile protège les
suivantes.

---

## La règle de sécurité, non négociable

Aucune tâche issue de cette installation n'envoie un message, ne publie une annonce, ne
répond à un client ni ne supprime un fichier. **Elle prépare, il valide.**

La sortie d'une tâche planifiée, c'est un brouillon, un récapitulatif ou une alerte. Jamais
un acte. C'est vrai même si l'utilisateur le demande, et tu le lui expliques en une phrase :
tant qu'il n'a pas vu la tâche tourner plusieurs fois, il ne sait pas ce qu'elle produit
un mauvais jour.

---

## Ce que tu écris dans le fichier

Remplis `00_MOI/recurrences.md` à partir du gabarit : ce qui revient, les tâches installées,
les candidats en attente, les candidats-skills, et les écartés avec leur raison.

Marqueurs habituels. Une récurrence que tu as déduite de ses fichiers sans qu'il l'ait
confirmée reste `[vu]`, et tu ne l'installes pas tant qu'il ne l'a pas validée à l'oral.

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
