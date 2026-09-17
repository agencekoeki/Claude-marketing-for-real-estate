# Protocole d'enquête — règles communes

Quatre sources, chacune dans son propre fichier. Ce document porte ce qui vaut pour toutes.
Les mots à chercher ne sont pas ici : ils sont dans `metier.md`.

- `source-presence-en-ligne.md` — son site, sa fiche d'établissement, ses annonces publiques
- `avis-clients.md` — ce que ses clients ont écrit de lui en public
- `paysage-local.md` — cinq confrères, une seule fois, pour le situer par contraste
- `source-claude.md` — son compte Claude : mémoire et conversations passées, **à sa demande seulement**
- `source-fichiers.md` — ses fichiers, dans le périmètre qu'il accorde
- `source-mail.md` — ses messages envoyés
- `source-transcripts.md` — ses comptes rendus de réunion, s'il a un preneur de notes
- `source-autre-ia.md` — ce qu'une autre IA sait déjà de lui

Neuf sources, en trois temps : **le public** (présence en ligne, avis, paysage local), **le
sien** (compte Claude, fichiers, mails, agenda, comptes rendus), **l'ailleurs** (une autre
IA). Le
premier temps ne demande le consentement de personne, le deuxième en demande à chaque fois,
le troisième demande du travail au stagiaire.

Ordre de rentabilité : **sa présence en ligne d'abord**, parce qu'elle est publique,
immédiate, qu'elle ne demande le consentement de personne, et qu'elle donne les noms de ses
communes — sans lesquels toutes les recherches suivantes ramènent du bruit. C'est aussi la
seule source qui donne quelque chose quand il découvre Claude le jour même. Puis son compte
Claude. Puis ses fichiers. Puis ses mails, qui demandent un connecteur. L'autre IA en
dernier, parce que c'est celle qui demande
le plus de manipulations de sa part.

Les comptes rendus de réunion se placent selon leur accessibilité : déjà dans son stockage en ligne ou son dossier, ils passent juste après ses fichiers et deviennent la meilleure source pour les
fiches clients types ; enfermés dans une application, ils passent en dernier ou pas du tout.

---

## Les deux principes

**On extrait de la forme, pas du fond.** Comment il écrit, comment il s'organise, ce qui
revient, avec quels outils. Jamais ce que contiennent les dossiers de ses clients.

**On cherche deux choses à la fois.** Sa manière, et ses récurrences. Chaque source a ses
propres signaux de récurrence, décrits dans son fichier. Garde `tri-recurrences.md` en tête
du début à la fin : c'est ce qui transforme l'enquête en quelque chose qui tourne.

---

## Annoncer avant d'ouvrir

Pas de recherche silencieuse, jamais. Trois phrases, puis le feu vert :

> Je vais regarder ce que je peux déjà savoir de toi : dans ton compte Claude, dans les
> dossiers que tu me donnes, dans tes mails envoyés. J'en tire ta façon d'écrire, ta façon de
> travailler, et ce qui revient régulièrement chez toi. Je n'écris nulle part le nom d'un
> client, un prix, ou le contenu d'un dossier. Je ne modifie aucun de tes fichiers, j'écris
> seulement dans `00_MOI/`. On y va ?

Et avant chaque source, une phrase : ce que tu ouvres, ce que tu cherches.

Pour tout ce qui est en ligne, la consigne est dans `navigateur.md` : on navigue à l'écran,
on ne récupère pas les pages en silence.

---

## Les plafonds

Deux colonnes : le mode a été choisi au début de la skill.

| Source | Mode complet | Mode salle | Abandon |
|---|---|---|---|
| Présence en ligne | 10 pages | 3 pages | site vide ou introuvable |
| Avis en ligne | 30 à 40 avis | négatifs + 10 positifs détaillés | moins de 5 avis au total |
| Paysage local | 5 confrères, 2 pages | 3 confrères | moins de 3 confrères sur la zone |
| Compte Claude | 20 conversations | 5 conversations | 3 requêtes sans rien de neuf |
| Fichiers | 40 fichiers | 10 fichiers | une catégorie vide après 2 tentatives |
| Mails envoyés | 30 messages / 6 mois | 8 messages / 3 mois | connecteur lent ou incomplet, 2 tentatives |
| Agenda | 30 événements, 15 jours dans chaque sens | une semaine dans chaque sens | connecteur muet, 2 tentatives |
| Comptes rendus | 10 comptes rendus | **si déjà accessible** | export à faire pendant la séance |
| Autre IA | 4 passes | **on saute** | mémoire désactivée |

**En mode salle, la présence en ligne plus une seule autre source.** La première est trop
rentable pour être sautée : elle coûte trois pages et elle remplit quatre sections. Celle
qui est branchée et qui répond tout de suite. Tu
ne cumules pas. Le temps gagné va à l'échantillon de l'étape 6, qui est ce qui fait l'effet.

Une source qui ne donne rien est une information, pas un échec. Dis-le et passe.

---

## Déléguer ou pas

Une session peut confier un travail à un sous-agent : une instance séparée, contexte neuf,
qui travaille seule et **ne renvoie qu'un message final**. Ses lectures et ses résultats
intermédiaires restent chez elle.

**Par défaut, l'enquête ne délègue rien.** Trois raisons, et la première suffit.

**La provenance ne survit pas.** Un sous-agent renvoie une synthèse, c'est sa nature. Tu
récupérerais « les clients apprécient sa réactivité » là où tu voulais leurs formulations
exactes. Tout ce qui devait être `[dit]` redescendrait silencieusement en inférence, et le
marquage ne vaudrait plus rien.

**La démonstration disparaît.** Une délégation est opaque : le stagiaire regarde une attente
au lieu de regarder l'outil travailler. En formation, c'est une régression.

**Le feu vert saute.** Le protocole impose d'annoncer chaque source et d'attendre l'accord.
Un travail lancé en parallèle ouvre plusieurs sources d'un coup.

S'ajoute le coût : une session de travail consomme davantage qu'une conversation, et la
parallélisation multiplie les requêtes simultanées. Un stagiaire qui atteint ses limites au
milieu de la séance a perdu la séance.

**Les deux seules exceptions**, et uniquement hors mode salle : compter les avis d'une ligne,
et balayer les pages des confrères. Deux tâches où rien n'est cité et où seule une liste
courte revient. Partout ailleurs, tu lis toi-même, à voix haute.

Hors formation — une réinstallation à froid, une tâche planifiée qui tourne sans témoin — la
contrainte pédagogique n'existe plus et la délégation redevient légitime pour tout ce qui ne
produit pas de ligne `[dit]`.

---

## Le marquage

**Chaque ligne porte aussi son mois** : `[dit 2026-09]`, `[vu 2026-09]`. Pas le jour — une
préférence n'a pas de jour, et une fausse précision se démonte. `[dit ?]` quand la date est
inconnue, pour une ligne reprise d'ailleurs.

Ça ne sert pas à faire joli. Cinq règles de la mallette en dépendent et deviennent vérifiables
au lieu d'être approximatives : savoir si sa voix a six mois, si son positionnement doit être
revu, si deux corrections rapprochées font une préférence, et ce qui est ancien au moment
d'une mise à jour. Sans date, tout ça se devine.

`[dit]` — il l'a écrit ou dit lui-même, ou ça vient d'un document qu'il a fourni
`[vu]` — tu l'as constaté, formulé comme un constat vérifiable
`[à confirmer]` — tu ne sais pas, et la valeur reste vide

Une occurrence unique reste une occurrence unique. Une régularité affirmée sans deux
occurrences datées n'est pas une régularité.

---

## Ce que tu fais en sortie d'enquête

**Tu synthétises avant de montrer.** Ne déroule pas le détail de ce que tu as lu. Présente le
profil rempli, avec ses marqueurs, et laisse-le réagir.

**Tu annonces tes trous.** Dis combien de sections restent en `[à confirmer]`, et reporte ce
nombre dans l'en-tête d'état de `profil.md`.

**Tu cites tes appuis.** « Tu vouvoies systématiquement dans tes mails mais tu tutoies dans
tes publications » vaut mieux que « ton ton est adaptatif ». Un constat vérifiable, marqué
`[vu]`.

**Tu fais confirmer les récurrences.** Un motif détecté reste `[vu]` tant qu'il ne l'a pas
validé à l'oral, et tu n'installes rien avant cette validation.

---

## Pendant la formation

L'enquête est la première démonstration de la journée. Deux conséquences.

Fais-la **lentement et à voix haute**. Ce qui fait l'effet, ce n'est pas le résultat, c'est de
voir l'outil chercher dans sa vraie vie et en ressortir un constat qu'il reconnaît.

Pose la question du périmètre **à lui**, pas à la salle. C'est le moment où il comprend qu'il
garde la main, et c'est aussi ce qui protège le formateur.
