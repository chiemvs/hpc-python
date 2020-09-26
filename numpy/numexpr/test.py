import numpy as np
import numexpr

x = np.random.random((1000000,1))

def numway():
    c = 0.2 * x**2
    c += 1.5 * x**3
    c -= 2.3 * x**0.5

def numway2():
    c = (0.2 * x**2) + (1.5 * x**3 - 2.3 * x**0.5)

def numexprway():
    c = numexpr.evaluate("0.2*x**2 + 1.5*x**3 - 2.3*x**0.5")

if __name__ == "__main__":
    numway()
