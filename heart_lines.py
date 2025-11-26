import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(50,50))
plt.axis("equal")
plt.axis("off")

# Heart equation
t = np.linspace(0, 2*np.pi, 900)
x = 16 * np.sin(t)**3
y = (13 * np.cos(t)) - (5 * np.cos(2*t)) - (2 * np.cos(3*t)) - (np.cos(4*t))

# Draw radiating lines
for i in range(len(x)):
    plt.plot([0, x[i]], [0, y[i]], linewidth=0.4)

plt.show()
