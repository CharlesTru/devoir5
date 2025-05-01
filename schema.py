import numpy as np
from euler_explicite import euler_explicite

def schema(sigma, L, f, h, tau, K):
    n = int(L / h)
    x = np.linspace(0, L, n+1)
    
    # Initialisation de U0 (n-1 composantes, points intérieurs)
    U0 = np.array([f(x[j]) for j in range(1, n)])

    # Construction de la matrice Ah de taille (n-1)x(n-1)
    Ah = np.zeros((n-1, n-1))
    for i in range(n-1):
        Ah[i, i] = -2
        if i > 0:
            Ah[i, i-1] = 1
        if i < n-2:
            Ah[i, i+1] = 1
    Ah = (sigma / h**2) * Ah

    # Fonction F(t, U) = Ah @ U
    def F(t, U):
        return Ah @ U

    # Appel d'euler_explicite
    t_vals, y_vals = euler_explicite(F, 0, U0, tau, K * tau)

    return t_vals, y_vals