import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD

myrank = comm.Get_rank()

n = 100000
dtype = int
data = np.full((n,), myrank, dtype = dtype)
other = np.empty((n,), dtype = dtype)

comm.Send([data, n, MPI.INT], dest = abs(myrank -1))
comm.Recv([other, n, MPI.INT], source = abs(myrank -1))

print(f'myrank: {myrank}, recieved: {other[0]}')
