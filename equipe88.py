import numpy as np
import matplotlib.pyplot as plt
from schema import schema

# Paramètres
sigma = 1
L = 1
f = lambda x: np.sin(np.pi * x)
h = 1/10
x_vals = np.linspace(0, L, int(L/h) + 1)

# Solution exacte
def u_exact(x, t):
    return np.exp(-np.pi**2 * t) * np.sin(np.pi * x)

# Étapes de temps
for tau in [0.01, 0.001]:
    K = int(1 / tau)
    t_vals, y_vals = schema(sigma, L, f, h, tau, K)

    times_to_plot = [0, 0.05, 0.1, 1]
    indices = [int(t / tau) for t in times_to_plot]

    plt.figure(figsize=(10, 6))
    for idx, t in zip(indices, times_to_plot):
        u_num = np.zeros(len(x_vals))
        u_num[1:-1] = y_vals[:, idx]
        u_ex = u_exact(x_vals, t)
        plt.plot(x_vals, u_num, label=f"Numérique t={t}")
        plt.plot(x_vals, u_ex, '--', label=f"Exact t={t}")

    plt.title(f"Comparaison solution exacte vs numérique (τ = {tau})")
    plt.xlabel("x")
    plt.ylabel("Température u(x,t)")
    plt.legend()
    plt.grid()
    plt.show()