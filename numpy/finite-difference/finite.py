import numpy as np

def diff(func = np.sin, dx = 0.1):
    arr = np.arange(0,np.pi,dx)
    return (func(arr[2:]) - func(arr[:-2]))/(2*dx)
    
