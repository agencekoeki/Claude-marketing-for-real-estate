# Contrôler avant de livrer

Une passe, dix-neuf points, dans cet ordre. Elle prend trente secondes et elle évite les deux
seules erreurs qui coûtent vraiment : le hors-cadre et le chiffre faux.

**Cette passe est entière à tous les niveaux.** C'est le niveau qui décide de ce qu'on demande
à l'utilisateur et de ce qu'on prescrit sur la forme, jamais de ce qu'on vérifie avant de
livrer.

---

## 0. Retourne tes propres affirmations

**Avant de vérifier quoi que ce soit d'autre, interroge ton propre texte.** Reprends chaque
affirmation et pose-lui une seule question : **sur quoi repose-t-elle ?**

- « le quartier est recherché » → sur quoi ? Si la réponse est « ça se dit », ça sort.
- « les délais s'allongent » → sur quoi ? Sans un chiffre à lui avec sa date, ça sort.
- « les acquéreurs cherchent surtout X » → sur quoi ? Si ce n'est pas dans une fiche client,
  ça sort.

Trois réponses sont recevables : un fait qu'il t'a donné, une ligne d'un fichier de `00_MOI/`,
ou une source datée. **Toute autre réponse fait tomber l'affirmation.**

Puis, sur celles qui restent, **le test de la négation** : écris l'affirmation contraire et
donne-lui sa meilleure raison. Si les deux tiennent aussi bien, ce n'est pas un constat, c'est
une opinion — on la retire, ou on l'écrit à la première personne. La méthode complète est dans
`eprouver.md`.

Cette passe est invisible pour lui et elle prend vingt secondes. Elle attrape ce que tous
les points suivants ne voient pas : une phrase qui sonne juste et ne repose sur rien.

## 1. Les faits

Chaque chiffre, chaque surface, chaque date, chaque caractéristique du bien vient-il de
`01_BIENS/` ou de ce qu'il t'a dit ?

**Tout ce qui ne vient pas de là n'existe pas.** Si une information manque, laisse un blanc
visible dans le texte — `[surface à compléter]` — et signale-le : c'est le rang 1 de
`livrer.md`, celui qui passe toujours. Ne comble jamais,
même par une approximation prudente.

## 2. Ce qui vient d'une page

Si une page a servi de matière : chaque fait qui en vient porte-t-il sa source et sa date ?
Aucun texte, aucune tournure et aucune photo n'en a-t-il été repris ? Et le texte prend-il un
angle que la page ne prenait pas, plutôt que de la reformuler ?

S'il s'agissait de l'annonce d'un tiers, on ne publie pas — voir `depuis-une-page.md`.

## 3. Le cadre

Relis `00_MOI/cadre.md`, section publication en ligne. Trois questions :

- ce texte est-il de ceux qu'il a le droit de publier lui-même ?
- les mentions obligatoires de son métier y figurent-elles, ou la case est-elle
  `[à confirmer]` — auquel cas tu laisses un blanc visible et tu le dis ?
- les photos évoquées sont-elles diffusables, et avec quelle autorisation ?

**Une case `[à confirmer]` ne se comble pas par du bon sens.** C'est la règle de l'init et
elle tient ici.

## 4. Les tiers

Aucun nom de client, aucune adresse exacte, aucun montant de transaction, aucun motif de
vente personnel. Même s'il te les a donnés pour le contexte, ils ne vont ni dans le texte ni
dans le brouillon enregistré.

Un bien identifiable par recoupement compte comme une adresse.

## 5. Sa voix

Relis le texte contre les interdits de `voix.md` — les siens et les formules saturées de sa
zone. Puis vérifie la longueur, le tutoiement, l'emoji, la clôture contre ses arbitrages.

## 6. La cible

Une seule fiche client, et le texte lui parle. Si en relisant tu vois qu'il s'adresse aux
deux côtés, c'est raté : reprends l'angle, pas les phrases.

Puis quatre vérifications tirées de `cible.md`, qui distinguent un texte écrit *pour* une
fiche d'un texte écrit *à côté* :

- l'accroche touche-t-elle le **déclencheur**, ou seulement le sujet ?
- l'objection traitée est-elle celle de la fiche, et n'y en a-t-il qu'une ?
- la preuve finale est-elle le **levier documenté**, avec son fait ?
- rien du champ « ce qui le fait fuir » n'a-t-il glissé dans le texte ?

Et deux interdits : **la fiche n'est jamais nommée** — pas de « chers primo-accédants » — et
**la personne n'est jamais décrite**, seulement ce qu'elle vit.

## 7. L'USP

Si la section 4 de son profil porte une USP : ce texte contredit-il un de ses trois
comportements ? Traite-t-il un sujet qu'elle exclut ? Une USP contredite une fois sur deux
se démonte en public.

Et vérifie qu'il ne s'annonce pas : on ne publie pas son USP, on le démontre.

## 8. Le transfert

À qui, concrètement, le lecteur enverrait-il ce texte, et qu'écrirait-il en l'envoyant ? Si tu
ne peux pas répondre, il est lisible mais il ne circulera pas — et sur les plateformes
d'image, c'est le signal qui ouvre l'accès aux gens qui ne le suivent pas.

Ça se corrige en visant plus précisément, jamais en ajoutant « partagez ».

## 9. La signature de l'outil

Sept vérifications mécaniques, dix secondes :

- **aucun tiret cadratin** : c'est le marqueur le plus discriminant, et il désigne le modèle
  qui écrit plus que l'IA en général
- **aucune parallélisme négative** — « ce n'est pas X, c'est Y » —, aucun triplet, aucune
  phrase miroir
- aucune espace insécable avant `: ; ! ?`, guillemets droits — sauf s'il écrit lui-même
  comme ça
- aucune tournure de la liste : « il est important de noter », « en conclusion », « de plus »,
  « en outre », « par conséquent », « n'hésitez pas à », « dans un monde où »
- aucun anglicisme traduit : « faire du sens », « adresser un problème », « impacter »
- au moins une aspérité — une tournure familière, un mot de son glossaire, une phrase qui
  n'est pas parfaitement équilibrée
- aucune phrase qu'il a écrite ou corrigée n'a été relissée

**Puis la mesure, si `voix.md` porte une signature mesurée :** écris le brouillon dans un
fichier temporaire et lance `.claude/skills/immo-init/scripts/stylo.py compare <brouillon>
00_MOI/voix.md --registre publications` — sinon `--registre "messages à Claude"`, sinon sans
registre. Ce qu'il rend est un signal externe — la seule chose qui ne dérive pas quand
on juge la voix. Une phrase trop régulière, un tiret cadratin qu'il ne met jamais, un mot
qu'il emploie sans arrêt et que le brouillon n'a pas : tu corriges avant de livrer. Si
`voix.md` n'a pas de signature, le script le dit et tu passes.

Le détail et le fondement sont dans `signature-ia.md`. Rappel de l'ordre de priorité : ses
échantillons portent la voix, la suppression des tics vient ensuite, la typographie en
dernier.

## 10. Le rythme

Quatre vérifications qui se font à l'œil, en dix secondes, et qui ne dépendent d'aucun goût :

- trois phrases d'affilée de longueur comparable → casse la série
- un connecteur logique en tête de paragraphe → supprime-le, le lien tient sans lui
- le même nom répété trois fois dans un texte court → substitue
- le même registre du début à la fin → varie quelque part

## 11. La coupe

L'accroche tient-elle entièrement avant la pliure ? Une accroche coupée au milieu est pire
qu'une accroche courte. Et rien d'essentiel — une date, une information pratique, une mention
obligatoire — ne doit se trouver au-dessous. L'appel à l'action, lui, a le droit d'y être :
il s'adresse à ceux qui ont déjà décidé de lire.

Voir `apercu.md` pour les seuils, et la règle qui va avec : on calibre sur la lecture mobile,
la plus serrée.

## 12. Le visuel est faisable

Le temps demandé par le visuel tient-il dans son rythme réel ? Une vidéo proposée à quelqu'un
qui n'a pas quarante-cinq minutes cette semaine ne sera pas tournée, et la publication
entière restera en
brouillon.

Vérifie aussi le rapport d'image — vertical ou carré, jamais paysage — et, s'il y a du texte
sur l'image, qu'il est loin des bords.

## 13. La cohérence graphique

Si un visuel accompagne le texte : porte-t-il ses deux couleurs et son bloc de signature — nom
et commune, en bas ? Et respecte-t-il ce que son réseau impose, si `cadre.md` le dit ?

Un visuel aux couleurs par défaut n'est pas une faute. C'est le rang 7 de `livrer.md`, et il
ne passe le plafond que si rien de plus urgent n'attend.

S'il s'agit d'un carrousel ou d'un visuel fabriqué, le moteur a déjà rendu son rapport : aucun
BLOQUANT ne passe. Puis la liste fermée en fin de `carrousels.md` : la couverture promet sans
expliquer, cinq à huit diapos, trois variantes au maximum, la vignette se lit, le pied est
identique partout.

**Et reprend-il une de ses compositions récurrentes ?** On reconnaît quelqu'un à une forme
répétée, pas à une palette : un visuel d'une forme nouvelle à chaque fois n'installe rien.

Son visage n'apparaît que sur ce qui parle de lui, jamais sur un tableau, une chronologie ou
un chiffre isolé, où il vole l'attention de l'information.

## 14. L'honnêteté de l'image

Si une image a été générée ou retouchée : **modifie-t-elle ce que l'acquéreur croit acheter ?**
Un défaut effacé, une vue changée, un ciel remplacé, un élément du bâti ajouté ou retiré : on
ne livre pas.

Un ameublement virtuel est acceptable **s'il est annoncé sur l'image elle-même**, pas dans une
mention en bas du texte.

Sur une image générée, vérifie aussi le rendu maison : dominante jaune, composition trop
centrée, tout trop neuf et trop propre. Si c'est là, le prompt n'a pas été neutralisé — voir
`outils-image.md`.

Et si un texte figure sur une image générée, relis-le lettre par lettre : c'est ce qui rate le
plus souvent.

**Une image générée ou retouchée est traçable.** Les générateurs des deux grandes familles y
embarquent une marque invisible, et des applications grand public savent la lire — certaines
indiquent même quelle portion de l'image est marquée, donc une retouche partielle se repère.
Voir `signature-ia.md`. Ce n'est pas un argument moral, c'est un argument de risque.

## 15. La mise en forme

Quatre vérifications à l'œil, dix secondes : une idée par ligne, du blanc entre les idées,
l'accroche isolée, aucun bloc de plus de quatre lignes. Voir `mise-en-forme.md`.

Et si un visuel accompagne le texte : une seule idée, le message en haut, lisible en
vignette, six lignes de contenu au maximum, carré ou portrait, et sa source visible si un
chiffre y figure. Voir `mises-en-page.md`.

## 16. Le livrable correspond au format

Le format annoncé et ce que tu rends se répondent-ils ? Un carrousel promis et un texte livré,
une vidéo annoncée et un script rendu sans le dire : c'est là que la confiance se perd.

La table est dans `plateformes.md`. Dis ce qu'il lui reste à faire — téléverser, filmer,
saisir — en une ligne, à la fin.

## 16 ter. Si le visuel le montre, lui

Le second consentement de `cadre.md` est un oui. La photo ou le personnage vient de
`03_RESSOURCES/`, nommé par son fichier. Le prompt interdit de modifier le visage, ou
demande le personnage à l'identique. Aucune scène réaliste de lui. Le geste « joins, puis
colle » est écrit. La mention de `cadre.md` est dans le texte du post.

## 16 bis. Si c'est un short

Cent mots au plus, une idée, l'accroche sans « bonjour », des lignes de dix mots, une fin
qu'on peut dire en regardant l'objectif. Comparé au registre oral s'il existe, pas à l'écrit.
Et aucune consigne sur la façon d'être : le prompteur est dans ses mots, le reste est lui.

## 17. Le kit est complet

Le texte seul n'est pas un livrable. Vérifie que le brouillon porte aussi le plan de prise de
vue — combien de photos, laquelle en premier, dans quel ordre, ce qu'il ne faut pas montrer —
et la plateforme visée.

Si l'angle ne demande aucune image, dis-le explicitement plutôt que de laisser un vide : un
vide se lit comme un oubli.

## 18. Le doublon

Dernier passage sur `publies/`. Le texte que tu viens d'écrire ressemble-t-il à quelque chose
de sorti ces trois derniers mois ?

---

## Ce qui est rédhibitoire

Cinq choses. Si l'une est présente, **tu ne livres pas** — tu dis ce qui manque et tu
attends.

- un chiffre ou un fait que tu ne peux pas sourcer
- un texte, une tournure ou une photo repris d'une page qui n'est pas la sienne
- une image qui modifie ce que l'acquéreur croit acheter
- une mention obligatoire absente alors que le cadre la désigne
- une donnée qui identifie un tiers

Le reste se corrige avec lui, en direct.

---

## Quand il dit « c'est nul, refais »

Sans indication, ça ne veut rien dire, et redemander « qu'est-ce qui ne va pas ? » n'obtient
généralement rien de plus.

**Propose deux hypothèses tirées du texte**, comme partout ailleurs : « c'est le ton, ou c'est
le sujet ? » Il désigne, et tu as l'information.

**S'il ne désigne rien**, réécris une fois en changeant **une seule chose** — le plus souvent
l'accroche, parce que c'est ce qu'on lit en premier et ce qu'on juge. Dis laquelle tu as
changée.

**S'il rejette la deuxième aussi**, arrête. Garde les deux versions en brouillon, propose de
reprendre plus tard, et note dans `voix.md` ce qu'il a refusé deux fois : deux refus font une
préférence, c'est la règle d'`apres.md`.

Ne t'excuse pas, ne demande pas d'explications, ne produis pas une troisième version dans la
foulée. Un texte rejeté deux fois est un signe que la fiche ou l'angle sont faux, pas que
l'écriture est mauvaise.

---

## Comment tu livres

**Pas ici.** `livrer.md` possède la sortie : la forme, le plafond de remarques, la question
finale. Le contrôle dit ce qui est juste, il ne dit pas ce qui s'affiche.

Une seule chose à retenir en sortant d'ici : **ce que tu as trouvé pendant cette passe ne
devient pas automatiquement une remarque.** Un blanc à compléter, oui. Le reste passe par le
classement de `livrer.md`, et ce qui n'entre pas dans le plafond va dans le kit enregistré.
