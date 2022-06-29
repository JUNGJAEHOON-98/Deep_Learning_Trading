import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title("sin & cos")
plt.plot(x, y1, 'g', label="sin")
plt.plot(x, y2, 'r', linestyle="--", label="cos")
plt.xlabel("Input")
plt.ylabel("Value")
plt.legend()
plt.show()