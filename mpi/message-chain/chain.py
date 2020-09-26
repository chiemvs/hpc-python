import numpy as np
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD

myid = comm.Get_rank()
ntasks =comm.Get_size()

msg = np.full((10,), myid, dtype = int)
rcv = np.empty((10,), dtype = int)

#if myid < ntasks - 1:
#    comm.Isend([msg,10,MPI.INT],dest = myid + 1)
#    print(f'I, {myid}, send out {len(msg)} elements')
#if myid >= 1:
#    req = comm.Irecv([rcv,10,MPI.INT], source = myid - 1)
#    print(f'I, {myid}, received {len(rcv)} elements with first element {rcv[0]}')
#    req.wait()
#    print(f'I, {myid}, received {len(rcv)} elements with first element {rcv[0]}')


#trgt = myid + 1 if myid < (ntasks - 1) else MPI.PROC_NULL
#src = myid - 1 if myid > 1 else MPI.PROC_NULL
#comm.Sendrecv([msg,10,MPI.INT], dest = trgt, recvbuf = [rcv,10,MPI.INT], source = src)
#print(f'I, {myid}, send out {len(msg)} elements')
#print(f'I, {myid}, received {len(rcv)} elements with first element {rcv[0]}')

trgt = myid + 1 if myid < (ntasks - 1) else MPI.PROC_NULL
src = myid - 1 if myid >= 1 else MPI.PROC_NULL

reqs = []
reqs.append(comm.Isend([msg,10,MPI.INT],dest = trgt))
reqs.append(comm.Irecv([rcv,10,MPI.INT],source = src))
MPI.Request.waitall(reqs)
print(f'I, {myid}, send out {len(msg)} elements')
print(f'I, {myid}, received {len(rcv)} elements with first element {rcv[0]}')
