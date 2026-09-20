# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Classe para obter os dados do Microcontrolador via USB
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#

import numpy.typing as npt
from abc import ABC, abstractmethod


class ColetaDadosInterface(ABC):
    """Contrato da comunicação serial com o microcontrolador (ver `ColetaDados`)."""

    @abstractmethod
    def get_dados(self) -> npt.ArrayLike:
        """Retorna a janela atual de amostras recebidas."""

    @abstractmethod
    def set_amplitude(self, amplitude: str) -> None:
        """Envia a amplitude do sinal de referência."""

    @abstractmethod
    def set_frequencia(self, frequencia: str) -> None:
        """Envia a frequência do sinal de referência."""

    @abstractmethod
    def set_offset(self, offset: str) -> None:
        """Envia o offset do sinal de referência."""

    @abstractmethod
    def set_sinal(self, sinal: str) -> None:
        """Envia um código de comando ao firmware."""

    @abstractmethod
    def listar_dir(self) -> None:
        """Prepara o diretório e o nome do arquivo do ensaio."""

    @abstractmethod
    def salvar_dados_colhidos(self):
        """Grava em CSV as amostras acumuladas."""

    @abstractmethod
    def reconectar(self):
        """Reabre a porta serial após uma falha."""
