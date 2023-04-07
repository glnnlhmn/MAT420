# Import required libraries
import numpy as np
import matplotlib.pyplot as plt


# Define function to calculate logistic growth with proportional harvesting
def logistic_harvesting(r, K, h, alpha, t, N0):
    N = np.zeros(len(t))
    N[0] = N0
    for i in range(1, len(t)):
        N[i] = N[i-1] + r*N[i-1]*(1 - N[i-1]/K) - h*N[i-1]**alpha
    return N

# Define parameter values
r = 0.3    # growth rate
K = 1000   # carrying capacity
h = 0.5    # harvesting rate
alpha = 1  # harvest exponent
N0 = 100   # initial population size

# Define time range
t = np.arange(0, 50, 0.1)

# Calculate population size over time
N = logistic_harvesting(r, K, h, alpha, t, N0)

# Plot population size over time
plt.plot(t, N)
plt.xlabel('Time')
plt.ylabel('Population size')
plt.title('Logistic growth with proportional harvesting')

# Define parameter ranges for sensitivity tests
r_range = np.arange(0.1, 1, 0.1)
K_range = np.arange(500, 1500, 100)
h_range = np.arange(0.05, 0.15, 0.01)
alpha_range = np.arange(0.5, 1.5, 0.1)
N0_range = np.arange(50, 150, 10)

# Define empty arrays to store sensitivity test results
r_sensitivity = np.zeros(len(r_range))
K_sensitivity = np.zeros(len(K_range))
h_sensitivity = np.zeros(len(h_range))
alpha_sensitivity = np.zeros(len(alpha_range))
N0_sensitivity = np.zeros(len(N0_range))

# Perform sensitivity tests
for i in range(len(r_range)):
    r_sensitivity[i] = logistic_harvesting(r_range[i], K, h, alpha, t, N0)[-1] - N0
for i in range(len(K_range)):
    K_sensitivity[i] = logistic_harvesting(r, K_range[i], h, alpha, t, N0)[-1] - N0
for i in range(len(h_range)):
    h_sensitivity[i] = logistic_harvesting(r, K, h_range[i], alpha, t, N0)[-1] - N0
for i in range(len(alpha_range)):
    alpha_sensitivity[i] = logistic_harvesting(r, K, h, alpha_range[i], t, N0)[-1] - N0
for i in range(len(N0_range)):
    N0_sensitivity[i] = logistic_harvesting(r, K, h, alpha, t, N0_range[i])[-1] - N0

# Plot sensitivity test results
plt.figure()
plt.plot(r_range, r_sensitivity)
plt.xlabel('Growth rate')
plt.ylabel('Population size sensitivity')
plt.title('Sensitivity of final population size to growth rate')

plt.figure()
plt.plot(K_range, K_sensitivity)
plt.xlabel('Carrying capacity')
plt.ylabel('Population size sensitivity')
plt.title('Sensitivity of final population size to carrying capacity')

plt.figure()
plt.plot(h_range, h_sensitivity)
plt.xlabel('Harvesting rate')
plt.ylabel('Population size sensitivity')
plt.title('Sensitivity of final population size to harvesting rate')

plt.figure()
