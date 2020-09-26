import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt('points_circle.dat')

plt.plot(arr[:,0],arr[:,1], 'o')
plt.show()

translate = np.array([2.1,1.1])

translated = arr * translate

plt.plot(translated[:,0],translated[:,1], 'o')
plt.show()
