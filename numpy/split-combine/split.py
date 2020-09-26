import numpy as np

data = np.random.sample((8,8))

a1, a2 = np.split(data, 2, axis = 0)
