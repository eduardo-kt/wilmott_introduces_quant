import random
from src.chapter1 import RandomWalk


class RandomWalkTimeScales(RandomWalk):
    def __init__(
        self,
        inicial: float,
        periodos: int,
        fator_alta: float,
        fator_baixa: float,
    ):
        super().__init__(inicial, periodos)
        self.fator_alta = fator_alta
        self.fator_baixa = fator_baixa

    @property
    def fator_alta(self):
        return self._fator_alta

    @fator_alta.setter
    def fator_alta(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                "O valor precisa ser um número decimal positivo maior ou igual a 1.0"
            )
        if value < 1.0:
            raise ValueError(
                "O valor precisa ser um número decimal positivo maior ou igual a 1.0"
            )
        self._fator_alta = float(value)

    @property
    def fator_baixa(self):
        return self._fator_baixa

    @fator_baixa.setter
    def fator_baixa(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                "O valor precisa ser um número decimal positivo entre 0.0 e 1.0"
            )
        if value <= 0.0 or value >= 1.0:
            raise ValueError(
                "O valor precisa ser um número decimal positivo entre 0.0 e 1.0"
            )
        self._fator_baixa = value

    def generate_values(self):
        self.valores = [self.inicial]
        for _ in range(self.periodos):
            ultimo = self.valores[-1]
            if random.randint(0, 1) == 1:
                self.valores.append(round(ultimo * self.fator_alta, 2))
            else:
                self.valores.append(round(ultimo * self.fator_baixa, 2))
        return self.valores


if __name__ == "__main__":
    try:
        r_walk_custom = RandomWalkTimeScales(
            100.0, 100, fator_alta=1.05, fator_baixa=0.95
        )
        r_walk_custom.generate_values()
        r_walk_custom.plot()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
