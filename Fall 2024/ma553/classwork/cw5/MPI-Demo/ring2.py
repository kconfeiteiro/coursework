#/usr/bin/env python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 1000000
s = np.empty(n, dtype=np.float64)
s[:] = rank
r = np.zeros(n, dtype=np.float64)

src = rank - 1 if rank != 0        else size - 1
dst = rank + 1 if rank != size - 1 else 0

if rank % 2 == 0:
    comm.Send(s, dest=dst)
    comm.Recv(r, source=src)
else:
    comm.Recv(r, source=src)
    comm.Send(s, dest=dst)
print(rank, r[:10])
