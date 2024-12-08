import numpy as np
from utils.orbital_mechanics import rk4_method, calculate_orbital_elements

def initialize_population(pop_size):
    # Generate initial population of random orbital parameters
    population = []
    for _ in range(pop_size):
        semi_major_axis = np.random.uniform(7000, 8000)  # Example range in km
        eccentricity = np.random.uniform(0, 0.1)
        inclination = np.random.uniform(0, np.pi)
        omega = np.random.uniform(0, 2 * np.pi)
        argument_of_periapsis = np.random.uniform(0, 2 * np.pi)
        mean_anomaly = np.random.uniform(0, 2 * np.pi)
        population.append([semi_major_axis, eccentricity, inclination, omega, argument_of_periapsis, mean_anomaly])
    return population

def evaluate_fitness(population, target_trajectory):
    # Calculate fitness for each solution based on how close the propagated orbit is to the target trajectory
    fitness_scores = []
    for individual in population:
        initial_state = calculate_orbital_elements(*individual)
        propagated_state = rk4_method(initial_state, time=3600)  # Example propagation time
        fitness = -np.linalg.norm(propagated_state - target_trajectory.reshape(2, 3))  # Negative distance to target
        fitness_scores.append(fitness)
    return fitness_scores

def tournament_selection(population, fitness_scores):
    # Implement a simple tournament selection
    selected = []
    for _ in range(len(population)):
        i, j = np.random.randint(0, len(population), 2)
        selected.append(population[i] if fitness_scores[i] > fitness_scores[j] else population[j])
    return selected

def evolve_population(population, fitness_scores):
    # Combine selection and mutation
    selected = tournament_selection(population, fitness_scores)
    next_generation = []
    for individual in selected:
        mutated = individual + np.random.normal(0, 0.1, len(individual))
        next_generation.append(mutated)
    return next_generation
