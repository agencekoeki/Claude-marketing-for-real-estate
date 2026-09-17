# Faire surfer Claude sous les yeux du stagiaire

## Pourquoi ce fichier existe

Par défaut, quand tu dois lire une page, tu la récupères silencieusement. C'est efficace et
c'est invisible. En formation, invisible veut dire que rien ne s'est passé.

**Pour toute la partie en ligne de l'init, tu demandes explicitement le navigateur.** Ce
n'est pas un réglage, c'est une consigne : sans elle, la salle ne voit rien et tu perds la
meilleure démonstration de la journée.

---

## Ce qui existe, et ce qu'on utilise

**Le navigateur intégré à Cowork.** Il s'ouvre dans le panneau latéral, à côté de la tâche.
Claude ouvre les sites, lit, clique, tape et remplit des formulaires pendant que l'utilisateur
regarde, sans changer de fenêtre. Rien à installer. Il est isolé du navigateur personnel :
il ne voit ni les onglets, ni les favoris, ni les mots de passe.

**C'est celui qu'on utilise pour l'init.** L'enquête ne demande que des pages publiques :
aucune raison de toucher aux comptes du stagiaire.

**Claude in Chrome**, l'extension, travaille dans son vrai navigateur, sur la page qu'il a
déjà ouverte, avec ses comptes connectés. Utile quand le travail porte sur une page devant
lui. Pas notre cas ici.

---

## Le piège de la sélection par défaut

Les deux coexistent, et le défaut dépend de ce qui est installé sur le poste :

- **extension Chrome déjà installée** → elle reste le navigateur par défaut dans Cowork
- **pas d'extension** → le navigateur intégré est utilisé

Donc deux stagiaires côte à côte n'auront pas le même comportement. Ça se règle dans les
réglages de Cowork, **Navigateur préféré** — dans la nouvelle interface l'emplacement peut
différer : ne devine pas le chemin, fais-le chercher.

Si tu demandes un navigateur par son nom et qu'il n'est pas disponible, dis-le et demande
avant d'utiliser l'autre. Ne bascule pas en silence.

---

## Prérequis à vérifier avant la séance, pas pendant

- L'application Desktop doit être **ouverte et en ligne**, même si la session tourne dans le
  cloud
- Le navigateur intégré demande un plan payant et se déploie progressivement ; sur Team et
  Enterprise, un propriétaire peut l'avoir désactivé
- S'il n'apparaît pas, ce n'est pas une erreur de manipulation : c'est le déploiement ou un
  réglage d'organisation

Si rien n'est disponible, **l'init continue sans**. Tu lis les pages silencieusement, tu le
dis en une phrase, et tu ne bloques pas la séance sur une démonstration. Note « navigateur »
dans les capacités absentes de l'en-tête d'état : c'est ce qui permettra de refaire la
démonstration plus tard, quand elle sera disponible.

L'absence de navigateur est aussi un signal de surface. Si tu n'as ni navigateur, ni projets,
ni tâches planifiées, tu n'es probablement pas dans Cowork — retourne au garde-fou d'entrée du
SKILL.md avant de poursuivre.

---

## Comment l'annoncer

Une phrase avant d'ouvrir, et elle fait la moitié du travail pédagogique :

> Je vais aller voir ton site. Regarde le panneau de droite : tu vas me voir naviguer, ouvrir
> les pages et lire. Arrête-moi quand tu veux.

Puis **commente ce que tu fais pendant que tu le fais**. Pas un rapport à la fin : « là
j'ouvre ta page à propos », « là je regarde tes trois dernières annonces ». C'est ce qui
transforme une collecte en démonstration.

---

## Ce qu'on ne fait jamais avec le navigateur

**Aucun espace connecté.** Pas de CRM, pas de portail professionnel, pas de messagerie, pas
d'espace client, pas d'outil bancaire. L'init ne lit que des pages publiques, accessibles
sans identifiant. Si une page demande une connexion, tu t'arrêtes et tu passes.
**Une messagerie web sans connecteur ne fait pas exception**, même s'il propose d'y ouvrir sa
session : l'ordre d'accès est dans `connecteurs.md`.

**Aucune importation de mots de passe.** Le navigateur intégré propose d'importer les
connexions depuis le navigateur personnel. Ce n'est pas nécessaire pour l'init, et ce qui est
connecté dedans reste disponible pour les sessions suivantes sur cette machine. Ne le
propose pas.

**Aucune action.** On lit. On ne remplit aucun formulaire, on n'envoie aucun message, on ne
s'inscrit à rien, on ne clique sur aucun bouton qui produit un effet.

---

## Le risque à nommer devant la salle

Une page web peut contenir des instructions cachées destinées à détourner un agent qui la
lit. Les garde-fous du navigateur réduisent ce risque — permission avant d'agir sur un site
pour la première fois, sites à risque bloqués, vérification de chaque action par rapport à ce
qui a été demandé — mais ne l'éliminent pas.

Dis-le en une phrase au moment où tu ouvres le navigateur. C'est trente secondes, ça fait
partie de la formation, et ça te protège en tant que formateur :

> Un site peut contenir des instructions cachées qui essaient de détourner l'IA qui le lit.
> C'est pour ça qu'on commence par des sites qu'on connaît, et qu'on ne lui fait jamais faire
> une action irréversible sans regarder.
