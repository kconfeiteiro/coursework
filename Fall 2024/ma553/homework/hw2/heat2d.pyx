#!/usr/bin/env python
#
# heat2d.pyx - Simulates two-dimensional heat equation on a square domain
#              This one is optimized using Cython.
#
# cython: language_level=3
import time
cimport cython
from libc.math cimport abs
import numpy as np

from heat2dparams import D, Nx, Ny, plot, tmax, tout, xmax, xmin, ymax, ymin
from heat2dplot import plotsol

cdef void initialize(double[:, :] u, double[:] x, double[:] y):
    """Apply the initial condition u(x,y,0)=u0(x,y)"""
    cdef int nx=x.shape[0]
    cdef int ny=y.shape[0]
    cdef int i, j
    cdef double ui, uj
    for i in range(1, nx - 1):
        ui=1 - abs(1 - 4 * abs((x[i] - (x[0] + x[-1]) / 2) / (x[-1] - x[0])))
        for j in range(1, ny - 1):
            uj=1 - abs(1 - 4 * abs((y[j] - (y[0] + y[-1]) / 2) / (y[-1] - y[0])))
            u[i, j]=ui * uj

cdef void evolve(double[:, :] u_new, double[:, :] u, double dt, double dx2, double dy2):
    """Update PDE by advancing one time step with size dt."""
    cdef int nx=u.shape[0]
    cdef int ny=u.shape[1]
    cdef int i, j
    cdef double laplacian
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            laplacian=(u[i + 1, j] - 2 * u[i, j] + u[i - 1, j]) / dx2 + (
                u[i, j + 1] - 2 * u[i, j] + u[i, j - 1]
            ) / dy2
            u_new[i, j]=u[i, j] + D * dt * laplacian

cdef void iterate(double[:, :] u_new, double[:, :] u, double dt, double dx2, double dy2, int nsteps, int plot_interval):
    """Run fixed number of time steps of heat equation"""
    cdef double simtime=0.0
    cdef int s
    print(' at t={0:5.2f}'.format(simtime))
    if plot:
        plotsol(u, xmin, xmax, ymin, ymax, first=True)
    for s in range(nsteps + 1):
        evolve(u_new, u, dt, dx2, dy2)  # Advance one step in time

        # Swap array pointers so t+1 becomes the new t, and update simulation time.
        u, u_new = u_new, u
        simtime += dt
        # Plot and report time.
        if (s + 1) % plot_interval == 0:
            print(' at t={0:5.2f}'.format(simtime))
            if plot:
                plotsol(u, xmin, xmax, ymin, ymax)

# the driver routine
def main():
    # Parameters set in heat2dparams.py:
    cdef double dx=(xmax - xmin) / Nx
    cdef double dy=(ymax - ymin) / Ny
    cdef double dx2=dx**2
    cdef double dy2=dy**2
    cdef double dt=(dx2 * dy2) / (2 * D * (dx2 + dy2))  # time step size (edge of stability)
    cdef int nsteps=int(tmax / dt)  # number of steps of that size to reach tmax
    cdef int plot_interval=int(tout / dt)  # how many steps between snapshots
    if plot_interval == 0:
        plot_interval=1

    # Allocate arrays x, y, u, u_new
    cdef double[:] x = np.linspace(xmin, xmin + Nx * dx, Nx + 1, dtype=np.float64)
    cdef double[:] y = np.linspace(ymin, ymin + Ny * dy, Ny + 1, dtype=np.float64)

    # Create 2D arrays for u and u_new directly using np.zeros
    cdef double[:, :] u = np.zeros((Nx + 1, Ny + 1), dtype=np.float64)
    cdef double[:, :] u_new = np.zeros((Nx + 1, Ny + 1), dtype=np.float64)

    # Initialize and output/plot initial profile.
    initialize(u, x, y)
    print("\nHeat equation solver")
    print("Parameters")

    print("----------")
    print("D={}, xmin={}, xmax={}, ymin={}, ymax={}".format(D, xmin, xmax, ymin, ymax))
    print("dx={}, dy={}, dt={}".format(dx, dy, dt))
    print("\nTotal time steps={}, plot interval={}\n".format(nsteps, plot_interval))

    # Iterate and plot solution
    cdef double t0=time.time()
    iterate(u_new, u, dt, dx2, dy2, nsteps, plot_interval)
    cdef double t1=time.time()

    print('\tAt t={0:5.2f}'.format(tmax))
    print("\nSimulation finished in {0} s".format(t1 - t0))

