from scipy.stats import chi2
import matplotlib.pyplot as plt

# Specified probability parameter
df1 = 10
df2 = 20
df3 = 30
df4 = 40
df5 = 50

# calculate range we want to display
x = np.linspace(0,
                30, 500)

# Sample according to chi2 distribution
rv1 = chi2(df1)
rv2 = chi2(df2)
rv3 = chi2(df3)
rv4 = chi2(df4)
rv5 = chi2(df5)

plt.plot(x, rv1.pdf(x), 'r', label='df = 10')
plt.plot(x, rv2.pdf(x), 'g',label='df = 20')
plt.plot(x, rv3.pdf(x), 'b', label='df = 30')
plt.plot(x, rv4.pdf(x), 'black',label='df = 40')
plt.plot(x, rv5.pdf(x), 'yellow',label='df = 50')
plt.legend(loc="upper left")

plt.show()