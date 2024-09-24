#!/usr/bin/env python

from matplotlib import pyplot as plt
from matplotlib import animation
from random import uniform
import numpy as np
import numexpr as ne
import time
import timeit


class Particle:
    __slots__ = ("x", "y", "ang_speed")
    def __init__(self, x, y, ang_speed):
        self.x = x
        self.y = y
        self.ang_speed = ang_speed


class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles

    #@profile
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



def visualize(simulator, tmax=0.01, dt=0.00001):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect="equal")
    line, = ax.plot(X, Y, "ro")

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
    anim.save("Animation.gif", writer="imagemagick", fps=30)
    plt.show()


def plot_trajectory(simulator,tmax=0.01, dt=0.00001):
    x=[p.x for p in simulator.particles]
    y=[p.y for p in simulator.particles]
    x0=[x[0]]; y0=[y[0]]
    x1=[x[1]]; y1=[y[1]]
    x2=[x[2]]; y2=[y[2]]
    nsteps=int(tmax/dt)
    for i in range(nsteps):
        simulator.evolve(dt,dt) # compute new position after one step
        x=[p.x for p in simulator.particles]
        y=[p.y for p in simulator.particles]
        x0.append(x[0]);x1.append(x[1]);x2.append(x[2])
        y0.append(y[0]);y1.append(y[1]);y2.append(y[2])
    fig=plt.figure()
    ax = fig.add_subplot(111, aspect="equal")
    ax.plot(x0,y0,"r-",x1,y1,"g-",x2,y2,"b-")
    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()

def benchmark():
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                  for i in range(1000)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

def benchmark_memory():
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                  for i in range(100000)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.001)

if __name__ == "__main__":
    dt=0.00001
    tmax=1
    particles = [Particle( 0.3, 0.5, +1),
                 Particle( 0.0, -0.5, -1),
                 Particle(-0.1, -0.4, +3)]
    simulator = ParticleSimulator(particles)
    plot_trajectory(simulator,tmax,dt)
    visualize(simulator)
    benchmark()

    benchmark_memory()
