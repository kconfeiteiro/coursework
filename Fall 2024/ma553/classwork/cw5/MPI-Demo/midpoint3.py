#!/usr/bin/env python 
from mpi4py import MPI
from math import pi, sqrt, exp, erf 

"""
To implement the midpoint rule for numerical integration   
"""

def f(x):
    y = exp(-x**2)
    return y 

def g(x):
    y = 0.5*sqrt(pi)*erf(x) 
    return y 

def mid_sum(f,a,b,n):
    dx=(b-a)/n
    msum=0.0
    for i in range(n): 
        xibar = a+(0.5+i)*dx
        msum += f(xibar) 
    return dx*msum 

###########################################
if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    a=0.0
    b=1.0
    part=(b-a)/size 

    a_new = a+rank*part  
    b_new = a_new+part  
    n=4

    y = mid_sum(f,a_new,b_new,n)
    y_tot = comm.reduce(y, op=MPI.SUM, root=0)

    print('rank: {0:}; y= {1:}, y_total={2:}'.format(rank, y, y_tot))
    
    if rank == 0: 
       abs_err=abs(y_tot-g(1))
       print('approx integral={0:}, abs_error={1:}'.format(y_tot,abs_err))
