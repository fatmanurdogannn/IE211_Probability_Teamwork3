# CLT simulation
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, probplot

n_values = [2, 5, 10, 30, 50]
m = 1000

mu = 0.5
sigma = np.sqrt(1 / 12)

np.random.seed(42)

for n in n_values:
    samples = np.random.uniform(0, 1, size=(m, n))
    S_n = np.sum(samples, axis=1)

    Z = (S_n - n * mu) / (sigma * np.sqrt(n))

    # Histogram + Normal Overlay
    plt.figure()
    plt.hist(Z, bins=30, density=True, alpha=0.7)
    x = np.linspace(-4, 4, 400)
    plt.plot(x, norm.pdf(x))
    plt.title(f"Histogram of Standardized Sums (n = {n})")
    plt.xlabel("Z")
    plt.ylabel("Density")
    plt.show()

    # Q-Q Plot
    plt.figure()
    probplot(Z, dist="norm", plot=plt)
    plt.title(f"Normal Q-Q Plot (n = {n})")
    plt.show()
