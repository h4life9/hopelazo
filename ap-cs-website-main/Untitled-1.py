
import numpy as np
import matplotlib.pyplot as plt

# Given values
L = 0.100
D = 0.010
dx = 0.010
k = 15
h = 30
T_inf = 20
T_base = 100

# Fin parameters
Ac = np.pi * D**2 / 4
P = np.pi * D
r = h * P * dx**2 / (k * Ac)

# 11 nodes: 0 through 10
N = int(L / dx) + 1
A = np.zeros((N, N))
b = np.zeros(N)

# Base boundary condition
A[0, 0] = 1
b[0] = T_base

# Interior nodes
for i in range(1, N - 1):
    A[i, i-1] = 1
    A[i, i] = -(2 + r)
    A[i, i+1] = 1
    b[i] = -r * T_inf

# Insulated tip boundary condition
A[N-1, N-2] = 2
A[N-1, N-1] = -(2 + r)
b[N-1] = -r * T_inf

# Solve the system
T = np.linalg.solve(A, b)
x = np.arange(N) * dx

# Display results
print("Node   x (mm)   Temperature (C)")
for i in range(N):
    print(f"{i:3d}    {x[i]*1000:5.0f}       {T[i]:8.2f}")

# Plot temperature distribution
plt.plot(x * 1000, T, "o-")
plt.xlabel("Distance along fin (mm)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Distribution Along an Insulated Fin")
plt.grid(True)
plt.tight_layout()
plt.show()
