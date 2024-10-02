#!/usr/bin/env python

from cevolve import c_evolve # type: ignore
import time
import timeit
import numpy as np
from random import uniform
from matplotlib import pyplot as plt
from matplotlib import animation


class Particle:

    __slots__ = ('x', 'y', 'ang_speed')

    def __init__(self, x, y, ang_speed):
        self.x = x
        self.y = y
        self.ang_speed = ang_speed


class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles

    #################################################################
    # Original Python function
    def evolve(self, tmax, dt=0.00001):
        nsteps = int(tmax/dt)
        for i in range(nsteps):
            for p in self.particles:
                norm = (p.x**2 + p.y**2)**0.5
                v_x = (-p.y)/norm
                v_y = p.x/norm
                d_x = dt * p.ang_speed * v_x
                d_y = dt * p.ang_speed * v_y
                p.x += d_x
                p.y += d_y
    #################################################################
    # Modified by changing the loop order
    def evolve_python(self, tmax, dt=0.00001):
        nsteps = int(tmax/dt)
        for p in self.particles:
            dt_x_ang = dt * p.ang_speed
            for i in range(nsteps):
                norm = (p.x**2 + p.y**2)**0.5
                p.x = p.x - dt_x_ang * p.y/norm
                p.y = p.y + dt_x_ang * p.x/norm
    #################################################################
    # Modified using NumPy
    def evolve_numpy(self, tmax, dt=0.00001):
        nsteps = int(tmax/dt)

        r_i = np.array([[p.x, p.y] for p in self.particles])
        ang_speed_i = np.array([p.ang_speed for p in self.particles])
        v_i = np.empty_like(r_i)

        for i in range(nsteps):
            norm_i = np.sqrt((r_i ** 2).sum(axis=1))

            v_i = r_i[:, [1, 0]]
            v_i[:, 0] *= -1
            v_i /= norm_i[:, np.newaxis]

            d_i = dt * ang_speed_i[:, np.newaxis] * v_i

            r_i += d_i

        for i, p in enumerate(self.particles):
            p.x, p.y = r_i[i]
    #################################################################
    # Modified using Cython, c_evolve() is in cevolve.pyx
    def evolve_cython(self, tmax, dt=0.00001):
        nsteps = int(tmax/dt)

        r_i = np.array([[p.x, p.y] for p in self.particles])
        ang_speed_i = np.array([p.ang_speed for p in self.particles])

        c_evolve(r_i, ang_speed_i, dt, nsteps)

        for i, p in enumerate(self.particles):
            p.x, p.y = r_i[i]
    #################################################################

def visualize(simulator, tmax=0.01, dt=0.00001):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will be run when the animation starts
    def init():
        line.set_data([], [])
        return line, # The comma is important!

    def animate(i):
        simulator.evolve(tmax, dt)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return line,

    # Call the animate function each 10 ms
    anim=animation.FuncAnimation(fig,
                                 animate,
                                 init_func=init,
                                 blit=True,
                                 interval=10)
    anim.save('Animation.gif', writer='imagemagick', fps=30)
    plt.show()

def plot_trajectory(simulator,tmax=0.01, dt=0.00001):
    x=[p.x for p in simulator.particles]
    y=[p.y for p in simulator.particles]
    x0=[x[0]]; y0=[y[0]]
    x1=[x[1]]; y1=[y[1]]
    x2=[x[2]]; y2=[y[2]]
    nsteps=int(tmax/dt)
    for i in range(nsteps):
        #simulator.evolve(dt,dt) # compute new position after one step
        #simulator.evolve_python(dt,dt)
        #simulator.evolve_numpy(dt,dt)
        simulator.evolve_cython(dt,dt)
        x=[p.x for p in simulator.particles]
        y=[p.y for p in simulator.particles]
        x0.append(x[0]);x1.append(x[1]);x2.append(x[2])
        y0.append(y[0]);y1.append(y[1]);y2.append(y[2])
    fig=plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.plot(x0,y0,'r-',x1,y1,'g-',x2,y2,'b-')
    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()

def benchmark(n=100, method='python'):
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                  for i in range(n)]
    simulator = ParticleSimulator(particles)
    if method == 'python':
       simulator.evolve_python(0.1)
    if method == 'numpy':
       simulator.evolve_numpy(0.1)
    if method == 'cython':
       simulator.evolve_cython(0.1)

def benchmark_memory(n=1000, method='python'):
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                  for i in range(100000)]
    simulator = ParticleSimulator(particles)
    if method == 'python':
       simulator.evolve_python(0.001)
    if method == 'numpy':
       simulator.evolve_numpy(0.001)
    if method == 'cython':
       simulator.evolve_cython(0.001)

###########################################################################
if __name__ == '__main__':
    dt=0.00001
    tmax=1.0
    particles = [Particle( 0.3, 0.5, 1.0),
                 Particle( 0.0, -0.5, 1.0),
                 Particle(-0.1, -0.4, 3.0)]
    simulator = ParticleSimulator(particles)
    plot_trajectory(simulator,tmax,dt)
    #visualize(simulator)
    #benchmark(100, 'python')
    #benchmark(100, 'numpy')
    benchmark(100, 'cython')
    #benchmark_memory(1000, 'python')
    #benchmark_memory(1000, 'numpy')
    #benchmark_memory(1000, 'cython')


