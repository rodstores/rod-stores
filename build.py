#!/usr/bin/env python3
"""Générateur du site statique Rod'Stores.

Usage : python build.py
Produit les pages HTML dans docs/ (servi tel quel par GitHub Pages),
ainsi que sitemap.xml et robots.txt. Les contenus des pages sont dans content.py.
"""
import datetime
import json
import os
import re
import struct
from html import escape

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT_DIR, "docs")

SITE = {
    "name": "Rod'Stores",
    "url": "https://rodstores.fr",
    "phone": "07 68 16 02 68",
    "phone_e164": "+33768160268",
    "email": "rodstores.services@gmail.com",
    "city": "Roanne",
    "postal": "42300",
    "region": "Loire",
    "instagram": "https://www.instagram.com/rod.stores/",
    "facebook": "https://www.facebook.com/profile.php?id=61587493753974",
    "google": "https://share.google/G2dC7RXC4SZobGMtx",
    # Chemin absolu du site, utilisé par la page 404 (servie à n'importe quelle profondeur).
    # "/rod-stores/" tant que le site est servi sur julien-crepieux.github.io/rod-stores/,
    # à remplacer par "/" une fois le domaine rodstores.fr branché sur GitHub Pages.
    "base_path": "/rod-stores/",
}

NAV = [
    ("Services", None, [
        ("Fenêtres", "fenetres/"),
        ("Volets roulants", "volets-roulants/"),
        ("Dépannage volets roulants", "depannage-volets-roulants/"),
        ("Portes d'entrée", "porte/"),
        ("Portes de garage & portails", "portes-de-garage/"),
        ("Velux & fenêtres de toit", "velux-fenetres-de-toit/"),
        ("Moustiquaires & stores", "moustiquaires/"),
    ]),
    ("Réalisations", "nos-realisations/", None),
    ("À propos", "a-propos/", None),
    ("Contact", "contact/", None),
]

# ---------------------------------------------------------------- icônes
ICONS = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "check-circle": '<circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
    "arrow": '<path d="M5 12h14M13 5l7 7-7 7"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "left": '<path d="m15 18-6-6 6-6"/>',
    "right": '<path d="m9 18 6-6-6-6"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>',
    "home": '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "thermo": '<path d="M14 14.8V4a2 2 0 0 0-4 0v10.8a4 4 0 1 0 4 0z"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
    "volume": '<path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/>',
    "ruler": '<path d="M21.3 15.3 8.7 2.7a1 1 0 0 0-1.4 0L2.7 7.3a1 1 0 0 0 0 1.4l12.6 12.6a1 1 0 0 0 1.4 0l4.6-4.6a1 1 0 0 0 0-1.4zM7.5 10.5l2-2M10.5 13.5l2-2M13.5 16.5l2-2"/>',
    "instagram": '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/>',
    "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    "google": '<path d="M21.8 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.5a4.7 4.7 0 0 1-2 3.1v2.6h3.3c1.9-1.8 3-4.4 3-7.5z"/><path d="M12 22c2.7 0 5-.9 6.7-2.4l-3.3-2.6c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3v2.6A10 10 0 0 0 12 22z"/><path d="M6.4 13.9a6 6 0 0 1 0-3.8V7.5H3a10 10 0 0 0 0 9z"/><path d="M12 6c1.5 0 2.8.5 3.8 1.5l2.9-2.9A10 10 0 0 0 3 7.5l3.4 2.6C7.2 7.8 9.4 6 12 6z"/>',
    "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
}


def icon(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true" viewBox="0 0 24 24"><use href="#i-{name}"/></svg>'


def sprite():
    syms = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items())
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true">{syms}</svg>'


# ---------------------------------------------------------------- images
_dims_cache = {}


def webp_size(path):
    """Lit largeur/hauteur d'un fichier WebP sans dépendance."""
    if path in _dims_cache:
        return _dims_cache[path]
    with open(path, "rb") as f:
        head = f.read(40)
    chunk = head[12:16]
    if chunk == b"VP8 ":
        w, h = struct.unpack("<HH", head[26:30])
        w, h = w & 0x3FFF, h & 0x3FFF
    elif chunk == b"VP8L":
        b = head[21:25]
        w = 1 + (((b[1] & 0x3F) << 8) | b[0])
        h = 1 + (((b[3] & 0xF) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6))
    elif chunk == b"VP8X":
        w = 1 + int.from_bytes(head[24:27], "little")
        h = 1 + int.from_bytes(head[27:30], "little")
    else:
        raise ValueError(path)
    _dims_cache[path] = (w, h)
    return w, h


def variants(name):
    """Liste triée des largeurs disponibles pour une image (docs/img/<name>-<w>.webp)."""
    ws = []
    for fn in os.listdir(os.path.join(OUT, "img")):
        m = re.fullmatch(re.escape(name) + r"-(\d+)\.webp", fn)
        if m:
            ws.append(int(m.group(1)))
    if not ws:
        raise FileNotFoundError(name)
    return sorted(ws)


class Ctx:
    """Contexte de rendu d'une page (chemin relatif vers la racine)."""

    def __init__(self, path, root=None):
        self.path = path
        depth = path.count("/")
        self.root = root or ("../" * depth if depth else "./")

    def u(self, href):
        if href.startswith(("http", "mailto:", "tel:", "#")):
            return href
        return self.root + href

    def src(self, name, w=None):
        ws = variants(name)
        return f"{self.root}img/{name}-{w or ws[-1]}.webp"

    def img(self, name, alt, sizes="100vw", cls="", eager=False, w=None):
        ws = variants(name)
        lw, lh = webp_size(os.path.join(OUT, "img", f"{name}-{ws[-1]}.webp"))
        srcset = ", ".join(f"{self.root}img/{name}-{x}.webp {x}w" for x in ws)
        load = 'fetchpriority="high"' if eager else 'loading="lazy"'
        c = f' class="{cls}"' if cls else ""
        return (f'<img src="{self.root}img/{name}-{ws[0]}.webp" srcset="{srcset}" sizes="{sizes}" '
                f'width="{lw}" height="{lh}" alt="{escape(alt)}" {load} decoding="async"{c}>')


# ---------------------------------------------------------------- gabarit
def header(ctx, current):
    def active(href):
        return ' aria-current="page"' if href == current else ""

    items = []
    mob = []
    for label, href, sub in NAV:
        if sub:
            subs = "".join(f'<li><a href="{ctx.u(h)}"{active(h)}>{escape(l)}</a></li>' for l, h in sub)
            items.append(f'<li class="has-sub"><button type="button" aria-haspopup="true">{label} {icon("chevron")}</button>'
                         f'<ul class="submenu">{subs}</ul></li>')
            mob.append(f'<li><a href="{ctx.u("")}#services">{label}</a></li>')
            mob += [f'<li class="sub"><a href="{ctx.u(h)}">{escape(l)}</a></li>' for l, h in sub]
        else:
            items.append(f'<li><a href="{ctx.u(href)}"{active(href)}>{label}</a></li>')
            mob.append(f'<li><a href="{ctx.u(href)}">{label} {icon("right")}</a></li>')
    return f"""<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="wrap header-in">
    <a class="brand" href="{ctx.u('')}" aria-label="Rod'Stores – accueil">
      <img src="{ctx.root}img/logo.webp" width="480" height="323" alt="Rod'Stores – portes, volets, fenêtres">
    </a>
    <nav class="nav" aria-label="Navigation principale"><ul>{''.join(items)}</ul></nav>
    <a class="btn btn--sm header-cta" href="tel:{SITE['phone_e164']}">{icon('phone')} {SITE['phone']}</a>
    <button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="menu-mobile">
      {icon('menu', 'icon i-menu')}{icon('x', 'icon i-close')}
    </button>
  </div>
</header>
<div class="mobile-menu" id="menu-mobile">
  <ul>{''.join(mob)}</ul>
  <a class="btn" href="tel:{SITE['phone_e164']}">{icon('phone')} Appeler le {SITE['phone']}</a>
</div>"""


def footer(ctx):
    services = "".join(f'<li><a href="{ctx.u(h)}">{escape(l)}</a></li>' for l, h in NAV[0][2])
    year = datetime.date.today().year
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="{ctx.root}img/logo.webp" width="480" height="323" alt="Rod'Stores" loading="lazy">
        <p>Entreprise familiale père &amp; fils basée à Roanne : pose, rénovation, motorisation et dépannage de fenêtres, volets roulants et portes dans toute la Loire et les départements limitrophes.</p>
        <div class="socials">
          <a href="{SITE['instagram']}" rel="noopener" target="_blank" aria-label="Instagram Rod'Stores">{icon('instagram')}</a>
          <a href="{SITE['facebook']}" rel="noopener" target="_blank" aria-label="Facebook Rod'Stores">{icon('facebook')}</a>
          <a href="{SITE['google']}" rel="noopener" target="_blank" aria-label="Avis Google Rod'Stores">{icon('google')}</a>
        </div>
      </div>
      <div>
        <h2>Nos services</h2>
        <ul>{services}</ul>
      </div>
      <div>
        <h2>Rod'Stores</h2>
        <ul>
          <li><a href="{ctx.u('nos-realisations/')}">Nos réalisations</a></li>
          <li><a href="{ctx.u('a-propos/')}">Entreprise père &amp; fils</a></li>
          <li><a href="{ctx.u('contact/')}">Devis gratuit</a></li>
          <li><a href="{ctx.u('mention-legales/')}">Mentions légales</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul class="nap">
          <li>{icon('phone')}<a href="tel:{SITE['phone_e164']}">{SITE['phone']}</a></li>
          <li>{icon('mail')}<a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li>{icon('pin')}<span>Roanne (42) – Loire et départements limitrophes</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {year} Rod'Stores – Fenêtres, volets roulants &amp; portes à Roanne</span>
      <span><a href="{ctx.u('mention-legales/')}">Mentions légales &amp; confidentialité</a></span>
    </div>
  </div>
</footer>
<div class="callbar">
  <a class="btn" href="tel:{SITE['phone_e164']}">{icon('phone')} Appeler</a>
  <a class="btn btn--ghost" href="{ctx.u('contact/')}">{icon('file')} Devis gratuit</a>
</div>
<dialog class="lightbox" id="lightbox" aria-label="Photo agrandie">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="">
  <p></p>
  <button class="lb-close" type="button" aria-label="Fermer">{icon('x')}</button>
  <button class="lb-nav lb-prev" type="button" aria-label="Photo précédente">{icon('left')}</button>
  <button class="lb-nav lb-next" type="button" aria-label="Photo suivante">{icon('right')}</button>
</dialog>"""


def business_schema():
    areas = ["Roanne", "Riorges", "Charlieu", "Feurs", "Montbrison", "Balbigny", "Saint-Just-en-Chevalet",
             "Saint-Étienne", "Lyon", "Vichy"]
    return {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": SITE["url"] + "/#entreprise",
        "name": "Rod'Stores",
        "alternateName": "Rod'Stores – Menuiseries & dépannage",
        "description": "Spécialiste fenêtres, volets roulants et portes à Roanne : installation, rénovation, motorisation et dépannage. Entreprise familiale père & fils, devis gratuit, sans sous-traitance.",
        "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/img/logo.png",
        "image": SITE["url"] + "/img/og-rodstores.jpg",
        "telephone": SITE["phone_e164"],
        "email": SITE["email"],
        "address": {"@type": "PostalAddress", "addressLocality": SITE["city"], "postalCode": SITE["postal"],
                    "addressRegion": "Auvergne-Rhône-Alpes", "addressCountry": "FR"},
        "areaServed": [{"@type": "City", "name": a} for a in areas] + [{"@type": "AdministrativeArea", "name": "Loire"}],
        "sameAs": [SITE["instagram"], SITE["facebook"]],
        "knowsAbout": ["Fenêtres PVC", "Fenêtres aluminium", "Volets roulants", "Motorisation de volets roulants",
                       "Dépannage de volets roulants", "Portes d'entrée", "Portes de garage", "Portails", "Velux",
                       "Moustiquaires", "Stores"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Services Rod'Stores",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": l, "url": SITE["url"] + "/" + h}}
                                for l, h in NAV[0][2]],
        },
    }


def breadcrumb_schema(trail):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE["url"] + "/" + h}
                            for i, (n, h) in enumerate(trail)],
    }


def faq_schema(faqs):
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs],
    }


def page(ctx, *, title, description, body, current="", schemas=(), og_image="img/og-rodstores.jpg", noindex=False):
    canonical = SITE["url"] + "/" + ctx.path
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#ff7a0a">
<meta name="geo.region" content="FR-42">
<meta name="geo.placename" content="Roanne">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Rod'Stores">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE['url']}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{ctx.root}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{ctx.root}img/apple-touch-icon.png">
<link rel="manifest" href="{ctx.root}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{ctx.root}css/style.css">
{ld}
</head>
<body>
{sprite()}
{header(ctx, current)}
<main id="contenu">
{body}
</main>
{footer(ctx)}
<script src="{ctx.root}js/main.js" defer></script>
</body>
</html>
"""


def write(path, html):
    target = os.path.join(OUT, path, "index.html") if not path.endswith(".html") else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return target


def main():
    import content
    today = datetime.date.today().isoformat()
    urls = []
    for p in content.PAGES:
        ctx = Ctx(p["path"], p.get("root"))
        html = page(ctx, **p["render"](ctx))
        write(p["path"], html)
        if not p.get("noindex"):
            urls.append((SITE["url"] + "/" + p["path"], p.get("priority", "0.7")))
        print("ok", p["path"] or "/")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>" for u, pr in urls]
    sm.append("</urlset>")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(sm) + "\n")
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    print(f"sitemap : {len(urls)} URL")


if __name__ == "__main__":
    main()
