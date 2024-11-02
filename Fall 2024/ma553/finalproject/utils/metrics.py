import numpy as np

def calculate_rmse(predicted, observed):
    # Calculate Root Mean Square Error
    return np.sqrt(np.mean((np.array(predicted) - np.array(observed)) ** 2))

def calculate_mae(predicted, observed):
    # Calculate Mean Absolute Error
    return np.mean(np.abs(np.array(predicted) - np.array(observed)))

def calculate_mse(predicted, observed):
    # Calculate Mean Square Error
    return np.mean((np.array(predicted) - np.array(observed)) ** 2)

def calculate_r2(predicted, observed):
    # Calculate R-squared
    observed_mean = np.mean(observed)
    ss_total = np.sum((np.array(observed) - observed_mean) ** 2)
    ss_residual = np.sum((np.array(observed) - np.array(predicted)) ** 2)
    return 1 - (ss_residual / ss_total)
