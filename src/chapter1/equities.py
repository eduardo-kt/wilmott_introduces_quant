import random
import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, inicial: float, periodos: int):
        self.inicial = inicial
        self.periodos = periodos
        self.valores = []

    @property
    def inicial(self):
        return self._inicial

    @inicial.setter
    def inicial(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("O valor inicial precisa ser um número decimal positivo")
        if value <= 0:
            raise ValueError("O valor inicial precisa ser um número positivo")
        self._inicial = float(value)

    @property
    def periodos(self):
        return self._periodos

    @periodos.setter
    def periodos(self, value):
        if not isinstance(value, int):
            raise TypeError("Períodos prcisa ser um número inteiro positivo")
        if value <= 0:
            raise ValueError("Períodos prcisa ser um número inteiro positivo")
        self._periodos = value

    def generate_values(self):
        self.valores = [self.inicial]
        for _ in range(self.periodos):
            if random.randint(0, 1) == 1:
                self.valores.append(round(self.valores[-1] * 1.1, 2))
            else:
                self.valores.append(round(self.valores[-1] * 0.9, 2))
        return self.valores

    def plot(self):
        if not self.valores:
            self.generate_values()
        plt.plot(self.valores)
        plt.title("Random Walk")
        plt.xlabel("Time")
        plt.ylabel("Valor")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    try:
        r_walk = RandomWalk(100.00, 100)
        r_walk.generate_values()
        r_walk.plot()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
