"""
Code from Homework 3.
"""

import numpy as np
import random
from numba import njit
import multiprocessing as mp
from time import time
import matplotlib.pyplot as plt
import datetime

@njit
def mc_volume_worker(points_per_worker):
    """Worker function to approximate part of the volume using Monte Carlo integration."""
    count = 0
    for _ in range(points_per_worker):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        z = random.uniform(0, 2)

        if x**2 + y**2 < z**2 and x**2 + y**2 < z * (2 - z):
            count += 1

    return count

def mc_volume(total_points, num_workers):
    """Approximate the volume by distributing work among multiple workers."""
    start = time()
    points_per_worker = total_points // num_workers  # floor division

    # create pool of worker processes
    with mp.Pool(processes=num_workers) as pool:
        # each worker calculates a count based on their subset of points
        results = pool.map(mc_volume_worker, [points_per_worker] * num_workers)

    total_count = sum(results)  # total count from workers
    print("MC vol calculated in {} seconds with {} workers.".format(time() - start, num_workers))
    return 8 * (total_count / total_points)

# example usage:
if __name__ == "__main__":
    start = time()
    total_points = 1_000_000  # random points for Monte Carlo
    num_workers = 8  # number of worker processes
    results = []
    for workers in range(1, num_workers + 1):
        approx_volume = mc_volume(total_points, num_workers=workers)
        print(f"\tApproximate volume of the ice cream cone: {approx_volume}")
        results.append(approx_volume)

    avg_result = np.average(results)
    print("Average result: ", round(avg_result, 5))
    print(f"Script ran in {round(time() - start, 5)} seconds")


    # Calculate speedup and efficiency
    speedups = [results[0] / result for result in results]
    efficiencies = [speedup / (i + 1) for i, speedup in enumerate(speedups)]

    # Plot speedup and efficiency using subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plot speedup
    fig.suptitle("Monte Carlo Ice Cream Cone Volume Calculation: Speedup and Efficiency", fontsize=16)

    axes[0].plot(range(1, num_workers + 1), speedups, marker="o")
    axes[0].set_title("Speedup")
    axes[0].set_xlabel("Number of Workers")
    axes[0].set_ylabel("Speedup")
    axes[0].grid(True)

    # Plot efficiency
    axes[1].plot(range(1, num_workers + 1), efficiencies, marker="o")
    axes[1].set_title("Efficiency")
    axes[1].set_xlabel("Number of Workers")
    axes[1].set_ylabel("Efficiency")
    axes[1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fig.savefig(f"plots/Monte Carlo_Ice_Cream_Cone_Volume_Calculation_Speedup_and_Efficiency_{num_workers}workers_{timestamp}.jpg")
    plt.show()
