# Installer la mallette

## Avant tout

- **Un abonnement Claude payant** : Pro, Max ou Team.
- **L'exécution de code activée** dans les réglages de Claude. Sans elle, les compétences apparaissent grisées ; dans une organisation, c'est le propriétaire du compte qui l'active.
- Pour travailler avec votre dossier : **Claude Desktop**, sur un projet relié à un dossier de votre ordinateur.

## 1. Claude Desktop, par la marketplace — recommandé

1. Ouvrez **Personnaliser**.
2. Cherchez l'endroit où l'on ajoute une marketplace depuis GitHub, et collez : `https://github.com/agencekoeki/Claude-marketing-for-real-estate`
3. Installez le plugin **mallette-immo** : les cinq outils arrivent ensemble.

Les intitulés changent d'une version de l'application à l'autre. Si vous ne trouvez pas le menu, passez par les fichiers ci-dessous : le résultat est le même, seules les mises à jour se font à la main.

## 2. claude.ai, par fichiers `.zip` ou `.skill`

1. Téléchargez les cinq outils de la dernière version, au format de votre choix — c'est le même contenu :
   - immo-init : [.zip](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-init.zip) · [.skill](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-init.skill)
   - immo-parcours : [.zip](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-parcours.zip) · [.skill](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-parcours.skill)
   - immo-annonce : [.zip](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-annonce.zip) · [.skill](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-annonce.skill)
   - immo-reseaux-sociaux : [.zip](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-reseaux-sociaux.zip) · [.skill](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-reseaux-sociaux.skill)
   - immo-penser-savoir : [.zip](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-penser-savoir.zip) · [.skill](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest/download/immo-penser-savoir.skill)
   Pas les archives « Source code » de la page des versions : c'est le dépôt entier.
2. Dans **Personnaliser › Compétences**, importez-les un par un, sans les décompresser.
3. À chaque nouvelle version, supprimez les anciens et importez les nouveaux.

## 3. Claude Code

```
/plugin marketplace add agencekoeki/Claude-marketing-for-real-estate
/plugin install mallette-immo@sebastien-grillot
```

Ici, les scripts tournent sur votre ordinateur. Il y faut **Python 3**, et pour les carrousels :
`python3 -m pip install reportlab pillow pypdf`.

Sous Windows : l'installeur de [python.org](https://www.python.org/downloads/), en cochant « Add python.exe to PATH », ou `winget install Python.Python.3.12` dans un terminal. Attention : taper `python` avant de l'avoir installé peut ouvrir le Microsoft Store au lieu de répondre.

## Premier pas

Tapez « / » et choisissez **immo-init**. L'outil vérifie l'environnement, pose ses questions, et écrit votre profil dans votre dossier.

## Dépannage

| Ce que vous voyez | Ce que ça veut dire | Quoi faire |
|---|---|---|
| les compétences sont grisées | l'exécution de code est désactivée | l'activer dans les réglages ; dans une organisation, demander au propriétaire |
| « workspace unavailable » | la machine virtuelle de Claude Desktop ne démarre pas | redémarrer l'application ; en attendant, les carrousels passent par un gabarit à exporter |
| les outils portent un préfixe dans le menu « / » | ils sont installés en plugin | c'est normal : choisissez-les par leur nom |
| Claude Code ne trouve pas Python | Python n'est pas installé sur l'ordinateur | lancer immo-init : il propose de vous guider |

## Mettre à jour

- **Marketplace** : vérifiez les mises à jour du plugin ; dans Claude Code, `/plugin marketplace update`.
- **Fichiers** (`.zip` ou `.skill`) : réimportez les outils de la [dernière version](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest).
- Ou demandez à n'importe quel outil : « y a-t-il une mise à jour ? ».
