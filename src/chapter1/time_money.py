import math
import matplotlib.pyplot as plt


def compound_r(juro, tempo, principal=1, composicao=1):
    return principal * (1 + juro / composicao) ** (composicao * tempo)


def continuous_compound_r(juro, tempo, principal=1):
    return principal * math.exp(juro * tempo)


valor_continuo = [continuous_compound_r(0.1, x) for x in range(50)]

plt.figure(figsize=(8, 6))

for valor in [1, 3, 7]:
    sequencia = [compound_r(0.1, x, composicao=valor) for x in range(50)]
    plt.plot(sequencia)

plt.plot(valor_continuo)

plt.title("Sequência Exponencial")
plt.xlabel("x")
plt.ylabel(r"$f(x)$")
plt.grid(True)
plt.legend()
plt.show()
