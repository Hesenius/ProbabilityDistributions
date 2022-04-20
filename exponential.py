from scipy.stats import expon
import matplotlib.pyplot as plt

# Specified probability parameter
mu = 2
n = 100
x = [i for i in range(0,n)]

# Sample according to Binomail distribution
y = expon.rvs(scale=2, size=n)

plt.plot(x,y, "ob)