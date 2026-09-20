"""Análises complementares da identificação e da malha fechada, feitas para o artigo.

Usa o mesmo ensaio, pré-processamento e divisão de dados de metricas_validacao.py e acrescenta:
- varredura de ordens ARX (na, nb) com ajuste de validação (FIT) e AIC/BIC na identificação;
- busca conjunta (na, nb, nk) com seleção num trecho separado (últimos 25 % do segmento de
  estimação), sem usar o segmento de validação na escolha da estrutura;
- resíduos de predição um passo à frente: autocorrelação, correlação cruzada com a entrada e
  estatística de Ljung-Box;
- polos dos modelos e frequência natural/amortecimento do par dominante;
- espectro e estatística de chaveamento do sinal de excitação;
- dispersão (quartis) das métricas de malha fechada e figuras para o artigo.

Uso (a partir da raiz do repositório):
    uv run --with numpy --with pandas --with control --with scipy --with matplotlib python \
        materiais_complementares/Identificacao_de_Sistemas/identificacao_aeropendulo/ident_up/analise_complementar.py
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal, stats

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[3]
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(RAIZ / "materiais_complementares/analise_malha_fechada"))

from metricas_validacao import carregar, estimar, nrmse, rmse_graus, simular  # noqa: E402
import metricas_malha_fechada as mf  # noqa: E402

TS = 0.02
FIG = RAIZ / "artigo_ieee_latam_en/figuras"
TINTA, AZUL, LARANJA, VERDE = "#1a1a19", "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({
    "font.family": "serif", "font.size": 8, "axes.linewidth": 0.6,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#d9d9d9", "grid.linewidth": 0.4,
    "legend.frameon": False, "lines.linewidth": 1.0, "savefig.bbox": "tight",
})
LARGURA = 3.45


def residuos(theta, na, nb, u, y, ini, fim):
    k = np.arange(max(na, nb), fim)
    k = k[k >= ini]
    phi = np.column_stack([y[k - i - 1] for i in range(na)] + [u[k - j] for j in range(nb)])
    return y[k] - phi @ theta, k


def estimar_nk(u, y, ni, na, nb, nk):
    k0 = max(na, nb + nk - 1)
    idx = np.arange(k0, ni + k0)
    m = np.column_stack([y[idx - i - 1] for i in range(na)] + [u[idx - nk - j] for j in range(nb)])
    return np.linalg.lstsq(m, y[idx], rcond=None)[0]


def sim_nk(theta, na, nk, u):
    return signal.lfilter(np.r_[np.zeros(nk), theta[na:]], np.r_[1.0, -theta[:na]], u)


def residuos_nk(theta, na, nb, nk, u, y, ini, fim):
    k = np.arange(max(na, nb + nk - 1), fim)
    k = k[k >= ini]
    phi = np.column_stack([y[k - i - 1] for i in range(na)] + [u[k - nk - j] for j in range(nb)])
    return y[k] - phi @ theta, k


def fit_janela(y, ys, i0, i1):
    return (1 - np.linalg.norm(y[i0:i1] - ys[i0:i1]) / np.linalg.norm(y[i0:i1] - y[i0:i1].mean())) * 100


def busca_conjunta(u, y, ni):
    ns = int(0.75 * ni)
    linhas = []
    for na in range(1, 13):
        for nb in range(1, 11):
            for nk in range(16):
                th = estimar_nk(u, y, ns, na, nb, nk)
                if estavel(th, na):
                    linhas.append(dict(na=na, nb=nb, nk=nk, p=na + nb,
                                       fsel=fit_janela(y, sim_nk(th, na, nk, u), ns, ni)))
    return ns, pd.DataFrame(linhas)


def criterios(theta, na, nb, u, y, ni):
    e, _ = residuos(theta, na, nb, u, y, 0, ni + na)
    n, p = len(e), na + nb
    s2 = np.mean(e ** 2)
    return n * np.log(s2) + 2 * p, n * np.log(s2) + p * np.log(n)


def sim_arx(theta, na, u):
    return signal.lfilter(theta[na:], np.r_[1.0, -theta[:na]], u)


def estavel(theta, na):
    return np.all(np.abs(np.roots(np.r_[1.0, -theta[:na]])) < 1)


def varredura(u, y, ni):
    linhas = []
    for na in range(1, 21):
        for nb in range(1, 17):
            th = estimar(u, y, ni, na, nb)
            aic, bic = criterios(th, na, nb, u, y, ni)
            fit = nrmse(y, sim_arx(th, na, u), ni) if estavel(th, na) else np.nan
            linhas.append(dict(na=na, nb=nb, p=na + nb, fit=fit, aic=aic, bic=bic))
    return pd.DataFrame(linhas)


def ljung_box(e, lags=20):
    n = len(e)
    e = e - e.mean()
    r = np.array([np.sum(e[k:] * e[:-k]) for k in range(1, lags + 1)]) / np.sum(e ** 2)
    q = n * (n + 2) * np.sum(r ** 2 / (n - np.arange(1, lags + 1)))
    return q, stats.chi2.sf(q, lags)


def correlacoes(e, u, lags=40):
    e = (e - e.mean()) / e.std()
    u = (u - u.mean()) / u.std()
    n = len(e)
    ree = np.array([np.sum(e[k:] * e[:n - k]) / n for k in range(lags + 1)])
    # r_eu(k) = (1/n) sum_t e(t) u(t-k)
    reu = np.array([np.sum(e[k:] * u[:n - k]) / n if k >= 0 else np.sum(e[:n + k] * u[-k:]) / n
                    for k in range(-lags, lags + 1)])
    return ree, reu, 1.96 / np.sqrt(n)


def polos(theta, na):
    z = np.roots(np.r_[1.0, -theta[:na]])
    s = np.log(z.astype(complex)) / TS
    return z, s


def dominante(s):
    comp = s[np.imag(s) > 1e-9]
    if len(comp) == 0:
        return None
    par = comp[np.argmax(np.real(comp))]
    wn = abs(par)
    return wn, -np.real(par) / wn


def excitacao(u):
    niveis = np.unique(np.round(u, 3))
    trocas = np.where(np.abs(np.diff(u)) > 1e-6)[0]
    duracoes = np.diff(trocas) * TS
    f, pxx = signal.welch(u - u.mean(), fs=1 / TS, nperseg=1024)
    return niveis, duracoes, f, pxx, np.sum(pxx[f <= 1.5]) / np.sum(pxx)


def main():
    u, y, ni = carregar()
    bruto = pd.read_csv(RAIZ / "softwares_aeropendulo/src_interface/dados_de_ensaio/arquivo_9_9_2023_13_33_24.csv",
                        index_col=0).astype(float)
    u_volts = bruto.iloc[49:, 4].to_numpy()
    assert len(u_volts) == len(u) and np.allclose(u_volts - u_volts.mean(), u)
    print(f"linhas de dados no arquivo: {len(bruto)}, tempo {bruto.iloc[0, 6]:.2f}-{bruto.iloc[-1, 6]:.2f} s")
    print(f"N = {len(y)}, identificação = {ni} ({100 * ni / len(y):.1f} %), validação = {len(y) - ni}")

    tab = varredura(u, y, ni)
    print("\nVarredura (FIT de validação, AIC e BIC na identificação):")
    print("melhor FIT :", tab.loc[tab.fit.idxmax()].round(2).to_dict())
    print("menor AIC  :", tab.loc[tab.aic.idxmin()].round(2).to_dict())
    print("menor BIC  :", tab.loc[tab.bic.idxmin()].round(2).to_dict())
    print("instáveis  :", int(tab.fit.isna().sum()), "de", len(tab))
    for crit in ["aic", "bic"]:
        m = tab.loc[tab[crit].idxmin()]
        print(f"  mínimo de {crit} com na<=12, nb<=6:",
              tab[(tab.na <= 12) & (tab.nb <= 6)].sort_values(crit).iloc[0][["na", "nb", "fit"]].to_dict(),
              "| grade toda:", m[["na", "nb", "fit"]].to_dict())
    plato = tab[tab.fit >= tab.fit.max() - 2].sort_values("p").iloc[0]
    print("  modelo mais simples a até 2 p.p. do melhor FIT:", plato[["na", "nb", "fit"]].to_dict())
    piv = tab.pivot(index="na", columns="nb", values="fit").round(1)
    print(piv.to_string())
    for na, nb in [(2, 3), (10, 4)]:
        print(f"({na},{nb}):", tab[(tab.na == na) & (tab.nb == nb)].round(2).to_dict("records")[0])
    melhor_nb = tab.groupby("na").fit.max()
    print("melhor FIT por na:", melhor_nb.round(1).to_dict())

    fig, ax = plt.subplots(1, 2, figsize=(LARGURA * 2 + 0.2, 1.9))
    for nb, cor, ls in [(3, AZUL, "-"), (4, LARANJA, "--"), (8, VERDE, "-.")]:
        d = tab[tab.nb == nb]
        ax[0].plot(d.na, d.fit, color=cor, ls=ls, marker="o", ms=3, label=f"$n_b={nb}$")
        ax[1].plot(d.na, d.bic, color=cor, ls=ls, marker="o", ms=3, label=f"$n_b={nb}$")
    ax[0].set(xlabel="$n_a$", ylabel="Validation FIT (%)")
    ax[1].set(xlabel="$n_a$", ylabel="BIC (identification)")
    fig.legend(*ax[0].get_legend_handles_labels(), loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.08))
    ax[1].ticklabel_format(axis="y", style="sci", scilimits=(3, 3), useMathText=True)
    fig.subplots_adjust(wspace=0.3)
    for a in ax:
        a.set_xticks(range(2, 21, 2))
    fig.savefig(FIG / "order-sweep.pdf")
    plt.close(fig)

    print("\nVarredura do atraso de entrada nk (modelo reestimado a cada nk):")
    curvas = {}
    for na, nb in [(2, 3), (10, 4)]:
        fits = []
        for k in range(21):
            th = estimar_nk(u, y, ni, na, nb, k)
            fits.append(nrmse(y, sim_nk(th, na, k, u), ni) if estavel(th, na) else np.nan)
        fits = np.array(fits)
        curvas[(na, nb)] = fits
        print(f"  ARX({na},{nb}): nk*={np.nanargmax(fits)} ({np.nanargmax(fits) * TS:.2f} s) FIT {np.nanmax(fits):.2f}; "
              f"nk=0 {fits[0]:.2f}; nk=8..14:", np.round(fits[8:15], 1))
    th23 = estimar_nk(u, y, ni, 2, 3, 11)
    e, k = residuos_nk(th23, 2, 3, 11, u, y, ni, len(y))
    q, pv = ljung_box(e)
    z, sp = polos(th23, 2)
    print(f"  ARX(2,3,nk=11): FIT {nrmse(y, sim_nk(th23, 2, 11, u), ni):.2f}, "
          f"RMSE {np.rad2deg(np.sqrt(np.mean((y[ni:] - sim_nk(th23, 2, 11, u)[ni:]) ** 2))):.3f} graus, "
          f"polos z {np.round(z, 4)}, s {np.round(sp, 2)}, Ljung-Box Q(20)={q:.1f} p={pv:.3g}")
    print(f"  coeficientes a={np.round(th23[:2], 5)}, b={np.round(th23[2:], 5)}")
    aic, bic = [np.nan, np.nan]
    n = len(residuos_nk(th23, 2, 3, 11, u, y, 0, ni + 11)[0])
    s2 = np.mean(residuos_nk(th23, 2, 3, 11, u, y, 0, ni + 11)[0] ** 2)
    print(f"  ARX(2,3,11) AIC {n * np.log(s2) + 10:.1f}, BIC {n * np.log(s2) + 5 * np.log(n):.1f}")
    ns, conj = busca_conjunta(u, y, ni)
    print(f"\nBusca conjunta: estimação interna {ns}, seleção {ni - ns}, validação {len(y) - ni}, "
          f"{len(conj)} modelos estáveis")
    escolhidos = {}
    for rot, filtro in [("melhor geral", conj.p > 0), ("p<=5", conj.p <= 5), ("p<=8", conj.p <= 8),
                        ("p<=14", conj.p <= 14), ("(2,3,nk)", (conj.na == 2) & (conj.nb == 3)),
                        ("(10,4,nk)", (conj.na == 10) & (conj.nb == 4))]:
        b = conj[filtro].sort_values("fsel").iloc[-1]
        chave = (int(b.na), int(b.nb), int(b.nk))
        th = estimar_nk(u, y, ni, *chave)
        ys = sim_nk(th, chave[0], chave[2], u)
        escolhidos[rot] = chave
        print(f"  {rot:12s} -> ARX{chave}: FIT seleção {b.fsel:.2f}; validação FIT {nrmse(y, ys, ni):.2f}, "
              f"RMSE {rmse_graus(y, ys, ni):.3f}")
    nk_sel = {k: conj[(conj.na == k[0]) & (conj.nb == k[1])].set_index("nk").fsel for k in [(2, 3), (10, 4)]}

    fig, ax = plt.subplots(figsize=(LARGURA, 1.8))
    for (na, nb), cor in [((2, 3), AZUL), ((10, 4), LARANJA)]:
        ax.plot(nk_sel[(na, nb)].index, nk_sel[(na, nb)].values, color=cor, ls="-", marker="o", ms=2.5,
                label=f"ARX({na},{nb}), selection")
        ax.plot(np.arange(16), curvas[(na, nb)][:16], color=cor, ls="--", lw=0.8,
                label=f"ARX({na},{nb}), validation")
    ax.set(xlabel="Input delay $n_k$ (samples)", ylabel="FIT (%)", ylim=(40, 95))
    ax.legend(loc="lower right", ncol=1, fontsize=6.5)
    fig.savefig(FIG / "delay-sweep.pdf")
    plt.close(fig)

    casos = [(2, 3, 0), (10, 4, 0), escolhidos["(2,3,nk)"], escolhidos["(10,4,nk)"],
             escolhidos["p<=5"], escolhidos["melhor geral"]]
    modelos = {}
    for na, nb, nk in casos:
        th = estimar_nk(u, y, ni, na, nb, nk)
        if nk == 0:
            assert np.allclose(th, estimar(u, y, ni, na, nb))
        n_id = len(residuos_nk(th, na, nb, nk, u, y, 0, ni + max(na, nb + nk - 1))[0])
        s2 = np.mean(residuos_nk(th, na, nb, nk, u, y, 0, ni + max(na, nb + nk - 1))[0] ** 2)
        e, k = residuos_nk(th, na, nb, nk, u, y, ni, len(y))
        q, pv = ljung_box(e)
        ree, reu, lim = correlacoes(e, u[k])
        z, sp = polos(th, na)
        dom = dominante(sp)
        ys = sim_nk(th, na, nk, u)
        print(f"\nARX({na},{nb},{nk}): FIT {nrmse(y, ys, ni):.2f} %, RMSE {rmse_graus(y, ys, ni):.3f} graus, "
              f"Ljung-Box Q(20) = {q:.1f} (p = {pv:.2g}); |r_ee|>lim em {int(np.sum(np.abs(ree[1:]) > lim))}/40, "
              f"|r_eu|>lim em {int(np.sum(np.abs(reu) > lim))}/81 (lim {lim:.3f})")
        print("  polos s:", np.round(sp[np.argsort(-np.real(sp))], 2))
        if dom:
            print(f"  par complexo dominante: wn = {dom[0]:.2f} rad/s ({dom[0] / (2 * np.pi):.3f} Hz), zeta = {dom[1]:.3f}")
        modelos[(na, nb, nk)] = (th, ys, ree, reu, lim)

    fig, ax = plt.subplots(1, 2, figsize=(LARGURA * 2 + 0.2, 1.8))
    estilos = [((2, 3, 0), AZUL, ":"), (escolhidos["(2,3,nk)"], AZUL, "-"), (escolhidos["(10,4,nk)"], LARANJA, "--")]
    for chave, cor, ls in estilos:
        _, _, ree, reu, lim = modelos[chave]
        rot = "ARX(%d,%d,%d)" % chave
        ax[0].plot(np.arange(1, 41), ree[1:], color=cor, ls=ls, label=rot)
        ax[1].plot(np.arange(-40, 41), reu, color=cor, ls=ls, label=rot)
    for a in ax:
        a.axhspan(-lim, lim, color="#e6e6e6", lw=0)
        a.set_xlabel("Lag (samples)")
    ax[0].set_ylabel(r"$\hat r_{\varepsilon\varepsilon}$")
    ax[1].set_ylabel(r"$\hat r_{\varepsilon u}$")
    ax[0].legend(loc="upper right")
    fig.savefig(FIG / "residual-correlation.pdf")
    plt.close(fig)

    t = np.arange(len(y)) * TS
    th10 = modelos[(10, 4, 0)][0]
    assert np.allclose(modelos[(10, 4, 0)][1], simular(th10, 10, 4, u, True), atol=1e-8)
    print(f"\nFIT da TF publicada (ARX(10,4,0) simulado com 7 amostras extras): "
          f"{nrmse(y, simular(th10, 10, 4, u, False), ni):.2f}")
    fig, ax = plt.subplots(2, 1, figsize=(LARGURA, 3.0), sharex=True, gridspec_kw={"height_ratios": [1, 2.4]})
    ax[0].step(t, u_volts, where="post", color=TINTA, lw=0.7)
    ax[0].set_ylabel("$u$ (V)")
    ax[1].plot(t, np.rad2deg(y), color=TINTA, lw=1.3, label="Measured")
    for chave, cor, ls in estilos:
        ax[1].plot(t, np.rad2deg(modelos[chave][1]), color=cor, ls=ls, lw=0.9, label="ARX(%d,%d,%d)" % chave)
    ax[1].set(ylabel=r"$\theta - \bar\theta$ (deg)", xlabel="Time (s)")
    for a in ax:
        a.set_xlim(t[ni] - 1, t[ni] + 14)
        a.axvline(t[ni], color="#8c8c8c", lw=0.6, ls=":")
    ax[0].legend(*ax[1].get_legend_handles_labels(), loc="lower center", ncol=2,
                 bbox_to_anchor=(0.5, 1.02))
    fig.savefig(FIG / "validation.pdf")
    plt.close(fig)

    niveis, dur, f, pxx, f95 = excitacao(u_volts)
    print(f"\nExcitação: níveis {niveis}, {len(dur) + 1} trocas, duração dos níveis "
          f"min {dur.min():.2f} s, mediana {np.median(dur):.2f} s, max {dur.max():.2f} s")
    print("  durações distintas (s):", np.unique(np.round(dur, 2))[:15])
    print(f"  fração da potência abaixo de 1,5 Hz: {100 * f95:.1f} %; pico em {f[np.argmax(pxx)]:.2f} Hz")
    fig, ax = plt.subplots(figsize=(LARGURA, 1.6))
    ax.semilogy(f, pxx, color=AZUL)
    ax.set(xlabel="Frequency (Hz)", ylabel="PSD (V$^2$/Hz)", xlim=(0, 5))
    ax.set_ylim(1e-5, 1e-1)
    ax.axvspan(0.4, 1.0, color="#e6e6e6", lw=0)
    fig.savefig(FIG / "excitation-psd.pdf")
    plt.close(fig)

    print("\nMalha fechada (mediana [Q1, Q3]):")
    for nome in mf.ENSAIOS:
        tt, r, yy = mf.carregar(nome)
        d = pd.DataFrame(list(mf.degraus(tt, r, yy)))
        for sentido, g in d.groupby("sentido"):
            partes = []
            for c in ["sobressinal_pct", "subida_s", "acomodacao_s", "erro_regime"]:
                q1, q2, q3 = g[c].quantile([0.25, 0.5, 0.75])
                partes.append(f"{c} {q2:.2f} [{q1:.2f}, {q3:.2f}]")
            print(f"  {nome[8:18]} {sentido:7s} n={len(g)}: " + "; ".join(partes))
    tt, r, yy = mf.carregar(mf.ENSAIOS[0])
    ctrl = pd.read_csv(mf.DADOS / mf.ENSAIOS[0], index_col=0).iloc[1:, 3].astype(float).to_numpy()
    j = (tt >= tt[0] + 20) & (tt <= tt[0] + 35)
    print(f"  sinal de controle 13/09: min {ctrl.min():.3f} V, max {ctrl.max():.3f} V; "
          f"amostras com u+1 V < 1 V (u<0): {100 * np.mean(ctrl < 0):.1f} %")
    fig, ax = plt.subplots(2, 1, figsize=(LARGURA, 2.7), sharex=True, gridspec_kw={"height_ratios": [2, 1]})
    ax[0].plot(tt[j] - tt[j][0], r[j], color=TINTA, lw=0.8, ls="--", label="Reference")
    ax[0].plot(tt[j] - tt[j][0], yy[j], color=AZUL, lw=1.0, label="Measured")
    ax[0].set_ylabel(r"$\theta$ (deg)")
    ax[0].legend(loc="upper right", ncol=2)
    ax[1].plot(tt[j] - tt[j][0], ctrl[j], color=LARANJA, lw=0.9)
    ax[1].axhline(0, color="#8c8c8c", lw=0.6, ls=":")
    ax[1].set(ylabel="PID output (V)", xlabel="Time (s)")
    fig.savefig(FIG / "closed-loop.pdf")
    plt.close(fig)


if __name__ == "__main__":
    main()
