from scipy.stats import binom
import matplotlib.pyplot as plt

# Specified probability parameter
p = 0.5
n = 10
x = [i for i in range(0,n)]

# Sample according to Binomail distribution
y = binom.rvs(n, p, size=10)

plt.plot(x,y, "ob")
plt.show()