from scipy.stats import bernoulli
import matplotlib.pyplot as plt

# Specified probability parameter
p = 0.5

x = [i for i in range(0,10)]
# Sample according to Bernoulli distribution
y = bernoulli.rvs(p, size=10)

plt.plot(x,r, "ob")
plt.show()
