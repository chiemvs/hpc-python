import numpy as np
import matplotlib.pyplot as plt

arr = np.random.sample((1000,))

print(arr.mean())
print(arr.std())

plt.hist(arr)
plt.show()
