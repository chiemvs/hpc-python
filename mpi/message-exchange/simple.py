from mpi4py import MPI

comm = MPI.COMM_WORLD

myrank = comm.Get_rank()

comm.send({'rank':myrank}, dest = abs(myrank -1))
other = comm.recv(source = abs(myrank - 1))

print(f'I, {myrank}, recieved this {other}')

