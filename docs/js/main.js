// Rod'Stores — interactions légères, sans dépendance
(function () {
  "use strict";

  // Menu mobile
  var burger = document.querySelector(".burger");
  if (burger) {
    burger.addEventListener("click", function () {
      var open = document.body.classList.toggle("menu-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".mobile-menu a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("menu-open");
        burger.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Comparateurs avant / après
  document.querySelectorAll(".ba-frame").forEach(function (frame) {
    var range = frame.querySelector(".ba-range");
    if (!range) return;
    var set = function () { frame.style.setProperty("--pos", range.value + "%"); };
    range.addEventListener("input", set);
    set();
  });

  // Filtres de la galerie
  var filters = document.querySelector(".filters");
  if (filters) {
    var items = document.querySelectorAll("[data-cat]");
    filters.addEventListener("click", function (e) {
      var btn = e.target.closest("button");
      if (!btn) return;
      filters.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
      var cat = btn.dataset.filter;
      items.forEach(function (it) {
        it.hidden = cat !== "all" && it.dataset.cat.split(" ").indexOf(cat) === -1;
      });
    });
  }

  // Visionneuse photo
  var lb = document.getElementById("lightbox");
  if (lb && typeof lb.showModal === "function") {
    var lbImg = lb.querySelector("img");
    var lbTxt = lb.querySelector("p");
    var list = [];
    var idx = 0;
    var show = function (i) {
      idx = (i + list.length) % list.length;
      var b = list[idx];
      lbImg.src = b.dataset.full;
      lbImg.alt = b.querySelector("img").alt;
      lbTxt.textContent = b.dataset.caption || "";
    };
    document.addEventListener("click", function (e) {
      var b = e.target.closest("[data-full]");
      if (!b) return;
      list = Array.prototype.filter.call(document.querySelectorAll("[data-full]"), function (x) { return !x.closest("[hidden]"); });
      show(list.indexOf(b));
      lb.showModal();
    });
    lb.querySelector(".lb-close").addEventListener("click", function () { lb.close(); });
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) lb.close(); });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
    });
  }

  // Formulaire de demande de devis : prépare un e-mail
  var form = document.getElementById("devis-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var subject = "Demande de devis – " + (d.get("projet") || "Projet") + " – " + (d.get("ville") || "");
      var body = [
        "Bonjour Rod'Stores,",
        "",
        "Projet : " + (d.get("projet") || ""),
        "Ville : " + (d.get("ville") || ""),
        "",
        d.get("message") || "",
        "",
        "Nom : " + (d.get("nom") || ""),
        "Téléphone : " + (d.get("tel") || ""),
      ].join("\n");
      window.location.href = "mailto:" + form.dataset.to + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }

  // Apparition au défilement
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("is-in"); });
  }
})();
