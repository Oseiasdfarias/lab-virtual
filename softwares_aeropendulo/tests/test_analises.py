"""Reprodutibilidade dos scripts de análise publicados na documentação."""

import importlib.util

import pandas as pd
import pytest

from conftest import RAIZ


def carregar(caminho):
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


@pytest.fixture(scope="module")
def ident():
    return carregar(RAIZ / "materiais_complementares/Identificacao_de_Sistemas/identificacao_aeropendulo/ident_up/metricas_validacao.py")


@pytest.fixture(scope="module")
def malha_fechada():
    return carregar(RAIZ / "materiais_complementares/analise_malha_fechada/metricas_malha_fechada.py")


@pytest.mark.parametrize("na, nb", [(2, 3), (10, 4)])
def test_coeficientes_iguais_ao_notebook(ident, na, nb):
    u, y, ni = ident.carregar()
    theta = ident.estimar(u, y, ni, na, nb)
    assert theta == pytest.approx(ident.THETA_NOTEBOOK[(na, nb)], abs=5e-8)


@pytest.mark.parametrize(
    "na, nb, completar, esperado",
    [(2, 3, True, 51.35), (10, 4, False, 55.97), (10, 4, True, 78.30)],
)
def test_nrmse_publicado(ident, na, nb, completar, esperado):
    u, y, ni = ident.carregar()
    yp = ident.simular(ident.estimar(u, y, ni, na, nb), na, nb, u, completar)
    assert ident.nrmse(y, yp, ni) == pytest.approx(esperado, abs=0.01)


@pytest.mark.parametrize(
    "arquivo, sentido, sobressinal",
    [
        ("arquivo_13_9_2023_23_48_56.csv", "subida", 5.84),
        ("arquivo_13_9_2023_23_48_56.csv", "descida", 25.49),
        ("arquivo_14_9_2023_20_31_13.csv", "subida", 5.88),
        ("arquivo_14_9_2023_20_31_13.csv", "descida", 26.91),
    ],
)
def test_sobressinal_publicado(malha_fechada, arquivo, sentido, sobressinal):
    t, r, y = malha_fechada.carregar(arquivo)
    tabela = pd.DataFrame(list(malha_fechada.degraus(t, r, y)))
    mediana = tabela[tabela.sentido == sentido].sobressinal_pct.median()
    assert mediana == pytest.approx(sobressinal, abs=0.01)
