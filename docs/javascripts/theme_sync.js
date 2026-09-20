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
      if (diag.dataset.hasGlightbox) return;
      diag.dataset.hasGlightbox = "true";
      diag.classList.add("lv-zoomable-element");
      diag.setAttribute("title", "Clique para expandir o diagrama");

      diag.addEventListener("click", (e) => {
        e.preventDefault();
        const svg = diag.querySelector("svg");
        if (!svg) return;

        // Clona e prepara o SVG com namespace e estilo de visualização
        const clonedSvg = svg.cloneNode(true);
        clonedSvg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
        
        // Assegura largura e altura adequadas para visualização nítida
        const bbox = svg.getBBox ? svg.getBBox() : null;
        if (bbox && bbox.width && bbox.height) {
          if (!clonedSvg.getAttribute("viewBox")) {
            clonedSvg.setAttribute("viewBox", `${bbox.x} ${bbox.y} ${bbox.width} ${bbox.height}`);
          }
        }

        const svgXml = new XMLSerializer().serializeToString(clonedSvg);
        const svgBlob = new Blob([svgXml], { type: "image/svg+xml;charset=utf-8" });
        const blobUrl = URL.createObjectURL(svgBlob);

        const lb = GLightbox({
          elements: [{
            href: blobUrl,
            type: "image",
            title: "Diagrama de Fluxo (Mermaid)",
            description: "Clique na imagem ou use o scroll para zoom; arraste para navegar."
          }],
          touchNavigation: true,
          zoomable: true,
          draggable: true
        });

        lb.on("close", () => {
          setTimeout(() => URL.revokeObjectURL(blobUrl), 1000);
        });

        lb.open();
      });
    });

  }

  // Executa após o carregamento da página e em navegações instantâneas do Material
  window.addEventListener("DOMContentLoaded", inicializarZoomDiagramasEIlustracoes);
  window.addEventListener("load", () => setTimeout(inicializarZoomDiagramasEIlustracoes, 600));
  if (typeof document$ !== "undefined") {
    document$.subscribe(() => setTimeout(inicializarZoomDiagramasEIlustracoes, 600));
  }
})();

