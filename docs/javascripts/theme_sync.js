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
})();
