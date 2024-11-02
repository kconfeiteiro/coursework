from multiprocessing import Process
import os
import time

def hello(n):
    time.sleep(1)
    print('Hello World, from process {0} with PID {1}'.format(n,os.getpid()))
    #print('My Parent\'s PID is {0}'.format(os.getppid()))

#N=int(input('Enter the no. of processors to be spawned:'))
N=10

# Create parallel processes
procs = [Process(target=hello, args=[n]) for n in range(N)]

# Start the process
for p in procs:
    p.start()
print('Spawned a new process from PID {0}'.format(os.getpid()))

# End the process
for p in procs:
    p.join()

