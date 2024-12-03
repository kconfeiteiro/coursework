import time
import matplotlib.pyplot as plt
import numpy as np
from mpi4py import MPI

# define function to execute the ping pong test
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
        return total_time / (2 * repetitions)
    else:
        comm.Recv([message, MPI.BYTE], source=partner)
        comm.Send([message, MPI.BYTE], dest=partner)
        for _ in range(repetitions):
            comm.Recv([message, MPI.BYTE], source=partner)
            comm.Send([message, MPI.BYTE], dest=partner)
        return None

# function for least squarese fit
def least_squares_fit(message_lengths, times):
    A = np.vstack([message_lengths, np.ones(len(message_lengths))]).T
    lambda_, mu = np.linalg.lstsq(A, times, rcond=None)[0]
    return lambda_, mu

# final function for tests and plotting
def run_tests_and_plot():
    message_lengths = [2**i for i in range(10, 21)]  # Message sizes from 1KB to 1MB
    repetitions = 1000
    times = []

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    for length in message_lengths:
        if rank == 0:
            time_per_message = ping_pong_test(length, repetitions)
            times.append(time_per_message)
        else:
            ping_pong_test(length, repetitions)

    if rank == 0:
        lambdaa, mu = least_squares_fit(message_lengths, times)
        print(f"Estimated lambdaa (start-up time): {lambdaa} seconds")
        print(f"Estimated mu (communication bandwidth): {mu} seconds/byte")
        plt_title = 'Ping-Pong Communication Time vs Message Length'

        fig, ax = plt.subplots(tight_layout=True)
        ax.plot(message_lengths, times, 'o', label='Measured times')
        ax.plot(message_lengths, lambdaa * np.array(message_lengths) + mu, 'r', label='Fitted line')
        ax.set_xlabel('Message Length (bytes)')
        ax.set_ylabel('Time (seconds)')
        ax.legend()
        ax.set_title(plt_title)
        ax.set_xscale('log')
        ax.set_yscale('log')

        fig.savefig(f"plots/p2{plt_title}.jpg")
        plt.show()

if __name__ == "__main__":
    run_tests_and_plot()

# run code with: mpiexec -n 2 python p2_ping_pong_test.py
