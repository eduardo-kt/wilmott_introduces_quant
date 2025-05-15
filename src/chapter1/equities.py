import random
import matplotlib.pyplot as plt


def random_walk(inicial: float, periodos: int) -> list:
    values = [inicial]
    for i in range(periodos):
        if random.randint(0, 1) == 1:
            values.append(round(values[-1] * 1.1, 2))
        else:
            values.append(round(values[-1] * 0.9, 2))
    return values


if __name__ == "__main__":
    r_walk = random_walk(100.00, 100)
    plt.plot(r_walk)
    plt.title("Random Walk")
    plt.xlabel("Time")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.show()
