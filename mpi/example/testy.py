from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

data = np.empty(100,dtype = float)
if rank == 0:
    #data = {'a':5, 'g':['f',22.0]}
    data[:] = np.arange(100,dtype = float)
else:
    #data = comm.recv(source=rank - 1)
    comm.Recv(data, source = rank -1)
if rank < size - 1:
    comm.Send(data, dest = rank + 1) 
print(f"I, rank {rank} in a group of {size}, finished, lastitem: {data[-1]}")
