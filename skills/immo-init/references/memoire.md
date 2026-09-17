# La mémoire du compte — auditer et imprimer

La mémoire suit l'utilisateur d'une session à l'autre et d'une surface à l'autre, sans
dépendre d'un dossier connecté. C'est utile, et c'est exactement pour ça qu'il faut y mettre
très peu de choses.

**Règle qui gouverne tout ce fichier : la mémoire est redondante, jamais porteuse.** Si elle
est inactive, l'init se déroule entièrement. Rien dans la mallette ne cesse de fonctionner.

---

## En entrée — l'audit

**À sa demande seulement.** Tu ne lis pas la mémoire de son compte de ta propre initiative. S'il te
demande de partir de ce qu'elle sait de lui, c'est au tout début de l'enquête ; sinon, l'init se
déroule entièrement sans elle.

Lis alors ce qu'elle contient déjà sur lui. C'est de la matière brute, déjà écrite, sans
coût. Elle donne souvent l'identité, le métier, les préférences stabilisées. Prends-la telle
quelle et marque `[dit]`.

**Trois choses à repérer.**

**Ce qui est juste et utile** → tu le reportes dans le profil, marqué `[dit]`.

**Ce qui contredit ce que l'enquête trouve** → tu ne tranches pas tout seul. Tu montres les
deux et tu demandes :

> Ta mémoire dit que tu es chez [X]. Dans tes fichiers récents je vois plutôt [Y]. C'est quoi
> aujourd'hui ?

Une contradiction n'est jamais résolue silencieusement, ni dans un sens ni dans l'autre.

**Ce qui n'a rien à y faire** → une ligne sur sa santé, sa situation familiale, ses opinions,
ses finances personnelles. Tu ne la recopies nulle part. Tu peux le lui signaler une fois, en
une phrase neutre, et lui dire qu'il peut la supprimer lui-même. Tu n'insistes pas et tu ne
commentes pas le contenu.

**Si la mémoire est vide ou inactive**, ce n'est pas un échec : note l'état en section 13 du
profil, dis en une phrase ce que ça lui coûte — pas de continuité entre les sessions — et
passe à la source suivante. N'attends pas qu'il l'active.

---

## En sortie — l'impression

À l'étape 9, une fois le profil rempli et validé — et rien ne s'écrit sans son accord explicite.

### Ce qu'on écrit

Le pointeur, jamais le contenu. **Six lignes maximum.**

```
- Agent immobilier, [statut] — exerce sous le nom [nom d'exercice, s'il diffère du sien]
- Travaille avec la mallette immo, init [x.y], installée le [date]
- Son profil, sa voix, son cadre et ses clients types vivent dans ses fichiers : le dossier du projet « [nom] » sur son ordinateur, et une copie datée dans ce projet pour son téléphone
- Ses outils : /immo-annonce pour une annonce, /immo-reseaux-sociaux pour un post ou son carnet, /immo-parcours pour ses clients et son parcours, /immo-init pour son profil — installée en plugin, le menu « / » peut les préfixer
- Avant toute production pour lui, relire ces fichiers plutôt que redemander ; ne jamais inventer un chiffre, une surface ni une date
- Il ne veut rien de ses clients retenu sur lui — ni nom, ni adresse, ni montant
```

### Ce qu'on n'écrit pas

Ses règles de voix, ses objections, ses récurrences, ses chiffres, son secteur détaillé.
**Aucun chemin de dossier** : la mémoire le suit sur son téléphone, où ce chemin n'existe pas —
c'est la règle des instructions du projet, elle vaut ici.
Tout ça vit dans les fichiers, change souvent, et se relit à chaque fois. Une mémoire qui
double les fichiers devient une mémoire fausse dès la première correction qu'il fait à la
main dans `profil.md`.

Et rien, jamais, de ce que les règles non négociables de la skill interdisent. La règle vaut
doublement ici : un fichier, il l'ouvre et le relit ; la mémoire, il l'oublie.

### Où on l'écrit — le piège du cloisonnement

La mémoire d'un projet est **scopée à ce projet** : ce que Claude y apprend ne se transmet
pas aux autres. Les six lignes de pointeur ne servent que si elles sont disponibles partout.

Donc fais-les écrire **depuis une conversation hors projet**. Dis-le-lui explicitement : il
ne le devinera pas, et c'est exactement le genre de détail qui fait qu'une installation
marche en salle et plus jamais après.

### Comment on l'écrit

**Tu ne l'écris pas de ta propre initiative.** Tu affiches les lignes exactes, telles qu'elles
seront retenues, et tu demandes :

> Voilà les six lignes que je te propose de retenir durablement sur toi, pour ne pas avoir à
> tout redemander à chaque fois. Tu valides, tu corriges, ou on n'en garde aucune ?

C'est sa validation qui déclenche l'écriture. Ce détour n'est pas une contrainte : c'est le
moment où il voit exactement ce qui est retenu sur lui, et c'est un des meilleurs moments de
la séance.

S'il refuse, tu n'écris rien et tu ne le redemandes pas. La mallette fonctionne sans.

---

## Ce que les outils de production en font

Rien, de leur propre initiative : **les outils ne lisent pas la mémoire du compte**, les fichiers
font foi.

**S'il dit lui-même que la mallette est installée** alors que son profil n'est pas lisible ici,
l'outil le croit : il ne propose pas `/immo-init` — il ferait naître
un second profil — : il dit que le profil est sur l'ordinateur, produit avec ce qu'il a, et
propose de déposer le miroir. C'est écrit dans chaque outil, au paragraphe « Et si le profil
n'est pas là ».

**Le pointeur sert Claude hors de la mallette.** Quand aucun outil ne se déclenche, la mémoire du
compte — que Claude utilise de lui-même, selon les réglages de l'utilisateur — peut lui rappeler
les bonnes commandes. La mallette, elle, n'y lit rien, sauf si l'utilisateur le demande.

## Ce que la mémoire fait sans la mallette

Depuis août 2026, la mémoire du compte est commune au chat et à Cowork, elle se remplit pendant
les conversations — plus seulement à la fin — et elle se consulte, se corrige et se supprime
dans les réglages. Deux conséquences.

**Elle peut retenir ce que la mallette refuse d'écrire** : un nom de client dit en passant, un
montant. La mallette ne peut pas l'en empêcher ; l'audit mensuel le fait chercher
(`audit.md`, point 6).

**Elle n'est pas la même partout.** La mémoire d'un projet reste dans ce projet. Celle d'une
tâche Cowork qui a tourné seulement sur l'ordinateur reste avec cette tâche. Et Claude Code
s'appuie sur ses fichiers `CLAUDE.md`, relus à chaque ouverture — la mémoire la plus prévisible
des trois, d'où les trois lignes de `~/.claude/CLAUDE.md` (`projet-cowork.md`).

## Consigner

L'écriture en mémoire ne laisse aucune trace dans les fichiers. Consigne-la dans l'en-tête
d'état de `profil.md` : date, ou « refusée », ou « mémoire inactive ». Les trois sont des
résultats, l'absence de mention n'en est pas un.

## En mise à jour

Quand l'init est relancé sur un profil existant, l'étape mémoire ne réécrit pas tout. Elle
compare, montre ce qui a changé, et ne propose que le delta. Une ligne périmée se corrige,
elle ne s'empile pas à côté de la nouvelle.
