#!/usr/bin/env python
#
# heat2d_np.py - Simulates two-dimensional heat equation on a square domain
#                This version uses numpy for array operations.
#
import time
import numpy as np
from heat2dparams import D, Nx, Ny, plot, tmax, tout, xmax, xmin, ymax, ymin
from heat2dplot import plotsol

def initialize(u, x, y):
    """Apply the initial condition u(x,y,0)=u0(x,y)"""
    X, Y = np.meshgrid(x, y, indexing='ij')
    u[:, :] = (1 - np.abs(1 - 4 * np.abs((X - (x[0] + x[-1]) / 2) / (x[-1] - x[0])))) * \
              (1 - np.abs(1 - 4 * np.abs((Y - (y[0] + y[-1]) / 2) / (y[-1] - y[0]))))

def evolve(u_new, u, dt, dx2, dy2):
    """Update PDE by advancing one time step with size dt."""
    laplacian = (np.roll(u, 1, axis=0) - 2 * u + np.roll(u, -1, axis=0)) / dx2 + \
                (np.roll(u, 1, axis=1) - 2 * u + np.roll(u, -1, axis=1)) / dy2
    u_new[:, :] = u + D * dt * laplacian

def iterate(u_new, u, dt, dx2, dy2, nsteps, plot_interval):
    """Run fixed number of time steps of heat equation"""
    simtime = 0 * dt
    print(' at t = {0:5.2f}'.format(simtime))
    if plot:
        plotsol(u, xmin, xmax, ymin, ymax, first=True)
    for s in range(nsteps + 1):
        evolve(u_new, u, dt, dx2, dy2)  # Advance one step in time
        # Swap array pointers so t+1 becomes the new t, and update simulation time.
        u, u_new = u_new, u
        simtime += dt
        # Plot and report time.
        if (s + 1) % plot_interval == 0:
            print(' at t = {0:5.2f}'.format(simtime))
            if plot:
                plotsol(u, xmin, xmax, ymin, ymax)

# the driver routine
def main():
    # Parameters set in heat2dparams.py:
    dx = (xmax - xmin) / Nx
    dy = (ymax - ymin) / Ny
    dx2 = dx**2
    dy2 = dy**2
    dt = (dx2 * dy2) / (2 * D * (dx2 + dy2))  # time step size (edge of stability)
    nsteps = int(tmax / dt)  # number of steps of that size to reach tmax
    plot_interval = int(tout / dt)  # how many steps between snapshots
    if plot_interval == 0:
        plot_interval = 1

    # Allocate arrays x, y, u, u_new.
    x = np.linspace(xmin, xmax, Nx + 1)  # x values
    y = np.linspace(ymin, ymax, Ny + 1)  # y values
    u = np.zeros((Nx + 1, Ny + 1))  # time step t
    u_new = np.zeros((Nx + 1, Ny + 1))  # time step t+1

    # Initialize and output/plot initial profile.
    initialize(u, x, y)
    print("\nHeat equation solver")
    print("Parameters")
    print("----------")
    print("  D={}, xmin={}, xmax={}, ymin={}, ymax={}".format(D, xmin, xmax, ymin, ymax))
    print("  dx={}, dy={}, dt={}".format(dx, dy, dt))
    print("  total time steps={}, plot interval={}\n".format(nsteps, plot_interval))

    # Iterate and plot solution
    t0 = time.time()
    iterate(u_new, u, dt, dx2, dy2, nsteps, plot_interval)
    t1 = time.time()

    print('\tat t = {0:5.2f}'.format(tmax))
    print("\nSimulation finished in {0} s".format(t1 - t0))

if __name__ == '__main__':
    main()
