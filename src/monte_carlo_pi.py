import numpy as np
import matplotlib.pyplot as plt

# 1. Settings: Number of points to generate
n = 10000 

# 2. Generate random (x, y) points inside the unit square
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

# 3. Check if points fall inside the unit circle
distance = x**2 + y**2
inside_circle = distance <= 1

# 4. Estimate the value of Pi
pi_estimates = 4 * np.cumsum(inside_circle) / np.arange(1, n + 1)
final_estimate = pi_estimates[-1]

print(f"Estimated Pi value with n={n}: {final_estimate}")

# 5. Visualization: Plotting the convergence
plt.figure(figsize=(10, 6))
plt.plot(pi_estimates, label='Monte Carlo Estimation')
plt.axhline(y=np.pi, color='r', linestyle='--', label=f'True Pi Value ({np.pi:.5f})') # Reference line

# Grafik metinlerini İngilizceye çevirdiğimiz kısım:
plt.title(f'Monte Carlo Pi Estimation Convergence Graph (n={n})') # Başlık
plt.xlabel('Number of Points (n)') # X ekseni
plt.ylabel('Pi Estimate') # Y ekseni
plt.legend()
plt.grid(True)

# 6. Save the figure
plt.savefig('results/figures/pi_estimation.png')
plt.show()
