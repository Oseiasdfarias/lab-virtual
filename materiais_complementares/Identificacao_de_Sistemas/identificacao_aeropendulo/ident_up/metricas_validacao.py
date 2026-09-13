"""Reproduz a identificação do notebook Ensaio2-identificacao_aeropendulo.ipynb e mede o
ajuste de cada modelo nos dados de validação.

Compara duas montagens da função de transferência de 10ª ordem:
- "publicada": ct.tf([b0..b3], [1, -a1..-a10]), como no notebook e na monografia; o
  python-control lê os vetores em potências positivas de z, o que acrescenta 7 amostras de
  atraso em relação à regressão estimada;
- "ARX": numerador completado com zeros até o tamanho do denominador, que é exatamente a
  equação de diferenças ajustada (u[k]..u[k-3], y[k-1]..y[k-10]).

Uso (a partir da raiz do repositório):
    uv run --with numpy --with pandas --with control python \
        materiais_complementares/Identificacao_de_Sistemas/identificacao_aeropendulo/ident_up/metricas_validacao.py
"""

from pathlib import Path

import control as ct
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[4]
CSV = RAIZ / "softwares_aeropendulo/src_interface/dados_de_ensaio/arquivo_9_9_2023_13_33_24.csv"

THETA_NOTEBOOK = {
    (2, 3): [1.17551813, -0.18492522, -0.00260201, 0.00496163, 0.01630073],
    (10, 4): [0.89318233, 0.31622634, 0.01363859, -0.13344083, -0.1469042,
              -0.01163669, 0.0532, 0.11886751, 0.01877396, -0.14748834,
              -0.00295795, 0.00227106, 0.00166716, 0.00976541],
}
NRMSE_NOTEBOOK = {(2, 3): 51.35, (10, 4): 55.97}


def carregar():
    dados = pd.read_csv(CSV, header=None, sep=",").values
    dados[0][0] = 0.0
    tempo = np.array(dados[:, 7], dtype=float)
    entrada = np.array(dados[:, 6], dtype=float)
    saida = np.deg2rad(np.array(dados[:, 2], dtype=float))
    u = entrada[50:] - np.mean(entrada[50:])
    y = saida[50:] - np.mean(saida[50:])
    ni = int(0.6 * len(entrada))
    return u, y, ni


def estimar(u, y, ni, na, nb):
    idx = np.arange(na, ni + na)
    m = np.zeros((ni, na + nb))
    for l in range(na):
        m[:, l] = y[idx - l - 1]
    for l in range(nb):
        m[:, na + l] = u[idx - l]
    return np.linalg.inv(m.T @ m) @ m.T @ y[idx]


def simular(theta, na, nb, u, completar_numerador):
    a = theta[:na]
    b = list(theta[na:])
    den = [1.0, *(-a)]
    num = b + [0.0] * (len(den) - len(b)) if completar_numerador else b
    _, yp = ct.forced_response(ct.tf(num, den, 0.02), U=u)
    return yp


def nrmse(y, yp, ni):
    erro = np.sqrt(np.sum((y[ni:] - yp[ni:]) ** 2))
    base = np.sqrt(np.sum((y[ni:] - np.mean(y[ni:])) ** 2))
    return (1 - erro / base) * 100


def rmse_graus(y, yp, ni):
    return np.rad2deg(np.sqrt(np.mean((y[ni:] - yp[ni:]) ** 2)))


def main():
    u, y, ni = carregar()
    print(f"amostras após o descarte inicial: {len(y)}, identificação: {ni}, validação: {len(y) - ni}\n")
    for na, nb in [(2, 3), (10, 4)]:
        theta = estimar(u, y, ni, na, nb)
        confere = np.allclose(theta, THETA_NOTEBOOK[(na, nb)], atol=5e-8)
        print(f"ordem na={na}, nb={nb}: coeficientes iguais aos do notebook? {confere}")
        for rotulo, completar in [("publicada", False), ("ARX", True)]:
            if na == 2 and not completar:
                continue
            yp = simular(theta, na, nb, u, completar)
            print(f"  {rotulo:9s} NRMSE = {nrmse(y, yp, ni):6.2f} %   RMSE = {rmse_graus(y, yp, ni):.3f} graus")
        print(f"  notebook  NRMSE = {NRMSE_NOTEBOOK[(na, nb)]:6.2f} %\n")


if __name__ == "__main__":
    main()
