#!/usr/bin/env python
#
# heat2d_numexpr.py - Simulates two-dimensional heat equation on a square domain
#                     This one uses numexpr for faster computations.
#
import time
import numexpr as ne
import numpy as np

from heat2dparams import D, Nx, Ny, plot, tmax, tout, xmax, xmin, ymax, ymin
from heat2dplot import plotsol


def initialize(u, x, y):
    """Apply the initial condition u(x,y,0)=u0(x,y)"""
    nx = len(x)
    ny = len(y)
    for i in range(1, nx - 1):
        ui = 1 - abs(1 - 4 * abs((x[i] - (x[0] + x[-1]) / 2) / (x[-1] - x[0])))
        for j in range(1, ny - 1):
            uj = 1 - abs(1 - 4 * abs((y[j] - (y[0] + y[-1]) / 2) / (y[-1] - y[0])))
            u[i, j] = ui * uj

def evolve(u_new, u, dt, dx2, dy2):
    """Update PDE by advancing one time step with size dt."""
    laplacian = ne.evaluate(
        "(u_ip1j - 2 * u_ij + u_im1j) / dx2 + (u_ijp1 - 2 * u_ij + u_ijm1) / dy2",
        local_dict={
            'u_ip1j': u[2:, 1:-1], 'u_ij': u[1:-1, 1:-1], 'u_im1j': u[:-2, 1:-1],
            'u_ijp1': u[1:-1, 2:], 'u_ijm1': u[1:-1, :-2], 'dx2': dx2, 'dy2': dy2
        }
    )
    u_new[1:-1, 1:-1] = ne.evaluate("u + D * dt * laplacian", local_dict={'u': u[1:-1, 1:-1], 'D': D, 'dt': dt, 'laplacian': laplacian})

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
