import random
import numpy as np
import multiprocessing as mp

from time import time

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
    points_per_worker = total_points // num_workers

    # Create a pool of worker processes
    with mp.Pool(processes=num_workers) as pool:
        # Each worker calculates a count based on their subset of points
        results = pool.map(mc_volume_worker, [points_per_worker] * num_workers)

    # Total count from all workers
    total_count = sum(results)

    print("MC vol calculated in {} seconds with {} workers.".format(start - time(), num_workers))
    return 8 * total_count / total_points

# Example usage:
if __name__ == "__main__":
    total_points = 1_000_000  # random points for Monte Carlo
    num_workers = 4 # number of worker processes
    results = []
    for workers in range(1, num_workers + 1):
        approx_volume = mc_volume(total_points, num_workers=workers)
        print(f"\tApproximate volume of the ice cream cone: {approx_volume}")
        results.append(approx_volume)

    avg_result = np.average(results)
    print("Average result: ", round(avg_result, 5))
