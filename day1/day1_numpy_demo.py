import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
noise = np.random.normal(0, 1, size=x.shape)
y = 2 * x + 3 + noise
print("x mean:", np.mean(x))
print("y mean:", np.mean(y))
print("x shape:", x.shape)
print("y shape:", y.shape)

plt.scatter(x, y, s=12)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Day 1: Simple Data Visualization")
plt.savefig("day1_plot.png", dpi=200)
plt.show()