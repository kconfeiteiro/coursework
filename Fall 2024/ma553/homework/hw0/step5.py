import time

N = 1000  # Run with different values 1,10,100,1000, [^18^][18]...
R = 1000  # Choose R large so that execution time can be accurately measurable![^19^][19]

# Initialize a, b, c, d as lists of floats 0.0, 1.0, 2.0 and 3.0 respectively[^20^][20].
a = [0.0] * N
b = [1.0] * N
c = [2.0] * N
d = [3.0] * N

t_start = time.time()  # get the time stamp[^21^][21]

for j in range(R):  # Repeat the calculation[^22^][22]
    for i in range(N):
        a[i] = b[i] + c[i] * d[i]  # 3 loads and 1 store[^24^][24]

t_end = time.time()  # get the time stamp

# compute mflop/sec
mflops = R * N * 2.0 / ((t_end - t_start) * 1e6)
line = f"Performance: {mflops} MFlops/sec\n"
print(line)

with open("log.txt", "+a") as file:
    file.write(line)
