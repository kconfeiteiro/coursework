#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 13:02:27 2022

@author: Khanal
"""
"""
======================================================
 To solve one dimensial advection diffusion equation
     u_t + au_x = u_xx for  0<=t<=T
 with the initial and boundary conditions:
     u(x,0)= f(x)
 using an explicit finite difference method:
 central difference (diffusion) + upwind (advection)
======================================================
"""
import mpi4py
mpi4py.rc.initialize=False
mpi4py.rc.finalize=False
from mpi4py import MPI

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def u_init(x):
    if x >= 1 and x <= 2:
       return 5
    else:
       return 0

def update_pde_expl(u1, dx, dt):
    N=len(u1) - 2
    u2=np.zeros(N + 2)

    for i in range(1, N + 1):
        adv=a*(u1[i] - u1[i + 1]) / dx
        diff=D*(u1[i - 1] - 2 * u1[i] + u1[i + 1]) / (dx * dx)
        u2[i] = u1[i] + dt * (adv + diff)
    return u2

def exchange_boundary(u):
    if rank != 0:
       # Send u[1] to the left, and receive (u[-2] from left) to u[0]
       comm.send(u[1], dest=left)
       ## TO DO: u[0]=comm.recv(source=left)
    if rank != size-1:
       # Send u[-2] to the right, and receive (u[1] from right) to u[-1]
       ## TO DO: comm.send()
       u[-1]=comm.recv(source=right)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
if __name__=='__main__':
###############################################################################
    L=25 # Length
    tmax=10 # End time
    N=1000  # Number of points in  x
    M=5000  # Number of points in  t
    out_num=25 # Number of times to save results for plotting
    a=2.0
    D=1.0/16

    # Start MPI parallelization
    MPI.Init()

    # MPI globals
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank==0:
       x,dx = np.linspace(0,L,N+2,retstep=True,dtype=float) # 1D array in x
       dt = tmax/M  # Temporal step-size
       u = np.zeros(N+2, dtype=float) # u array
       for i in range(0,N+2): # Initial conditions For loop
           u[i] = u_init(x[i])
       uu = u[1:-1]  # copy of u at internal nodes to scatter/gather
       # Broatcast the shape, dtype of the array uu
       shape=uu.shape
       dtype=uu.dtype
       comm.bcast(shape,0)  # broadcast shape of uu
       comm.bcast(dtype,0)  # broadcast dtype of uu
       comm.bcast(dx,0)     # broadcast dx
       comm.bcast(dt,0)     # broadcast dt
    else:
       uu=None
       shape=comm.bcast(None,0)
       dtype=comm.bcast(None,0)
       dx=comm.bcast(None,0)
       dt=comm.bcast(None,0)

    comm.Barrier()

    # Left/Right neighbouring MPI ranks
    left = rank - 1
    if left < 0:
       left = MPI.PROC_NULL
    right = rank + 1
    if right > size - 1:
       right = MPI.PROC_NULL

    assert shape[0]==N

    Np = N//size
    if N%size:
        raise ValueError('Number of interval (' \
                + str(N) + ') needs to be divisible by the number ' \
                + 'of MPI tasks (' + str(size) + ').')

    # Distribute data to all processes within the communicator
    u_loc = np.zeros(Np+2,dtype)    # need two ghost nodes!
    rbuff = np.zeros(Np,dtype)
    ## TO DO: Scatter the data uu to all processes equally (length=Np)
    #  comm.Scatter(uu , , )
    u_loc[1:-1] = rbuff             # copy data to non-ghost nodes

    tm=0
    if rank==0:
       t=np.linspace(0,tmax,out_num) # t array to save output
       u_sol=np.zeros((out_num,N+2)) # Matrix where desired values are stored
       for i in range(0,N+2): # Save initial values into matrix
           u_sol[0,i]=u[i]

    P=M//out_num
    diff=P-1

    for m in range(1,M): # begin time stepping loop
        tm +=dt
        exchange_boundary(u_loc)
        u_loc=update_pde_expl(u_loc,dx,dt)
        if m%P==0 or m==M-1:
           ## TO DO: Gather results from all processes to form complete uu array
           # comm.Gather(u_loc[1:-1], , )
           if rank==0:
               for i in range(1,N):
                   u_sol[m-diff,i]=uu[i]
           diff = diff+P-1
    # End time stepping loop

    if rank==0:
       # Plot 1: u(x,t) plotted against x at various times
       f1=plt.figure()
       for m in range(0,len(u_sol[:,0])):
           if m==0:
               plt.plot(x[:],u_sol[m,:],'k-')
               plt.legend(['0s'],loc='best')
               plt.xlabel(r'$x$')
               plt.ylabel(r'$u(x,t)$')
               plt.title(r'Numerical Solution to $u_t+au_x=Du_{xx}$')
               plt.grid()
           else:
               plt.plot(x[:],u_sol[m,:],'-')
       f1.savefig('fig1.png', bbox_inches='tight')
       plt.show()

       x_mat, t_mat = np.meshgrid ( x, t ) # create a grid of x and t for plotting

       # Plot 2: surface plot of the solution u(x,t), saved at the specific time
       f2 = plt.figure ( )
       ax = f2.add_subplot ( 111, projection = '3d' )
       surf=ax.plot_surface ( x_mat, t_mat, u_sol, cmap=cm.coolwarm, linewidth=0, antialiased=False )
       plt.tight_layout()
       plt.xlabel ( r'<--- $x$ --->' )
       plt.ylabel ( r'<--- $t$ --->' )
       plt.title ( r'Numerical Solution to $u_t+au_x=Du_{xx}$' )
       f2.colorbar(surf, shrink=0.5, aspect=5) # add a color bar
       f2.savefig ( 'fig2.png' )
       plt.show ( )

    MPI.Finalize()
