#!/usr/bin/env python 
from mpi4py import MPI
from math import pi, sqrt, exp, erf 
import numpy as np

"""
To implement the midpoint rule for numerical integration   
"""


def f(x):
    y = np.exp(-x**2)
    return y 

def g(x):
    y = 0.5*sqrt(pi)*erf(x) 
    return y 

def trapezoid_rule(f,a,b,n):
    x,dx=np.linspace(a,b,n+1,retstep=True)
    y=f(x)
    tsum=np.sum(y[1:-1])
    return dx*(tsum+0.5*(y[0]+y[-1]))

###########################################
if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    a=0.0
    b=1.0
    part=(b-a)/size 

    # Divide the interval to all the workers 
    a_new = a+rank*part  
    b_new = a_new+part  
    n=10

    y = trapezoid_rule( , , , )
    # y_tot = comm.reduce( , , ) # reduce the result to the total sum of sums

    print('rank: {0:}; y= {1:}, y_total={2:}'.format(rank, y, y_tot))
    
    if rank == 0: 
       abs_err=abs(y_tot-g(1))
       print('approx integral={0:}, abs_error={1:}'.format(y_tot,abs_err))
