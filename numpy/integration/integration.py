import numpy as np

def integrate(a = 0, b = np.pi/2, dx = 0.1):
    xs = np.arange(a,b,dx)
    change = (xs[1:] + xs[:-1])/2.0
    total = np.sum(np.sin(change) * dx)
    return total

    
