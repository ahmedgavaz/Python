import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('SIN(X)')
plt.title('Function SIN(X)')
plt.grid()
plt.show()
