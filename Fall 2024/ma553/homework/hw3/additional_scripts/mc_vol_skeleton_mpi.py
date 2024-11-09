#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 13:02:27 2022

@author: Khanal
"""
import mpi4py
mpi4py.rc.initialize=False
mpi4py.rc.finalize=False
from mpi4py import MPI

import random 
import math


def mc_volume(n):
    """ Approximates volume of the solid 
    below x^2+y^2+(z-1)^2=1 and above z^2=x^2+y^2 
    using Monte Carlo integration with n random points."""
    count=0
    for i in range(n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        z=random.uniform(0,2)
        if x**2+y**2 < z**2 and x**2+y**2 < z*(2-z): 
           count += 1
    #return 8*count/n 
    return count # return just the number of hits  

if __name__=='__main__':
    n=100000

    # Start MPI parallelization 
    MPI.Init()

    # MPI globals
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Let each process work independently with n points
    local_count = mc_volume(n) 

    ## if rank>0, send local_count to the master (rank=0) 
    ## if rank=0, receive local_count from all processes 
    ##            calculate vol = 8*total_count/(size*n)
    ##            print the result

    if rank > 0:
       ## TO DO: comm.send() 
       print( 'local_count sent from rank',rank)
    else:
       total_count=local_count
       for i in range(1,size):
           ## TO DO: total_count += comm.recv() 
           print( 'local_count received from rank',rank)
       approx_vol=8*total_count/(n*size) 
       print( 'with {}x{}={} points:'.format(size,n,n*size))
       print( 'Vol of the "Ice-Cream Cone"=',approx_vol)
       print( 'Approx error=',abs(approx_vol-math.pi))

    MPI.Finalize()

