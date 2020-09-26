import numpy as np
import itertools

inp = np.random.sample((4,4))
print('full:', inp)

print(inp[1,:])
print(inp[:,2])

inp[:2,:2] = 0.21

print(inp)

# Chequerboard pattern

base = np.zeros((8,8))

base[slice(0,8,2),slice(0,8,2)] = 1
base[slice(1,8,2),slice(1,8,2)] = 1
print(base)
