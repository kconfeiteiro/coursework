from mpi4py import MPI

comm = MPI.COMM_WORLD # communicator object 

Nproc = comm.Get_size() # Get the number of processes
Pid = comm.Get_rank() # Get the individual process ID

if Pid == 0: 
   print(" Master: No. of processes={}".format(Nproc))

print(" Process {} Hays 'Hello, world!' ".format(Pid)) 
