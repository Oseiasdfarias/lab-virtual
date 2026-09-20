// Sincroniza o tema claro/escuro do MkDocs Material com os iframes dos simuladores 3D
(function() {
  function notificarIframes(temaEscuro) {
    const iframes = document.querySelectorAll("iframe");
    iframes.forEach((ifr) => {
      try {
        if (ifr.contentWindow) {
          ifr.contentWindow.postMessage({ temaEscuro: temaEscuro }, "*");
        }
      } catch (e) {
        // Fallback silencioso
      }
    });
  }

  function checarTemaAtual() {
    const scheme = document.body.getAttribute("data-md-color-scheme");
    return scheme === "slate";
  }

  // Observador de mutação no atributo data-md-color-scheme do <body>
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((m) => {
      if (m.attributeName === "data-md-color-scheme") {
        notificarIframes(checarTemaAtual());
      }
    });
  });

  if (document.body) {
    observer.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
  } else {
    document.addEventListener("DOMContentLoaded", () => {
      observer.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });
    });
  }

  // Quando qualquer iframe carregar, envie o tema atual imediatamente
  window.addEventListener("load", () => {
    const escuro = checarTemaAtual();
    const iframes = document.querySelectorAll("iframe");
    iframes.forEach((ifr) => {
      ifr.addEventListener("load", () => {
        try {
          ifr.contentWindow.postMessage({ temaEscuro: escuro }, "*");
        } catch (e) {}
      });
    });
    notificarIframes(escuro);
  });

  // Habilitar GLightbox com desfoque de fundo em Diagramas Mermaid e Ilustrações SVG
  function inicializarZoomDiagramasEIlustracoes() {
    if (typeof GLightbox === "undefined") return;

    // 1. Ilustrações Técnicas (.lv-aeropendulo-card com SVG)
    document.querySelectorAll(".lv-aeropendulo-card").forEach((card, idx) => {
      if (card.dataset.hasGlightbox) return;
      card.dataset.hasGlightbox = "true";
      card.classList.add("lv-zoomable-element");
      card.setAttribute("title", "Clique para expandir a ilustração técnica");

      const inlineId = "inline-svg-illus-" + idx;
      let modalContent = document.getElementById(inlineId);
      if (!modalContent) {
        modalContent = document.createElement("div");
        modalContent.id = inlineId;
        modalContent.style.display = "none";
        modalContent.className = "lv-glightbox-inline-box";
        modalContent.innerHTML = card.innerHTML;
        document.body.appendChild(modalContent);
      }

      card.addEventListener("click", () => {
        const lb = GLightbox({
          elements: [{
            content: document.getElementById(inlineId),
            width: "90vw",
            height: "auto"
          }],
          touchNavigation: true,
          zoomable: true,
          draggable: true
        });
        lb.open();
      });
    });

    // 2. Diagramas Mermaid (.mermaid)
    document.querySelectorAll(".mermaid").forEach((diag, idx) => {
      if (diag.dataset.hasZoomAction) return;
      diag.dataset.hasZoomAction = "true";
      diag.classList.add("lv-zoomable-element");
      diag.setAttribute("title", "Clique para ver o diagrama ampliado");

      // Botão visível de maximizar no canto superior direito do diagrama
      if (!diag.querySelector(".lv-mermaid-zoom-btn")) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "lv-mermaid-zoom-btn";
        btn.setAttribute("aria-label", "Maximizar diagrama");
        btn.setAttribute("title", "Maximizar diagrama");
        btn.innerHTML = `<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg> <span>Expandir</span>`;
        diag.appendChild(btn);
      }
    });
  }

  function abrirModalMermaid(mermaidContainer) {
    const svg = mermaidContainer.querySelector("svg");
    if (!svg) return;

    let holder = document.getElementById("mermaid-global-zoom-holder");
    if (!holder) {
      holder = document.createElement("div");
      holder.id = "mermaid-global-zoom-holder";
      holder.style.display = "none";
      holder.className = "lv-glightbox-inline-box";
      document.body.appendChild(holder);
    }

    holder.innerHTML = "";
    const clone = svg.cloneNode(true);
    clone.style.width = "100%";
    clone.style.maxWidth = "1150px";
    clone.style.height = "auto";
    clone.style.display = "block";
    clone.style.margin = "0 auto";
    holder.appendChild(clone);

    if (typeof GLightbox !== "undefined") {
      const lb = GLightbox({
        elements: [{
          content: holder,
          width: "94vw",
          height: "auto"
        }],
        touchNavigation: true,
        zoomable: false,
        draggable: false
      });
      lb.open();
    }
  }

  // Intercepta cliques no container mermaid ou no botão de expandir
  document.addEventListener("click", function(e) {
    const mermaidContainer = e.target.closest(".mermaid");
    if (mermaidContainer) {
      e.preventDefault();
      abrirModalMermaid(mermaidContainer);
    }
  });

  // Executa após o carregamento da página e em navegações instantâneas do Material
  window.addEventListener("DOMContentLoaded", inicializarZoomDiagramasEIlustracoes);
  window.addEventListener("load", () => {
    inicializarZoomDiagramasEIlustracoes();
    setTimeout(inicializarZoomDiagramasEIlustracoes, 500);
    setTimeout(inicializarZoomDiagramasEIlustracoes, 1500);
  });
  if (typeof document$ !== "undefined") {
    document$.subscribe(() => {
      inicializarZoomDiagramasEIlustracoes();
      setTimeout(inicializarZoomDiagramasEIlustracoes, 500);
      setTimeout(inicializarZoomDiagramasEIlustracoes, 1500);
    });
  }
})();

