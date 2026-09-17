# Couche métier — agent immobilier

**C'est le seul fichier à réécrire pour décliner cette mallette sur un autre métier.**
Tout le reste de la skill est générique. Si tu adaptes ce fichier, garde ses titres de
sections : le squelette y renvoie nommément.

---

## Le métier en une ligne

Agent immobilier indépendant ou en réseau, qui prospecte, rentre des mandats, fait visiter,
négocie, et communique lui-même sur son secteur.

---

## Arborescence à créer

```
.claude/skills/      les outils de la mallette, un sous-dossier par skill
00_MOI/              profil.md, voix.md, cadre.md, clients-types.md, recurrences.md
01_BIENS/            un sous-dossier par bien, photos et infos
02_PUBLICATIONS/     brouillons/ et publies/
03_RESSOURCES/       son logo et sa photo professionnelle, tels quels — des fichiers, pas des faits
```

`00_MOI/` et `.claude/` sont invariants dans toute la mallette. Les trois autres sont propres à
ce métier.

---

## Ce qu'on cherche dans son agenda

Trois passes, dans `source-agenda.md`. Pour ce métier, les titres qui reviennent sont
typiquement : estimation, visite, signature, compromis, relance, point vendeurs, porte
ouverte. Un type de rendez-vous qui revient au même créneau chaque semaine est un rituel ;
son volume par semaine est son rythme réel.

## Batteries de requêtes — compte Claude et autre IA

Cinq passes, courtes, deux à quatre mots. Arrête-toi dès que les résultats se répètent.

**Métier.** `mandat` · `estimation` · `acquéreur` · `vendeur` · `visite` · `compromis` ·
`offre d'achat` · `DPE` · `honoraires` · `copropriété`
Plus le nom de ses communes dès que tu les as.

**Production.** `post LinkedIn` · `annonce` · `publication` · `rédiger` · `newsletter` ·
`flyer` · `photo bien` · `story`

**Outils.** `Canva` · `Excel` · le nom de son réseau immobilier · `CRM` · `logiciel` ·
`export`

**Correction.** `plus court` · `trop long` · `ne dis pas` · `réécris` · `pas comme ça` ·
`je préfère`

**Temporelle.** Par fenêtres de dates, pas par sujet. Le mois dernier, il y a trois mois, il
y a six mois. Sert à voir à quels moments il sollicite.

---

## Segments d'interlocuteurs — fouille des mails

- **Vendeur** : `in:sent mandat` · `in:sent estimation` · `in:sent "votre bien"`
- **Acquéreur** : `in:sent visite` · `in:sent "offre"` · `in:sent disponibilité`
- **Notaire ou confrère** : `in:sent compromis` · `in:sent acte` · `in:sent dossier`
- **Interne** : `in:sent` vers le domaine de sa structure

L'écart entre le segment vendeur et le segment acquéreur est la trouvaille la plus
spectaculaire de tout l'init sur ce métier. Cherche-la en priorité.

---

## Dans sa présence en ligne

Pages à ouvrir en priorité : sa page à propos, cinq à huit annonces réparties entre
typologies, sa page d'avis ou sa fiche d'établissement, ses mentions.

Dans une annonce, relever : l'ordre de présentation du bien, s'il décrit les pièces ou la vie
dans le bien, la place donnée au quartier, la longueur, l'ouverture, la clôture, l'appel à
l'action. Jamais l'adresse, jamais le prix, jamais la référence.

Dans le stock agrégé : nombre de biens, typologies dominantes, communes, fourchettes de
surface, ancienneté des annonces en ligne. C'est le périmètre observé, à confronter au
périmètre déclaré.

Identité visuelle à relever au passage : les deux couleurs dominantes du site, le logo et son
origine, sa photo professionnelle, et le style de ses photos d'annonce — grand angle, lumière
naturelle, pièces meublées ou vides. Tout est `[vu]` tant qu'il ne l'a pas confirmé : un site
fait par le réseau ne dit rien de ses goûts.

Identité visuelle à relever au passage : les deux couleurs dominantes du site, le logo et son
origine, sa photo professionnelle, et le style de ses photos d'annonce — grand angle, lumière
naturelle, pièces meublées ou vides. Tout est `[vu]` tant qu'il ne l'a pas confirmé : un site
fait par le réseau ne dit rien de ses goûts.

Repères locaux à relever par quartier, parce que ce sont eux qui ancrent un texte : gare et
transports, écoles et collèges, marché et commerces, équipements sportifs, axes routiers,
zones d'activité, éléments naturels. Les noms, jamais les chiffres.

---

## Plateformes d'avis à connaître dans ce métier

Fiche d'établissement Google, non modérée, la plus consultée. Plateformes certifiées :
Immodvisor, la plus répandue dans l'immobilier français, Opinion System, Avis Vérifiés.
Ailleurs : Trustpilot, Pages Jaunes, recommandations Facebook, Meilleurs Agents, et les
portails d'annonces qui rediffusent les avis d'un partenaire.

Ne pars pas à la chasse : demande-lui avec quel outil son agence collecte ses avis.

Hors périmètre : Glassdoor, Indeed et les plateformes d'avis d'employés. Ce sont des avis sur
un employeur, pas sur un agent.

---

## Chez les confrères

Qui compte comme concurrent réel : ceux qui apparaissent sur « agence immobilière + sa
commune », qui ont des biens dans ses communes et sur ses typologies, et qui ont des avis
récents sur sa zone. Pas les plus grosses enseignes du département.

Formules à surveiller parce qu'elles saturent ce métier : coup de cœur, rare sur le secteur,
idéalement situé, produit rare, à ne pas manquer, opportunité à saisir, charme de l'ancien,
lumineux et fonctionnel.

Ce que les agences mettent en avant sur leur page à propos : ancienneté, appartenance à un
réseau, nombre de ventes, connaissance du quartier, estimation gratuite, outils et
technologie, photos et vidéos. La liste sert à faire émerger le différenciant par contraste.

---

## Dans les comptes rendus de réunion

Types de rendez-vous à répartir plutôt que de prendre les plus récents : le rendez-vous
d'estimation, le débriefing de visite, le point de commercialisation, la négociation d'offre.
Chacun donne des objections différentes.

Objections à relever telles qu'elles sont formulées, sans jamais le contexte qui les entoure :
sur le prix, sur le délai, sur l'exclusivité, sur les honoraires, sur le fait de réfléchir.

---

## Signaux de récurrence propres au métier

Vocabulaire déclencheur à relever tel quel : « à chaque nouveau mandat », « avant chaque
visite », « le point du lundi », « la relance à trois semaines », « en fin de mois pour mes
vendeurs », « le bilan de commercialisation ».

Rituels fréquents dans ce métier : le point de commercialisation envoyé au vendeur, la
relance des acquéreurs sur un bien, la veille des nouveautés du secteur, le récapitulatif
d'agence hebdomadaire, la publication du bien fraîchement rentré.

---

## Habillage du profil

À injecter dans `profil.template.md` au moment de la copie. Les treize sections sont
génériques, les sous-questions ci-dessous sont propres à ce métier.

**Section 1 — Qui je suis.** Statut et réseau de rattachement. Depuis quand. Vente, location,
gestion, neuf, ancien : ce qu'il fait et ce qu'il ne fait pas.

**Section 2 — Mon secteur.** Communes et quartiers couverts. Types de biens traités le plus.
Ce qui caractérise son marché local en une phrase. Saisonnalité : les mois qui bougent, les
mois qui dorment.

**Section 3 — Mes clients.** Primo-accédants, familles, investisseurs, vendeurs seniors. Ce
qui les fait bouger. Les trois objections les plus entendues. Les mots qu'ils emploient, eux,
pour parler de leur projet.

**Section 4 — Ce qui me distingue.** Pourquoi on l'appelle lui et pas l'agence d'en face. Ce
qu'il refuse de faire même si ça se vend.

**Section 7 — Ce que je sais déjà.** Ce qu'il ne faut pas lui réexpliquer. Son vocabulaire
métier et ses abréviations. Les noms de dossiers, de secteurs, de résidences ou de lotissements
qu'il emploie sans les expliquer, et les surnoms qu'il donne à ses biens ou à ses quartiers.
Sigles courants dans ce métier qu'il utilise sans les développer.

**Section 8 — Où je publie.** Plateformes par ordre d'importance. Fréquence réellement tenue.
Formats qui marchent, formats abandonnés.

**Section 9 — Ce qui revient.** Rendez-vous annuels du métier : rentrée, évolution des taux,
fêtes, saison des mandats.

**Section 10 — Ma matière première.** Avis clients exploitables. Chiffres citables : nombre
de ventes, délai moyen, écart entre prix affiché et prix vendu. Anecdotes de vente déjà bien
racontées. Où sont ses photos. Et ses publications qui ont produit un contact entrant.

**Section 12 et `cadre.md`.** Côté publication, ce que le réseau impose : compte officiel
contre compte personnel, visuels et gabarits imposés, ce qu'il n'a pas le droit de publier
lui-même, mentions d'appartenance à faire figurer.

---

## Bloc cadre métier

À injecter dans `cadre.template.md`, section « Mentions obligatoires ».

**Rappel impératif : ces lignes restent vides tant que l'utilisateur ou le formateur ne les
renseigne pas. Aucun outil de la mallette ne complète cette section de sa propre initiative
et ne suppose une obligation légale.**

- Annonce de vente — mentions à faire figurer
- Annonce de location — mentions à faire figurer
- Diagnostic de performance énergétique — ce que j'affiche et comment
- Honoraires — qui les paie, où c'est indiqué
- Carte professionnelle, numéro, titulaire
- Mandat — ce que je ne publie pas tant qu'il n'est pas signé
- Référence ou source qui fait foi pour moi

Confidentialité propre au métier : coordonnées de clients, prix négociés non publics, motifs
de vente personnels, photos d'intérieur non validées par le propriétaire. Autorisation du
propriétaire avant publication : oui, non, cas par cas.

---

## Grille de situations candidates

**À faire confirmer ou écarter, jamais à écrire d'office.** Cette liste sert à accélérer le
regroupement après l'entretien des trois derniers dossiers, pas à remplir les fiches. Le
stagiaire reconnaît, corrige ou raye. S'il ne reconnaît rien, c'est son entretien qui fait
foi, pas cette liste.

**Côté vendeur**
- la succession — plusieurs décideurs, personne n'est pressé sauf un
- la mutation — échéance dure, le prix passe après le calendrier
- le départ des enfants — attachement fort, pas d'urgence
- la séparation — décision contrainte, communication tendue entre deux interlocuteurs
- le vendeur qui teste — veut un chiffre, pas un mandat
- l'investisseur qui arbitre — raisonne en rendement, pas en attachement

**Côté acquéreur**
- le primo-accédant — dépend d'un financement, avance au rythme de la banque
- la famille qui s'agrandit — contrainte par l'école et le calendrier scolaire
- le retour au pays ou l'arrivée dans la région — ne connaît pas les quartiers
- l'investisseur locatif — compare des chiffres, visite peu
- l'acquéreur qui cherche depuis longtemps — a vu beaucoup, hésite, a déjà raté un bien

**Déclencheurs qui reviennent dans ce métier**
Naissance, séparation, décès, mutation professionnelle, départ en retraite, départ des
enfants, hausse ou baisse des taux, un voisin qui vend.

**Cercles d'influence qui reviennent**
Le conjoint, l'enfant adulte, le proche « qui s'y connaît en immobilier », le notaire, le
voisin qui vient de vendre, les estimateurs en ligne.

---

## Formulations métier des questions

Reprend les huit questions de `references/questions.md` avec les mots de ce métier.

**1. Le cadre imposé.**
> Ton réseau s'occupe déjà d'une partie de ta communication. Qu'est-ce qu'il produit à ta
> place, et qu'est-ce que tu n'as pas le droit de publier toi-même ?

**2. Le différenciant.**
> Un vendeur a trois agents devant lui. Pourquoi il te choisit toi ?
> S'il sèche : qu'est-ce que tes clients te disent le plus souvent quand ils te remercient ?

**3. Les objections.**
> Les trois phrases que tu entends le plus souvent et qui bloquent un dossier ?

**4. Le rythme réel.**
> Tu publies combien de fois par mois, vraiment, pas dans l'idéal ?

**5. Le repoussoir.**
> Qu'est-ce qui t'a déjà été écrit à ta place et qui ne te ressemblait pas du tout ?

**6. Le protocole.**
> Tu préfères que je te sorte une proposition tout de suite quitte à ce que tu la corriges,
> ou que je te pose des questions avant de produire ?

**7. Ce qui a marché.**
> Quel truc que tu as publié t'a rapporté un appel, un message ou un rendez-vous ?
> S'il sèche : ton dernier contact entrant qui n'était pas une recommandation, il venait d'où ?

**8. Ce qu'il aurait aimé avoir fait.**
> Montre-moi deux ou trois publications que tu aurais voulu signer. De qui tu veux, même
> hors immobilier. Des liens ou des captures, je ne te demande pas de les décrire.

---

## Point de vigilance propre au métier

Beaucoup d'agents travaillent sous une boîte mail fournie par leur réseau, qui ne leur
appartient pas. Avant de brancher la messagerie, pose la question en une phrase : « ta boîte
mail, c'est la tienne ou celle du réseau ? » S'il ne sait pas, ou si c'est celle du réseau,
tu proposes la source suivante sans insister et tu le notes en section 13.
