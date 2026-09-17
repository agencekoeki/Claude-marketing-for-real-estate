# Récupérer ce qu'une autre IA sait déjà de lui

**En mode salle, on saute entièrement cette source.** Quatre copier-coller dans un compte
tiers, c'est le pire rapport temps sur effet de tout l'init. Elle est faite pour
l'installation complète, à froid.

## Pourquoi un seul prompt ne suffit pas

ChatGPT a deux couches de mémoire. Les **mémoires enregistrées** sont une liste courte, que
l'utilisateur peut consulter et modifier. La **référence à l'historique des conversations**
est implicite, bien plus riche, et remonte au-delà d'un an.

« Qu'est-ce que tu sais de moi » interroge la première couche. Elle est courte par
construction. La seconde ne se réveille que sur une question assez précise pour déclencher
une recherche dans l'historique.

D'où la règle : **on ne pose pas une question large, on pose une série de questions étroites.**
Chacune va chercher, chacune ramène de la matière.

---

## Passe 0 — Le raccourci qui bat tous les prompts

Avant tout prompt, fais-lui ouvrir ses réglages : **Réglages > Personnalisation > Mémoire**.
Ce qu'il y lit est la matière brute, sans interprétation du modèle. Il copie, il te colle.

Depuis juin 2026, l'affichage est un résumé unique réécrit automatiquement plutôt qu'une
liste d'entrées. L'ancienne liste existe encore comme option héritée selon les comptes.
Prends ce qu'il y a, quelle que soit la forme.

Deux cas où ça ne donnera rien : la mémoire est désactivée, ou il travaille en conversation
temporaire, qui la contourne entièrement. Dans ce cas, passe directement en passe 1 :
l'historique peut être exploitable même quand les mémoires enregistrées sont vides.

Si le compte est un compte d'entreprise, la mémoire peut être coupée par défaut côté
administrateur. Ne le fais pas chercher, passe à autre chose.

---

## Passe 1 — Le métier

Un seul message, mais huit questions dedans. Fais-lui coller ceci :

```
Tu m'as aidé sur des sujets professionnels depuis un moment. Cherche dans nos
échanges passés, pas seulement dans ce que tu as mémorisé, et réponds point
par point. Quand tu ne trouves rien sur un point, écris "rien trouvé" au lieu
de déduire.

1. Quel métier j'exerce, sous quel statut, et pour quelle structure
2. Quels lieux, quels secteurs, quels types de dossiers reviennent
   dans nos échanges
3. Quels types de clients je te décris le plus souvent
4. Quelles difficultés et quels blocages je te rapporte régulièrement
5. Quels outils et logiciels je mentionne
6. Quels noms de dossiers, de secteurs, d'abréviations j'emploie sans
   te les expliquer
7. Qu'est-ce que je t'ai demandé de produire le plus souvent
8. Quelles dates approximatives pour chacun de ces éléments

Pour chaque point, cite la formulation que j'ai employée moi, entre guillemets,
plutôt que de la reformuler.
```

La dernière consigne est celle qui change tout : ses formulations exactes valent dix fois
une synthèse, parce que c'est son vocabulaire, pas celui du modèle.

---

## Passe 2 — Le style, par l'écart et pas par la description

```
Toujours en cherchant dans nos échanges passés :

1. Qu'est-ce que je t'ai demandé de changer le plus souvent dans tes réponses
2. Quelles formules, quels mots, quels tics je t'ai demandé d'éviter
3. Quand je réécris un texte que tu m'as proposé, qu'est-ce que je change
   systématiquement : la longueur, le ton, le vouvoiement, la ponctuation
4. Est-ce que je te tutoie, est-ce que je te demande de tutoyer mes lecteurs
5. Quels textes que tu as produits pour moi j'ai gardés tels quels, et
   lesquels j'ai rejetés

Cite mes propres mots quand tu en as.
```

Le point 5 est le plus rentable de toute la passe : ce qu'il a gardé est un échantillon de
sa voix validé par lui.

---

## Passe 3 — Les récurrences

C'est la passe que la plupart des gens ne font jamais, et c'est celle qui produit les tâches
planifiées.

```
Dernière chose, et c'est la plus précise. Cherche dans nos échanges les demandes
qui REVIENNENT.

1. Quelles demandes je t'ai faites plusieurs fois, même reformulées
   différemment, à des semaines ou des mois d'intervalle
2. Pour chacune, donne-moi les dates approximatives de chaque occurrence
3. À quels moments du mois ou de la semaine je te sollicite le plus
4. Quelles expressions de périodicité j'emploie : "tous les lundis",
   "en fin de mois", "à chaque nouveau dossier", "avant chaque"
5. Qu'est-ce que je refais visiblement à la main alors que ça se répète

Ne suppose aucune régularité que tu ne peux pas appuyer sur au moins
deux occurrences datées.
```

---

## Passe 4 — Les trous

```
Pour finir : qu'est-ce que tu ne sais pas de moi et qui te manquerait pour
travailler beaucoup mieux avec moi ? Liste-le, sans le combler.
```

Cette réponse te donne gratuitement une partie de ton plan de questions.

---

## La clause de confidentialité à ajouter partout

Ajoute cette ligne à la fin de chaque passe :

```
N'inclus rien sur ma santé, mes opinions politiques ou religieuses, ma vie
privée, ma situation familiale ou ma situation financière personnelle,
ni sur celle de tiers, même si je t'en ai parlé.
```

---

## Ce que tu fais des réponses

**Statut.** Tout ce qui sort marque `[dit]` quand c'est une citation de ses propres mots,
`[à confirmer]` quand c'est une synthèse du modèle. La distinction compte : l'autre IA
interprète, et son interprétation n'est pas un fait.

**Vérification ciblée.** Prends les trois affirmations les plus structurantes et fais-les
confirmer en une seule question groupée. Pas les vingt, les trois.

**Récurrences.** La passe 3 arrive directement dans le tri de `tri-recurrences.md`. Une
récurrence appuyée sur deux occurrences datées est exploitable, une récurrence affirmée
sans date ne l'est pas.

**Coût.** Quatre passes, c'est quatre copier-coller. C'est long en salle. S'il faut choisir,
garde la passe 0 et la passe 3 : le résumé brut et les récurrences. Ce sont celles qui
produisent quelque chose d'actionnable.

---

## Autres assistants

Le même découpage fonctionne ailleurs. Adapte la première phrase de chaque passe, le reste
tient tel quel. Les modèles qui n'ont aucune mémoire répondront depuis la conversation
courante seulement : n'insiste pas, ça ne donnera rien.

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
