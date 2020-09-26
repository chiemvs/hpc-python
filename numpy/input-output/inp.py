import numpy as np

arr = np.loadtxt('xy-coordinates.dat')
arr[:,1] = arr[:,1] + 2.5

np.savetxt(fname = 'new-coors.dat', X = arr)
