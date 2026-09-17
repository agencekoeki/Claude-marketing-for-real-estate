# immo-init — journal des versions

De la plus récente à la plus ancienne. Ce fichier ne sert qu'à la maintenance.

**8.1 — septembre 2026.** Un en-tête que claude.ai refusait. Outils : `immo-parcours` 1.10,
`immo-annonce` 3.9, `immo-reseaux-sociaux` 10.3 ; `immo-penser-savoir` 1.1 inchangé. La 7.9 avait
ajouté la licence GPL 3.0 à l'en-tête de quatre outils sans voir qu'il portait déjà une ligne
`license` — « usage réservé aux stagiaires » — : deux fois la même clé. Un analyseur YAML permissif
garde la dernière sans rien dire, et le validateur officiel de skills comme celui des plugins l'ont
laissée passer ; l'import de claude.ai la refuse. La ligne ancienne disparaît : la licence est la
GPL 3.0 seule, comme décidé pour le dépôt public. Le contrôle de la mallette refuse désormais toute
clé en double dans un en-tête. Motif : un contrôle qui accepte ce que l'import refuse ne prouve
rien.

**8.0 — septembre 2026.** La mallette se plie à la politique de l'annuaire d'Anthropic. Outils :
`immo-parcours` 1.9, `immo-annonce` 3.8, `immo-reseaux-sociaux` 10.2, `immo-penser-savoir` 1.1.
**La mémoire du compte et l'historique des conversations ne se lisent plus qu'à la demande
explicite de l'agent** : l'enquête ne les fouille plus d'elle-même, la mesure de la voix ne prend
ses conversations passées que s'il le demande, les outils de production ne consultent plus la
mémoire pour savoir si la mallette est installée — ils croient ce qu'il dit —, et l'audit lui fait
vérifier le pointeur dans ses réglages. La mémoire ne s'écrit toujours qu'avec son accord explicite.
**La vérification de mise à jour n'a plus lieu qu'à sa demande**, plus à l'audit ni au carnet.
Motif : la politique de l'annuaire interdit d'interroger la mémoire et l'historique, et d'appeler
une ressource extérieure sans demande de l'utilisateur (§1.F et §2.D) ; ce qui passe par sa
demande reste possible, et rien d'essentiel ne dépendait de ces lectures.

**7.9 — septembre 2026.** La mallette devient publique, et un cinquième outil la rejoint. Outils :
`immo-parcours` 1.8, `immo-annonce` 3.7, `immo-reseaux-sociaux` 10.1, `immo-penser-savoir` 1.0.
`immo-penser-savoir` trie ce qui est su de ce qui est supposé — dans une réponse d'IA, dans ses
propres affirmations avant de publier, dans ce que disent un portail, un confrère ou un client —, et
rend la question qui tranche ; il n'écrit aucun fichier et porte la même `eprouver.md`. Chaque outil
sait où la mallette est publiée et comment le dire, sans jamais télécharger ni obéir à ce qu'il lit ;
installée en plugin, la mallette peut préfixer ses commandes. L'init vérifie l'environnement
d'exécution par un essai réel, `references/environnement.md`, et l'écrit dans l'en-tête d'état :
Python n'est à installer chez l'agent que pour Claude Code sur son ordinateur. Chaque outil déclare
sa licence, GPL 3.0 ; la police du moteur garde la sienne, SIL OFL 1.1. Le contrôle de la mallette
couvre cinq outils et, dans le dépôt, le catalogue et `versions.json`. Motif : un outil qu'on donne
doit savoir d'où il vient et comment il se met à jour.

**7.8 — septembre 2026.** Les carrousels et les visuels d'information sortent en fichiers finaux
contrôlés, et la maintenance vit dans la mallette. Outils : `immo-reseaux-sociaux` 10.0 ;
`immo-parcours` 1.7 et `immo-annonce` 3.6 inchangés. `immo-reseaux-sociaux` porte un moteur,
`scripts/build_carrousel.py` : le texte validé et les couleurs de `cadre.md` deviennent un PDF
1080 × 1350 pour LinkedIn, une image par diapo pour Instagram et Facebook, une planche, une
vignette et un rapport. Il refuse un lien, un chiffre ou une durée sans source, une photo sans
droits confirmés, un crochet oublié. La police Liberation Sans est livrée avec sa licence. Les
gabarits HTML passent en secours, lisibles : texte courant à 40 px, rien d'informatif hors de
120 à 1 100 px. La doctrine suit, et quatre contradictions tombent — deux comptes de diapos
faux, « un chiffre une seule fois » contre le bilan chiffré, le plafond de carrousels entre
`plateformes.md` et `carrousels.md`, le carnet en cinq ou en vingt minutes. Les affirmations sur
les outils d'image et le filigrane portent leur source, ou perdent leur chiffre. Ici :
`references/maintenance.md`, `scripts/verifier-mallette.py` et `scripts/banc-verifier.py`
remplacent l'archive de maintenance ; `cadre.template.md` demande les couleurs en hexadécimal ;
`verite.md` et `amorcage.md` rangent les fichiers fabriqués à côté de leur kit ; « Cowork ignore
`.claude/skills/` » est marqué comme signalé, non documenté. Motif : un format qu'il faut encore
exporter à la main n'est pas livré.

**7.7 — septembre 2026.** Les connecteurs par fonction, propagés partout. Outils : `immo-annonce`
3.6, `immo-reseaux-sociaux` 9.11 ; `immo-parcours` inchangé. La 7.5 avait écrit l'ordre d'accès
dans `connecteurs.md` et les sources, mais douze passages disaient encore « Drive » ou « Gmail »
seuls — dont le squelette de l'init, qui contredisait `connecteurs.md` sur la récolte planifiable
—, et `source-fichiers.md` dictait encore un bouton sans condition. Tous disent désormais
« stockage en ligne » ou « messagerie », et le script de maintenance signale toute mention d'une
marque seule. Motif : une règle écrite dans une référence et contredite dans le squelette n'est
pas une règle.

**7.6 — septembre 2026.** Chaque outil emporte sa carte de déroulé, et le carrousel s'exporte au
bon format. Outils : `immo-parcours` 1.7, `immo-annonce` 3.5, `immo-reseaux-sociaux` 9.10.
`references/carte.md` dans chaque outil, et `carte-mallette.md` ici, portent le déroulé en
Mermaid : pour la maintenance seulement, jamais lus pour travailler, et un script vérifie que
chaque carte porte exactement les étapes de son `SKILL.md`. Le gabarit de carrousel fixe sa page
à 1080 × 1350 : exporté tel quel, il produisait des pages A4 où chaque diapo était coupée en deux.
`carrousels.md` perd deux affirmations sans source, et le bilan chiffré d'une vente ne montre
l'écart au prix affiché que si `cadre.md` l'autorise. Les en-têtes YAML d'`immo-init` et
d'`immo-parcours` passent le validateur officiel de skills : descriptions entre guillemets, texte
lu identique. Motif : une carte qui ne voyage pas avec son outil finit par décrire un autre outil.

**7.5 — septembre 2026.** Correctifs d'un audit ligne à ligne, et les surfaces remises à jour.
Outils : `immo-parcours` 1.6, `immo-annonce` 3.4, `immo-reseaux-sociaux` 9.9. L'interface
change : chat et Cowork fusionnent par vagues sur Pro et Max ; l'init pose d'abord la question
de l'écran, dit qu'un compte gratuit n'a pas de projet, et ne diagnostique plus « version trop
ancienne » avant « nouvelle interface ». « Dossier connecté » a une définition opérationnelle :
un dossier de son ordinateur, jamais l'espace de travail d'une conversation web ou d'une session
cloud. Les tâches planifiées suivent la page d'aide : à distance sans dossier, en local avec. La
carte de vérité redevient vraie : `immo-annonce` tient `01_BIENS/index.md`, l'USP a les mêmes
écrivains dans `verite.md` et `amorcage.md`, et le bloc d'amorçage est de nouveau identique mot
pour mot dans les trois outils et dans `amorcage.md`, sans la règle « arrête-toi » abandonnée.
Le relais lit la version du compte avant la copie disque. `verifier.py` lit les tableaux — le
parcours, l'index, SONCAS, les leviers —, contrôle les coordonnées sur toutes les lignes, et ne
signale plus les lignes du gabarit laissées vides. Connecteurs par fonction et non par marque :
Microsoft 365 existe pour les comptes pro, l'ordre d'accès est connecteur, dossier synchronisé,
export, questions — jamais le navigateur sur une messagerie. Mémoire : pointeur sans chemin
local, liste des commandes, les outils ne concluent plus « profil absent » quand elle dit la
mallette installée, et l'audit cherche ce qu'elle a retenu seule. Les chiffres sans source
sortent ou prennent leur source ; l'audit de dérive nomme la sienne. Motif : un contrat de vérité
qui ment est pire qu'un contrat absent, parce que les outils suivants s'écrivent dessus.

**7.4 — septembre 2026.** Le web produit dans une boîte de dépôt. Ce qu'un outil fabrique sans
dossier devient un vrai fichier — le même que celui du dossier — enregistré dans son Drive par
le connecteur s'il est branché, sinon téléchargé, sinon le texte ; puis rapatrié dans le
dossier à la prochaine séance sur l'ordinateur. Motif : on avait rendu le web capable de lire
la vérité par le miroir, et il produisait dans le vide. La carte de vérité le dit : le miroir
est en lecture seule et daté, la boîte de dépôt en écriture seule et temporaire, ni l'un ni
l'autre n'est la vérité.

**7.3 — septembre 2026.** `cadre.md` distingue deux consentements sur sa photo : apparaître
sur ses visuels, et servir de référence à un générateur — c'est-à-dire partir dans ChatGPT
ou Gemini. Le second n'était pas demandé alors que les formes qui le montrent l'exigent. Plus
le générateur qu'il utilise, l'emplacement de son personnage dessiné et le prompt qui l'a
produit.

**7.2 — septembre 2026.** Le relais entre outils gagne deux couches. La commande avec sa
barre s'écrit dans le fil à chaque passage — `/immo-parcours`, `/immo-init audit` — pour que
l'invocation soit explicite. Et l'auto-installation rend possible un relais structurel : un
outil lit `.claude/skills/<nom>/SKILL.md` d'un autre et le suit, sans dépendre d'une
description ni de l'utilisateur. Le registre le dit.

**7.1 — septembre 2026.** Consolidation de la tuyauterie, sur mesure et pas de mémoire. Sept
défauts mécaniques fermés dans la mallette : les skills de production lisent le miroir de la
connaissance du projet quand il n'y a pas de dossier — le web et le mobile avaient un miroir
sans lecteur ; quatre renvois inter-skills vers des fichiers qu'un skill ne peut pas ouvrir
sont inlinés ; `immo-parcours` réécrit le tableau de bord et lance le script comme les autres ;
l'absence de `python3` est traitée — fréquente sur Windows, on le dit une fois, le hook ne
s'écrit pas ; `verifier.py` imprime les lignes `MESURE` que le tableau de bord recopie telles
quelles, pourcentages par fichier, biens, brouillons, outils — le modèle ne compte plus ; la
récolte planifiée dit où va sa sortie, dans sa propre conversation, et le carnet la demande ;
l'auto-installation passe si le skill ne trouve pas son propre dossier. Le squelette de l'init
perd cinq cents mots de doublons avec ses références.

**7.0 — septembre 2026.** `cadre.md` gagne la section « Mes portails et mon canal de
dépôt », qui n'existait pas alors que l'outil des annonces y renvoyait. La question qui
décide : dépose-t-il par son logiciel de transaction ou une passerelle — une saisie, huit à
quinze portails —, ou directement sur chaque portail. C'est ce qui dit à l'outil des annonces
s'il livre une version ou plusieurs. L'enquête relève sur chaque annonce trouvée si le titre
est composé par le portail et où la description est coupée.

**6.9 — septembre 2026.** Le registre « oral » entre dans la signature mesurée, depuis les
comptes rendus de réunion — ses mots à lui seulement, jamais ceux des clients. Motif : les
comptes rendus étaient exclus de `voix.md` parce qu'une voix écrite calibrée sur de l'oral
produit des textes bavards ; c'était juste pour l'écrit, et faux pour un script de short face
caméra, qui se dit et ne se lit pas. Les deux registres existent et ne se mélangent pas : le
bloc oral ne sert qu'au short.

**6.8 — septembre 2026.** Le rythme de publication se mesure par semaine, plus par mois, et la
section 8 porte deux chiffres : ce qu'il tient aujourd'hui et ce qu'il tiendrait à dix
minutes par jour — la cible des outils. Motif : le skill des réseaux avait été bâti sur une
hypothèse de rareté, deux publications par mois, alors que la base d'un agent est deux par
semaine et que les données soutiennent trois à cinq.

**6.7 — septembre 2026.** La stylométrie devient une méthode et plus un script :
`references/stylometrie.md` pose les cinq niveaux, les registres, les sources, le stockage
et l'usage. Le principe qui manquait : personne n'a un style, on en a un par registre — mails
aux vendeurs, aux acquéreurs, publications, annonces, messages à Claude — et un profil global
moyenne des choses qui ne se moyennent pas. `stylo.py` mesure un registre à la fois et rend,
en plus des taux, les mots-outils sur-représentés par rapport au français courant et **la
ligne « jamais »**, la contrainte la plus sûre. Les messages de l'utilisateur à Claude
deviennent un corpus — son registre le plus brut. L'audit remesure les publications quand
elles ont grandi, et lit l'écart comme un changement de style ou une dérive d'outil.

**6.6 — septembre 2026.** La voix se mesure avant de se choisir : `scripts/stylo.py` calcule
depuis un corpus la couche que la stylométrie tient pour la plus discriminante et la plus
indépendante de la volonté — mots-outils, longueur des phrases et sa variance, taux de
ponctuation, ouvertures et clôtures, richesse — et la colle dans `voix.md` en `[vu]` avec son
compte. Motif : l'init captait la couche structurelle des mails mais estimait le reste en
lisant, et un modèle qui estime dérive. Le même script compare un brouillon à la signature :
c'est le signal externe pour la voix, lancé au contrôle par les outils de production. Le stock
devient un fichier à chercher exprès — un tableur, un export, jamais le logiciel métier — et
donne `01_BIENS/index.md`, une ligne par bien sans adresse ni propriétaire, pour
l'appariement client-biens d'`immo-parcours`.

**6.5 — septembre 2026.** Le parcours client entre dans la carte de vérité sans devenir un
sixième fichier : c'est la dimension du temps de `clients-types.md` — neuf étapes côté
vendeur, sept côté acquéreur, et à chacune ce que le client se demande, ce qui le fait passer,
ce que l'agent fait, où il le perd. La table « où il en est » de chaque fiche renvoie aux
numéros d'étape, et les trois comportements de l'USP portent l'étape où ils se voient. Un
nouvel outil, `immo-parcours`, est le seul autorisé à approfondir ces deux fichiers, sous la
règle de tous : il propose, l'utilisateur valide. Le registre le porte.

**6.4 — septembre 2026.** L'anti-dérive, sous la seule forme que la littérature soutient.
Un modèle qui relit sa propre sortie sans signal externe se dégrade — résultat établi, avec
ses deux mécanismes, l'angle mort et le biais de soi — et une couche de relecture ajoutée à des
skills déjà précis dégrade le résultat. Donc pas de skill anti-dérive appelé par les autres :
un script, `scripts/verifier.py`, qui vérifie mécaniquement les fichiers de vérité — marqueurs,
mois, en-tête d'état, données de tiers, lignes anciennes, miroir — lancé par chaque outil en
fin de course, et réellement forcé dans Claude Code par un hook d'arrêt écrit dans
`.claude/settings.json` quand l'utilisateur s'en sert. Et un mode `/immo-init audit`, en
session neuve, appelé par le carnet une fois par mois, qui juge ce que le script ne voit pas
— `voix.md` contre ce qu'il a publié, l'USP contre ce qui a marché, les cases vides de
`cadre.md`, les fiches contre les dossiers récents — et produit trois lignes dans le tableau de
bord, jamais une modification. Ce qu'aucun des deux ne traite est dit : la complaisance reste
distribuée dans la posture des outils.

**6.3 — septembre 2026.** Ajout de `references/verite.md`, le modèle unique des fichiers de
vérité : qui écrit quoi, qui lit quoi, quand, pour quoi, et sur quelle surface ça arrive —
Cowork, Claude Code, web et mobile. Motif : l'init est une enquête dont la seule sortie
durable est un jeu de fichiers, et tout le reste de la mallette n'est que des lecteurs ; le
risque à ce stade n'est plus l'erreur locale mais la dérive de cohérence entre outils. Règle
qui en découle : un fichier de vérité n'apparaît jamais par nécessité locale d'un skill, il
s'ajoute d'abord à la carte. Le miroir du projet gagne sa procédure exacte — vérifier trente
secondes si la synchronisation a déjà porté les fichiers, sinon le bouton « + » de la
connaissance du projet — et sa règle de rafraîchissement : chaque outil qui fait changer une
ligne de `00_MOI/` le dit en une phrase. `CLAUDE.md` porte le pointeur vers l'USP et la façon
de travailler, parce que c'est la seule porte de Claude Code. `03_RESSOURCES/` est enfin
défini — son logo, sa photo, des fichiers et pas des faits — et lu par les outils qui
fabriquent un visuel.

**6.2 — septembre 2026.** Les sources connectées sont recâblées sur ce que Cowork fait
vraiment. `source-fichiers.md` supposait un accès aux fichiers de l'utilisateur : Cowork ne
voit que le dossier connecté, créé vide — le fichier dit maintenant le geste, « Ajouter un
dossier » pour un dossier de son ordinateur, le connecteur Drive pour son Drive, et jamais le
disque ni le dossier personnel entier. Ajout de `connecteurs.md`, le hub : ce qu'est un
connecteur, les quatre clics, le fait que chaque requête est un appel distinct qui demande
son accord — d'où la consigne de le prévenir du nombre d'autorisations —, que ce qui est lu
reste attaché à la conversation, que Drive ne lit que le texte, ce qui peut casser et
l'abandon après deux tentatives. L'agenda devient la neuvième source, `source-agenda.md` :
un journal daté de ce qu'il fait, la source la plus nette pour les rituels et le rythme réel,
lue par titres et horaires sans jamais ouvrir les notes ni les invités. La récolte mensuelle
du skill des réseaux ne se planifie que si Gmail et l'agenda sont branchés : c'est écrit
comme le branchement le plus rentable de tout l'init.

**6.1 — septembre 2026.** Huit trous fermés après une revue de robustesse pensée pour des
utilisateurs qui ne savent rien des projets, de Cowork, de Claude Code ni des skills. Le
choix « dossier existant » à la création du projet n'était pas détectable : une question à
l'étape 9, consignée, avec la conséquence dite et la correction proposée pour plus tard. Un
`00_MOI/` renommé à la main déclenchait une seconde installation : désormais, si les dossiers
numérotés existent sans lui, on demande au lieu de recréer, dans les trois skills ; et
`CLAUDE.md` le dit à l'utilisateur. Les copies dans `.claude/skills/` n'étaient jamais
rafraîchies : chaque outil compare sa version à sa copie à chaque usage et remplace. Une
demande qui relève d'un autre outil est renvoyée en une phrase au lieu d'être faite à sa place.
Le texte collé — pas un lien — est traité comme une page. Une demande ponctuelle contraire à
`voix.md` est honorée pour ce texte sans modifier le fichier. Une photo envoyée ne donne que
les faits sans interprétation, confirmés. Une contradiction sur un fait qu'il a lui-même donné
déclenche une question, jamais un choix ni une moyenne. Et l'absence totale de présence en
ligne est une information consignée, pas un échec.

**6.0 — septembre 2026.** L'USP entre dans l'init, à l'étape 7, dérivée et jamais demandée.
Motif : l'acquéreur choisit une maison, mais le vendeur choisit une personne — le mandat est
un achat à fort enjeu, invérifiable avant, où « qui est cet agent » est le produit ; c'est le
cas que la littérature de grande consommation ne couvre pas et où l'USP a son sens. Elle se
trouve dans ce que les champs « ce qui le décide » des fiches clients ont en commun, croisé
avec ce dont les avis le remercient — des faits collectés quarante minutes plus tôt, pas une
description de lui-même. Deux phrases proposées, trois tests, puis trois comportements
vérifiables : c'est la partie qui sert, parce qu'une phrase ne se contrôle pas et qu'un
comportement oui. `references/usp.md` porte la méthode et la table d'usage pour toute la
mallette, sous une règle unique : l'USP se démontre, elle ne s'annonce pas. Le bloc de la
section 4 devient « Mon USP », le relevé la montre en tête de l'acte Toi, les instructions du
projet portent ses comportements plutôt que sa phrase.

**5.6 — septembre 2026.** Rien n'est simulé. Chaque valeur du tableau de bord et des écrans
est câblée à une source exacte — une ligne de fichier ou un comptage — avec une table de
dérivation complète dans `coque.md`, la règle du « — » quand la source est vide, et la source
en commentaire HTML à côté de chaque valeur dans les gabarits, là où le modèle regarde en
remplissant. Motif : une démonstration avec des chiffres inventés est exactement ce qu'un
modèle produit quand la consigne ne l'en empêche pas mécaniquement, et elle ment avec une belle
mise en page. Trois trous fermés au passage : « visites » n'existait dans aucun champ — ajouté
à `annonce.md`, rempli seulement quand il le dit ; les pourcentages par fichier n'avaient pas
de règle de calcul — c'est le ratio des lignes marquées ; la prochaine occurrence d'une tâche
n'est stockée nulle part — elle ne s'affiche plus.

**5.5 — septembre 2026.** Une coque commune à tous les écrans de livraison de la mallette,
`references/coque.md` : bandeau d'état, à faire, le principal, rangé — toujours dans cet ordre,
avec une règle de priorité qui ne se négocie pas : ce qu'il doit faire se lit sans défiler.
Les cinq écrans des trois outils sont régénérés dessus. Ajout du tableau de bord,
`tableau-de-bord.html` à la racine, créé à l'étape 2, rempli à l'étape 10, puis réécrit par
chaque outil en fin de course depuis ce qui est sur le disque — jamais de mémoire. C'est le
seul fichier qu'il ouvrira pour savoir où il en est, et le relevé le désigne en premier.
`ecran-0.html` est retiré : l'écran 0 ne se rend plus depuis la 5.0.

**5.4 — septembre 2026.** Le paysage local regarde aussi deux annonces par confrère — ce
qu'elles ouvrent, quelle photo, ce qu'elles omettent toutes — et le note en section 4 du
profil, sans nom. Motif : `immo-annonce` a besoin de savoir à quoi ressemble « pareil » pour
écrire différemment, et on ne se distingue pas de gens dont on ignore ce qu'ils écrivent.

**5.3 — septembre 2026.** Deux corrections réclamées depuis le début et jamais faites. Le nom
du projet n'a plus de valeur par défaut : la règle de la 3.7 disait de le laisser choisir, et
le skill continuait à proposer « Mon assistant immo » — retiré des quatre endroits où il
restait, y compris le titre du relevé. Deux garde-fous seulement, pas « assistant », pas
« Claude ». Et la convention `.claude` de Claude Code est enfin installée dans le dossier :
l'init crée `<dossier>/.claude/skills/` et s'y copie lui-même à l'étape 2, chaque outil de la
mallette faisant de même la première fois qu'il tourne. Motif vérifié : Claude Code lit les
skills du projet à cet endroit, au même format que ce qu'on téléverse sur le compte, alors
que Cowork n'a pas de skills à l'échelle du projet et ignore ce dossier — le dossier devient
autonome pour l'un sans gêner l'autre. Ce que l'init ne crée pas est dit aussi : ni
`settings.json`, ni `rules/`, ni `agents/`, réglages de développeur sans objet ici.

**5.2 — septembre 2026.** Le geste d'alimentation du panneau de progression était un souhait
et pas une consigne : « déclare les onze étapes en tâches » ne disait ni comment, ni quand, ni
quoi faire si ça ne prenait pas — donc le modèle posait son propre plan. Il est maintenant
écrit en termes opérationnels : le plan se pose dans la toute première réponse, avant tout
affichage, avec les titres des onze écrans mot pour mot, et chaque étape se marque terminée au
moment où elle l'est. Si le panneau ne se remplit pas, on ne le mentionne pas. L'emplacement du
dossier est motivé au lieu d'être asserté — dans ses documents, pas le bureau ni les
téléchargements, parce qu'il le gardera des années et que c'est aussi un répertoire de projet
Claude Code. Vingt-quatre lignes soudées par les substitutions successives sont reformatées
dans les deux skills.

**5.1 — septembre 2026.** Tout l'ASCII disparaît. Les onze cartouches à chasse fixe sont
remplacés par deux lignes de markdown — un titre de niveau trois et une citation — rendues par
la typographie de l'application, qui est plus lisible que tout ce qu'on dessinerait et qui
s'adapte à la largeur de l'écran. Le compteur sort du titre : la position est déjà dans le
panneau de progression, l'écrire deux fois est du bruit. `ecrans.md` est réécrit en entier dans
les deux skills, et il ne reste plus un seul caractère de cadre.

**5.0 — septembre 2026.** Le panneau de progression de Cowork remplace le cartouche comme
indicateur de position : il affiche nativement les tâches déclarées, donc les onze étapes se
déclarent en tâches au lieu d'être dessinées. Trois contraintes documentées — seul le titre
s'affiche, seules les tâches touchées dans l'échange en cours sont rendues, et c'est une vue
qu'on alimente sans l'éditer. Conséquence sur les écrans rendus : **le panneau est une
ressource unique**, un artefact le remplace et rétrécit la conversation. L'écran 0 ne se rend
donc plus — ses dix étapes sont exactement ce que la progression affiche. Et le périmètre est
cadré : `00_MOI/` décrit la personne et sert tous les outils, les autres dossiers sont le
domaine du jour, la communication. Un dossier par domaine dans le même projet, jamais un
projet par domaine — un second projet perdrait l'accès à `00_MOI/`.

**4.8 — septembre 2026.** Quatre corrections issues du premier essai en conditions réelles.
La jauge des cartouches utilisait `░` pour la partie vide, qui rend comme un bloc plein dans
beaucoup de polices : une barre à zéro ressemblait à une barre pleine. Remplacé par un point
médian. Le geste d'affichage d'un écran rendu manquait — le skill savait que les pages
existaient mais pas comment les montrer, donc il retombait systématiquement sur le cartouche ;
il est maintenant écrit, avec ses trois règles. Le paramétrage du projet — nom, description et
instructions — est donné **au moment de la création**, seul instant où l'utilisateur a les
trois champs sous les yeux ; l'étape 9 devient une révision au lieu d'une écriture. Et l'écran
0 se rend même sans dossier : voir les dix étapes rend les quatre clics évidents, là où un
message d'arrêt seul ressemble à un refus.

**4.7 — septembre 2026.** Chaque ligne de `00_MOI/` porte désormais son mois en plus de son
marqueur : `[dit 2026-09]`, `[vu 2026-09]`, `[dit ?]` quand la date est inconnue. Pas le jour,
une préférence n'en a pas. Motif : cinq règles déjà écrites dépendaient de l'âge d'une ligne
et n'avaient aucun moyen de le connaître — savoir si sa voix a six mois, si son positionnement
doit être revu, si deux corrections rapprochées font une préférence, ce qui est ancien au
moment d'une mise à jour. Elles deviennent vérifiables pour un mot par ligne. Correction au
passage : l'arborescence de `metier.md` décrivait `00_MOI/` avec quatre fichiers depuis la
2.2, il en manquait un.

**4.6 — septembre 2026.** Une cinquième portée s'ajoute à la répartition des instructions :
`~/.claude/CLAUDE.md`, la mémoire personnelle chargée dans tout projet Claude Code. Motif :
Claude Code lit ses mémoires en remontant depuis le répertoire ouvert jusqu'à la racine, donc
**le `CLAUDE.md` écrit à la racine du dossier de travail est déjà lu par lui sans rien faire**
— ce qui manquait était le cas où l'utilisateur travaille ailleurs. Trois lignes dans sa
mémoire personnelle suffisent, et elles ne s'écrivent que s'il utilise Claude Code, ce qui se
vérifie au lieu de se supposer. Décision explicite de **ne jamais déplacer `00_MOI/` dans
`~/.claude/`** : un dossier caché que l'utilisateur ne trouvera jamais annulerait la propriété
centrale de la mallette, à savoir que ces fichiers sont à lui et qu'il les corrige à la main.
Le relevé gagne un bloc « où tout se trouve » — dossier, projet, fichiers, accès mobile,
commande pour recommencer — qui manquait entièrement : le relevé montrait ce qu'on avait
trouvé, jamais ce qui avait été installé ni comment y revenir.

**4.5 — septembre 2026.** Ajout de `references/eprouver.md`, transposition du mécanisme
d'auto-interrogation récursive : déplier une affirmation en « parce que » jusqu'à toucher une
ancre — un `[dit]`, une ligne d'un fichier, une source datée — puis **tester par la
négation**, en écrivant l'affirmation contraire et en lui donnant sa meilleure raison. Si les
deux tiennent aussi bien, ce n'est pas un constat mais une impression, et la ligne redescend
en `[à confirmer]` ou se précise. Le mécanisme se déclenche sur toute ligne destinée à être
marquée `[vu]` et sur le regroupement des fiches clients, où « ces deux dossiers se
ressemblent » est une conclusion et non une observation.

**4.4 — septembre 2026.** Deux règles tirées des travaux sur la clarification d'intention.
Quand une question risque de rester sans réponse, on propose deux options plutôt que de la
laisser ouverte : le choix désigné produit des réponses plus justes et plus rapides que la
question libre, et c'est le principe du choix forcé sur la voix généralisé au reste. Et on ne
construit jamais un enchaînement de questions en entonnoir, difficile à produire correctement
et sur lequel un stagiaire décroche à la troisième. La vérification des `[vu]` à l'étape 10 se
fait désormais en retournant la ligne — « sur quoi repose-t-elle ? » — plutôt qu'en la
relisant, avec trois réponses recevables et une seule conséquence sinon : la ligne tombe.

**4.3 — septembre 2026.** L'enquête en ligne relève désormais l'identité visuelle pendant
qu'elle est déjà sur la page : les deux couleurs dominantes, le logo et son origine, la photo
professionnelle, le style des photos d'annonce. Tout est `[vu]` tant qu'il ne l'a pas
confirmé — un site fait par le réseau ne dit rien de ses goûts. `cadre.md` gagne une section
« mon identité visuelle », avec la question qui prime : le réseau impose-t-il une charte et
des gabarits ? Sans ces informations, tous les visuels fabriqués par la mallette sortent aux
couleurs de l'outil et pas aux siennes.

**4.2 — septembre 2026.** La section 4 du profil accueille le positionnement — une phrase sur
ce pour quoi l'utilisateur veut être connu, avec les trois sujets qu'il possède, ce qu'il ne
traite pas et les deux dossiers qui le prouvent. Elle ne se remplit jamais à l'installation :
positionner quelqu'un qu'on ne connaît pas encore produit une phrase qu'il ne tiendra pas. Sa
construction et son audit périodique sont portés par `immo-reseaux-sociaux`. Quand elle
existe, elle a aussi sa place dans les instructions du projet.

**4.1 — septembre 2026.** Les échantillons de `voix.md` sont promus au rang de partie la plus
importante du fichier, et l'init a désormais pour consigne d'en collecter trois à cinq. Motif :
une évaluation portant sur plus de quatre cents auteurs réels montre qu'un modèle à qui l'on
décrit un style échoue à l'imiter — moins de sept pour cent de réussite — alors que quelques
exemples suffisent, avec des gains qui s'épuisent au-delà de quatre ou cinq. Le choix forcé
produit des arbitrages, c'est-à-dire une description : il sert à trancher ce que les
échantillons laissent ambigu, il ne les remplace pas. Ajout de la règle anti-relissage : ce
que l'utilisateur a réécrit lui-même se conserve tel quel.

**4.0 — septembre 2026.** Les écrans rendus sont écrits, plus seulement décrits :
`assets/ecran-0.html` et `assets/ecran-4.html`, à remplir comme le relevé plutôt qu'à
fabriquer. Même logique que les cartouches — ce qui doit être identique d'un stagiaire à
l'autre est pré-écrit. Les trois pages partagent les couleurs du relevé : les écrans du
parcours et la page de fin appartiennent au même monde, et cette continuité fait plus pour
l'effet final que n'importe quel ornement. Chaque page est autonome, sans ressource externe
ni police à charger, avec le mode sombre géré, pour s'afficher dans un panneau qui ne fournit
rien.

**3.9 — septembre 2026.** Trois registres d'affichage au lieu d'un : un écran rendu dans un
panneau quand c'est possible, le cartouche sinon, deux lignes de texte en dernier recours, et
la dégradation se fait sans commentaire ni question au stagiaire. Le principe qui rend
l'écran rendu compatible avec le tunnel : **il affiche, la conversation demande** — un panneau
ne renvoie rien, et il n'a pas à le faire. Discipline imposée : trois écrans rendus au
maximum, l'écran 0 pour la promesse, l'écran 4 pour la reconnaissance, l'écran 10 qui est déjà
une page. Rien de ce qu'il doit copier ou corriger ne va dans un panneau.

**3.8 — septembre 2026.** Les écrans deviennent visibles. Chaque étape s'ouvre sur un
cartouche à chasse fixe de quarante caractères — titre, position, barre d'avancement — et les
onze sont écrits tout faits dans `ecrans.md`, alignés au caractère près, à recopier tels quels
plutôt qu'à recalculer. Correction d'une erreur de la 3.3 : les accents ne cassent pas
l'alignement dans un bloc de code, seuls les emoji le font, en occupant deux colonnes. Règle
de repli si le rendu se brise sur un écran étroit, et interdiction de mettre dans un bloc de
code quoi que ce soit qu'il doive lire, copier ou corriger. Les contenus comparatifs passent
en tableaux markdown.

**3.7 — septembre 2026.** Répartition des instructions entre les quatre endroits qui en
portent : le `SKILL.md` d'un outil, les instructions du projet, `CLAUDE.md`, les fichiers de
`00_MOI/`. `CLAUDE.md` et les instructions du projet disaient la même phrase presque mot pour
mot ; la règle posée n'est pas « ne jamais répéter » mais « ne jamais laisser fuir ce qui est
propre à un contexte ». Conséquence principale : **aucun chemin de dossier dans les
instructions du projet**, puisqu'elles s'appliquent depuis un téléphone où le dossier n'existe
pas. Inversement, le protocole d'interaction sort de `CLAUDE.md`, qui se limite désormais aux
règles de rangement. Le gabarit d'instructions gagne la ligne qui manquait le plus : ne rien
inventer et laisser vide, seule règle de marquage qui survive hors du dossier. Ajout des cinq
fonctions du projet — il en contient le dossier, porte ce qui vaut pour toute séance, met le
profil sur son téléphone, cloisonne la mémoire, porte les tâches planifiées — et des trois
déclencheurs de mise à jour des instructions.

**3.6 — septembre 2026.** Mise à jour liée à l'arrivée du deuxième skill de la mallette.
`amorcage.md` porte désormais la liste des skills, ce que chacun lit et écrit, et la règle qui
décide de leur comportement en l'absence de profil : un outil qui calcule ou qui engage
s'arrête, un outil qui rédige un texte relu produit quand même en l'annonçant. Les renvois à
`immo-post` sont remplacés par `immo-reseaux-sociaux`.

**3.5 — septembre 2026.** Quatre ambiguïtés levées, trouvées en déroulant la skill à blanc.
L'ordre du début était contradictoire entre trois fichiers — le SKILL.md disait de demander
le mode « avant toute chose », le garde-fou le précédait, et `ecrans.md` le plaçait en fin
d'écran 0 : une séquence unique de quatre temps est désormais énoncée en tête du SKILL.md et
fait autorité, avec la raison — demander la durée d'une séance qui ne peut pas avoir lieu est
la pire ouverture possible. Le compte des sources était faux : « six » annoncé deux fois alors
que le tableau, `protocole.md` et les plafonds en listent huit. L'étape 3 faisait 80 lignes
contre 6 et 9 pour les étapes 4 et 5 : elle est découpée en trois temps non interchangeables —
le public, le sien, l'ailleurs — avec la règle du mode salle rendue explicite. Et l'en-tête
d'un écran vient désormais toujours en premier, y compris avant un bloc à écrire mot pour mot.

**3.4 — septembre 2026.** Trois corrections issues d'un audit de tenue. Le relevé passe de
cinq blocs à quatre actes : il montrait cinq lignes et cinq barres alors que l'init collecte
les arbitrages de voix, les formules saturées, SONCAS, les leviers, les rôles dans la décision,
les canaux pondérés et l'écart entre périmètre déclaré et périmètre observé — rien de tout
cela n'était restitué. La ligne de partage est posée : les fichiers portent ce qui se lit, le
relevé porte ce qui se regarde. Ajout du carnet de commandes, les récurrences repérées et non
installées avec ce qu'elles deviendraient et ce qu'il faudrait — c'est ce qui annonce la suite
de la mallette. Le sommaire du SKILL.md est réécrit en vocabulaire de déclenchement : quinze
de ses vingt lignes reprenaient les mots du titre du fichier décrit, ce qui n'apporte aucun
signal au moment où il faut choisir quel fichier ouvrir. Chaque ligne dit maintenant la
situation qui appelle le fichier, pas son contenu. Ajout de l'écran 0, qui cadre tout ce qui
précède l'étape 1 — contrôle de surface, choix du mode, garde-fou du dossier — c'est-à-dire la
partie la plus technique de la séance et celle où le stagiaire décroche le plus vite.

**3.3 — septembre 2026.** L'init se déroule désormais en écrans : `references/ecrans.md`, un
cadre fixe de trois lignes par étape, dix écrans nommés, et quatre réponses affichées dès
qu'une question est posée — répondre, « je ne sais pas », « on passe », « où on en est ».
Toutes légitimes et consignées : un stagiaire qui veut faire échouer la séance tire son
pouvoir de l'imprévu, et quand refuser est prévu il n'y a plus rien à casser. Le sabotage a
sa section dans `quand-ca-derape.md` : on traite comme un « je ne sais pas » et on passe, sans
se justifier. Pas de caractères de cadre ni de bloc de code, qui s'alignent mal avec les
accents, cassent sur mobile, et ressemblent à la chose technique que le stagiaire ne comprend
pas. L'en-tête d'état de `profil.md` devient un point de reprise : il gagne l'étape terminée
et les étapes sautées, et se met à jour au fil des étapes pour qu'une session interrompue
reprenne au lieu de tout refaire.

**3.2 — septembre 2026.** Une correction de fait et une production nouvelle. Correction :
une tâche planifiée **ne peut pas être liée à un dossier de l'ordinateur** — elle tourne avec
les connecteurs et les fichiers du compte. `tri-recurrences.md` disait l'inverse et aurait
fait installer en salle des tâches qui n'auraient jamais tourné. Une récurrence alimentée par
des fichiers locaux devient soit une tâche à la demande, soit un candidat à condition de faire
remonter la matière. Ajout de la règle de terrain : on lance la tâche une fois à la main avant
de la planifier, parce que la première exécution est la seule qui révèle les permissions
manquantes et les sources muettes. Production nouvelle : le relevé d'installation, une page
HTML autonome écrite à la racine du dossier et ouverte en artefact — `references/rapport.md`
pour la méthode, `assets/rapport.template.html` pour la page. Elle s'ouvre sur un constat tiré
du `[vu]`, jamais du `[dit]`, avec son appui chiffré, et se termine sur une seule action.
Interdiction d'inventer le constat si l'enquête n'en a pas produit.

**3.1 — septembre 2026.** Audit des productions et des surfaces. Le garde-fou d'entrée
teste désormais la surface avant le dossier, par trois vérifications fonctionnelles — dossier,
navigateur, recherche dans les conversations — parce qu'un même skill est visible dans les
trois onglets de l'application et qu'un modèle ne peut pas déterminer de façon fiable dans
lequel il tourne. Le cas dangereux est nommé : un répertoire de travail sans navigateur ni
projet laisse l'init démarrer et produire une installation à moitié faite sans que rien ne le
signale. Tableau des dégradations par capacité absente, avec la règle qu'une capacité absente
se note et se dit mais n'arrête jamais l'init. Distinction ajoutée entre ce que la skill écrit
elle-même et ce qu'elle fait faire au stagiaire — projet, miroir, tâche planifiée, mémoire —
avec obligation de consigner chaque action dictée, faite ou non, dans l'en-tête d'état de
`profil.md`, qui gagne deux lignes pour ça. La passe de contrôle de l'étape 10 passe de cinq
à six vérifications et couvre maintenant les actions dictées.

**3.0 — septembre 2026.** Version issue d'un audit des liens entre fichiers. Cinq
corrections. L'écriture est désormais instruite explicitement au fil de l'enquête, source par
source, au lieu d'être supposée entre l'étape 3 et l'étape 4. Les quatre sections-miroir du
profil — 3, 5, 9 et 12, qui résument `clients-types.md`, `voix.md`, `recurrences.md` et
`cadre.md` — entrent dans la passe de contrôle de l'étape 10 : aucun fichier détaillé ne doit
rester derrière une section vide. La section 7, le glossaire maison, était orpheline : aucune
source ne disait comment la remplir. Elle est maintenant alimentée par le compte Claude, les
comptes rendus et les mails, et `questions.md` précise qu'elle ne se demande jamais. Les deux
renvois circulaires entre `clients-types.md`, `avis-clients.md` et `paysage-local.md` sont
coupés dans un sens. `amorcage.md` est marqué hors init, en tête de fichier et dans la liste
des fichiers. Et la clôture présente la section 13 comme une feuille de route plutôt que
comme un inventaire de pannes.

**2.9 — septembre 2026.** Version de robustesse, tirée d'un audit et de la littérature sur
l'adhérence aux instructions. Sept incohérences corrigées : numéros d'étapes périmés dans
`memoire.md` et `projet-cowork.md`, comptes de fichiers et de sources faux à cinq endroits.
Ajout d'une liste de contrôle recopiée en début de session. Ajout d'un accusé de réception des
trois règles à l'étape 1 — une règle explicitement reprise est mieux suivie qu'une règle
seulement lue. Rappel du marquage ajouté en fin de chaque fichier de source, là où
l'extraction a lieu, parce que la conformité se dégrade à mesure qu'on produit et que la
première omission arrive tôt. Ajout d'une passe de contrôle en tête de l'étape 10, avant de
montrer quoi que ce soit. Ajout de `references/quand-ca-derape.md` et d'une règle non
négociable sur la complaisance : une observation ne s'efface pas devant une affirmation.

**2.8 — septembre 2026.** Règle de délégation ajoutée dans `protocole.md` et dans les règles
non négociables : l'enquête ne se confie pas à des sous-agents. Un sous-agent ne renvoie que
son message final, donc une synthèse — ce qui détruit la provenance, rend la recherche
invisible au stagiaire et contourne le feu vert par source. Deux exceptions, hors mode
salle : compter les avis d'une ligne et balayer les pages des confrères. Hors formation, la
délégation redevient légitime pour tout ce qui ne produit pas de ligne `[dit]`.

**2.7 — septembre 2026.** Les avis en ligne deviennent une source à part entière :
`references/avis-clients.md`. Règle des deux corpus — le spontané penche négatif, le
sollicité penche positif, l'écart est l'information. Séparation stricte entre ce qui nomme
l'agent et ce qui concerne l'agence. Ordre de lecture par valeur : tous les négatifs et les
moyens d'abord, un avis trois étoiles avec du texte valant dix avis cinq étoiles sans texte.
Limite énoncée : un avis s'écrit après la signature, il dit ce qui fait basculer et non ce
qui bloque. Glassdoor et les plateformes d'avis d'employés explicitement exclues — ce sont des
avis sur un employeur, pas sur un agent. Aucun nom d'auteur écrit, aucune réponse rédigée
pendant l'init, republication laissée en `[à confirmer]` dans `cadre.md`.

**2.6 — septembre 2026.** Deux ajouts liés. `references/navigateur.md` : toute la partie en
ligne se fait au navigateur intégré de Cowork, demandé explicitement — sans consigne, les
pages sont récupérées silencieusement et la salle ne voit rien. Prérequis, piège du navigateur
par défaut quand l'extension Chrome est installée, interdiction de tout espace connecté et de
toute action, et risque d'injection à nommer devant la salle. `references/paysage-local.md` :
cinq confrères regardés une seule fois, pour le différenciant par contraste, le niveau de jeu
local, les angles vides, et surtout les formules saturées qui deviennent des interdits de
voix. Aucun barème concurrent relevé, aucun nom en production, aucun jugement.

**2.5 — septembre 2026.** Sixième source, placée en tête :
`references/source-presence-en-ligne.md`. Publique, sans consentement à demander, elle remplit
quatre sections du profil, donne les noms des communes qui conditionnent toutes les
recherches suivantes, et reste la seule source exploitable quand le stagiaire découvre Claude
le jour même. Stock relevé en agrégé et jamais bien par bien. Géographie ramenée aux noms de
lieux et de repères, avec interdiction d'écrire un chiffre de marché dans `00_MOI/`. Les
mentions déjà publiées sur son site sont relevables et marquées `[vu]` — relever n'est pas
rédiger. Question obligatoire sur l'auteur des textes du site avant tout usage pour la voix.

**2.4 — septembre 2026.** Cinquième source d'enquête : `references/source-transcripts.md`,
les comptes rendus de réunion produits par un preneur de notes automatique. Verrou de
confidentialité renforcé — règle lexicale, on extrait des tournures et jamais des situations —
et interdiction d'alimenter `voix.md` avec de l'oral. Les fiches clients types gagnent la
grille SONCAS en tête, les rôles dans la décision à la place de la liste d'influences, et une
pondération des canaux en trois crans avec obligation de citer l'origine.

**2.3 — septembre 2026.** Deux questions ajoutées à la passe groupée, transversales à toute
production : ce qu'il a publié et qui lui a rapporté un contact, et les publications d'autres
qu'il aurait voulu signer. Les échantillons de `voix.md` privilégient désormais ce qui a
produit un effet réel sur ce qu'il trouve réussi. `cadre.md` gagne une section « côté
publication en ligne ». Tout ce qui est propre à un canal — longueur par plateforme,
hashtags, moment de publication, commentaires — reste hors de l'init et se remplira dans les
skills de production, sur un cas réel.

**2.2 — septembre 2026.** Ajout des fiches clients types, cinquième fichier de `00_MOI/` et
socle transversal de toute la mallette : `references/clients-types.md` pour la méthode,
`assets/clients-types.template.md` pour le gabarit, grille de situations candidates dans
`metier.md`. La construction passe par l'entretien des trois derniers dossiers et d'un perdu,
jamais par une description. Grille de six leviers mêlant la recherche de Google sur les
décisions d'achat et trois leviers propres à l'immobilier, avec la transposition signalée
comme une lecture et non comme un résultat d'étude. Liste de vocabulaire marketing interdit
devant l'utilisateur. Étapes renumérotées : les fiches deviennent l'étape 7.

**2.1 — septembre 2026.** Garde-fou d'entrée réécrit : on crée un projet Cowork « Partir de
zéro », pas un dossier — un projet créé depuis un dossier existant n'est pas enregistré sur
le compte et ne suit pas le stagiaire sur mobile. Ajout de `references/voix-qcm.md`, passe de
choix forcé insérée avant l'échantillon de l'étape 6. Ajout de `references/projet-cowork.md`
et élargissement de l'étape 8 aux trois dépôts (instructions, fichiers miroir, mémoire), avec
la règle du cloisonnement mémoire par projet. Dans `tri-recurrences.md` : règle skill contre
tâche planifiée, une tâche appelle un skill au lieu de recopier une procédure, contrainte
d'horaire, et rendez-vous de contrôle à trois semaines.

**2.0 — septembre 2026.** Séparation squelette / couche métier dans `metier.md`. Ajout du
mode salle avec budget temps. Ajout de l'en-tête d'état dans `profil.md`. Ajout de l'étape
mémoire du compte et de `references/memoire.md`. Ajout de `references/amorcage.md`. Champ
`allowed-tools` supprimé : il listait des outils de Claude Code et n'autorisait aucune des
sources d'enquête. Renommage de `recurrences.md` en `tri-recurrences.md` pour lever la
collision avec le fichier produit. Fichiers de fouille renommés en `source-*`.

**1.0.** Version initiale.
