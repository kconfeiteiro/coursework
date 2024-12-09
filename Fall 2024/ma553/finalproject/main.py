import matplotlib.pyplot as plt
import numpy as np
from mpi4py import MPI
from utils.genetic_algorithm import initialize_population, evaluate_fitness_ne, evolve_population
from utils.metrics import time_function
import time
from utils.metrics import calculate_rmse, calculate_mae, calculate_mse, calculate_r2

# TODO - get mpi to run using custom command

@time_function()
def main():
    start_time = time.time()

    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Genetic Algorithm parameters
    pop_size, generations = 100, 50

    # Target trajectory
    target_trajectory = np.array([[7100, 0.18, 0.09, 0.028, 7.7, 0.018]])

    # Initialize population
    population = initialize_population(pop_size)

    # evaluate fitness and evolve population
    for generation in range(generations):
        fitness_scores = evaluate_fitness_ne(population, target_trajectory)
        population = evolve_population(population, fitness_scores)
        if rank == 0 and generation % 5 == 0:
            print(f"Generation {generation}: Best fitness (ne) = {max(fitness_scores)}")

    # Collect orbital parameters
    best_individual = population[np.argmax(fitness_scores)]
    print("Best solution (ne): ", best_individual)

    # Plot the orbital parameters
    if rank == 0:
        gens = range(len(fitness_scores))
        fitness_score_title = "Fitness Score Evolution Over Generations"
        fig1, axes1 = plt.subplots(figsize=(16, 4), tight_layout=True)
        axes1.plot(gens, fitness_scores, label='NumExpr', marker='x')
        axes1.set_xlabel("Generation")
        axes1.set_ylabel("Fitness Score")
        axes1.grid(True)
        fig1.suptitle(fitness_score_title)
        fig1.savefig("figures/" + fitness_score_title.replace(" ", "_") + f"(Pop_Size_{pop_size}_Generations_{generations}).jpg")
        axes1.legend()


        # Calculate metrics
        rmse = calculate_rmse(best_individual, target_trajectory)
        mae = calculate_mae(best_individual, target_trajectory)
        mse = calculate_mse(best_individual, target_trajectory)
        r2 = calculate_r2(best_individual, target_trajectory)

        # write all important elements to a text file for logging
        total_time = time.time() - start_time

        with open("log.log", "a") as log_file:
            # log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
            log_file.write(f"[=============================== NEW RUN ===============================]\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Population Size: {pop_size}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Number of generations: {generations}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Number of workers: {size}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Target Trajectory: {target_trajectory}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Best Fitness (NumExpr): {max(fitness_scores)}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Best Solution (NumExpr): {best_individual}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Total Time: {total_time} seconds\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] RMSE: {rmse}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] MAE: {mae}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] MSE: {mse}\n")
            log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] R-squared: {r2}\n")

        plt.show()

if __name__ == "__main__":
    main()
