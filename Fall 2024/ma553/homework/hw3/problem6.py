import pandas as pd
import numpy as np
from scipy.stats import linregress

# read data
data = pd.read_csv("problem6data.txt", delim_whitespace=True)
data = data.rename(columns={"Peak": "Peak Speed", "speed": "Units"})

# convert all units to GLOPS
data.loc[data["Units"] == "TFLOPS", "Peak Speed"] *= 1_000
data.loc[data["Units"] == "PFLOPS", "Peak Speed"] *= 1_000_000
data["Units"] = "GFLOPS"

# extract columns
years = data["Year"].to_numpy()
gflops = data["Peak Speed"].to_numpy()

# shift years to start from zero (i.e., t_0 = 1993)
years_shifted = years - years[0]

# take the natural logarithm of GFLOPS for regression
log_gflops = np.log(gflops)

# perform linear regression on (shifted years, log(GFLOPS))
slope, intercept, _, _, _ = linregress(years_shifted, log_gflops)

# calculate t^* as the inverse of the slope, converted to base-2 for consistency with doubling time
t_star = np.log(2) / slope 

# calculate G0 as the exponential of the intercept, converting back from log scale
G0 = np.exp(intercept)

# predict performance for the year 2025
year_predict = 2025 - years[0]  # shifted year for 2025
G_2025 = G0 * np.exp(slope * year_predict)

# display results
print(f"Estimated doubling time (t*): {t_star:.2f} years")
print(f"Estimated G0 (GFLOPS at t0={years[0]}): {G0:.2f} GFLOPS")
print(f"Predicted peak performance in 2025: {G_2025:.2f} GFLOPS")
