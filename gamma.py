from scipy.stats import gamma
import matplotlib.pyplot as plt

# Specified probability parameter
a = 2
b = 3
n = 100
x = [i for i in range(0,n)]

# Sample according to Gamma distribution
y = gamma.rvs(a, b, size=n)

plt.plot(x,y, "ob")
plt.show()