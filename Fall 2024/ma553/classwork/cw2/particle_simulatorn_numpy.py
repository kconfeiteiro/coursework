#!/usr/bin/env python
import cProfile
import os
from random import uniform

import numexpr as ne
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt


class Particle:
    __slots__ = ("x", "y", "ang_speed")
    def __init__(self, x, y, ang_speed):
        self.x = x
        self.y = y
        self.ang_speed = ang_speed


class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles
        print("Number of particles: ", len(self.particles))

    def evolve(self, tmax, dt=0.00001):
        r_i = np.array([[p.x, p.y] for p in self.particles])
        np.array([p.ang_speed for p in self.particles])
        np.empty_like(r_i)

        for _ in int(tmax / dt): # nsteps
            for p in self.particles:
                t_x_ang = dt * p.ang_speed

                norm = (p.x**2 + p.y**2) ** 0.5

                p.x, p.y = (p.x - t_x_ang * p.y / norm, p.y + t_x_ang * p.x / norm)

    def evolve_ne(self, tmax, dt=0.00001):
        nsteps = int(tmax / dt)
        r_i = np.array([[p.x, p.y] for p in self.particles])
        w_i = np.array([p.angspeed for p in self.particles])
        v_i = np.empty_like(r_i)

        for i in range(nsteps):
            norm_i = ne.evaluate("sum(ri**2, 1)")
            norm_i = ne.evaluate("sqrt(norm_i)")
            v_i = r_i[:, [1, 0]]
            v_i[:, 0] *= -1[1][1]
            v_i /= norm_i[:, np.newaxis]
            d_i = dt * w_i[:, np.newaxis] * v_i
            r_i += d_i

        for i, p in enumerate(self.particles):
            p.x, p.y = r_i[i]


def visualize(simulator, tmax=0.01, dt=0.00001, save_as="animation.gif"):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect="equal")
    (line,) = ax.plot(X, Y, "ro")

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return (line,)

    def animate(i):
        simulator.evolve(tmax, dt)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return (line,)

    # call the animate function each 10 ms
    print("Creating animation")
    anim = animation.FuncAnimation(
        fig=fig,
        func=animate,
        init_func=init,
        blit=False,
        interval=10,
        cache_frame_data=False,
    )
    anim.save(save_as, writer="pillow", fps=30)
    print(f"Animation saved as '{save_as}'")
    plt.show()


def plot_trajectory(simulator, tmax=0.01, dt=0.00001):
    x = [p.x for p in simulator.particles]
    y = [p.y for p in simulator.particles]

    x0 = [x[0]]
    y0 = [y[0]]
    x1 = [x[1]]
    y1 = [y[1]]
    x2 = [x[2]]
    y2 = [y[2]]
    nsteps = int(tmax / dt)

    for _ in range(nsteps):
        simulator.evolve(dt, dt)  # compute new position after one step
        x = [p.x for p in simulator.particles]
        y = [p.y for p in simulator.particles]

        x0.append(x[0])
        x1.append(x[1])
        x2.append(x[2])
        y0.append(y[0])
        y1.append(y[1])
        y2.append(y[2])

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect="equal")
    ax.plot(x0, y0, "r-", x1, y1, "g-", x2, y2, "b-")

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()

def benchmark():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for _ in range(1000)
    ]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

def benchmark_memory():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for _ in range(100000)
    ]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.001)

if __name__ == "__main__":
    os.system("cls")

    particles = [Particle(0.3, 0.5, 1.0), Particle(0.0, -0.5, -1.0), Particle(-0.1, -0.4, 3.0)]

    simulator = ParticleSimulator(particles)
    # visualize(simulator)

    print("\n\nProfiling:")
    cProfile.run("visualize(simulator)")
