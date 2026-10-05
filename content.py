"""Contenus des pages du site Rod'Stores (utilisé par build.py)."""
from html import escape

from build import SITE, Ctx, breadcrumb_schema, business_schema, faq_schema, icon, variants

TEL = f'tel:{SITE["phone_e164"]}'

# ---------------------------------------------------------------- données partagées
TESTIMONIALS = [
    ("Kelly D.", "Volet roulant pour Velux",
     "Nous avons fait appel à Rod'Stores pour l'installation d'un volet roulant pour notre Velux. Nous sommes très satisfaits de la prestation. Devis clair, installation rapide et soignée. Nous n'hésiterons pas à recommander cette entreprise auprès de notre entourage."),
    ("Julien P.", "Porte d'entrée & volets roulants",
     "Délais respectés, prestation également. Enfin une porte de maison qui ferme, où l'air chaud ou froid (hiver) ne passe plus, et surtout des volets roulants qui fonctionnent enfin correctement. Un très bon artisan, sympathique, dans les délais, puis surtout de bon conseil."),
    ("Client à Roanne", "Stores & moustiquaires",
     "La réalisation a été parfaite. Ça complète parfaitement la protection l'été, on peut allumer la lumière sans craindre les moustiques. La finition est parfaite et on est ravi."),
]

# (image, légende, catégories)
GALLERY = [
    ("atelier-apres", "Menuiseries aluminium RAL 7016 sur un atelier – après rénovation", "fenetres alu"),
    ("atelier-facade", "Châssis fixes et oscillo-battants alu, double vitrage G200", "fenetres alu"),
    ("atelier-cour", "Remplacement de verrières par des menuiseries alu", "fenetres alu"),
    ("atelier-interieur", "Vitrage G200 : lumière conservée, vue masquée", "fenetres alu"),
    ("craponne-porte-fenetre", "Porte-fenêtre neuve posée à Craponne (69)", "fenetres"),
    ("craponne-fenetre", "Fenêtre PVC oscillo-battante après remplacement", "fenetres"),
    ("craponne-volet-velux", "Volet roulant installé sur fenêtre de toit Velux", "velux volets"),
    ("craponne-velux", "Pose de Velux neuf en toiture tuiles", "velux"),
    ("craponne-tremie", "Création de trémie avant pose d'un Velux", "velux chantier"),
    ("craponne-chantier", "Chantier de rénovation des menuiseries à Craponne", "chantier"),
    ("velux-volet-solaire", "Volet roulant solaire extérieur Velux", "velux volets"),
    ("velux-toiture", "Volet solaire Velux posé sans gros travaux", "velux volets"),
    ("fenetre-roanne", "Remplacement de fenêtre à Roanne : dépose de l'ancien châssis", "fenetres chantier"),
    ("pere-fils", "Le père et le fils en intervention sur un chantier", "chantier"),
    ("porte-entree", "Porte d'entrée aluminium anthracite – région lyonnaise", "portes"),
    ("temoignage-moustiquaire", "Moustiquaire et stores posés chez un client à Roanne", "moustiquaires"),
]

FILTERS = [("all", "Tout"), ("fenetres", "Fenêtres"), ("velux", "Velux"), ("volets", "Volets roulants"),
           ("portes", "Portes"), ("moustiquaires", "Moustiquaires"), ("chantier", "Sur le chantier")]

INSTAGRAM = [
    ("ig-etapes-fenetre", "https://www.instagram.com/rod.stores/p/DbD8qn4FG99/", "Les étapes d'un remplacement de fenêtres"),
    ("velux-volet-solaire", "https://www.instagram.com/rod.stores/p/DdO_mKfiKLq/", "Avant / après : volet roulant solaire Velux"),
    ("ig-temoignages", "https://www.instagram.com/rod.stores/p/DbWBMv1jPUw/", "Témoignages clients Rod'Stores"),
    ("atelier-apres", "https://www.instagram.com/rod.stores/p/Dd6Ekcpjfsa/", "Avant / après : atelier en aluminium RAL 7016"),
    ("ig-depannage-vacances", "https://www.instagram.com/rod.stores/p/DcMFjgTlASN/", "Volet roulant en panne au retour de vacances"),
    ("ig-automne", "https://www.instagram.com/rod.stores/p/DdZUQQYiajz/", "Préparez votre maison pour l'hiver"),
]

ZONES = ["Roanne", "Riorges", "Mably", "Le Coteau", "Charlieu", "Balbigny", "Feurs", "Montbrison",
         "Saint-Just-en-Chevalet", "Saint-Étienne", "Vichy", "Lyon & ouest lyonnais"]


# ---------------------------------------------------------------- composants
def ba_slider(ctx, before, after, title, text, alt_before, alt_after):
    return f"""<figure class="ba reveal">
  <div class="ba-frame">
    {ctx.img(after, alt_after, "(min-width: 900px) 560px, 100vw")}
    {ctx.img(before, alt_before, "(min-width: 900px) 560px, 100vw", cls="ba-before")}
    <span class="ba-label ba-label--before">Avant</span><span class="ba-label ba-label--after">Après</span>
    <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Comparer avant et après : {escape(title)}">
    <span class="ba-handle"></span>
  </div>
  <figcaption><h3>{title}</h3><p>{text}</p></figcaption>
</figure>"""


def ba_atelier(ctx):
    return ba_slider(ctx, "atelier-avant", "atelier-apres", "Atelier : verrières remplacées par de l'aluminium",
                     "Anciennes verrières vieillissantes remplacées par des menuiseries alu RAL 7016, châssis fixes et oscillo-battants, double vitrage G200 qui garde la lumière tout en masquant la vue.",
                     "Avant : anciennes verrières vétustes de l'atelier, vitres cassées",
                     "Après : nouvelles menuiseries aluminium gris anthracite RAL 7016")


def ba_velux(ctx):
    return ba_slider(ctx, "velux-avant", "velux-apres", "Velux : du store intérieur au volet solaire",
                     "Un store intérieur abîmé remplacé par un volet roulant solaire extérieur Velux : meilleure protection contre la chaleur, occultation efficace, sans raccordement électrique ni gros travaux.",
                     "Avant : fenêtre de toit Velux avec store intérieur abîmé",
                     "Après : volet roulant solaire Velux installé, vue depuis l'intérieur")


def gallery_item(ctx, name, caption, cats="", sizes="(min-width: 1100px) 280px, (min-width: 700px) 33vw, 50vw"):
    return f"""<figure class="g-item reveal" data-cat="{cats}">
  <button type="button" data-full="{ctx.src(name)}" data-caption="{escape(caption)}" aria-label="Agrandir : {escape(caption)}">
    {ctx.img(name, caption, sizes)}
  </button>
  <figcaption>{escape(caption)}</figcaption>
</figure>"""


def stars():
    return '<div class="stars" aria-label="Avis 5 étoiles">' + icon("star") * 5 + "</div>"


def testimonials(ctx, items=TESTIMONIALS):
    cards = "".join(f"""<figure class="quote reveal">
  {stars()}
  <blockquote><p>« {escape(t)} »</p></blockquote>
  <figcaption><span class="avatar" aria-hidden="true">{escape(n[0])}</span><div>{escape(n)}<span>{escape(s)}</span></div></figcaption>
</figure>""" for n, s, t in items)
    return f"""<div class="quotes">{cards}</div>
<div class="reviews-cta">
  <a class="btn btn--ghost" href="{SITE['google']}" target="_blank" rel="noopener">{icon('google')} Lire nos avis Google</a>
  <a class="btn btn--ghost" href="{SITE['instagram']}" target="_blank" rel="noopener">{icon('instagram')} Nos chantiers sur Instagram</a>
</div>"""


def faq_block(faqs):
    items = "".join(f"<details><summary>{escape(q)}</summary><div><p>{a}</p></div></details>" for q, a in faqs)
    return f'<div class="faq">{items}</div>'


def cta_band(ctx, title="Un projet ou un dépannage ?", text="Devis gratuit et sans engagement. Un interlocuteur unique, du premier appel à la fin du chantier."):
    return f"""<section class="section" aria-label="Demande de devis">
  <div class="wrap">
    <div class="cta-band reveal">
      <div><h2>{title}</h2><p>{text}</p></div>
      <div class="btn-row">
        <a class="btn" href="{TEL}">{icon('phone')} {SITE['phone']}</a>
        <a class="btn btn--ghost" href="{ctx.u('contact/')}">Demander un devis</a>
      </div>
    </div>
  </div>
</section>"""


def crumbs(ctx, trail):
    lis = [f'<li><a href="{ctx.u("")}">Accueil</a></li>']
    for i, (n, h) in enumerate(trail):
        lis.append(f'<li><span aria-current="page">{escape(n)}</span></li>' if i == len(trail) - 1
                   else f'<li><a href="{ctx.u(h)}">{escape(n)}</a></li>')
    return f'<nav class="crumbs" aria-label="Fil d\'Ariane"><ol>{"".join(lis)}</ol></nav>'


def page_hero(ctx, trail, eyebrow, h1, lead, image=None, alt="", extra=""):
    media = f'<div class="page-hero-media">{ctx.img(image, alt, "(min-width: 900px) 440px, 100vw", eager=True)}</div>' if image else ""
    return f"""<section class="page-hero">
  <div class="wrap">
    {crumbs(ctx, trail)}
    <div class="page-hero-grid">
      <div>
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        <div class="btn-row">
          <a class="btn" href="{TEL}">{icon('phone')} {SITE['phone']}</a>
          <a class="btn btn--ghost" href="{ctx.u('contact/')}">Devis gratuit</a>
        </div>
        {extra}
      </div>
      {media}
    </div>
  </div>
</section>"""


def aside_card(ctx, title="Devis gratuit", text="Décrivez votre projet, nous vous rappelons rapidement pour fixer une visite."):
    return f"""<aside class="aside-sticky">
  <div class="aside-card">
    <h3>{title}</h3>
    <p>{text}</p>
    <a class="btn" href="{TEL}">{icon('phone')} {SITE['phone']}</a>
    <a class="btn btn--ghost" href="{ctx.u('contact/')}">Demande en ligne</a>
    <ul>
      <li>{icon('check')} Devis gratuit et sans engagement</li>
      <li>{icon('check')} Pose par nos soins, sans sous-traitance</li>
      <li>{icon('check')} Interlocuteur unique</li>
      <li>{icon('check')} Loire &amp; départements limitrophes</li>
    </ul>
  </div>
</aside>"""


def feature_list(items):
    return '<div class="feature-list">' + "".join(
        f'<div class="feature"><h3>{icon(ic)} {escape(t)}</h3><p>{d}</p></div>' for ic, t, d in items) + "</div>"


def related_gallery(ctx, names):
    lookup = {g[0]: g for g in GALLERY}
    items = "".join(gallery_item(ctx, n, lookup[n][1]) for n in names)
    return f"""<section class="section section--tint">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Nos réalisations</p><h2>Quelques chantiers récents</h2>
    <p class="lead">Des photos prises par nos soins sur nos chantiers dans la Loire et la région lyonnaise.</p></div>
    <div class="gallery">{items}</div>
    <p style="margin-top:24px"><a class="btn btn--ghost" href="{ctx.u('nos-realisations/')}">Voir toutes nos réalisations {icon('arrow')}</a></p>
  </div>
</section>"""


def service_page(ctx, *, path, name, title, description, eyebrow, h1, lead, image, alt, body, faqs, gallery, cta_title=None):
    trail = [(name, path)]
    html = page_hero(ctx, trail, eyebrow, h1, lead, image, alt) + f"""
<section class="section">
  <div class="wrap content-grid">
    <div class="prose">{body}</div>
    {aside_card(ctx)}
  </div>
</section>
{related_gallery(ctx, gallery)}
<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center"><p class="eyebrow">Questions fréquentes</p><h2>{escape(name)} : vos questions</h2></div>
    {faq_block(faqs)}
  </div>
</section>
{cta_band(ctx, cta_title or "Parlons de votre projet")}"""
    return dict(title=title, description=description, body=html, current=path,
                schemas=[business_schema(), breadcrumb_schema(trail), faq_schema(faqs),
                         {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": name,
                          "provider": {"@id": SITE["url"] + "/#entreprise"},
                          "areaServed": [{"@type": "City", "name": z} for z in ["Roanne", "Saint-Étienne", "Lyon", "Vichy", "Montbrison"]],
                          "url": SITE["url"] + "/" + path}])


# ---------------------------------------------------------------- accueil
HOME_FAQ = [
    ("Le devis est-il gratuit ?",
     "Oui. Le devis est gratuit et sans engagement. Nous nous déplaçons pour prendre les mesures et vous conseiller sur la solution la plus adaptée à votre maison et à votre budget."),
    ("Dans quelle zone intervenez-vous ?",
     "Nous sommes basés à Roanne et intervenons dans toute la Loire (Roanne, Riorges, Charlieu, Feurs, Montbrison, Saint-Étienne…) et les départements limitrophes, notamment vers Vichy et Lyon."),
    ("Faites-vous appel à des sous-traitants ?",
     "Non. Chaque chantier est réalisé et suivi personnellement par le père et le fils, sans sous-traitance. Vous gardez un interlocuteur unique du devis à la fin des travaux."),
    ("Mon volet roulant est bloqué, que dois-je faire ?",
     "Évitez de forcer sur le volet : vous risqueriez d'aggraver la panne. Appelez-nous au 07 68 16 02 68 : nous diagnostiquons et réparons tous types de volets roulants, manuels ou motorisés."),
    ("Peut-on motoriser un volet roulant existant ?",
     "Dans la plupart des cas, oui. Après vérification du coffre et du tablier, nous remplaçons la manœuvre manuelle par un moteur filaire, radio ou solaire, avec télécommande."),
    ("Intervenez-vous sur les fenêtres de toit Velux ?",
     "Oui, sur tous types de fenêtres de toit, anciennes ou récentes : remplacement, pose de volet roulant solaire, stores, réparation."),
]


def home(ctx):
    services = [
        ("fenetres/", "craponne-fenetre", "Fenêtres", "Fenêtres sur mesure PVC, aluminium ou bois : remplacement en rénovation et pose en neuf.", ""),
        ("volets-roulants/", "velux-volet-solaire", "Volets roulants", "Pose, remplacement et motorisation de volets roulants filaires, radio ou solaires.", ""),
        ("depannage-volets-roulants/", None, "Dépannage volets roulants", "Volet bloqué, moteur en panne, sangle cassée : intervention rapide pour remettre en service.", "urgent"),
        ("porte/", "porte-entree", "Portes d'entrée", "Portes alliant sécurité, isolation thermique et esthétique, en aluminium ou PVC.", ""),
        ("portes-de-garage/", "porte-garage", "Portes de garage & portails", "Portes sectionnelles, enroulables et portails, manuels ou motorisés.", ""),
        ("velux-fenetres-de-toit/", "craponne-velux", "Velux & fenêtres de toit", "Remplacement de Velux, volets roulants solaires et stores pour vos combles.", ""),
        ("moustiquaires/", "temoignage-moustiquaire", "Moustiquaires & stores", "Moustiquaires sur mesure enroulables ou plissées, stores intérieurs et extérieurs.", ""),
    ]
    cards = []
    for href, img, t, d, kind in services:
        if kind == "urgent":
            cards.append(f"""<article class="card card--urgent reveal">
  <div class="card-body" style="padding:26px 24px">
    <span class="tag">Urgence</span>
    <h3 style="margin-top:10px">{t}</h3><p>{d}</p>
    <ul class="checklist" style="margin-top:12px">
      <li>{icon('check')} Volet bloqué ouvert ou fermé</li>
      <li>{icon('check')} Moteur ou télécommande en panne</li>
      <li>{icon('check')} Lame cassée, tablier décalé</li>
    </ul>
    <a class="card-link" href="{ctx.u(href)}">Dépannage rapide {icon('arrow')}</a>
  </div>
</article>""")
        else:
            cards.append(f"""<article class="card reveal">
  <div class="card-media">{ctx.img(img, t, "(min-width: 1000px) 380px, (min-width: 640px) 50vw, 100vw")}</div>
  <div class="card-body"><h3>{t}</h3><p>{d}</p><a class="card-link" href="{ctx.u(href)}">Découvrir {icon('arrow')}</a></div>
</article>""")
    lookup = {g[0]: g for g in GALLERY}
    recent = "".join(gallery_item(ctx, n, lookup[n][1]) for n in
                     ["atelier-facade", "craponne-porte-fenetre", "craponne-volet-velux", "porte-entree", "velux-toiture", "fenetre-roanne"])
    insta = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="Instagram : {escape(c)}">{ctx.img(n, c, "(min-width: 900px) 180px, 33vw")}</a>'
                    for n, u, c in INSTAGRAM)
    zones = "".join(f"<li>{icon('pin')}{z}</li>" for z in ZONES)
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Roanne · Loire · départements limitrophes</p>
      <h1>Fenêtres, volets roulants &amp; portes : <em>pose, rénovation et dépannage</em></h1>
      <p class="lead">Rod'Stores, entreprise familiale père &amp; fils basée à Roanne, installe, remplace, motorise et répare vos menuiseries. Des solutions durables, un excellent rapport qualité-prix et une intervention rapide.</p>
      <div class="btn-row">
        <a class="btn" href="{TEL}">{icon('phone')} {SITE['phone']}</a>
        <a class="btn btn--ghost" href="{ctx.u('contact/')}">Devis gratuit</a>
      </div>
      <ul class="ticks">
        <li>{icon('check-circle')} Devis gratuit et sans engagement</li>
        <li>{icon('check-circle')} Chaque chantier suivi personnellement, sans sous-traitance</li>
        <li>{icon('check-circle')} Dépannage rapide de volets roulants</li>
      </ul>
    </div>
    <div class="hero-media">
      <figure class="m1">{ctx.img("pere-fils", "Le père et le fils de Rod'Stores posant une fenêtre sur un chantier", "(min-width: 900px) 320px, 58vw", eager=True)}</figure>
      <figure class="m2">{ctx.img("atelier-apres", "Menuiseries aluminium anthracite posées par Rod'Stores", "(min-width: 900px) 230px, 40vw", eager=True)}</figure>
      <figure class="m3">{ctx.img("craponne-volet-velux", "Volet roulant sur fenêtre de toit installé par Rod'Stores", "(min-width: 900px) 230px, 40vw")}</figure>
      <div class="hero-badge"><span class="dot">{icon('users')}</span><div><strong>Père &amp; fils</strong>Un interlocuteur unique sur chaque chantier</div></div>
    </div>
  </div>
</section>

<section class="trust" aria-label="Nos engagements">
  <div class="wrap">
    <ul>
      <li><span class="ic">{icon('file')}</span><div>Devis gratuit<small>Clair et sans engagement</small></div></li>
      <li><span class="ic">{icon('users')}</span><div>Entreprise familiale<small>Père &amp; fils, à Roanne</small></div></li>
      <li><span class="ic">{icon('shield')}</span><div>Sans sous-traitance<small>Qualité contrôlée</small></div></li>
      <li><span class="ic">{icon('zap')}</span><div>Intervention rapide<small>Pose &amp; dépannage</small></div></li>
    </ul>
  </div>
</section>

<section class="section" id="services">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Nos services</p>
      <h2>Des solutions complètes pour fermer et protéger votre maison</h2>
      <p class="lead">En neuf comme en rénovation, nous intervenons sur l'ensemble des équipements de fermeture : fenêtres, portes, volets roulants, portes de garage, portails, fenêtres de toit et moustiquaires.</p>
    </div>
    <div class="grid grid--3">{''.join(cards)}
      <article class="card reveal" style="justify-content:center">
        <div class="card-body" style="padding:26px 24px;justify-content:center">
          <h3>Un autre projet ?</h3>
          <p>Stores, menuiserie intérieure, réparation… Parlez-nous de votre besoin, nous trouverons la solution adaptée.</p>
          <a class="card-link" href="{ctx.u('contact/')}">Nous contacter {icon('arrow')}</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark" id="avant-apres">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Avant / après</p>
      <h2>La différence se voit tout de suite</h2>
      <p class="lead">Faites glisser le curseur pour comparer. Ce sont de vrais chantiers Rod'Stores, photographiés par nos soins.</p>
    </div>
    <div class="ba-grid">{ba_atelier(ctx)}{ba_velux(ctx)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Réalisations récentes</p>
      <h2>Ils nous ont fait confiance pour leurs travaux</h2>
      <p class="lead">Fenêtres, portes, Velux, volets roulants : un aperçu de nos chantiers dans la Loire et la région lyonnaise.</p>
    </div>
    <div class="gallery">{recent}</div>
    <p style="margin-top:24px"><a class="btn btn--ghost" href="{ctx.u('nos-realisations/')}">Voir toutes nos réalisations {icon('arrow')}</a></p>
  </div>
</section>

<section class="section section--tint" id="entreprise">
  <div class="wrap split">
    <div class="split-media reveal">
      {ctx.img("pere-fils", "Le père et le fils de Rod'Stores en intervention : pose d'une fenêtre", "(min-width: 900px) 540px, 100vw")}
      <div class="stamp"><small>Basés à</small>Roanne</div>
    </div>
    <div class="reveal">
      <p class="eyebrow">Qui sommes-nous</p>
      <h2>Une entreprise père &amp; fils</h2>
      <p>Rod'Stores est une entreprise familiale basée à Roanne, fondée par un père et son fils. L'un apporte plusieurs années d'expérience terrain et une maîtrise technique des installations et dépannages complexes. L'autre structure l'entreprise autour d'un fonctionnement clair : devis rapides, interventions réactives et suivi rigoureux des chantiers.</p>
      <p>Cette organisation à taille humaine garantit un interlocuteur unique, une prise de décision rapide et un contrôle direct de la qualité. Chaque chantier est suivi personnellement, sans sous-traitance, avec un objectif simple : un travail fiable et durable.</p>
      <ul class="checklist">
        <li>{icon('check')} Conseils honnêtes, adaptés à votre maison et à votre budget</li>
        <li>{icon('check')} Pose soignée : étanchéité, réglages, finitions</li>
        <li>{icon('check')} Chantier propre et délais respectés</li>
      </ul>
      <a class="btn btn--ghost" href="{ctx.u('a-propos/')}">En savoir plus {icon('arrow')}</a>
    </div>
  </div>
</section>

<section class="section" id="avis">
  <div class="wrap">
    <div class="section-head section-head--center">
      <p class="eyebrow">Avis clients</p>
      <h2>Le meilleur avis, c'est celui de nos clients</h2>
      <p class="lead" style="margin-inline:auto">Merci à celles et ceux qui prennent le temps de partager leur expérience avec Rod'Stores.</p>
    </div>
    {testimonials(ctx)}
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Notre méthode</p>
      <h2>De la dépose à la finition, une pose réalisée avec précision</h2>
      <p class="lead">Une fenêtre performante, ce n'est pas seulement une question de produit : c'est surtout une pose rigoureuse.</p>
    </div>
    <ol class="steps">
      <li class="reveal"><h3>Prise de contact</h3><p>Par téléphone ou en ligne, vous nous décrivez votre projet ou votre panne.</p></li>
      <li class="reveal"><h3>Visite &amp; devis gratuit</h3><p>Prise de mesures sur place, conseils et devis clair, sans engagement.</p></li>
      <li class="reveal"><h3>Pose soignée</h3><p>Dépose propre, pose précise, étanchéité et réglages contrôlés.</p></li>
      <li class="reveal"><h3>Finitions &amp; suivi</h3><p>Habillages, nettoyage du chantier et explications d'utilisation.</p></li>
    </ol>
  </div>
</section>

<section class="section" id="zones">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Zone d'intervention</p>
      <h2>Menuisier à Roanne, dans la Loire et au-delà</h2>
      <p>Depuis Roanne, nous intervenons dans toute la Loire et les départements limitrophes pour la pose, la rénovation et le dépannage de vos fenêtres, volets roulants et portes.</p>
      <ul class="zones">{zones}</ul>
    </div>
    <div class="map-card reveal" aria-hidden="true">
      <svg class="map" viewBox="0 0 400 300">
        <defs><radialGradient id="g" r=".5"><stop offset="0" stop-color="#ff7a0a" stop-opacity=".45"/><stop offset="1" stop-color="#ff7a0a" stop-opacity="0"/></radialGradient></defs>
        <circle cx="170" cy="110" r="130" fill="url(#g)"/>
        <g fill="none" stroke="rgba(255,255,255,.18)" stroke-dasharray="4 6"><circle cx="170" cy="110" r="60"/><circle cx="170" cy="110" r="120"/></g>
        <g font-family="Barlow, sans-serif" font-size="13" fill="#e9ecee">
          <circle cx="170" cy="110" r="8" fill="#ff7a0a"/><text x="184" y="106" font-weight="700" font-size="17" fill="#fff">Roanne</text>
          <circle cx="205" cy="62" r="4" fill="#fff"/><text x="214" y="66">Charlieu</text>
          <circle cx="120" cy="40" r="4" fill="#fff"/><text x="70" y="30">Vichy</text>
          <circle cx="210" cy="160" r="4" fill="#fff"/><text x="219" y="164">Balbigny</text>
          <circle cx="200" cy="200" r="4" fill="#fff"/><text x="209" y="204">Feurs</text>
          <circle cx="170" cy="240" r="4" fill="#fff"/><text x="90" y="244">Montbrison</text>
          <circle cx="225" cy="280" r="4" fill="#fff"/><text x="234" y="284">Saint-Étienne</text>
          <circle cx="330" cy="200" r="4" fill="#fff"/><text x="340" y="204">Lyon</text>
          <circle cx="95" cy="120" r="4" fill="#fff"/><text x="16" y="140">St-Just-en-Ch.</text>
        </g>
      </svg>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="section-head" style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:16px;max-width:none">
      <div><p class="eyebrow">Instagram</p><h2 style="margin:0">Suivez nos chantiers @rod.stores</h2></div>
      <a class="btn btn--ghost" href="{SITE['instagram']}" target="_blank" rel="noopener">{icon('instagram')} Nous suivre</a>
    </div>
    <div class="insta">{insta}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center"><p class="eyebrow">FAQ</p><h2>Questions fréquentes</h2></div>
    {faq_block(HOME_FAQ)}
  </div>
</section>
{cta_band(ctx)}"""
    return dict(
        title="Rod'Stores – Fenêtres, volets roulants & portes à Roanne",
        description="Rod'Stores, entreprise père & fils à Roanne : pose, rénovation, motorisation et dépannage de fenêtres, volets roulants, portes et Velux dans la Loire. Devis gratuit.",
        body=body, current="", schemas=[business_schema(), faq_schema(HOME_FAQ),
                                        {"@context": "https://schema.org", "@type": "WebSite", "name": "Rod'Stores", "url": SITE["url"] + "/", "inLanguage": "fr-FR"}])


# ---------------------------------------------------------------- réalisations
def realisations(ctx):
    trail = [("Nos réalisations", "nos-realisations/")]
    filters = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{l}</button>' for k, l in FILTERS)
    items = "".join(gallery_item(ctx, n, c, cats, "(min-width: 1100px) 280px, (min-width: 700px) 33vw, 50vw") for n, c, cats in GALLERY)

    def proj_imgs(names):
        lookup = {g[0]: g for g in GALLERY}
        return '<div class="gallery" style="grid-template-columns:1fr 1fr">' + "".join(
            gallery_item(ctx, n, lookup[n][1], "", "(min-width: 900px) 320px, 50vw") for n in names) + "</div>"

    projects = f"""
<article class="project">
  <div class="project-text">
    <div class="project-meta"><span class="chip">{icon('pin')} Loire</span><span class="chip">Menuiseries aluminium</span></div>
    <h3>Rénovation d'un atelier : des verrières à l'aluminium RAL 7016</h3>
    <p>Les anciennes verrières de cet atelier étaient vieillissantes, avec des vitrages cassés. Nous les avons remplacées par des menuiseries en aluminium gris anthracite RAL 7016.</p>
    <ul class="checklist">
      <li>{icon('check')} Châssis fixes et ouvrants oscillo-battants : luminosité et aération</li>
      <li>{icon('check')} Double vitrage G200 : lumière naturelle conservée, vue sur l'intérieur masquée</li>
      <li>{icon('check')} Façade modernisée et confort amélioré au quotidien</li>
    </ul>
  </div>
  {proj_imgs(["atelier-apres", "atelier-facade", "atelier-cour", "atelier-interieur"])}
</article>
<article class="project">
  <div class="project-text">
    <div class="project-meta"><span class="chip">{icon('pin')} Craponne (69)</span><span class="chip">Rénovation complète</span></div>
    <h3>Changement des menuiseries d'une maison près de Lyon</h3>
    <p>Dans le cadre de la rénovation de cette habitation à Craponne, nous sommes intervenus sur l'ensemble des menuiseries extérieures.</p>
    <ul class="checklist">
      <li>{icon('check')} Remplacement des fenêtres et portes-fenêtres</li>
      <li>{icon('check')} Installation de volets roulants</li>
      <li>{icon('check')} Création de trémie et pose de Velux</li>
    </ul>
    <p>Résultat : meilleure isolation, étanchéité renforcée, meilleures performances énergétiques et une maison modernisée.</p>
  </div>
  {proj_imgs(["craponne-porte-fenetre", "craponne-fenetre", "craponne-tremie", "craponne-volet-velux"])}
</article>
<article class="project">
  <div class="project-text">
    <div class="project-meta"><span class="chip">Fenêtre de toit</span><span class="chip">Volet solaire</span></div>
    <h3>Velux : volet roulant solaire à la place d'un store abîmé</h3>
    <p>Un petit changement, un vrai gain de confort : le store intérieur vétuste a laissé place à un volet roulant solaire extérieur Velux.</p>
    <ul class="checklist">
      <li>{icon('check')} Meilleure protection contre la chaleur sous les combles</li>
      <li>{icon('check')} Occultation efficace</li>
      <li>{icon('check')} Fonctionnement solaire autonome, aucun raccordement électrique</li>
      <li>{icon('check')} Pas de gros travaux ni de dégradation intérieure</li>
    </ul>
  </div>
  {proj_imgs(["velux-volet-solaire", "velux-toiture"])}
</article>
<article class="project">
  <div class="project-text">
    <div class="project-meta"><span class="chip">{icon('pin')} Roanne</span><span class="chip">Stores &amp; moustiquaires</span></div>
    <h3>Stores et moustiquaires : « La finition est parfaite »</h3>
    <p>Après la pose de ses stores et de ses moustiquaires, notre client nous a partagé son retour : « La réalisation a été parfaite. Ça complète parfaitement la protection l'été, on peut allumer la lumière sans craindre les moustiques. »</p>
    <a class="btn btn--ghost" href="https://www.instagram.com/rod.stores/reel/DeFOrZwEV2x/" target="_blank" rel="noopener">{icon('instagram')} Voir la vidéo du témoignage</a>
  </div>
  {proj_imgs(["temoignage-moustiquaire", "porte-entree"])}
</article>"""

    body = page_hero(ctx, trail, "Nos réalisations", "Nos chantiers en photos : fenêtres, volets, portes, Velux",
                     "Des photos réelles de nos chantiers dans la Loire et la région lyonnaise. Avant/après, détails de pose et retours clients : jugez sur pièce.") + f"""
<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Avant / après</p><h2>Comparez par vous-même</h2>
    <p class="lead">Faites glisser le curseur sur chaque photo.</p></div>
    <div class="ba-grid">{ba_atelier(ctx)}{ba_velux(ctx)}</div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Projets détaillés</p><h2>Quelques chantiers racontés</h2></div>
    {projects}
  </div>
</section>
<section class="section section--tint" id="galerie">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Galerie</p><h2>Toutes nos photos de chantier</h2></div>
    <div class="filters" role="group" aria-label="Filtrer les réalisations">{filters}</div>
    <div class="gallery gallery--4">{items}</div>
    <p style="margin-top:28px;text-align:center"><a class="btn btn--ghost" href="{SITE['instagram']}" target="_blank" rel="noopener">{icon('instagram')} Plus de chantiers sur Instagram</a></p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center"><p class="eyebrow">Avis clients</p><h2>Ce que disent nos clients</h2></div>
    {testimonials(ctx)}
  </div>
</section>
{cta_band(ctx, "Votre projet sera notre prochaine réalisation", "Devis gratuit et sans engagement, partout dans la Loire et les départements limitrophes.")}"""
    gallery_schema = {
        "@context": "https://schema.org", "@type": "ImageGallery", "name": "Réalisations Rod'Stores",
        "image": [{"@type": "ImageObject", "contentUrl": f"{SITE['url']}/img/{n}-{variants(n)[-1]}.webp", "caption": c}
                  for n, c, _ in GALLERY],
    }
    return dict(title="Nos réalisations avant/après | Rod'Stores Roanne",
                description="Photos avant/après de nos chantiers : fenêtres alu et PVC, volets roulants, Velux, portes d'entrée et moustiquaires posés par Rod'Stores dans la Loire et près de Lyon.",
                body=body, current="nos-realisations/",
                schemas=[business_schema(), breadcrumb_schema(trail), gallery_schema])


# ---------------------------------------------------------------- pages services
def fenetres(ctx):
    body = f"""
<h2>Remplacement et pose de fenêtres sur mesure</h2>
<p>Être spécialiste des fenêtres, ce n'est pas seulement poser un produit. C'est comprendre votre maison, vos besoins en isolation thermique et acoustique, votre confort au quotidien, la lumière et l'aération, mais aussi les contraintes de façade, de coffre existant ou de rénovation énergétique.</p>
<p>Rod'Stores installe et remplace vos fenêtres et portes-fenêtres sur mesure à Roanne et dans toute la Loire, en rénovation comme en construction neuve.</p>
{feature_list([
    ("home", "PVC", "Excellent isolant, facile d'entretien et au meilleur rapport qualité-prix."),
    ("shield", "Aluminium", "Profils fins, grandes surfaces vitrées, teintes comme le RAL 7016 anthracite."),
    ("sun", "Bois", "Le charme et la chaleur du bois, idéal pour l'habitat ancien."),
    ("ruler", "Sur mesure", "Oscillo-battant, coulissant, fixe, cintré : adapté à chaque ouverture."),
])}
<h2>Les étapes d'un remplacement de fenêtres</h2>
<p>Une fenêtre performante, c'est surtout une pose réalisée avec précision. Chaque intervention est pensée pour assurer une parfaite étanchéité, un fonctionnement fluide et une finition soignée :</p>
<ul class="checklist">
  <li>{icon('check')} <span><strong>Prise de cotes</strong> précise sur place et choix des options (vitrage, couleur, ouvrants).</span></li>
  <li>{icon('check')} <span><strong>Dépose</strong> soignée de l'ancienne menuiserie, en protégeant votre intérieur.</span></li>
  <li>{icon('check')} <span><strong>Pose et calage</strong> de la nouvelle fenêtre, d'aplomb et de niveau.</span></li>
  <li>{icon('check')} <span><strong>Étanchéité</strong> à l'air et à l'eau, puis réglage des ouvrants.</span></li>
  <li>{icon('check')} <span><strong>Finitions</strong> : habillages, joints, nettoyage du chantier.</span></li>
</ul>
<h2>Les bénéfices de nouvelles fenêtres</h2>
{feature_list([
    ("thermo", "Isolation thermique", "Moins de déperditions de chaleur en hiver, plus de fraîcheur en été."),
    ("volume", "Confort acoustique", "Un intérieur plus calme grâce au double vitrage et à une pose étanche."),
    ("lock", "Sécurité", "Ferrures et vitrages adaptés pour mieux protéger votre logement."),
    ("sun", "Lumière", "Des profils plus fins pour plus de clarté dans vos pièces."),
])}
<div class="alert">{icon('message')}<p><strong>Vitrages spéciaux :</strong> pour un atelier ou une salle de bain, un vitrage dépoli (type G200) laisse passer la lumière tout en masquant la vue. <a href="{ctx.u('nos-realisations/')}">Voir notre chantier d'atelier</a>.</p></div>
"""
    faqs = [
        ("Combien de temps dure le remplacement d'une fenêtre ?", "La plupart des remplacements se font dans la journée par fenêtre, sans gros travaux. Nous vous indiquons la durée exacte du chantier dans le devis."),
        ("PVC ou aluminium : que choisir ?", "Le PVC offre une excellente isolation au meilleur prix. L'aluminium permet des profils plus fins et des grandes baies, avec un rendu très contemporain. Nous vous conseillons selon votre maison et votre budget."),
        ("Faut-il changer les volets en même temps que les fenêtres ?", "Ce n'est pas obligatoire, mais c'est souvent le bon moment pour installer des volets roulants ou motoriser les volets existants, et profiter d'un seul chantier."),
        ("Intervenez-vous en dehors de Roanne ?", "Oui, dans toute la Loire (Riorges, Charlieu, Feurs, Montbrison, Saint-Étienne…) et les départements limitrophes, jusqu'à la région lyonnaise."),
    ]
    return service_page(ctx, path="fenetres/", name="Fenêtres",
                        title="Fenêtres sur mesure à Roanne – PVC, alu, bois | Rod'Stores",
                        description="Remplacement et pose de fenêtres sur mesure PVC, aluminium ou bois à Roanne et dans la Loire. Isolation, étanchéité, pose soignée sans sous-traitance. Devis gratuit.",
                        eyebrow="Fenêtres sur mesure", h1="Fenêtres sur mesure à Roanne : pose et remplacement",
                        lead="PVC, aluminium ou bois : nous remplaçons vos fenêtres pour gagner en isolation, en confort et en lumière, avec une pose précise et des finitions soignées.",
                        image="craponne-porte-fenetre", alt="Porte-fenêtre neuve posée par Rod'Stores", body=body, faqs=faqs,
                        gallery=["atelier-facade", "craponne-fenetre", "fenetre-roanne"])


def volets(ctx):
    body = f"""
<h2>Pose et remplacement de volets roulants</h2>
<p>Le volet roulant protège votre maison du froid, de la chaleur et des regards, tout en renforçant la sécurité. Rod'Stores installe des volets roulants adaptés à chaque ouverture, en neuf comme en rénovation, à Roanne et dans toute la Loire.</p>
{feature_list([
    ("home", "Volet rénovation", "Coffre extérieur ou intérieur posé sur la fenêtre existante, sans gros travaux."),
    ("ruler", "Volet traditionnel", "Coffre intégré au bâti pour la construction neuve ou les grosses rénovations."),
    ("sun", "Volet solaire", "Fonctionnement autonome grâce à un panneau solaire, sans raccordement électrique."),
    ("shield", "Lames alu ou PVC", "Tabliers isolants, coloris au choix pour s'accorder à votre façade."),
])}
<h2>Motorisation de volets roulants</h2>
<p>Fini les manivelles et les sangles qui cassent : nous motorisons vos volets roulants existants dans la plupart des cas, après vérification du coffre et du tablier.</p>
<ul class="checklist">
  <li>{icon('check')} Moteur filaire avec interrupteur, ou radio avec télécommande</li>
  <li>{icon('check')} Motorisation solaire, idéale quand il n'y a pas d'électricité à proximité</li>
  <li>{icon('check')} Centralisation possible de tous les volets de la maison</li>
</ul>
<h2>Pourquoi installer des volets roulants ?</h2>
{feature_list([
    ("thermo", "Isolation", "Une lame d'air supplémentaire devant la fenêtre, utile hiver comme été."),
    ("sun", "Protection solaire", "Gardez la fraîcheur dans les pièces exposées et sous les combles."),
    ("lock", "Sécurité", "Un frein efficace contre les intrusions, surtout en votre absence."),
    ("zap", "Confort", "Ouverture et fermeture d'un geste, même à distance."),
])}
<div class="alert">{icon('wrench')}<p><strong>Votre volet est en panne ?</strong> Consultez notre page <a href="{ctx.u('depannage-volets-roulants/')}">dépannage de volets roulants</a> : nous intervenons rapidement.</p></div>
"""
    faqs = [
        ("Peut-on installer un volet roulant sur une fenêtre existante ?", "Oui, grâce au volet roulant rénovation : le coffre se pose devant ou sous le linteau, sans toucher à la maçonnerie ni changer la fenêtre."),
        ("Volet roulant solaire : est-ce fiable ?", "Oui. La batterie se recharge même par temps couvert et assure le fonctionnement plusieurs jours sans soleil. C'est la solution idéale sans raccordement électrique."),
        ("Peut-on motoriser un volet manuel ?", "Dans la plupart des cas, oui. Nous vérifions l'état du coffre, de l'axe et du tablier, puis remplaçons la manœuvre par un moteur adapté."),
    ]
    return service_page(ctx, path="volets-roulants/", name="Volets roulants",
                        title="Volets roulants à Roanne – pose & motorisation | Rod'Stores",
                        description="Installation, remplacement et motorisation de volets roulants (filaires, radio, solaires) à Roanne et dans la Loire. Pose sans sous-traitance, devis gratuit.",
                        eyebrow="Volets roulants", h1="Volets roulants à Roanne : pose, remplacement et motorisation",
                        lead="Volets rénovation, traditionnels ou solaires : gagnez en isolation, en sécurité et en confort, avec une installation soignée par une entreprise locale.",
                        image="craponne-volet-velux", alt="Volet roulant installé par Rod'Stores", body=body, faqs=faqs,
                        gallery=["velux-volet-solaire", "craponne-volet-velux", "velux-toiture"])


def depannage(ctx):
    body = f"""
<h2>Votre volet roulant ne fonctionne plus ?</h2>
<p>Un volet roulant bloqué ou défaillant devient vite un problème au quotidien : pièce plongée dans le noir, maison impossible à fermer, sécurité compromise. Rod'Stores intervient rapidement pour diagnostiquer et réparer vos volets roulants, manuels ou motorisés, toutes marques.</p>
<div class="alert">{icon('message')}<p><strong>Notre conseil :</strong> évitez de forcer sur le volet, vous pourriez aggraver la panne. Appelez-nous au <a href="{TEL}">{SITE['phone']}</a>.</p></div>
<h2>Les pannes que nous réparons</h2>
{feature_list([
    ("lock", "Volet bloqué", "Bloqué ouvert, fermé ou à mi-hauteur, tablier coincé dans les coulisses."),
    ("zap", "Moteur en panne", "Le moteur ne répond plus, chauffe ou s'arrête : diagnostic et remplacement."),
    ("message", "Télécommande / inverseur", "Télécommande, récepteur radio ou interrupteur qui ne fonctionne plus."),
    ("wrench", "Mécanique", "Sangle ou manivelle cassée, lames abîmées ou décalées, attaches rompues."),
    ("volume", "Bruit anormal", "Grincements, frottements ou à-coups à la montée ou à la descente."),
    ("sun", "Volet solaire", "Batterie ou panneau défaillant sur les volets solaires, y compris Velux."),
])}
<h2>Panne au retour de vacances ?</h2>
<p>Après plusieurs semaines sans utilisation, une panne peut se révéler à votre retour : le volet ne remonte plus, le moteur ne répond plus, le tablier est décalé ou la télécommande ne fonctionne plus. Pas d'inquiétude : nous intervenons pour remettre vos volets en service.</p>
<h2>Réparer ou remplacer ?</h2>
<p>Nous privilégions toujours la réparation quand elle est possible et durable. Si le volet est trop ancien ou endommagé, nous vous proposons un devis de remplacement ou de motorisation, en toute transparence.</p>
<h3>Zones de dépannage</h3>
<p>Roanne, Riorges, Mably, Le Coteau, Charlieu, Feurs, Montbrison, Saint-Étienne, Vichy, Lyon et leurs environs.</p>
"""
    faqs = [
        ("Intervenez-vous rapidement ?", "Oui, le dépannage est une priorité : contactez-nous par téléphone, nous fixons une intervention dans les meilleurs délais selon votre secteur."),
        ("Réparez-vous toutes les marques de volets roulants ?", "Oui, nous intervenons sur les volets manuels et motorisés de toutes marques, ainsi que sur les volets solaires et les volets de fenêtres de toit."),
        ("Mon volet est bloqué en position fermée, que faire ?", "Ne forcez pas, ni à la main ni avec l'interrupteur. Coupez éventuellement l'alimentation si le moteur force et appelez-nous : nous débloquerons le volet sans l'abîmer."),
        ("Assurez-vous le dépannage en été ?", "Oui, nous assurons une permanence dépannage, y compris pendant la période estivale."),
    ]
    return service_page(ctx, path="depannage-volets-roulants/", name="Dépannage volets roulants",
                        title="Dépannage volet roulant Roanne, Loire, Lyon | Rod'Stores",
                        description="Volet roulant bloqué, moteur en panne, sangle cassée ? Dépannage rapide de volets roulants manuels, motorisés et solaires à Roanne, dans la Loire, à Lyon et Vichy.",
                        eyebrow="Dépannage rapide", h1="Dépannage de volets roulants à Roanne et dans la Loire",
                        lead="Volet bloqué, moteur ou télécommande en panne, lame cassée : nous intervenons rapidement pour réparer vos volets roulants, toutes marques.",
                        image="velux-volet-solaire", alt="Volet roulant solaire réparé par Rod'Stores", body=body, faqs=faqs,
                        gallery=["craponne-volet-velux", "velux-toiture", "pere-fils"], cta_title="Volet en panne ? Appelez-nous")


def portes(ctx):
    body = f"""
<h2>Pose de portes d'entrée sur mesure</h2>
<p>La porte d'entrée est la première image de votre maison, mais aussi un élément clé de sa sécurité et de son isolation. Nous installons des portes d'entrée alliant sécurité, isolation et esthétique, à Roanne et dans toute la Loire.</p>
{feature_list([
    ("lock", "Sécurité", "Serrures multipoints, paumelles renforcées, vitrages feuilletés."),
    ("thermo", "Isolation", "Fini les courants d'air : une porte étanche qui garde la chaleur en hiver."),
    ("home", "Esthétique", "Aluminium, PVC ou acier, nombreux modèles et coloris, vitrés ou pleins."),
    ("ruler", "Sur mesure", "Adaptée à votre ouverture, avec ou sans tierce et imposte."),
])}
<h2>Remplacement en rénovation</h2>
<p>Nous déposons votre ancienne porte et posons la nouvelle avec soin : calage, étanchéité, réglage de la fermeture et finitions intérieures et extérieures. Résultat : une porte qui ferme enfin parfaitement, comme en témoignent nos clients.</p>
<div class="alert">{icon('star')}<p>« Enfin une porte de maison qui ferme, où l'air chaud ou froid ne passe plus. » — Julien P., client Rod'Stores</p></div>
<h2>Réparation de porte d'entrée</h2>
<p>Porte qui frotte, serrure dure, joint usé : nous intervenons aussi pour réparer et régler votre porte existante lorsque c'est possible.</p>
"""
    faqs = [
        ("Quel matériau choisir pour une porte d'entrée ?", "L'aluminium offre robustesse et design, le PVC un excellent rapport isolation/prix, l'acier une sécurité renforcée. Nous vous présentons les options adaptées à votre maison."),
        ("Combien de temps dure la pose ?", "Le remplacement d'une porte d'entrée se fait généralement en une journée, votre logement restant fermé le soir."),
        ("Réparez-vous les portes existantes ?", "Oui, réglage, changement de serrure ou de joints : nous vous disons honnêtement si une réparation suffit."),
    ]
    return service_page(ctx, path="porte/", name="Portes d'entrée",
                        title="Porte d'entrée sur mesure à Roanne | Rod'Stores",
                        description="Pose et remplacement de portes d'entrée sur mesure en aluminium, PVC ou acier à Roanne et dans la Loire : sécurité, isolation et esthétique. Devis gratuit.",
                        eyebrow="Portes d'entrée", h1="Portes d'entrée à Roanne : sécurité, isolation, esthétique",
                        lead="Aluminium, PVC ou acier : une porte d'entrée sur mesure, posée avec soin, qui ferme parfaitement et protège votre maison du froid.",
                        image="porte-entree", alt="Porte d'entrée aluminium anthracite posée par Rod'Stores", body=body, faqs=faqs,
                        gallery=["porte-entree", "craponne-porte-fenetre", "pere-fils"])


def garages(ctx):
    body = f"""
<h2>Fourniture et pose de portes de garage</h2>
<p>Nous fournissons et posons des portes de garage pensées pour un usage quotidien fiable et pratique, à Roanne et dans toute la Loire.</p>
{feature_list([
    ("home", "Sectionnelle", "Ouverture verticale qui libère l'espace devant et dans le garage."),
    ("ruler", "Enroulable", "Idéale quand il y a peu de place au plafond, coffre compact."),
    ("lock", "Basculante / battante", "Des solutions simples et robustes, en remplacement à l'identique."),
    ("zap", "Motorisation", "Ouverture à distance par télécommande, en neuf ou sur porte existante."),
])}
<h2>Portails</h2>
<p>Portails battants ou coulissants, en aluminium ou PVC, manuels ou motorisés : nous vous conseillons sur le modèle adapté à votre accès et à l'esthétique de votre maison.</p>
<h2>Dépannage et motorisation</h2>
<p>Porte de garage qui ne s'ouvre plus, moteur en panne, télécommande perdue : nous intervenons pour diagnostiquer et réparer, ou motoriser une porte manuelle.</p>
"""
    faqs = [
        ("Peut-on motoriser une porte de garage existante ?", "Souvent oui, selon le type et l'état de la porte. Nous vérifions sur place et vous proposons la motorisation adaptée."),
        ("Quelle porte choisir pour un petit garage ?", "La porte sectionnelle ou enroulable : elles ne débordent pas à l'ouverture et laissent toute la place pour votre véhicule."),
        ("Posez-vous aussi les portails ?", "Oui, portails battants ou coulissants, manuels ou motorisés."),
    ]
    return service_page(ctx, path="portes-de-garage/", name="Portes de garage & portails",
                        title="Porte de garage & portail à Roanne | Rod'Stores",
                        description="Pose de portes de garage sectionnelles, enroulables et de portails, manuels ou motorisés, à Roanne et dans la Loire. Dépannage et motorisation. Devis gratuit.",
                        eyebrow="Portes de garage & portails", h1="Portes de garage et portails à Roanne",
                        lead="Sectionnelles, enroulables, portails battants ou coulissants : des fermetures fiables au quotidien, manuelles ou motorisées.",
                        image="porte-garage", alt="Porte de garage sectionnelle anthracite", body=body, faqs=faqs,
                        gallery=["porte-entree", "atelier-facade", "pere-fils"])


def velux_page(ctx):
    body = f"""
<h2>Pose et remplacement de fenêtres de toit</h2>
<p>Fenêtre de toit ancienne ou récente, nous pouvons vous accompagner pour l'équiper, la moderniser ou la réparer. Nous intervenons sur tous types de fenêtres de toit, dont les Velux, à Roanne, dans la Loire et jusqu'à la région lyonnaise.</p>
<ul class="checklist">
  <li>{icon('check')} Remplacement de fenêtre de toit vétuste ou qui fuit</li>
  <li>{icon('check')} Création d'ouverture et pose de Velux neuf (trémie, raccord d'étanchéité)</li>
  <li>{icon('check')} Stores intérieurs occultants ou pare-soleil</li>
  <li>{icon('check')} Réparation et entretien</li>
</ul>
<h2>Volet roulant solaire Velux : sans gros travaux</h2>
<p>Et si vous remplaciez votre store intérieur par un volet roulant solaire ? C'est la solution idéale en rénovation pour améliorer rapidement le confort d'une pièce sous les combles.</p>
{feature_list([
    ("sun", "Protection contre la chaleur", "Le volet extérieur bloque la chaleur avant qu'elle n'atteigne la vitre."),
    ("home", "Occultation efficace", "Pour mieux dormir dans les chambres sous les toits."),
    ("zap", "100 % solaire", "Fonctionnement autonome, aucun raccordement électrique à prévoir."),
    ("wrench", "Pas de gros travaux", "Pose par l'extérieur, sans dégradation à l'intérieur."),
])}
<div class="alert">{icon('check-circle')}<p>Découvrez notre <a href="{ctx.u('nos-realisations/')}">avant / après</a> : un store intérieur abîmé remplacé par un volet roulant solaire Velux.</p></div>
"""
    faqs = [
        ("Peut-on poser un volet roulant sur un vieux Velux ?", "Souvent oui : ancien ou récent, votre Velux peut généralement être équipé. Nous vérifions la compatibilité et vous conseillons la solution adaptée."),
        ("Faut-il de l'électricité pour un volet de fenêtre de toit ?", "Non avec un volet solaire : il fonctionne en autonomie grâce à son panneau et sa batterie."),
        ("Créez-vous de nouvelles ouvertures en toiture ?", "Oui, nous réalisons la trémie, posons la fenêtre de toit et son raccord d'étanchéité adapté à votre couverture."),
    ]
    return service_page(ctx, path="velux-fenetres-de-toit/", name="Velux & fenêtres de toit",
                        title="Velux & fenêtres de toit à Roanne | Rod'Stores",
                        description="Pose et remplacement de fenêtres de toit Velux, volets roulants solaires et stores à Roanne, dans la Loire et près de Lyon. Sans gros travaux, devis gratuit.",
                        eyebrow="Fenêtres de toit", h1="Velux et fenêtres de toit : pose, volets solaires, stores",
                        lead="Remplacement, création d'ouverture, volet roulant solaire : plus de confort sous les combles, été comme hiver.",
                        image="craponne-velux", alt="Fenêtre de toit Velux posée en toiture par Rod'Stores", body=body, faqs=faqs,
                        gallery=["velux-toiture", "craponne-tremie", "craponne-volet-velux"])


def moustiquaires(ctx):
    body = f"""
<h2>Moustiquaires sur mesure</h2>
<p>Profitez de l'été fenêtres ouvertes, sans moustiques ni insectes. Nos moustiquaires sur mesure sont idéales pour préserver le confort intérieur sans sacrifier la ventilation.</p>
{feature_list([
    ("home", "Enroulable", "Pour les fenêtres : la toile s'enroule dans un coffre discret."),
    ("ruler", "Plissée / coulissante", "Pour les portes-fenêtres et baies : passage facile au quotidien."),
    ("lock", "Cadre fixe", "Simple et robuste pour les ouvertures peu utilisées."),
    ("sun", "Toiles adaptées", "Toile standard, renforcée anti-animaux ou anti-pollen."),
])}
<h2>Stores intérieurs et extérieurs</h2>
<p>Stores occultants, stores pare-soleil, stores de fenêtre de toit : nous vous conseillons la solution qui complète au mieux la protection de votre maison en été.</p>
<div class="alert">{icon('star')}<p>« Ça complète parfaitement la protection l'été, on peut allumer la lumière sans craindre les moustiques. La finition est parfaite. » — Client Rod'Stores à Roanne</p></div>
"""
    faqs = [
        ("Les moustiquaires empêchent-elles d'utiliser les volets ?", "Non, elles sont conçues pour s'intégrer à vos menuiseries et fonctionner avec vos volets roulants."),
        ("Peut-on installer une moustiquaire sur une baie coulissante ?", "Oui, avec une moustiquaire plissée ou coulissante adaptée aux grandes ouvertures."),
        ("Les moustiquaires sont-elles faites sur mesure ?", "Oui, nous prenons les cotes sur place pour un ajustement parfait de chaque ouverture."),
    ]
    return service_page(ctx, path="moustiquaires/", name="Moustiquaires & stores",
                        title="Moustiquaires sur mesure & stores à Roanne | Rod'Stores",
                        description="Moustiquaires sur mesure enroulables, plissées ou fixes et stores pour fenêtres, baies et Velux à Roanne et dans la Loire. Pose soignée, devis gratuit.",
                        eyebrow="Moustiquaires & stores", h1="Moustiquaires sur mesure et stores à Roanne",
                        lead="Fenêtres ouvertes, sans insectes : des moustiquaires et des stores sur mesure, posés avec une finition soignée.",
                        image="temoignage-moustiquaire", alt="Client Rod'Stores devant sa moustiquaire de baie vitrée", body=body, faqs=faqs,
                        gallery=["temoignage-moustiquaire", "craponne-porte-fenetre", "velux-volet-solaire"])


# ---------------------------------------------------------------- à propos / contact / légal
def about(ctx):
    trail = [("À propos", "a-propos/")]
    body = page_hero(ctx, trail, "À propos", "Rod'Stores, une entreprise familiale père &amp; fils à Roanne",
                     "Un savoir-faire de terrain, une organisation claire et un engagement simple : un travail fiable et durable, chantier après chantier.",
                     "pere-fils", "Le père et le fils de Rod'Stores au travail") + f"""
<section class="section">
  <div class="wrap content-grid">
    <div class="prose">
      <h2>Notre histoire</h2>
      <p>Rod'Stores est une entreprise familiale basée à Roanne, fondée par un père et son fils. L'un apporte plusieurs années d'expérience terrain et une maîtrise technique des installations et dépannages complexes. L'autre structure l'entreprise autour d'un fonctionnement clair : devis rapides, interventions réactives et suivi rigoureux des chantiers.</p>
      <h2>Notre engagement</h2>
      <p>Cette organisation à taille humaine garantit un interlocuteur unique, une prise de décision rapide et un contrôle direct de la qualité sur chaque intervention. Chaque chantier est suivi personnellement, sans sous-traitance.</p>
      {feature_list([
          ("users", "Interlocuteur unique", "Celui qui fait le devis est celui qui pose."),
          ("shield", "Sans sous-traitance", "La qualité est contrôlée directement sur chaque chantier."),
          ("clock", "Réactivité", "Devis rapides et interventions dans les meilleurs délais."),
          ("check-circle", "Travail durable", "Une pose rigoureuse pour des menuiseries performantes longtemps."),
      ])}
      <h2>Une expertise globale pour vos menuiseries</h2>
      <p>Nous accompagnons les particuliers et les professionnels dans l'ensemble de leurs projets de menuiserie et de fermeture : fenêtres sur mesure en PVC, aluminium ou bois, volets roulants et leur motorisation, portes d'entrée, portes de garage, portails, fenêtres de toit et moustiquaires. Chaque solution est étudiée en fonction de votre maison, de vos besoins réels et de votre budget.</p>
    </div>
    {aside_card(ctx)}
  </div>
</section>
<section class="section section--tint">
  <div class="wrap">
    <div class="section-head section-head--center"><p class="eyebrow">Avis clients</p><h2>Ils nous recommandent</h2></div>
    {testimonials(ctx)}
  </div>
</section>
{cta_band(ctx)}"""
    return dict(title="À propos – Entreprise père & fils à Roanne | Rod'Stores",
                description="Rod'Stores, entreprise familiale père & fils à Roanne : fenêtres, volets roulants, portes. Interlocuteur unique, sans sous-traitance, devis rapides.",
                body=body, current="a-propos/", schemas=[business_schema(), breadcrumb_schema(trail)])


def contact(ctx):
    trail = [("Contact", "contact/")]
    options = "".join(f"<option>{o}</option>" for o in ["Fenêtres", "Volets roulants", "Dépannage volet roulant", "Porte d'entrée",
                                                       "Porte de garage / portail", "Velux / fenêtre de toit", "Moustiquaires / stores", "Autre"])
    body = page_hero(ctx, trail, "Contact &amp; devis gratuit", "Demandez votre devis gratuit",
                     "Un projet de fenêtres, de volets ou de portes ? Un volet en panne ? Appelez-nous ou décrivez votre besoin : nous vous répondons rapidement.") + f"""
<section class="section">
  <div class="wrap contact-grid">
    <div>
      <h2>Nous joindre</h2>
      <div class="contact-tiles">
        <a class="contact-tile" href="{TEL}"><span class="ic">{icon('phone')}</span><div><strong>{SITE['phone']}</strong><span>Le plus rapide, pour un devis ou un dépannage</span></div></a>
        <a class="contact-tile" href="sms:{SITE['phone_e164']}"><span class="ic">{icon('message')}</span><div><strong>Envoyer un SMS</strong><span>Joignez une photo de votre volet ou de votre fenêtre</span></div></a>
        <a class="contact-tile" href="mailto:{SITE['email']}"><span class="ic">{icon('mail')}</span><div><strong>{SITE['email']}</strong><span>Pour vos demandes détaillées</span></div></a>
        <div class="contact-tile"><span class="ic">{icon('pin')}</span><div><strong>Roanne (42)</strong><span>Intervention dans toute la Loire et les départements limitrophes</span></div></div>
      </div>
      <div class="socials" style="margin-top:20px">
        <a class="btn btn--ghost btn--sm" href="{SITE['instagram']}" target="_blank" rel="noopener">{icon('instagram')} Instagram</a>
        <a class="btn btn--ghost btn--sm" href="{SITE['facebook']}" target="_blank" rel="noopener">{icon('facebook')} Facebook</a>
      </div>
    </div>
    <form class="form" id="devis-form" data-to="{SITE['email']}">
      <h2 style="margin:0">Décrivez votre projet</h2>
      <div class="row">
        <div><label for="f-nom">Nom</label><input id="f-nom" name="nom" autocomplete="name" required></div>
        <div><label for="f-tel">Téléphone</label><input id="f-tel" name="tel" type="tel" autocomplete="tel" required></div>
      </div>
      <div class="row">
        <div><label for="f-projet">Votre besoin</label><select id="f-projet" name="projet">{options}</select></div>
        <div><label for="f-ville">Ville</label><input id="f-ville" name="ville" autocomplete="address-level2" placeholder="ex. Roanne"></div>
      </div>
      <div><label for="f-msg">Message</label><textarea id="f-msg" name="message" placeholder="Nombre de fenêtres, dimensions approximatives, type de panne…"></textarea></div>
      <button class="btn" type="submit">{icon('mail')} Préparer ma demande par e-mail</button>
      <p class="hint">Le bouton ouvre votre messagerie avec votre demande pré-remplie. Aucune donnée n'est enregistrée sur ce site.</p>
    </form>
  </div>
</section>
<section class="section section--tint">
  <div class="wrap">
    <div class="section-head section-head--center"><p class="eyebrow">Zone d'intervention</p><h2>Où intervenons-nous ?</h2></div>
    <ul class="zones" style="justify-content:center">{''.join(f"<li>{icon('pin')}{z}</li>" for z in ZONES)}</ul>
  </div>
</section>"""
    return dict(title="Contact & devis gratuit – Rod'Stores Roanne | 07 68 16 02 68",
                description="Contactez Rod'Stores à Roanne pour un devis gratuit fenêtres, volets roulants, portes ou un dépannage : 07 68 16 02 68 ou rodstores.services@gmail.com.",
                body=body, current="contact/", schemas=[business_schema(), breadcrumb_schema(trail)])


def legal(ctx):
    trail = [("Mentions légales", "mention-legales/")]
    body = f"""
<section class="page-hero"><div class="wrap">{crumbs(ctx, trail)}<h1>Mentions légales &amp; confidentialité</h1></div></section>
<section class="section"><div class="wrap prose">
  <h2>Éditeur du site</h2>
  <p>Rod'Stores – entreprise de pose et dépannage de menuiseries<br>
  Siège : Roanne (42300), France<br>
  Téléphone : <a href="{TEL}">{SITE['phone']}</a><br>
  E-mail : <a href="mailto:{SITE['email']}">{SITE['email']}</a><br>
  SIRET et forme juridique : informations disponibles sur simple demande.</p>
  <h2>Hébergement</h2>
  <p>GitHub Pages – GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
  <h2>Propriété intellectuelle</h2>
  <p>Les textes, les photographies de chantiers et le logo présents sur ce site sont la propriété de Rod'Stores, à l'exception de certains visuels d'illustration de produits. Toute reproduction sans autorisation est interdite.</p>
  <h2>Données personnelles</h2>
  <p>Ce site ne collecte aucune donnée personnelle et n'utilise pas de cookies de suivi. Le formulaire de contact ouvre simplement votre messagerie : les informations que vous choisissez d'envoyer par e-mail ou par téléphone sont utilisées uniquement pour répondre à votre demande et ne sont jamais cédées à des tiers.</p>
  <p>Conformément au RGPD, vous pouvez demander l'accès, la rectification ou la suppression de vos données en écrivant à <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
  <h2>Services tiers</h2>
  <p>Les polices de caractères sont chargées depuis Google Fonts. Les liens vers Instagram, Facebook et Google ouvrent ces services, soumis à leurs propres politiques de confidentialité.</p>
</div></section>"""
    return dict(title="Mentions légales – Rod'Stores", description="Mentions légales et politique de confidentialité du site Rod'Stores.",
                body=body, current="mention-legales/", schemas=[breadcrumb_schema(trail)])


def not_found(ctx):
    body = f"""<section class="section"><div class="wrap" style="text-align:center;max-width:640px">
  <p class="eyebrow" style="justify-content:center">Erreur 404</p>
  <h1>Cette page est introuvable</h1>
  <p class="lead" style="margin-inline:auto">La page a peut-être été déplacée. Retrouvez nos services depuis l'accueil, ou appelez-nous directement.</p>
  <div class="btn-row" style="justify-content:center"><a class="btn" href="{ctx.u('')}">Retour à l'accueil</a><a class="btn btn--ghost" href="{TEL}">{icon('phone')} {SITE['phone']}</a></div>
</div></section>"""
    return dict(title="Page introuvable – Rod'Stores", description="Page introuvable.", body=body, noindex=True)


PAGES = [
    {"path": "", "render": home, "priority": "1.0"},
    {"path": "nos-realisations/", "render": realisations, "priority": "0.9"},
    {"path": "fenetres/", "render": fenetres, "priority": "0.9"},
    {"path": "volets-roulants/", "render": volets, "priority": "0.9"},
    {"path": "depannage-volets-roulants/", "render": depannage, "priority": "0.9"},
    {"path": "porte/", "render": portes, "priority": "0.8"},
    {"path": "portes-de-garage/", "render": garages, "priority": "0.8"},
    {"path": "velux-fenetres-de-toit/", "render": velux_page, "priority": "0.8"},
    {"path": "moustiquaires/", "render": moustiquaires, "priority": "0.8"},
    {"path": "a-propos/", "render": about, "priority": "0.6"},
    {"path": "contact/", "render": contact, "priority": "0.8"},
    {"path": "mention-legales/", "render": legal, "priority": "0.2"},
    {"path": "404.html", "render": not_found, "noindex": True, "root": SITE["base_path"]},
]
