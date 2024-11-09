from mpi4py import MPI
import math

comm = MPI.COMM_WORLD  # communicator object containing all processes
rank = comm.Get_rank()

if rank == 0:
   data = {'e': math.e, 'pi': math.pi}
   comm.send(data, dest=1)
elif rank == 1:
   data = comm.recv(source=0)

if rank == 1:
   print("Received: " + str(data))

