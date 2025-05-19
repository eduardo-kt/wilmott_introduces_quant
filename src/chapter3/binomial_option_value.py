import math


def option_value(
    r: float,
    delta_t: int,
    sigma: float,
    v_positive: float,
    v_negative: float,
) -> float:

    u = 1 + sigma * math.sqrt(delta_t)
    v = 1 - sigma * math.sqrt(delta_t)

    p = 1 / 2 + (r * math.sqrt(delta_t)) / (2 * sigma)

    expected_value = p * v_positive + (1 - p) * v_negative

    option_value = expected_value / (1 + r * delta_t)

    return option_value


if __name__ == "__main__":
    s = 100
    r = 0.1
    delta_t = 1 / 12  # 1 / 252
    sigma = 0.2
    v_positive = 12.0
    v_negative = 5.0
    value = option_value(r, delta_t, sigma, v_positive, v_negative)
    print(f"{value:.2f}")
