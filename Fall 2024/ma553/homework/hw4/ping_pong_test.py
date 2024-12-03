from mpi4py import MPI
import numpy as np
import time

def ping_pong_test(message_length, repetitions):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size != 2:
        raise ValueError("This test requires exactly 2 processors")

    message = np.zeros(message_length, dtype='b')
    partner = 1 - rank

    if rank == 0:
        comm.Send([message, MPI.BYTE], dest=partner)
        comm.Recv([message, MPI.BYTE], source=partner)
        start_time = time.time()
        for _ in range(repetitions):
            comm.Send([message, MPI.BYTE], dest=partner)
            comm.Recv([message, MPI.BYTE], source=partner)

        total_time = time.time() - start_time
        latency_bandwidth = total_time / (2 * repetitions)
        print(f"Latency and Bandwidth: {latency_bandwidth} seconds. Total time: {round(total_time)} seconds")
    elif rank == 1:
        comm.Recv([message, MPI.BYTE], source=partner)
        comm.Send([message, MPI.BYTE], dest=partner)
        for _ in range(repetitions):
            comm.Recv([message, MPI.BYTE], source=partner)
            comm.Send([message, MPI.BYTE], dest=partner)

if __name__ == "__main__":
    message_length = 1024  # Length of the message in bytes
    repetitions = 1000  # Number of repetitions
    ping_pong_test(message_length, repetitions)

# run code with: mpiexec -n 2 python ping_pong_test.py
