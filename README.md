# Rod'Stores — site web

Site vitrine de **Rod'Stores**, entreprise familiale père & fils basée à Roanne (Loire) :
fenêtres, volets roulants, portes, Velux, moustiquaires — pose, rénovation, motorisation et dépannage.

- En ligne : https://julien-crepieux.github.io/rod-stores/
- Domaine cible : https://rodstores.fr/

## Structure

| Chemin | Rôle |
| --- | --- |
| `build.py` | Générateur : gabarit commun (en-tête, pied de page, SEO, Schema.org), sitemap, robots.txt |
| `content.py` | Contenu de toutes les pages (textes, FAQ, galerie, témoignages) |
| `docs/` | Site généré, servi tel quel par GitHub Pages (branche `main`, dossier `/docs`) |
| `docs/css/style.css` | Styles (mobile d'abord) |
| `docs/js/main.js` | Menu mobile, comparateur avant/après, filtres et visionneuse de la galerie |
| `docs/img/` | Images optimisées en WebP (photos issues du compte Instagram @rod.stores) |

## Modifier le site

1. Modifier les textes dans `content.py` (ou le gabarit dans `build.py`).
2. Régénérer : `python build.py` (Python 3, aucune dépendance).
3. Commiter et pousser : GitHub Pages republie automatiquement.

Pour ajouter une photo de chantier : déposer `docs/img/<nom>-540.webp` et `docs/img/<nom>-1080.webp`,
puis ajouter une ligne dans `GALLERY` (`content.py`).

## Brancher le domaine rodstores.fr

1. Chez le registrar du domaine, créer les enregistrements DNS GitHub Pages :
   - `A` sur `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` sur `www` → `julien-crepieux.github.io`
2. Dans GitHub → *Settings → Pages → Custom domain*, saisir `rodstores.fr` et cocher *Enforce HTTPS*.
3. Dans `build.py`, passer `SITE["base_path"]` à `"/"` puis relancer `python build.py`.

Les adresses des pages reprennent celles de l'ancien site (`/fenetres/`, `/volets-roulants/`,
`/depannage-volets-roulants/`, `/porte/`, `/portes-de-garage/`, `/nos-realisations/`, `/contact/`…)
pour conserver le référencement acquis.
