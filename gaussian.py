from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(-20, 20, 0.1)
y1 = norm.pdf(x1, 0, 5)
y2 = norm.pdf(x1, 0, 3)
y3 = norm.pdf(x1, 5, 3)

plt.plot(x1, y2)
plt.plot(x1, y1)
plt.plot(x1, y3)

plt.legend(["Standard deviation 3", "Standard deviation 5", "mean value of 5"], loc ="upper left")
plt.show()