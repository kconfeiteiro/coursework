from functools import wraps
import time
import numpy as np

def calculate_rmse(predicted, observed):
    # root Mean Square Error
    return np.sqrt(np.mean((np.array(predicted) - np.array(observed)) ** 2))

def calculate_mae(predicted, observed):
    # mean Absolute Error
    return np.mean(np.abs(np.array(predicted) - np.array(observed)))

def calculate_mse(predicted, observed):
    # calculate Mean Square Error
    return np.mean((np.array(predicted) - np.array(observed)) ** 2)

def calculate_r2(predicted, observed):
    # calculate R-squared
    observed_mean = np.mean(observed)
    ss_total = np.sum((np.array(observed) - observed_mean) ** 2)
    ss_residual = np.sum((np.array(observed) - np.array(predicted)) ** 2)
    return 1 - (ss_residual / ss_total)

def time_function(log_file="execution_times.txt"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
            log_message = f"[{timestamp}] Function '{func.__name__}()' executed in {elapsed_time:.4f} seconds"
            print(log_message)
            if log_file:
                with open(log_file, 'a') as f:
                    f.write(log_message + '\n')
            return result
        return wrapper
    return decorator
