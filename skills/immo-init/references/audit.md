# L'audit de dérive

## Pourquoi il existe, et pourquoi il n'est pas un skill qu'on appelle

Un modèle qui relit sa propre sortie sans signal externe ne se corrige pas — il se dégrade.
C'est établi pour l'auto-correction dite intrinsèque, sans retour extérieur : sur des tâches de
raisonnement, elle échoue ou fait baisser la performance (Huang et al., « Large Language Models
Cannot Self-Correct Reasoning Yet », ICLR 2024), et un modèle qui juge sa propre production la
favorise (Xu et al., « Pride and Prejudice », ACL 2024). L'évaluation faite dans un contexte
long hérite en plus de la dérive même qui a produit l'erreur. Une couche de relecture ajoutée à des skills déjà précis **dégrade** le résultat.

**Ce qui n'est pas une relecture.** Cocher une liste fermée de critères vérifiables — un marqueur
par ligne, aucun nom propre de tiers, aucun chiffre sans source — est un contrôle : le critère
vient de l'extérieur du texte, et la réponse est oui ou non. Les contrôles des outils et
l'étape 10 de l'init sont de cette nature, et c'est pour ça qu'ils restent. Ce qui est interdit,
c'est la relecture ouverte — « est-ce que c'est bien ? » — qui n'a pour juge que le modèle qui a
écrit. Le test de la négation d'`eprouver.md` reste permis parce qu'il force un chemin contraire
au lieu de confirmer ; il ne remplace jamais le script.

Donc l'anti-dérive de la mallette n'est pas une instruction de plus. Ce sont **deux
mécanismes qui ne dérivent pas** :

**Un script**, qui vérifie les fichiers de vérité de façon déterministe. Il ne lit pas, il
exécute. Il ne dérive pas parce qu'il n'est pas un modèle.

**Une session neuve**, qui porte un jugement sur ce que le script ne peut pas voir — sans
hériter du contexte qui a produit les fichiers. C'est la séparation entre celui qui génère et
celui qui vérifie, celle que la littérature réclame.

---

## Le script : `scripts/verifier.py`

**Ce qu'il vérifie, et rien d'autre :** ce qui casse réellement un lecteur.

- `00_MOI/` existe — sinon, dossiers numérotés présents ou pas, pour distinguer un renommage
  d'une absence
- les cinq fichiers existent et ne sont pas vides
- l'en-tête d'état du profil est intact, et les sections 4 et 6 existent
- chaque ligne de fait porte un marqueur et un mois
- aucune adresse mail, aucun numéro de téléphone dans `00_MOI/` — **bloquant**, c'est une
  donnée de tiers
- les lignes de plus de six mois
- `CLAUDE.md`, `.claude/skills/`, les dossiers du domaine
- la date du miroir

**Ce qu'il ne vérifie pas :** la qualité, le style, le sens. Un script qui juge le style
devient un tyran de format qui bloque sur une virgule.

**Trois sorties :** `OK`, `ATTENTION`, `BLOQUANT`. Il rapporte, il ne corrige jamais.

**Qui le lance, et quand.** Chaque outil de la mallette, en fin de course, juste après avoir
réécrit le tableau de bord — il est dans `.claude/skills/immo-init/scripts/`, donc dans le
dossier de tout le monde. Un `BLOQUANT` se dit à l'utilisateur en une phrase, sans le cacher
sous le plafond de remarques. Les `ATTENTION` vont dans la zone « à faire » du tableau de
bord, trois au plus, les plus anciennes d'abord.

**Dans Claude Code, il est réellement forcé.** Si l'utilisateur s'en sert — section 13 —,
l'init écrit `.claude/settings.json` avec un *hook* d'arrêt qui exécute le script à la fin de
chaque session, sans que personne le décide :

```json
{ "hooks": { "Stop": [ { "hooks": [ { "type": "command",
  "command": "python3 .claude/skills/immo-init/scripts/verifier.py ." } ] } ] } }
```

C'est la seule chose de tout le système qui soit forcée au sens strict. Dans Cowork, ça reste
une consigne de fin de course — mais une consigne qui tient parce qu'elle est mécanique et
courte.

**Sans `python3`, rien de tout ça ne tourne** — et sur le Windows d'un agent immobilier il
n'y est pas. Alors : on le dit une fois, en une phrase, on ne l'installe pas à sa place, et le
contrôle reste celui des listes de chaque outil. Le hook Claude Code ne s'écrit que si
`python3` répond ; sinon on ne l'écrit pas, un hook qui échoue à chaque arrêt est pire que pas
de hook. Sur le web, il n'y a pas de terminal : pas de script, et on ne le mentionne pas.

---

## La session neuve : `/immo-init audit`

**Quand.** Une fois par mois, avant le carnet du skill des réseaux — c'est lui qui l'appelle,
en une ligne, au lieu de porter l'audit lui-même. Ou quand l'utilisateur le demande. **Jamais
en fin d'une séance de production** : c'est précisément là que le jugement hérite de la
dérive.

**Il ne peut pas tourner en tâche planifiée**, parce qu'une tâche planifiée ne lit pas le
dossier local. C'est une limite, pas un choix. Une tâche planifiée peut seulement rappeler
de le lancer.

**Ce qu'il fait, dans l'ordre :**

1. **Lance le script**, et lit son rapport. Les bloquants d'abord.
2. **`voix.md` contre `publies/`.** Les cinq publications les plus récentes qu'il a
   effectivement publiées, contre les arbitrages et les interdits. Si ce qu'il publie
   contredit ce que le fichier dit de lui, **c'est le fichier qui est faux** — on propose la
   ligne, on ne l'impose pas.
3. **L'USP contre ce qui a marché.** Section 4 contre section 10 : les trois comportements
   ont-ils été montrés depuis le dernier audit, et ce qui a produit un contact les
   confirme-t-il ? Un comportement jamais montré en trois mois est une USP de papier.
4. **`cadre.md`, les cases encore vides.** Chaque `[à confirmer]` est une chose qu'aucun outil
   ne pourra faire. Les trois qui bloquent le plus, avec ce qu'elles bloquent.
5. **Les fiches clients contre les dossiers récents.** Une fiche qui n'a rencontré aucun
   dossier depuis trois mois, ou un dossier récent qui ne rentre dans aucune fiche.
6. **Le miroir et la mémoire.** Date du dernier miroir. Le pointeur mémoire, il le vérifie
   lui-même dans ses réglages — existe-t-il encore, dit-il vrai : version, outils, nom du
   projet — ; tu ne le lis que s'il te le demande. **Et ce que la mémoire a retenu
   toute seule** : depuis août 2026 elle se remplit pendant les conversations, sans passer par
   la mallette. Il ouvre ses réglages de mémoire et y cherche un nom de client, une adresse, un
   montant ; s'il en trouve, il les supprime lui-même. Tu ne les lis pas à voix haute.
7. **La signature, si `publies/` a grandi.** Remesure le registre publications avec
   `stylo.py profil` et compare à la carte en place. Un écart dit soit qu'il a changé, soit
   qu'un outil a dérivé et que ses publications portent la signature de l'outil. Les deux se
   disent ; aucun ne se corrige seul.

**Ce qu'il produit :** trois lignes au plus dans la zone « à faire » du tableau de bord,
classées par ce qui bloque, et un paragraphe dans la conversation. **Pas un rapport.** Un
audit qui produit une page est un audit qu'on ne lit pas.

**Ce qu'il ne fait jamais :** modifier `00_MOI/`. Il propose des lignes, comme tout outil. Un
audit qui corrige seul est un outil qui réécrit la vérité sans témoin.

---

## Ce que ni l'un ni l'autre ne traite

**La dérive de complaisance** — le modèle qui va vers ce que l'utilisateur veut entendre. Un
script ne la voit pas, et une session neuve la porte aussi. Son seul remède est dans la
posture de chaque outil : le niveau 1 annonce ses choix pour être contredit, le test de la
négation force un autre chemin, et la correction de l'utilisateur est capturée après chaque
livraison par les outils de production.
C'est distribué, et ça doit le rester.

**La dérive dans la session** — l'instruction longue qu'on cesse de suivre. Son remède est
déjà là : le plan déclaré au panneau de progression, les listes de contrôle courtes, et le
fait que la livraison a une forme qui ne peut être produite qu'en ayant fait le contrôle.

On n'ajoute pas de couche par-dessus. **Une couche de plus est une dérive de plus.**
