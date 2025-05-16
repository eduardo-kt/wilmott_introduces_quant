# paridade call-put
# S(t) - C(t) + P(t) = Ke^(-r*(T-t))
# S(t) preço do ativo
# C(t) preço da call (ask)
# P (t) preço da put (bid)
# K strike price
# e^(-r*(T-t)) valor presente com taxa r e maturidade em T
import numpy as np
import matplotlib.pyplot as plt


class CallPutParity:
    def __init__(self, spot, call, put, r, strike, maturity):
        self.spot = np.array(spot)
        self.call = np.array(call)
        self.put = np.array(put)
        self.r = r
        self.strike = strike
        self.T = maturity / 252  # converter em anos

        if not len(self.spot) == len(self.call) == len(self.put):
            raise ValueError("Listas de preços devem ter o mesmo comprimento")

    def lhs_parity(self):
        return self.spot - self.call + self.put

    def rhs_parity(self):
        return self.strike * np.exp(-self.r * self.T)

    def arbitrage_ratio(self):
        return self.lhs_parity() / self.rhs_parity()

    def plot_arbitrage(self):
        ratio = self.arbitrage_ratio()
        plt.figure(figsize=(10, 5))
        plt.plot(ratio, label="Lado Esquerdo / Lado Direito")
        plt.axhline(
            1,
            color="gray",
            linestyle="--",
            label="Sem arbitragem (Proporção = 1)",
        )
        plt.axhline(
            1.02,
            color="green",
            linestyle=":",
            label="Possível arbitragem (Compra)",
        )
        plt.axhline(
            0.98,
            color="red",
            linestyle=":",
            label="Possível arbitragem (Venda)",
        )
        plt.title("Verificação da Paridade Call-Put")
        plt.xlabel("Tempo (índice)")
        plt.ylabel("Proporção")
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    call_put_model = CallPutParity(
        spot=[90, 93, 98, 100, 104, 102],
        call=[2.5, 2.5, 3.5, 5, 5.5, 6.5],
        put=[11.5, 8.5, 3.5, 1, 2.7, 1.4],
        r=0.13,
        strike=100,
        maturity=30,
    )

    call_put_model.plot_arbitrage()
