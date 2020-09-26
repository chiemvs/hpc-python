import numpy as np

arr = np.arange(1000)
dif = np.zeros(999, int)

def forl():
    for i in range(1,len(arr)):
        dif[i-1] = arr[i] - arr[i-1]

def vect():
    dif = arr[1:] - arr[:-1]
