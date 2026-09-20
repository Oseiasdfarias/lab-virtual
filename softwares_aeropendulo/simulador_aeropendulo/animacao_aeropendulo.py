# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# -----------------------------------------------------
#
# Laboratório Virtual Sistemas Dinâmicos e Controle
# Tema: Simulação Aeropêndulo
# Autor: Oséias Farias
# Orientadores: Prof. Dr: Raphael Teixeira,
#               Prof. Dr: Rafael Bayma
#
# Data: 2023
#  ----------------------------------------------------
#
import vpython as vp
from .interfaces.animacao_aeropendulo import AnimacaoAeropenduloInterface


class AnimacaoAeropendulo(AnimacaoAeropenduloInterface):
    """
    Classe que implementa a aminação do Aeropêndulo.

    Atributo:
        comprimento_braco: tamanho do braço do Aeropêndulo.
    """

    def __init__(self, comprimento_braco=4.4) -> None:
        # Parâmetros do Aeropêndulo
        """Cria a cena do VPython e desenha o aeropêndulo e a hélice.

        Args:
            comprimento_braco: comprimento do braço no modelo 3D, em unidades da cena.
        """
        self.comprimento_braco = comprimento_braco
        self.scene = vp.canvas(
            title="<center><h1>Aeropêndulo</h1><center/>",
            width=650,
            height=580,
            align="left",
            autoscale=0,
            range=5,
            center=vp.vec(0, 3, 0),
            background=vp.vector(1.7, 0.7, 0.9),
            color=vp.vec(1, 0.6, 0.6),
            forward=vp.vec(-0.3, 0, -1),
        )
        self.scene.range = 6
        # chamando a função para criar a aminação gráfica do Aeropêndulo.
        self.aeropendulo = self.__aminacao()
        self.__helice()

    def __aminacao(self) -> vp.compound:
        """
        Classe que implementa o Aeropêndulo.

        Usa o `self.comprimento_braco` definido em `__init__`.

        Returns:
            Retorna um objeto (vpython) que contêm a estrutura do Aeropêndulo.
        """
        self.base = vp.box(
            pos=vp.vec(0, -0.85, 0),
            size=vp.vec(30, 0.2, 15),
            texture=vp.textures.wood,
            color=vp.vec(0.85, 0.72, 0.55),
        )
        self.parede = vp.box(
            pos=vp.vec(0, 7.1, -7.55),
            size=vp.vec(30, 16, 0.2),
            color=vp.vec(0.12, 0.12, 0.14),
            shininess=0.01,
        )
        self.sitio = vp.text(
            pos=vp.vec(0, 8.1, -7.45),
            text="AEROPÊNDULO",
            color=vp.vec(0.9, 0.9, 0.95),
            align="center",
            depth=0,
        )

        self.__desenhar_pendulo()

        # Eixo de sustentação metálico.
        self.eixo = vp.cylinder(
            pos=vp.vec(0, 5.2, 0.3),
            radius=0.09,
            axis=vp.vec(0, 0, -2),
            color=vp.vec(0.75, 0.75, 0.8),
            shininess=0.8,
        )

        # Estrutura vertical de compensado e travessa de suporte.
        self.b1 = vp.box(
            pos=vp.vec(0, 1.7, -2),
            size=vp.vec(3, 8, 0.6),
            texture=vp.textures.wood,
            color=vp.vec(0.9, 0.75, 0.58),
        )

        self.b2 = vp.box(
            pos=vp.vec(0, -0.6, -1.5),
            size=vp.vec(4.5, 0.4, 2.5),
            texture=vp.textures.wood,
            color=vp.vec(0.85, 0.7, 0.52),
        )

        self.logo = vp.box(
            pos=vp.vec(0, 2.5, -1.699),
            texture="https://i.imgur.com/D2xnkpF.png",
            size=vp.vec(2, 2, 0.2),
        )

        self.ufpa = vp.text(
            pos=vp.vec(0, 3.7, -1.6),
            text="UFPA",
            color=vp.vec(0.95, 0.95, 1.0),
            height=0.5,
            align="center",
            depth=0,
        )

        return self.pendulo

    def __helice(self) -> None:
        """Cria as pás da hélice: uma sempre visível e três extras, inicialmente ocultas,
        defasadas de 45° entre si.
        """
        self.helice = vp.box(
            pos=vp.vec(0.8, 0.6, 0),
            size=vp.vec(0.05, 0.2, 2),
            color=vp.vec(0.12, 0.12, 0.14),
            shininess=0.4,
        )

        self.helice1 = vp.box(
            pos=vp.vec(0.8, 0.6, 0),
            size=vp.vec(0.05, 0.2, 2),
            color=vp.vec(0.12, 0.12, 0.14),
            shininess=0.4,
        )
        self.helice1.axis = self.pendulo.axis
        self.helice1.size = vp.vec(0.05, 0.2, 2)
        self.helice1.rotate(axis=vp.vec(1, 0, 0), angle=vp.pi / 4)

        self.helice2 = vp.box(
            pos=vp.vec(0.8, 0.6, 0),
            size=vp.vec(0.05, 0.2, 2),
            color=vp.vec(0.12, 0.12, 0.14),
            shininess=0.4,
        )
        self.helice2.axis = self.pendulo.axis
        self.helice2.size = vp.vec(0.05, 0.2, 2)
        self.helice2.rotate(axis=vp.vec(1, 0, 0), angle=vp.pi / 2)

        self.helice3 = vp.box(
            pos=vp.vec(0.8, 0.6, 0),
            size=vp.vec(0.05, 0.2, 2),
            color=vp.vec(0.12, 0.12, 0.14),
            shininess=0.4,
        )
        self.helice3.axis = self.pendulo.axis
        self.helice3.size = vp.vec(0.05, 0.2, 2)
        self.helice3.rotate(axis=vp.vec(1, 0, 0), angle=3 * vp.pi / 4.0)
        self.helice1.visible = False
        self.helice2.visible = False
        self.helice3.visible = False

    def pause_giro(self) -> None:
        """Torna visíveis as três pás extras da hélice."""
        self.helice1.visible = True
        self.helice2.visible = True
        self.helice3.visible = True

    def girar_helice(self) -> None:
        """Oculta as três pás extras da hélice."""
        self.helice1.visible = False
        self.helice2.visible = False
        self.helice3.visible = False

    def set_posicao_helice(self, angle: float) -> None:
        """Gira as pás da hélice em torno do pivô.

        Args:
            angle: ângulo de rotação, em radianos.
        """
        self.helice.rotate(axis=vp.vec(0, 0, 1), angle=angle, origin=vp.vec(0, 5.2, 0))
        self.helice.size = vp.vec(0.05, 0.2, 2)

        self.helice1.rotate(axis=vp.vec(0, 0, 1), angle=angle, origin=vp.vec(0, 5.2, 0))
        self.helice1.size = vp.vec(0.05, 0.2, 2)

        self.helice2.rotate(axis=vp.vec(0, 0, 1), angle=angle, origin=vp.vec(0, 5.2, 0))
        self.helice2.size = vp.vec(0.05, 0.2, 2)

        self.helice3.rotate(axis=vp.vec(0, 0, 1), angle=angle, origin=vp.vec(0, 5.2, 0))
        self.helice3.size = vp.vec(0.05, 0.2, 2)

    def update_helice(self, angle: float, ts: float) -> None:
        """Faz a hélice acompanhar o braço e girar.

        Realinha as pás ao eixo do braço, gira-as em torno do pivô de `angle * ts` radianos
        e aplica um pequeno giro em torno do eixo do motor.

        Args:
            angle: velocidade angular do braço, em rad/s.
            ts: intervalo desde a amostra anterior, em segundos.
        """
        self.helice.size = vp.vec(0.05, 0.2, 2)
        self.helice1.size = vp.vec(0.05, 0.2, 2)
        self.helice2.size = vp.vec(0.05, 0.2, 2)
        self.helice3.size = vp.vec(0.05, 0.2, 2)

        self.helice.axis = self.pendulo.axis
        self.helice.size = vp.vec(0.05, 0.2, 2)
        self.helice1.axis = self.pendulo.axis
        self.helice1.size = vp.vec(0.05, 0.2, 2)
        self.helice2.axis = self.pendulo.axis
        self.helice2.size = vp.vec(0.05, 0.2, 2)
        self.helice3.axis = self.pendulo.axis
        self.helice3.size = vp.vec(0.05, 0.2, 2)

        self.helice.rotate(
            axis=vp.vec(0, 0, 1), angle=angle * ts, origin=vp.vec(0, 5.2, 0)
        )
        self.helice.size = vp.vec(0.05, 0.2, 2)

        self.helice1.rotate(
            axis=vp.vec(0, 0, 1), angle=angle * ts, origin=vp.vec(0, 5.2, 0)
        )
        self.helice1.size = vp.vec(0.05, 0.2, 2)

        self.helice2.rotate(
            axis=vp.vec(0, 0, 1), angle=angle * ts, origin=vp.vec(0, 5.2, 0)
        )
        self.helice2.size = vp.vec(0.05, 0.2, 2)

        self.helice3.rotate(
            axis=vp.vec(0, 0, 1), angle=angle * ts, origin=vp.vec(0, 5.2, 0)
        )
        self.helice3.size = vp.vec(0.05, 0.2, 2)

        # obs tentando ajustar o diro das hélices apenas para um lado ....
        # if x[1] + interface.valor_angle < np.pi/2:
        #     ag = 0.3
        # else:
        #     ag = -0.8

        self.helice.rotate(axis=vp.vec(1, 0, 0), angle=0.09)
        self.helice1.rotate(axis=vp.vec(1, 0, 0), angle=0.09)
        self.helice2.rotate(axis=vp.vec(1, 0, 0), angle=0.09)
        self.helice3.rotate(axis=vp.vec(1, 0, 0), angle=0.09)

    def __desenhar_pendulo(self) -> None:
        # Braço do Aeropêndulo.
        """Desenha o braço e o conjunto do motor e os agrupa no objeto `self.pendulo`."""
        self.barra = vp.box(
            pos=vp.vec(0, -1.4, 0),
            size=vp.vec(0.18, self.comprimento_braco, 0.18),
            color=vp.vec(0.15, 0.15, 0.17),
            shininess=0.6,
        )

        # Suporte que acopla o motor ao braço (usinagem em alumínio).
        self.base_motor = vp.cylinder(
            pos=vp.vec(-0.2, -4, 0),
            radius=0.35,
            axis=vp.vec(0.4, 0, 0),
            color=vp.vec(0.2, 0.2, 0.23),
            shininess=0.7,
        )
        # Carcaça do motor Coreless DC.
        self.base2_motor = vp.box(
            pos=vp.vec(0.4, -4, 0),
            size=vp.vec(0.4, 0.35, 0.35),
            color=vp.vec(0.15, 0.15, 0.18),
            shininess=0.8,
        )

        # Eixo metálico da hélice do motor.
        self.base_helice = vp.cylinder(
            pos=vp.vec(0.4, -4, 0),
            radius=0.04,
            axis=vp.vec(0.4, 0, 0),
            color=vp.vec(0.8, 0.8, 0.85),
            shininess=0.9,
        )

        # Motor completo.
        self.motor = vp.compound([self.base_motor, self.base2_motor, self.base_helice])

        # Aeropêndulo
        self.pendulo = vp.compound([self.barra, self.motor])
        self.pendulo.pos = vp.vec(0.31, 2.7, 0)
