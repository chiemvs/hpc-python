import numpy as np

A = np.random.sample((2,2))
Asym = A + A.T
B = np.random.sample((2,2))
Bsym = B + B.T

print(Asym * Bsym)

C = np.dot(Asym,Bsym)

print(C)
