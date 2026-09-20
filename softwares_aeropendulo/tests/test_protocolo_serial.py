"""Codificação dos comandos da interface, conferida contra a decodificação do firmware.

A decodificação replica `ler_dados_serial()` de
firmwares_microcontroladores/PlatformIo/Esp32_ttgo_modulos/lib/ler_escrever_serial.
"""

import numpy as np
import pytest

from src_interface.coleta_dados import ColetaDados


class PortaFalsa:
    def __init__(self):
        self.escritas = []

    def reset_input_buffer(self):
        pass

    def reset_output_buffer(self):
        pass

    def flush(self):
        pass

    def write(self, dados):
        self.escritas.append(dados.decode("utf-8"))
        return len(dados)


def decodificar_firmware(valor):
    rlen = float(valor)
    if 1000.0 < rlen < 2001.0:
        return "amplitude", rlen * 30.0 / 1000.0 - 30.0
    if 2001.0 < rlen < 3001.0:
        return "frequencia", rlen * 5.0 / 1000.0 - 10.0
    if 3001.0 < rlen < 4001.0:
        return "offset", rlen * 120.0 / 1000.0 - 360.0
    return "codigo", rlen


@pytest.fixture
def coleta():
    objeto = ColetaDados.__new__(ColetaDados)
    objeto.disp = PortaFalsa()
    objeto.salvar_dados = np.array([[], [], [], [], [], [], []]).astype(object)
    return objeto


@pytest.mark.parametrize(
    "metodo, valor, campo",
    [
        ("set_amplitude", "15", "amplitude"),
        ("set_amplitude", "30", "amplitude"),
        ("set_frequencia", "2.5", "frequencia"),
        ("set_offset", "60", "offset"),
        ("set_offset", "120", "offset"),
    ],
)
def test_comando_decodificado_pelo_firmware(coleta, metodo, valor, campo):
    getattr(coleta, metodo)(valor)
    enviado = coleta.disp.escritas[-1]
    assert decodificar_firmware(enviado) == (campo, pytest.approx(float(valor), abs=0.2))


def test_codigo_de_execucao(coleta):
    coleta.set_sinal("12000")
    assert coleta.disp.escritas == ["12000"]


def test_gravacao_esvazia_o_buffer(coleta, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    amostra = np.arange(7, dtype="float64").reshape(7, 1)
    coleta.salvar_dados = np.append(coleta.salvar_dados, amostra, axis=1)
    coleta.salvar_dados_colhidos()
    assert coleta.salvar_dados.shape == (7, 0)

    coleta.salvar_dados = np.append(coleta.salvar_dados, amostra + 10, axis=1)
    coleta.salvar_dados_colhidos()
    arquivos = sorted((tmp_path / "dados_de_ensaio").glob("arquivo_*.csv"))
    assert arquivos, "nenhum CSV gravado"
    ultimo = np.loadtxt(arquivos[-1], delimiter=",", skiprows=1)
    assert ultimo.ndim == 1 and ultimo[1] == 10.0
