from scipy.stats import t
from scipy.stats import norm
import matplotlib.pyplot as plt

# Specified probability parameter
df1 = 1
df2 = 2
df3 = 3
df4 = 4

# calculate range we want to display
x = np.linspace(-10,
                10, 200)

# Sample according to t distribution
rv1 = t(df1)
rv2 = t(df2)
rv3 = t(df3)
rv4 = t(df4)

plt.plot(x, rv1.pdf(x), 'r', label='df = 10')
plt.plot(x, rv2.pdf(x), 'g',label='df = 20')
plt.plot(x, rv3.pdf(x), 'b', label='df = 30')
plt.plot(x, rv4.pdf(x), 'black',label='df = 40')
plt.plot(x, norm.pdf(x), 'yellow', label='Gaussian')
plt.legend(loc="upper left")

plt.show()
