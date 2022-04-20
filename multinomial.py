from scipy.stats import multinomial
import matplotlib.pyplot as plt

# Specified probability parameter
p = [0.3,0.2,0.5]
n = 10
x = [i for i in range(0,n)]

# Sample according to multinomial distribution
y = multinomial.rvs(n, p, size=10)

plt.plot(x,y, "ob")
plt.show()