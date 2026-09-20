"""Métricas de desempenho em malha fechada a partir dos ensaios gravados pela interface.

Os ensaios de malha fechada em softwares_aeropendulo/src_interface/dados_de_ensaio/ usam
referência em onda quadrada. Cada troca de nível é tratada como um degrau, e para cada um
calcula-se:

- sobressinal: maior ultrapassagem do valor final, em % do tamanho do degrau;
- tempo de subida: de 10 % a 90 % do degrau;
- tempo de acomodação: último instante em que a saída sai da faixa de ±5 % do degrau em torno
  do valor final (o ruído de leitura do potenciômetro torna a faixa de ±2 % pouco estável);
- erro em regime: |referência − valor final|, com o valor final igual à média dos últimos 20 %
  do intervalo até a próxima troca.

Grandezas em graus. O firmware grava a referência somada a 31 e calcula o erro como
referência − (ângulo − 31); o script confere essa relação antes de calcular.

Uso (a partir da raiz do repositório):
    uv run --with numpy --with pandas python \
        materiais_complementares/analise_malha_fechada/metricas_malha_fechada.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "softwares_aeropendulo/src_interface/dados_de_ensaio"
ENSAIOS = ["arquivo_13_9_2023_23_48_56.csv", "arquivo_14_9_2023_20_31_13.csv"]
FAIXA = 0.05


def carregar(nome):
    d = pd.read_csv(DADOS / nome, index_col=0)
    d.columns = ["ref31", "ang", "erro", "controle", "entrada", "entrada_dup", "t"]
    d = d.iloc[1:].reset_index(drop=True)
    r = d.ref31.to_numpy() - 31.0
    y = d.ang.to_numpy() - 31.0
    residuo = np.max(np.abs(d.erro.to_numpy() - (r - y)))
    assert residuo < 0.01, f"erro gravado não bate com referência − saída ({residuo:.3f})"
    return d.t.to_numpy(), r, y


def degraus(t, r, y):
    trocas = np.where(np.abs(np.diff(r)) > 1e-6)[0] + 1
    for i, k in enumerate(trocas[:-1]):
        fim = trocas[i + 1]
        antes, depois = r[k - 1], r[k]
        passo = depois - antes
        ts, ys = t[k:fim] - t[k], y[k:fim]
        final = ys[int(0.8 * len(ys)):].mean()
        sentido = np.sign(passo)
        sobressinal = max(0.0, np.max((ys - final) * sentido)) / abs(passo) * 100
        fr = (ys - antes) / passo
        subida = ts[np.argmax(fr >= 0.9)] - ts[np.argmax(fr >= 0.1)] if np.any(fr >= 0.9) else np.nan
        fora = np.where(np.abs(ys - final) > FAIXA * abs(passo))[0]
        acomodacao = ts[fora[-1]] if len(fora) else 0.0
        yield {
            "sentido": "subida" if passo > 0 else "descida",
            "passo": passo,
            "sobressinal_pct": sobressinal,
            "subida_s": subida,
            "acomodacao_s": acomodacao,
            "erro_regime": abs(depois - final),
            "janela_s": ts[-1],
        }


def main():
    for nome in ENSAIOS:
        t, r, y = carregar(nome)
        tab = pd.DataFrame(list(degraus(t, r, y)))
        print(f"\n{nome}: {len(tab)} degraus de ±{tab.passo.abs().median():.0f}°, "
              f"janela de {tab.janela_s.median():.2f} s por degrau")
        resumo = tab.groupby("sentido")[["sobressinal_pct", "subida_s", "acomodacao_s", "erro_regime"]].median()
        print(resumo.round(2).to_string())


if __name__ == "__main__":
    main()
