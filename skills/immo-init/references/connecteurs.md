# Les connecteurs

## Ce que c'est, dit simplement

Un connecteur, c'est une autorisation qu'il donne une fois pour que Claude puisse lire un de
ses outils — sa messagerie, son agenda, son stockage en ligne — **à sa place, avec ses droits, et rien de
plus**. Claude ne voit que ce qu'il pourrait voir lui-même.

Deux familles existent sur tous les plans, gratuit compris (pages d'aide Anthropic, septembre
2026) :

- **Google** — Gmail, Google Agenda, Google Drive
- **Microsoft 365** — Outlook, son agenda, OneDrive, SharePoint — **seulement avec un compte
  professionnel** rattaché à une organisation Microsoft, et après un accord unique de
  l'administrateur de cette organisation. Une adresse outlook.com, hotmail.com ou live.com ne se
  branche pas.

D'autres se trouvent dans l'annuaire des connecteurs. Une messagerie qui n'est ni Google ni
Microsoft 365 pro — celle d'un fournisseur d'accès, d'un hébergeur, celle de son logiciel
métier — n'en a souvent aucun : vérifie dans l'annuaire, ne le promets pas. Et un compte Team ou
Entreprise peut en avoir bloqué : dans ce cas, c'est l'administrateur qui décide, pas lui.

---

## Comment ça marche, parce que ça décide de la façon d'enquêter

**Une lecture est toujours une réponse à une question.** Claude n'ouvre pas la boîte et ne
lit pas tout : il cherche ce qu'on lui a demandé, et récupère le minimum. Donc **une enquête
n'est jamais une seule lecture, c'est une suite de requêtes ciblées** — les segments de
`source-mail.md`, les batteries de `metier.md`. Chaque requête est un appel distinct.

**Chaque appel demande son accord, par défaut.** C'est sa sécurité, et en séance ça veut dire
qu'il va cliquer « autoriser » plusieurs fois d'affilée. **Dis-le-lui avant la première fois** :

> Tu vas voir apparaître des demandes d'autorisation, une par recherche. C'est normal, c'est
> toi qui décides à chaque fois ce que je peux lire. Tu peux dire non à n'importe laquelle.

**Ce qui est lu reste attaché à la conversation.** S'il supprime la conversation, ce qui a été
lu part avec. Ça le rassure, et c'est vrai.

**Ce qui se lit dépend du format.** Le connecteur Google lit les Docs et, selon sa page d'aide,
aussi les tableurs, présentations, PDF, images et fichiers Office ; un scan ou une photo de
document peut pourtant ne rien donner d'exploitable. Vérifie sur un fichier avant de conclure
qu'une source est vide.

---

## L'ordre d'accès, quelle que soit la messagerie

Mails, agenda, fichiers : l'accès se choisit **par fonction, jamais par marque**, et toujours
dans cet ordre.

1. **Un connecteur**, s'il en existe un pour son outil et qu'il accepte de le brancher. C'est
   l'accès le plus étroit — une recherche, une réponse, un accord par appel —, et le seul qu'une
   tâche planifiée à distance sait lire.
2. **Un dossier synchronisé sur son ordinateur** — Google Drive, OneDrive ou Dropbox installés en
   local. Ses fichiers en ligne deviennent des fichiers du dossier : pas besoin de connecteur.
   Un fichier resté seulement en ligne peut refuser de s'ouvrir : il le rapatrie, ou on passe.
3. **Un export fait par lui** : vingt à trente mails envoyés copiés dans un fichier texte, un
   export `.ics` de son agenda, un tableur de son logiciel métier, déposés dans le dossier. En
   salle, c'est souvent plus rapide qu'un branchement qui bloque.
4. **Les questions** qui remplacent la source — voir `questions.md`.

**Jamais le navigateur sur un espace connecté** — messagerie web, agenda en ligne, logiciel
métier —, même s'il propose d'y ouvrir sa session. Quatre raisons, et chacune suffit : un mail
est un texte écrit par quelqu'un d'autre, donc l'endroit rêvé pour une instruction cachée ; une
boîte ouverte à l'écran, ce sont des noms, des montants et des adresses de clients devant la
salle ; un clic dans une messagerie a des effets — lu, archivé, envoyé ; et le navigateur ne
tourne qu'avec Claude Desktop ouvert, donc rien de ce qu'il lit ne se planifie.

**Consigne en section 13** l'éditeur de sa messagerie, de son agenda et de son stockage, et le
mode d'accès retenu pour chacun : connecteur, dossier synchronisé, export, ou rien.

## Comment on les branche — les quatre clics

Dans l'application : **Personnaliser, puis Connecteurs.** La liste apparaît, avec Google et
Microsoft 365 notamment. **Connecter**, une fenêtre de Google ou de Microsoft s'ouvre, il choisit
le compte qu'il veut que Claude lise, il lit l'écran des permissions, il accepte. Une fois par
connecteur. Avec Microsoft 365, si l'accord de l'administrateur manque, la connexion échoue :
en salle, on n'insiste pas, on passe à l'export.

Ce que l'écran de permissions peut dire et qui fait peur : « envoyer des e-mails ». Il faut le
dire avant qu'il le voie, et dire vrai : **le connecteur Gmail de Claude crée des brouillons mais
ne peut pas envoyer** ; celui de Microsoft 365 peut envoyer si l'administrateur a activé
l'écriture, et en mode manuel — le réglage par défaut — Claude demande avant d'agir. Dans tous
les cas, **la mallette n'envoie jamais rien** : elle prépare, il envoie.

**Ne pousse jamais.** Un connecteur refusé, on note le manque et on continue. Insister devant
ses collègues coûte la séance.

---

## Ce que chaque connecteur donne, et à qui

| Connecteur | Dans l'init | Après, dans la mallette |
|---|---|---|
| Messagerie — Gmail, Outlook | sa façon d'écrire, ses rituels, les questions qu'on lui pose — `source-mail.md` | la récolte mensuelle du carnet, planifiable |
| Agenda — Google, Outlook | ce qu'il fait vraiment et à quel rythme — `source-agenda.md` | la récolte mensuelle, les dates à préparer |
| Stockage — Drive, OneDrive | ses productions et ses modèles, s'ils sont là plutôt qu'en local — `source-fichiers.md` | ses photos de biens, ses documents type — et **la boîte de dépôt** de ce qu'il produit depuis son téléphone, rapatriée dans le dossier ensuite |

**Aucun connecteur n'est obligatoire.** Sans aucun, l'init tient avec la présence en ligne et
l'entretien. Avec la messagerie seule — ou son export —, la voix devient bonne. Avec l'agenda en plus, les récurrences
deviennent réelles et la récolte du carnet peut tourner seule.

---

## Ce qui peut casser, et ce qu'on fait

Les connecteurs tombent parfois : zéro outil exposé, « le demandeur n'a pas la permission »,
une lenteur qui ne se résout pas. **Deux tentatives, puis on abandonne la source et on le
dit** — sans diagnostic, sans lui faire reconnecter en séance. Ça se note en section 13 comme
un branchement à revoir.

**Une source qui tombe ne bloque rien.** C'est la règle de tout le protocole : chaque source
a une suivante, et les questions de l'étape 5 compensent.

---

## Ce qu'on consigne

Section 13 du profil, deux lignes : les connecteurs branchés, et ceux qui manquent avec ce
qu'ils ouvriraient. C'est ce que le relevé reprend dans « ce qui te manque » — et c'est ce que
les autres outils lisent pour savoir ce qu'ils peuvent faire tourner seuls.

**La récolte du carnet, dans le skill des réseaux, ne se planifie à distance que si sa
messagerie et son agenda sont branchés par connecteur** — Google ou Microsoft 365, peu importe. C'est le branchement le plus rentable de tous, et c'est ici qu'on le prépare.

---

## Rappel de marquage

Quels connecteurs il a branchés est `[dit]` — c'est lui qui a cliqué. Ce qu'ils ont donné est
`[vu]`, source par source. Rien de ce qu'un connecteur lit n'entre dans `00_MOI/` autrement
que sous la règle de chaque source : la forme, jamais le fond.
