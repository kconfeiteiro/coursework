import os
from multiprocessing import Process


def squared(x):
    print(' {0}x{0} = {1} computed from PID {2}'.format(x, x * x, os.getpid()))

# create a list of parallel processes
procs = [Process(target=squared, args=[x]) for x in range(1, 11)]

# start all processes
for p in procs:
    p.start()


# wait for all tasks to finish
for p in procs:
    p.join()
