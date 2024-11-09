#!/usr/bin/env python3
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
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mpi4py import MPI

def u_init(x):
    u0 = 5 * np.logical_and(x >= 1, x <= 2)
    return u0

def update_pde_expl(u1, dx, dt, rank, size):
    N = len(u1) - 1
    u2 = np.zeros(N + 1)

    # boundary conditions u(0, t) = u(L, t) = 0
    if rank == 0:
        u2[0] = 0.0
    if rank == size - 1:
        u2[N] = 0.0

    # Exchange boundary values with neighbors
    comm = MPI.COMM_WORLD
    if rank > 0:
        comm.send(u1[1], dest=rank-1)
        left_neighbor = comm.recv(source=rank-1)
    else:
        left_neighbor = 0.0

    if rank < size - 1:
        comm.send(u1[N - 1], dest=rank+1)
        right_neighbor = comm.recv(source=rank+1)
    else:
        right_neighbor = 0.0

    for i in range(1, N):
        if i == 1 and rank > 0:
            adv = a * (left_neighbor - u1[i]) / dx
            diff = D * (left_neighbor - 2 * u1[i] + u1[i + 1]) / (dx * dx)
        elif i == N-1 and rank < size - 1:
            adv = a * (u1[i] - right_neighbor) / dx
            diff = D * (u1[i - 1] - 2 * u1[i] + right_neighbor) / (dx * dx)
        else:
            adv = a * (u1[i] - u1[i + 1]) / dx
            diff = D * (u1[i - 1] - 2 * u1[i] + u1[i + 1]) / (dx * dx)
        u2[i] = u1[i] + dt * (adv + diff)

    return u2


if __name__=='__main__':
    N = 1000  # Number of points in  x
    out_num = 25 # Number of times to save results for plotting

    L = 25 # Length
    tmax = 10 # End time

    a = 2
    D = 1 / 16

    dx = L / (N + 1) # Spatial step-size
    x = np.linspace(0, L, N + 2) # 1D array in x

    dt_stable = dx / 5 #0.5*dx**2/(a*dx+2*D)
    tstep = int(tmax / dt_stable)
    M = tstep + out_num - tstep % out_num
    dt=tmax / M  # Temporal step-size

    u=np.zeros(N + 2) # u array
    u=u_init(x) # Initial condition
    t=np.linspace(0, tmax,out_num) # t array to save output
    sol_u=np.zeros((out_num, N + 2)) # Matrix where desired values are stored

    for i in range(0, N + 2): # Save initial values into matrix
        sol_u[0,i] = u[i]

    P=M // out_num
    diff = P - 1

    tm = 0
    for m in range(1,M): # begin time stepping loop
        tm +=dt
        u = update_pde_expl(u, dx, dt)
        if m % P==0 or m == M - 1:
            for i in range(0, N + 2):
                sol_u[m-diff,i] = u[i]
            diff = diff+P-1
    # end time stepping loop

    # Plot 1: u(x,t) plotted against x at various times
    f1=plt.figure()
    for m in range(0,len(sol_u[:,0])):
        if m==0:
            plt.plot(x[:], sol_u[m,:], 'k-')
            plt.legend(['0s'], loc='best')
            plt.xlabel(r'$x$')
            plt.ylabel(r'$u(x,t)$')
            plt.title(r'Numerical Solution to $u_t+au_x=Du_{xx}$')
            plt.grid()
        else:
            plt.plot(x[:], sol_u[m,:], '-')
            
    f1.savefig('fig1.png', bbox_inches='tight')
    plt.show()

    x_mat, t_mat = np.meshgrid(x, t) # create a grid of x and t for plotting

    # Plot 2: surface plot of the solution u(x,t), saved at the specific time
    f2 = plt.figure()
    ax = f2.add_subplot(111, projection='3d')
    surf=ax.plot_surface( x_mat, t_mat, sol_u, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.tight_layout()
    plt.xlabel(r'<--- $x$ --->')
    plt.ylabel(r'<--- $t$ --->')
    plt.title(r'Numerical Solution to $u_t+au_x=Du_{xx}$')
    f2.colorbar(surf, shrink=0.5, aspect=5)
    f2.savefig('fig2.png')
    plt.show()
