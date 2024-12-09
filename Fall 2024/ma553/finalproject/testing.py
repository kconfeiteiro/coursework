# %% imports
import matplotlib.pyplot as plt
import pandas as pd

# %% Load execution times from the log file
execution_times = pd.read_csv('execution_times.txt', sep=' ', header=None, usecols=[6], names=['time'])
execution_times["time"] = execution_times["time"] / execution_times["time"].max()


# %% Plot execution times
plt.figure(figsize=(10, 6))
plt.plot(execution_times['time'], marker='o')
plt.xlabel('Run')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of main() Function Over Different Runs')
plt.grid(True)
plt.show()
