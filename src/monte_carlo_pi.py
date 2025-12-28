import numpy as np
import matplotlib.pyplot as plt

# 1. Settings: Number of points to generate (Higher n leads to more accurate estimation)
n = 10000 

# 2. Generate random (x, y) points inside the unit square
# Both coordinates are between 0 and 1 (Standard Uniform Distribution)
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

# 3. Check if points fall inside the unit circle
# Formula: x^2 + y^2 <= 1
distance = x**2 + y**2
inside_circle = distance <= 1

# 4. Estimate the value of Pi
# Formula: 4 * (number of points inside circle / total number of points)
pi_estimates = 4 * np.cumsum(inside_circle) / np.arange(1, n + 1)
final_estimate = pi_estimates[-1]

print(f"Estimated Pi value with n={n}: {final_estimate}")

# 5. Visualization: Plotting the convergence of the estimation
plt.figure(figsize=(10, 6))
plt.plot(pi_estimates, label='Monte Carlo Estimation')
plt.axhline(y=np.pi, color='r', linestyle='--', label=f'True Pi Value ({np.pi:.5f})') # Theoretical reference

plt.title(f'Monte Carlo Pi Estimation Convergence (n={n})')
plt.xlabel('Number of Iterations (n)')
plt.ylabel('Pi Estimate')
plt.legend()
plt.grid(True)

# 6. Save the figure to the required directory
plt.savefig('results/figures/pi_estimation.png')
plt.show()# Monte Carlo Pi
