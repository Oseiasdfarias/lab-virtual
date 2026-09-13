// Aeropêndulo 3D da página Início.
// O ângulo do braço segue o modelo linearizado documentado em Modelagem Matemática:
//   θ(s)/V(s) = 2,79245283 / (s² + 0,71698113 s + 9,98490566)
// excitado por degraus de tensão de 0 a 2,5 V. É uma ilustração do modelo, não dados reais.

import * as THREE from "three";
import { OrbitControls } from "./../vendor/three/addons/controls/OrbitControls.js";

const MODELO = { b0: 2.79245283, a1: 0.71698113, a0: 9.98490566 };
const DEGRAU_V = 2.5;
const MEIO_PERIODO_S = 9;
const L = 1.15;
const PIVO = new THREE.Vector3(0, 1.75, 0);

const container = document.querySelector("[data-lv-hero3d]");
if (container) iniciar(container);

function webglDisponivel() {
  try {
    const canvas = document.createElement("canvas");
    return !!(canvas.getContext("webgl2") || canvas.getContext("webgl"));
  } catch {
    return false;
  }
}

function coresDoTema() {
  const css = getComputedStyle(document.body);
  const ler = (nome, padrao) => css.getPropertyValue(nome).trim() || padrao;
  return {
    tinta: new THREE.Color(ler("--lv-ink", "#1d1d1f")),
    fundo: new THREE.Color(ler("--lv-bg", "#ffffff")),
    borda: new THREE.Color(ler("--lv-border", "#e3e3e6")),
    fraco: new THREE.Color(ler("--lv-faint", "#bbbbbc")),
    escuro: document.body.getAttribute("data-md-color-scheme") === "slate",
  };
}

function iniciar(el) {
  const hudTheta = el.querySelector("[data-lv-theta]");
  const hudVolt = el.querySelector("[data-lv-volt]");
  const semMovimento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!webglDisponivel()) {
    el.querySelector(".lv-hero3d__fallback").hidden = false;
    el.querySelector(".lv-hero3d__hud").hidden = true;
    return;
  }

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  el.prepend(renderer.domElement);
  renderer.domElement.setAttribute("aria-label", "Modelo 3D interativo do aeropêndulo");
  renderer.domElement.setAttribute("role", "img");

  const cena = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(34, 1, 0.1, 50);
  camera.position.set(2.2, 1.9, 4.6);

  const controles = new OrbitControls(camera, renderer.domElement);
  controles.target.set(0, 1.05, 0);
  controles.enableZoom = false;
  controles.enablePan = false;
  controles.enableDamping = true;
  controles.dampingFactor = 0.08;
  controles.minPolarAngle = Math.PI * 0.2;
  controles.maxPolarAngle = Math.PI * 0.55;
  controles.autoRotate = !semMovimento;
  controles.autoRotateSpeed = 0.7;
  controles.update();

  const luzAmbiente = new THREE.HemisphereLight(0xffffff, 0x888888, 1.6);
  const luzChave = new THREE.DirectionalLight(0xffffff, 2.2);
  luzChave.position.set(3, 5, 4);
  const luzRecorte = new THREE.DirectionalLight(0xffffff, 0.8);
  luzRecorte.position.set(-4, 2, -3);
  cena.add(luzAmbiente, luzChave, luzRecorte);

  const matTinta = new THREE.MeshStandardMaterial({ roughness: 0.45, metalness: 0.15 });
  const matEstrutura = new THREE.MeshStandardMaterial({ roughness: 0.85, metalness: 0 });
  const matLinha = new THREE.LineDashedMaterial({ dashSize: 0.06, gapSize: 0.06 });

  // Estrutura: base e duas colunas com o eixo do pivô entre elas.
  const estrutura = new THREE.Group();
  const base = new THREE.Mesh(new THREE.BoxGeometry(1.9, 0.08, 0.9), matEstrutura);
  base.position.y = 0.04;
  estrutura.add(base);
  for (const z of [-0.26, 0.26]) {
    const coluna = new THREE.Mesh(new THREE.BoxGeometry(0.1, PIVO.y - 0.08 + 0.12, 0.1), matEstrutura);
    coluna.position.set(0, (PIVO.y + 0.08 + 0.12) / 2, z);
    estrutura.add(coluna);
  }
  const eixo = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.035, 0.62, 24), matTinta);
  eixo.rotation.x = Math.PI / 2;
  eixo.position.copy(PIVO);
  estrutura.add(eixo);
  cena.add(estrutura);

  // Linha de repouso (braço na vertical), como no símbolo da marca.
  const geoRepouso = new THREE.BufferGeometry().setFromPoints([
    PIVO.clone(),
    new THREE.Vector3(PIVO.x, PIVO.y - L - 0.25, PIVO.z),
  ]);
  const repouso = new THREE.Line(geoRepouso, matLinha);
  repouso.computeLineDistances();
  cena.add(repouso);

  // Braço: gira em torno do eixo z do pivô; θ = 0 é a posição de repouso.
  const braco = new THREE.Group();
  braco.position.copy(PIVO);
  cena.add(braco);

  const cubo = new THREE.Mesh(new THREE.CylinderGeometry(0.085, 0.085, 0.14, 32), matTinta);
  cubo.rotation.x = Math.PI / 2;
  braco.add(cubo);

  const haste = new THREE.Mesh(new THREE.CylinderGeometry(0.022, 0.022, L, 16), matTinta);
  haste.position.y = -L / 2;
  braco.add(haste);

  // Motor perpendicular à haste, no plano de rotação; hélice na ponta do motor.
  const motor = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 0.26, 28), matTinta);
  motor.rotation.z = Math.PI / 2;
  motor.position.set(-0.1, -L, 0);
  braco.add(motor);

  const helice = new THREE.Group();
  helice.position.set(-0.25, -L, 0);
  braco.add(helice);
  const cuboHelice = new THREE.Mesh(new THREE.SphereGeometry(0.03, 16, 12), matTinta);
  helice.add(cuboHelice);
  const pa = new THREE.Mesh(new THREE.BoxGeometry(0.018, 0.62, 0.055), matTinta);
  helice.add(pa);

  function aplicarTema() {
    const c = coresDoTema();
    matTinta.color.copy(c.tinta);
    matEstrutura.color.copy(c.escuro ? c.borda.clone().lerp(c.tinta, 0.08) : c.borda.clone().lerp(c.tinta, 0.05));
    matLinha.color.copy(c.fraco);
    luzAmbiente.intensity = c.escuro ? 2.2 : 1.6;
    renderer.render(cena, camera);
  }
  aplicarTema();
  new MutationObserver(aplicarTema).observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  });

  function redimensionar() {
    const { width, height } = el.getBoundingClientRect();
    if (!width || !height) return;
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.render(cena, camera);
  }
  new ResizeObserver(redimensionar).observe(el);
  redimensionar();

  const formato = new Intl.NumberFormat("pt-BR", { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  function atualizarHud(theta, v) {
    hudTheta.textContent = `θ = ${formato.format(THREE.MathUtils.radToDeg(theta))}°`;
    hudVolt.textContent = `V = ${formato.format(v)} V`;
  }

  if (semMovimento) {
    const thetaRegime = (MODELO.b0 / MODELO.a0) * DEGRAU_V;
    braco.rotation.z = thetaRegime;
    atualizarHud(thetaRegime, DEGRAU_V);
    controles.addEventListener("change", () => renderer.render(cena, camera));
    renderer.render(cena, camera);
    return;
  }

  let theta = 0;
  let omega = 0;
  let tempo = 0;
  let ultimo = null;
  let acumuladorHud = 0;
  let visivel = true;

  function passo(dt) {
    const v = Math.floor(tempo / MEIO_PERIODO_S) % 2 === 0 ? DEGRAU_V : 0;
    const sub = 8;
    const h = dt / sub;
    for (let i = 0; i < sub; i++) {
      const alfa = MODELO.b0 * v - MODELO.a1 * omega - MODELO.a0 * theta;
      omega += alfa * h;
      theta += omega * h;
    }
    tempo += dt;
    return v;
  }

  function quadro(agora) {
    if (!visivel) {
      ultimo = null;
      return;
    }
    const dt = ultimo === null ? 0 : Math.min((agora - ultimo) / 1000, 0.05);
    ultimo = agora;
    const v = passo(dt);
    braco.rotation.z = theta;
    helice.rotation.x += (v > 0 ? 0.55 : 0.08) + Math.abs(omega) * 0.05;
    acumuladorHud += dt;
    if (acumuladorHud > 0.1) {
      atualizarHud(theta, v);
      acumuladorHud = 0;
    }
    controles.update();
    renderer.render(cena, camera);
    requestAnimationFrame(quadro);
  }

  new IntersectionObserver((entradas) => {
    const estava = visivel;
    visivel = entradas[0].isIntersecting;
    if (visivel && !estava) requestAnimationFrame(quadro);
  }).observe(el);
  requestAnimationFrame(quadro);
}
