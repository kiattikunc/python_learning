import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(2.0, 10.0, num=7)
print(x)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x test label')
plt.ylabel('y test label')
plt.title("Test title")

plt.legend()
plt.show()