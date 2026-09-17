# L'environnement d'exécution

Ce fichier sert une fois, à l'étape 2, et chaque fois qu'un script de la mallette échoue.

## Où tourne le code, selon la surface — relevé en septembre 2026

Les scripts de la mallette — `verifier.py`, la mesure de la voix, le moteur de visuels — ont besoin
de Python 3. Le moteur a besoin en plus de deux bibliothèques, reportlab et Pillow, et de pypdf pour
relire le PDF qu'il fabrique.

| Où il travaille | Où s'exécute le code | Python à installer chez lui ? |
|---|---|---|
| claude.ai, ou Cowork en session dans le cloud | le bac à sable d'Anthropic | non |
| Claude Desktop, session locale | la machine virtuelle Linux de l'application | non — sauf si elle ne démarre pas |
| Claude Code sur son ordinateur | son ordinateur | oui |

Source : la page d'aide d'Anthropic sur l'architecture de Cowork, mise à jour le 16 septembre 2026.
Les sessions Cowork y tournent dans le cloud par défaut, l'exécution locale restant disponible pour
les installations existantes du bureau.

## L'essai, une fois

Lance `python3 -c "import reportlab, PIL; print('ok')"`. Sous Windows, dans Claude Code, essaie aussi
`python` puis `py -3` à la place de `python3`. Puis lis la réponse, et seulement elle :

| Ce que tu lis | Ce que ça veut dire | Ce que tu fais |
|---|---|---|
| `ok` | tout est là | tu notes, tu passes |
| une erreur de module introuvable | Python est là, pas les bibliothèques | `python3 -m pip install reportlab pillow pypdf` si l'environnement le permet ; sinon tu notes « absentes » : les carrousels passeront par le gabarit de secours |
| « workspace unavailable » | la machine virtuelle de l'application ne démarre pas | une phrase : redémarrer l'application règle souvent le problème ; en attendant, gabarits de secours, et `verifier.py` ne tourne pas |
| commande introuvable, ou le Microsoft Store qui s'ouvre | Claude Code sur un ordinateur sans Python | la proposition ci-dessous, une seule fois |

## Claude Code sans Python : une proposition, une seule

« Pour fabriquer tes carrousels et vérifier ton dossier, il faut Python sur ton ordinateur. Je te
guide, ou on continue sans — tes carrousels passeront alors par un gabarit que tu exporteras
toi-même. »

S'il accepte :

- **Windows** : l'installeur de python.org, en cochant « Add python.exe to PATH » ; ou, dans un
  terminal, `winget install Python.Python.3.12`. Puis fermer et rouvrir Claude Code.
- **macOS** : `python3 --version` dans le Terminal ; s'il manque, le système propose d'installer
  les outils de développement ; sinon, l'installeur de python.org.
- Puis `python3 -m pip install reportlab pillow pypdf`, et l'essai une seconde fois.

Tu ne lances aucune de ces commandes sans son accord explicite. Et sur Windows, un piège connu :
taper `python` sans l'avoir installé peut ouvrir le Microsoft Store au lieu de répondre.

## Ce qui s'écrit

Une ligne de l'en-tête d'état de `profil.md` : où s'exécutent les scripts, la date de l'essai, et si
les bibliothèques du moteur sont là. Les outils de production la lisent : « absentes », ils passent
directement par les gabarits de secours ; un script qui échoue quand même, ils refont l'essai.
