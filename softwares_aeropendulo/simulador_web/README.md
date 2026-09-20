# Simulador Web 3D (Substituto WebGL / Three.js do VPython)

Este diretório contém o módulo de simulação 3D em WebGL de alta fidelidade desenvolvido com **Three.js** e materiais **PBR (Physically Based Rendering)**, projetado para substituir a biblioteca legada **VPython** (`vpython`) no ecossistema do Laboratório Virtual do Aeropêndulo.

---

## 🎯 Por que migrar do VPython para Three.js?

1. **Independência de Servidor Local**: O VPython clássico necessita de um servidor WebSocket local (`vpython-backend`) em segundo plano acoplado a versões antigas de `setuptools`, gerando conflitos de dependências em distribuições modernas e sistemas operacionais de ponta.
2. **Alta Fidelidade Física e Texturas PBR**: Enquanto o VPython renderiza apenas sólidos prismáticos simples (caixas e cilindros de cor sólida), o modelo Three.js possui texturas procedurais ultraleves em alta resolução (1024×1024), bump mapping com relevo tátil, acabamento fosco industrial, serigrafia técnica e iluminação de estúdio.
3. **Representação Completa da Mecânica e Eletroeletrônica**:
   - **Mecânica Realista**: Base hexagonal de compensado naval, mastro elevado com reforço triangular, travessa usinada com régua técnica graduada, eixo com mancal axial, haste contínua em fibra de carbono 3K e hélice de drone bipá com spinner aerodinâmico.
   - **Eletrônica e Instrumentação Integradas**: Potenciômetro de precisão Bourns 10kΩ com gravação a laser no pivô, fiação com isolamento PVC, eletrodutos e chicotes estruturais sem colisão com sólidos, além do gabinete eletrônico completo na base contendo o microcontrolador **ESP32 TTGO T1** (setor de sinal 3.3V), placa de potência **Driver Ponte H MOSFET** (setor de potência 5V/3A) com dissipador aletado, capacitores low-ESR e **fonte industrial chaveada** perfurada em colmeia.
4. **Integração Universal Web e Desktop**:
   - Funciona nativamente em qualquer navegador sem plugins.
   - Pode ser embutido como `QWebEngineView` no PyQt/CustomTkinter ou servido via HTTP/WebSockets na plataforma em nuvem do laboratório.

---

## 📁 Arquivos e Recursos
 
- `aeropendulo_3d.html` (ou `index.html`): Aplicação Web 3D autocontida com simulação numérica contínua em tempo real (RK / integração de Euler sub-amostrada), gerador de formas de onda (senoide, quadrada, degrau e PRBS), rastro de trajetória 3D com apagamento em retorno, medição angular visual no pivô e botões de câmera com interpolação suave.
- **Painel de Controle Minimizável**: O painel HUD pode ser recolhido em uma pílula compacta de telemetria contínua ($\theta$ e $V$) clicando no botão da seta ou no próprio cabeçalho.
- **Parâmetros de URL Suportados**:
  - `?min=1` ou `?compact=1`: Inicia a simulação com o painel minimizado (ideal para embeds compactos como o hero da documentação).
- **Sincronização de Tema via `postMessage`**: O simulador aceita mensagens `{ temaEscuro: true|false }` via `window.postMessage`, permitindo que portais externos (como MkDocs Material ou LMS) controlem a iluminação e paleta em tempo real.

---

## 🚀 Como Executar

### 1. Diretamente no Navegador:
Basta abrir o arquivo no seu navegador de preferência:
```bash
# No Linux:
xdg-open aeropendulo_3d.html
# Ou no macOS:
open aeropendulo_3d.html
```

### 2. Servidor Local Leve (Opcional):
```bash
python3 -m http.server 8080
# Acesse http://localhost:8080/aeropendulo_3d.html
```

### 3. Integração com Python (Bridge Serial/WebSockets):
Os estados de ângulo $\theta(t)$, tensão $V(t)$ e referência podem ser atualizados diretamente via chamadas JavaScript ou ponte WebSocket com o firmware do ESP32 ou a GUI Python.

