from line_profiler import profile
import numpy as np
from mpi4py import MPI
from utils.genetic_algorithm import initialize_population, evaluate_fitness, evolve_population
from utils.metrics import time_function

# TODO - get mpi to run using custom command

# @profile
@time_function()
def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Genetic Algorithm parameters
    pop_size, generations = 100, 50

    # Target trajectory (example)
    target_trajectory = np.array([7000, 0, 0, 0, 7.5, 0])

    # Initialize population
    population = initialize_population(pop_size)

    for generation in range(generations):
        # Evaluate fitness
        fitness_scores = evaluate_fitness(population, target_trajectory)

        # Evolve population
        population = evolve_population(population, fitness_scores)

        if rank == 0:
            print(f"Generation {generation}: Best fitness = {max(fitness_scores)}")

    # Select the best solution
    best_solution = population[np.argmax(fitness_scores)]

    if rank == 0:
        print("\nBest Solution:", best_solution)

if __name__ == "__main__":
    main()
