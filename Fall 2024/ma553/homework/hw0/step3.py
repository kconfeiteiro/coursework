import time
import math as m

start_time = time.time()
start = 0
for i in range(10_000_000):
    print(f"{i}. {start}")
    start += 0.1

timed = time.time() - start_time
print("Executed time: ", timed)
