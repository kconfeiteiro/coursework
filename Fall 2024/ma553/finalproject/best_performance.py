import time
import matplotlib.pyplot as plt
import numpy as np
from mpi4py import MPI
from utils.genetic_algorithm import evaluate_fitness_ne, evolve_population, initialize_population
from utils.metrics import calculate_mae, calculate_mse, calculate_r2, calculate_rmse, time_function


@time_function()
def run_genetic_algorithm(pop_size, generations, target_trajectory):
    start_time = time.time()

    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Initialize population
    population = initialize_population(pop_size)

    # Evaluate fitness and evolve population
    for generation in range(generations):
        fitness_scores = evaluate_fitness_ne(population, target_trajectory)
        population = evolve_population(population, fitness_scores)
        if rank == 0 and generation % 5 == 0:
            print(f"Generation {generation}: Best fitness (ne) = {max(fitness_scores)}")

    # Collect orbital parameters
    best_individual = population[np.argmax(fitness_scores)]
    print("Best solution (ne): ", best_individual)

    # Calculate metrics
    rmse = calculate_rmse(best_individual, target_trajectory)
    mae = calculate_mae(best_individual, target_trajectory)
    mse = calculate_mse(best_individual, target_trajectory)
    r2 = calculate_r2(best_individual, target_trajectory)

    total_time = time.time() - start_time

    return {
        "pop_size": pop_size,
        "generations": generations,
        "num_workers": size,
        "best_fitness": max(fitness_scores),
        "best_individual": best_individual,
        "rmse": rmse,
        "mae": mae,
        "mse": mse,
        "r2": r2,
        "total_time": total_time,
    }


def main(
    target_trajectory=np.array([[7100, 0.18, 0.09, 0.028, 7.7, 0.018]]),
    versions=[(50, 30), (100, 50), (200, 150), (400, 200)],
):
    results = []
    for pop_size, generations in versions:
        result = run_genetic_algorithm(pop_size, generations, target_trajectory)
        results.append(result)

    # Find the best run
    best_run = max(results, key=lambda x: x['best_fitness'])

    # Print the final best result
    print("\nFinal Best Result:")
    print(f"Population Size: {best_run['pop_size']}")
    print(f"Number of Generations: {best_run['generations']}")
    print(f"Number of Workers: {best_run['num_workers']}")
    print(f"Best Solution: {best_run['best_individual']}")
    print(f"Best Fitness: {best_run['best_fitness']}")
    print(f"RMSE: {best_run['rmse']}")
    print(f"MAE: {best_run['mae']}")
    print(f"MSE: {best_run['mse']}")
    print(f"R-squared: {best_run['r2']}")
    print(f"Total Time: {best_run['total_time']} seconds")

    # Save results to a log file
    with open("performance_log.log", "a") as log_file:
        log_file.write(
            f"[=============================== NEW SESSION ===============================]\n"
        )
        for i, result in enumerate(results):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log_file.write(
                f"[>>>>>>>>>>>>>>>>>>>>>>  RUN {i}  <<<<<<<<<<<<<<<<<<<<<<<]\n"
            )
            log_file.write(f"[{timestamp}] Population Size: {result['pop_size']}\n")
            log_file.write(f"[{timestamp}] Number of generations: {result['generations']}\n")
            log_file.write(f"[{timestamp}] Number of workers: {result['num_workers']}\n")
            log_file.write(f"[{timestamp}] Best Solution: {result['best_individual']}\n")
            log_file.write(f"[{timestamp}] Best Fitness: {result['best_fitness']}\n")
            log_file.write(f"[{timestamp}] RMSE: {result['rmse']}\n")
            log_file.write(f"[{timestamp}] MAE: {result['mae']}\n")
            log_file.write(f"[{timestamp}] MSE: {result['mse']}\n")
            log_file.write(f"[{timestamp}] R-squared: {result['r2']}\n")
            log_file.write(f"[{timestamp}] Total Time: {result['total_time']} seconds\n")

    # Plot the results
    if MPI.COMM_WORLD.Get_rank() == 0:
        fig, axes = plt.subplots(3, 2, figsize=(20, 16), tight_layout=True)
        for result in results:
            label = f"Pop: {result['pop_size']}, Gen: {result['generations']}"
            axes[0, 0].plot(result["generations"], result["best_fitness"], label=label, marker='o')
            axes[0, 1].plot(result["generations"], result["rmse"], label=label, marker='o')
            axes[1, 0].plot(result["generations"], result["mae"], label=label, marker='o')
            axes[1, 1].plot(result["generations"], result["mse"], label=label, marker='o')
            axes[2, 0].plot(result["generations"], result["r2"], label=label, marker='o')
            axes[2, 1].plot(result["generations"], result["total_time"], label=label, marker='o')
        axes[0, 0].set_title("Best Fitness Over Generations")
        axes[0, 0].set_xlabel("Generations")
        axes[0, 0].set_ylabel("Best Fitness")
        axes[0, 0].legend()
        axes[0, 0].grid(True)

        axes[0, 1].set_title("RMSE Over Generations")
        axes[0, 1].set_xlabel("Generations")
        axes[0, 1].set_ylabel("RMSE")
        axes[0, 1].legend()
        axes[0, 1].grid(True)

        axes[1, 0].set_title("MAE Over Generations")
        axes[1, 0].set_xlabel("Generations")
        axes[1, 0].set_ylabel("MAE")
        axes[1, 0].legend()
        axes[1, 0].grid(True)

        axes[1, 1].set_title("MSE Over Generations")
        axes[1, 1].set_xlabel("Generations")
        axes[1, 1].set_ylabel("MSE")
        axes[1, 1].legend()
        axes[1, 1].grid(True)

        axes[2, 0].set_title("R-squared Over Generations")
        axes[2, 0].set_xlabel("Generations")
        axes[2, 0].set_ylabel("R-squared")
        axes[2, 0].legend()
        axes[2, 0].grid(True)

        axes[2, 1].set_title("Total Time Over Generations")
        axes[2, 1].set_xlabel("Generations")
        axes[2, 1].set_ylabel("Total Time (s)")
        axes[2, 1].legend()
        axes[2, 1].grid(True)

        fig.suptitle(f"Performance Metrics for Each Version (Workers: {results[0]['num_workers']})")
        plt.savefig("figures/performance_metrics.png")
        plt.show()


if __name__ == "__main__":
    main()
