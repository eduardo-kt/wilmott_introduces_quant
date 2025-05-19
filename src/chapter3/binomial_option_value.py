import math
from typing import Callable


def binomial_option_price(
    asset: float,
    sigma: float,
    rate: float,
    strike: float,
    expiry: float,
    numb_steps: int,
    payoff: Callable[[float, float], float],
) -> float:

    dt = expiry / numb_steps
    discount_factor = math.exp(-rate * dt)

    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(rate * dt) - d) / (u - d)

    S = [0.0 for _ in range(numb_steps + 1)]
    S[0] = asset

    for n in range(1, numb_steps + 1):
        for j in reversed(range(1, n + 1)):
            S[j] = u * S[j - 1]
        S[0] = d * S[0]

    V = [payoff(S[j], strike) for j in range(numb_steps + 1)]

    for n in reversed(range(1, numb_steps + 1)):
        for j in range(n):
            V[j] = (p * V[j + 1] + (1 - p) * V[j]) * discount_factor

    return V[0]


def call_payoff(S, K):
    return max(S - K, 0)


if __name__ == "__main__":
    price = binomial_option_price(
        asset=100,
        sigma=0.2,
        rate=0.05,
        strike=100,
        expiry=1,
        numb_steps=3,
        payoff=call_payoff,
    )
    print(f"Option Price: {price:.4f}")
