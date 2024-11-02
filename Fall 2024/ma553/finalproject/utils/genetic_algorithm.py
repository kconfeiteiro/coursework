import numpy as np

def initialize_population(pop_size):
    # Generate initial population of random solutions
    return [np.random.rand(10) for _ in range(pop_size)]

def evaluate_fitness(population):
    # Calculate fitness for each solution
    return [np.sum(individual) for individual in population]

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
    return [individual + np.random.normal(0, 0.1, len(individual)) for individual in selected]
