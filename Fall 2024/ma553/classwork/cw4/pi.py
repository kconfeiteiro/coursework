import multiprocessing
import random

darts = 10000

def pi_serial():
    hits = 0

    for _ in range(darts):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)

        if x**2 + y**2 <= 1:
            hits += 1

    return 4.0 * hits / darts

def sample():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1:
        return 1
    return 0

def pi_apply_async():
    with multiprocessing.Pool() as pool:
        results_async = [pool.apply_async(sample) for _ in range(darts)]
        hits = sum((r.get() for r in results_async))
        return 4.0 * hits / darts


def sample_multiple(darts_partial):
    return sum(sample() for _ in range(darts_partial))

def pi_apply_async_chunked():
    n_tasks = 10
    chunk_size = darts / n_tasks
    with multiprocessing.Pool() as pool:
        results_async = [pool.apply_async(sample_multiple, chunk_size) for _ in range(n_tasks)]
        hits = sum((r.get() for r in results_async))
        return 4.0 * hits / darts


if __name__ == '__main__':
    print('Approx pi with {0} darts = {1}'.format(darts, pi_serial()))
