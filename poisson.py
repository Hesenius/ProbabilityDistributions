rom scipy.stats import poisson
import matplotlib.pyplot as plt

# Specified probability parameter
mu = 2
n = 100
x = [i for i in range(0,n)]

# Sample according to Binomail distribution
y = poisson.rvs(mu, size=n)

plt.plot(x,y, "ob")
plt.show()