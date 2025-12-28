import numpy as np
import matplotlib.pyplot as plt

X = np.random.uniform(0, 1, n)

S_n = np.cumsum(X) / np.arange(1, n + 1)

plt.figure(figsize=(10, 6))
plt.plot(S_n, label='Cumulative Mean $S_n$')
plt.axhline(y=0.5, color='red', linestyle='--', label='μ = 0.5')

plt.xlabel('Number of Observations (n)')
plt.ylabel('Cumulative Mean')
plt.title('SLLN Simulation for U(0,1)')
plt.legend()
plt.grid(True)
plt.show()

