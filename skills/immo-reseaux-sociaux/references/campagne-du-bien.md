# La campagne d'un bien : révélez, animez, vendez

## Ce que ce fichier décide

Il dit « fais toute la campagne de ce bien », « révélez, animez, vendez », ou il arrive avec
une photo et une annonce et veut tout ce qui va avec. Quatre pièces sortent, dans cet ordre,
et chacune part de la précédente :

1. **Révélez** — la photo retouchée. Offre Google (Gemini).
2. **Animez** — un clip de quelques secondes tiré de cette photo. Offre Google, côté vidéo.
3. **Vendez** — l'affiche, avec la photo retouchée. Offre OpenAI (ChatGPT), parce qu'il y a
   du texte à rendre lisible.
4. **Vendez** — la légende du Reel qui porte le clip. **Celle-là, tu l'écris toi-même.**

Tu ne fabriques ni la photo, ni le clip, ni l'affiche : tu écris les trois prompts, tu dis
quoi joindre, et tu dis quoi vérifier. C'est la règle de `outils-image.md`, appliquée à un
bien d'un bout à l'autre. Compte une demi-heure la première fois.

## Avant de commencer

Trois choses, demandées en une fois, et rien de plus :

- **sa plus belle photo du bien**, et si elle est en largeur ou en hauteur — c'est elle qui
  décide du format du clip ;
- **le lien de l'annonce**, ou son texte collé ;
- **les outils qu'il a** : Gemini avec son compte Google, ChatGPT, et s'il a la vidéo dans
  Gemini. S'il n'a qu'un des deux, on fait avec — voir la fin.

Les faits viennent de l'annonce et de nulle part ailleurs. Un fait absent devient
« à compléter », sur l'affiche comme dans la légende.

La mention qui signale l'image : **son texte exact vient de `cadre.md`**. Les prompts
ci-dessous écrivent « Image retouchée » ; si `cadre.md` porte une autre formule, tu la
remplaces avant de les lui donner. Si la case est vide, tu gardes « Image retouchée » et tu le
lui signales à la livraison.

---

## 1. Révélez — le prompt de retouche

**Où** : Gemini, connecté à son compte Google. **Il joint** : la photo d'origine.

```
CONTEXTE
Je suis agent immobilier. Voici une photo d'un bien que je vends, prise dans l'annonce de mon agence : [JOIGNEZ VOTRE PHOTO]
Tu es retoucheur photo spécialisé en immobilier : tu rends une photo plus belle sans jamais tromper l'acheteur.
BUT
Obtenir une photo plus lumineuse et plus nette, prête pour Instagram, qui montre exactement le même bien.
ÉTAPES
1. Garde le même cadrage, les mêmes murs, les mêmes fenêtres, les mêmes meubles et la même vue.
2. Corrige la lumière : éclaircis les zones sombres, équilibre les couleurs, rends les blancs propres, sans effet artificiel.
3. Redresse les lignes verticales si la photo penche, et améliore la netteté.
4. Retire seulement les petits objets du quotidien qui encombrent : câble, papier, sac, objet personnel, photo de famille.
5. Ajoute en bas à droite, en petit et discrètement, la mention « Image retouchée ».
RÉSULTAT ATTENDU
L'image retouchée, au même format que la photo d'origine. Puis, sous l'image, 2 lignes maximum : ce que tu as changé.
EXEMPLES
Retouche acceptée : une pièce sombre rendue lumineuse, une photo penchée redressée, un câble qui traîne retiré.
Retouche refusée : une fissure ou une tache effacée, un vis-à-vis ou un poteau supprimé, une vue changée, un coucher de soleil ajouté, une pièce agrandie, un meuble ajouté.
LEVER LES AMBIGUÏTÉS
- Tu ne me poses aucune question : tu fais la retouche directement.
- Tu ne caches aucun défaut et tu ne changes ni la vue, ni la surface apparente, ni l'état du bien. Tout ce qui est fixé au mur, au sol ou au plafond reste.
- Si une retouche risque de tromper l'acheteur, tu ne la fais pas. Si un détail de la photo n'est pas clair, tu fais le choix le plus prudent. Dans les deux cas, tu me le signales à la fin, en une ligne.
```

**Il vérifie** : il met les deux photos côte à côte. Même pièce, rien de caché, la mention en
bas à droite. Puis il télécharge la photo retouchée : elle sert aux trois étapes suivantes.

## 2. Animez — le prompt du clip

**Où** : Gemini, menu « + », puis « Créer une vidéo ». **Il joint** : la photo retouchée.
**Format** : Paysage si la photo est en largeur, Portrait si elle est en hauteur. Un format qui
ne correspond pas oblige l'outil à inventer le haut et le bas de la pièce — c'est une image
fausse.

```
CONTEXTE
Je suis agent immobilier. Voici la photo retouchée d'un bien que je vends : [JOIGNEZ VOTRE PHOTO RETOUCHÉE]
Tu es vidéaste spécialisé en immobilier : tu fais vivre une photo sans jamais changer le bien.
BUT
Une courte vidéo, de 8 à 10 secondes, pour Instagram et Facebook, qui donne envie de visiter.
ÉTAPES
1. Pars exactement de cette photo : mêmes murs, mêmes fenêtres, mêmes meubles, même vue.
2. Un seul mouvement de caméra, lent et fluide : une avancée douce vers la fenêtre, comme un visiteur qui entre.
3. Seule la lumière vit : le soleil glisse doucement, le rideau bouge à peine.
4. Le son : une ambiance calme d'appartement, sans voix et sans musique forte.
RÉSULTAT ATTENDU
Une vidéo de 8 à 10 secondes, sans aucun texte à l'écran.
EXEMPLES
Mouvement voulu : un travelling avant très lent.
À éviter : zoom brutal, rotation, accéléré, effet « drone ».
LEVER LES AMBIGUÏTÉS
- Tu n'ajoutes ni personne, ni animal, ni meuble, ni objet, ni texte, ni logo.
- Tu ne changes ni la vue, ni la taille de la pièce, ni les matériaux, ni l'état du bien.
- La mention « Image retouchée » reste lisible en bas à droite.
- Si un détail risque de changer le bien, tu fais le choix le plus prudent.
```

Le mouvement se choisit sur la photo, **un seul** : vers la fenêtre s'il y en a une, sinon un
travelling avant lent vers le centre de la pièce. Jamais un mouvement qui révèle ce que la
photo ne montrait pas — une pièce voisine, un coin hors cadre : c'est la règle de
`outils-image.md`.

**Il vérifie** : il regarde le clip **jusqu'au bout**, image par image si besoin. Une fenêtre
qui se déforme, un meuble qui apparaît, une vue qui change : on jette, on ne corrige pas. Le
quota est court — quelques clips par jour sur un plan payant, les chiffres changent selon le
plan : dis-le avant qu'il en lance trois pour rien.

## 3. Vendez — le prompt de l'affiche

**Où** : ChatGPT. **Il joint** : la photo retouchée, et il colle le lien de l'annonce.

```
CONTEXTE
Je suis agent immobilier. Voici l'annonce d'un bien que je vends : [COLLEZ ICI LE LIEN DE VOTRE ANNONCE]
Et voici la photo du bien à mettre sur l'affiche : [JOIGNEZ VOTRE PHOTO]
Tu es directeur artistique dans une agence de communication immobilière.
BUT
Créer une affiche moderne et élégante qui donne envie de visiter, à publier sur Instagram et à afficher en vitrine.
ÉTAPES
1. Ouvre le lien et relève dans l'annonce : le type de bien, la ville ou le quartier, la surface, le nombre de pièces, le prix, les honoraires et qui les paie, la classe énergie et la classe climat.
2. Choisis une accroche de 6 mots maximum et les 3 atouts les plus forts, en 3 à 5 mots chacun.
3. Crée l'image de l'affiche, au format portrait 4:5 d'Instagram (si tu ne sais faire que du 2:3, garde tout le texte dans la zone centrale, loin des bords du haut et du bas, qu'Instagram coupe) : la photo en grand, l'accroche en haut, les 3 atouts, le prix bien visible ; puis, en petit : les honoraires, la classe énergie et la classe climat écrites en simple texte (par exemple « DPE : D · GES : C »), sans dessiner l'étiquette énergie, et un cadre vide « Logo et téléphone de l'agence ».
4. Style : sobre et haut de gamme, comme l'affiche d'une agence de prestige. Deux couleurs au maximum, tirées de la photo, plus du blanc. Une seule police sans empattement, en deux tailles au maximum, lisible à 2 mètres, avec un fort contraste. Le texte sur un bandeau ou un aplat de couleur, jamais sur une zone chargée de la photo. Des marges larges : aucun mot coupé ni collé au bord. Ni dégradé, ni icône 3D, ni émoji, ni effet brillant.
RÉSULTAT ATTENDU
L'image de l'affiche, puis, en dessous, le texte exact que tu as écrit sur l'affiche, pour que je puisse le vérifier. Puis relis l'image mot par mot : si un mot, une lettre ou un chiffre de l'image diffère de ce texte, signale-le en une ligne.
EXEMPLES
Des accroches dans l'esprit voulu : « Et si c'était chez vous ? » · « Le centre-ville, au calme ».
À éviter : « Affaire à saisir », « Coup de cœur assuré », les points d'exclamation.
LEVER LES AMBIGUÏTÉS
- Tu ne me poses aucune question : tu crées l'affiche directement.
- Tu gardes ma photo telle qu'elle est : tu ne redessines pas le bien, tu n'ajoutes ni meuble, ni vue, ni jardin, ni piscine, ni personne, ni ciel de coucher de soleil : même cadrage, mêmes fenêtres, mêmes portes, mêmes matériaux. Pas de « look IA » : ni HDR, ni couleurs saturées, ni teinte jaune ou orangée sur toute l'image, ni sols trop brillants ; les blancs restent blancs, les lignes droites restent droites. Si ma photo porte la mention « Image retouchée », elle reste visible sur l'affiche.
- Tous les chiffres de l'affiche viennent de l'annonce, recopiés à l'identique. Le texte est en français correct, accents compris, chaque mot écrit en entier. Un chiffre absent ne s'invente pas : tu écris « à compléter ».
- Si tu ne peux pas ouvrir le lien, tu ne devines rien : tu me le dis en une ligne et tu me demandes de coller le texte de l'annonce.
- Sur l'affiche, aucun autre texte que l'accroche, les 3 atouts, le prix, les honoraires, le DPE, le cadre vide de l'agence et la mention « Image retouchée » : ni faux logo, ni nom d'agence inventé, ni numéro de téléphone, ni adresse de site, ni QR code, ni petit texte décoratif. Aucun nom, aucune donnée personnelle.
- Aucune promesse de chiffre ou de performance : ni délai de vente, ni « prix imbattable ».
- Pour le reste (accroche, couleurs, atouts choisis), tu fais l'hypothèse la plus probable et tu me la signales à la toute fin, en une seule ligne qui commence par « Hypothèses : ».
```

**Il vérifie** : chaque chiffre contre l'annonce, et la photo contre l'originale. Un seul
détail cloche — une teinte jaune, un chiffre de travers, une lettre en trop : il ne
recommence pas, il écrit « Garde tout à l'identique et corrige seulement : … ». La dominante
jaune a sa propre parade dans `outils-image.md`.

## 4. Vendez — la légende du Reel

Celle-là, tu l'écris, avec ce que tu sais déjà de lui : `ecriture.md` pour la voix,
`plateformes.md` pour Instagram, `controle.md` avant de la livrer. La forme :

- une première ligne qui arrête le défilement : une scène de vie, jamais le prix ;
- trois ou quatre lignes courtes pour se projeter, une idée par ligne ;
- les faits de l'annonce : surface, pièces, prix, honoraires et qui les paie, DPE et GES ;
- un seul appel à l'action : message privé ou lien en bio — un lien écrit dans une légende
  Instagram n'est pas cliquable ;
- huit hashtags locaux, à part ;
- en dernière ligne, la mention de `cadre.md` pour une image retouchée et un clip généré. À
  défaut : « Image retouchée · vidéo générée par IA à partir d'une photo réelle ».

Entre 120 et 160 mots, trois émojis au plus. Aucun fait inventé.

**S'il travaille sans toi** — dans ChatGPT ou Gemini, dans la conversation de l'affiche — il
colle ceci :

```
Maintenant, écris la légende du Reel Instagram qui accompagnera la vidéo de ce bien (même bien, même annonce).
1. Une première ligne qui arrête le défilement : une scène de vie, jamais le prix.
2. 3 ou 4 lignes courtes pour se projeter, une idée par ligne.
3. Les faits de l'annonce : surface, pièces, prix, honoraires et qui les paie, DPE et GES.
4. Un seul appel à l'action : message privé ou lien en bio.
5. 8 hashtags locaux, à part.
6. En dernière ligne : « Image retouchée · vidéo générée par IA à partir d'une photo réelle ».
Entre 120 et 160 mots, 3 émojis au maximum. Aucun fait inventé : un fait absent devient « à compléter ». Tu ne me poses aucune question.
```

---

## S'il n'a pas tous les outils

Relevé en novembre 2026, à revérifier : les offres gratuites changent vite, et **s'il décrit
autre chose, c'est lui qui a raison**.

- **Pas de vidéo dans son Gemini** : Runway (runwayml.com) accepte une photo et un prompt,
  avec des crédits offerts à l'inscription. Le même prompt du clip sert tel quel.
- **Pas de ChatGPT** : l'affiche se fait dans Gemini avec le même prompt, mais le texte y est
  moins sûr — il relit chaque lettre. Ou le moteur de la mallette, si l'affiche n'a pas besoin
  de la photo (`visuels.md`).
- **Il veut aller plus loin** : IACréa (iacrea.com) est pensé pour les agents immobiliers —
  home staging virtuel, désencombrement, vidéo à partir de photos, avec un essai gratuit. Une
  pièce meublée par l'IA porte toujours la mention « Ameublement virtuel », sur la photo et
  dans l'annonce, avec le texte exact de `cadre.md` s'il en porte un.

## Livrer

Quatre pièces, et la forme de `livrer.md` quand même. **Avant les traits**, une phrase au
plus. **Entre les deux traits**, la légende du Reel, telle qu'elle sera publiée — jamais dans
un bloc de code. **Après**, ce qu'il doit faire : les trois étapes dans l'ordre, chacune avec
l'outil, ce qu'il joint, le prompt dans un cadre à copier — c'est une consigne, pas un texte à
juger — et ce qu'il vérifie, en une ligne. Puis les remarques, dans le plafond de `livrer.md`,
et la question.

Avec un dossier, le kit complet — les trois prompts, la légende, les faits relevés, ce qui
manquait — part dans `02_PUBLICATIONS/brouillons/` comme tout brouillon, et tu en dis une
ligne.

Et la phrase qui ne se saute pas : **il publie le clip seulement après l'avoir regardé
jusqu'au bout.** C'est la pièce qui trompe le plus facilement, et la seule qu'on ne relit pas
d'un coup d'œil.
