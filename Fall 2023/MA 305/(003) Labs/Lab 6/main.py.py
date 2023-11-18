"""
Krystian Ojeda Confeiteiro
Dr. Sam
MA-305 06DB: Lab 6
11/17/2023
"""

import warnings
from time import time

import matplotlib.pyplot as plt
import numpy as np

import helpers as hp

warnings.filterwarnings("ignore")

# code configurations
CONFIG = {
    "paths": ["DATA\\dataF.txt", "DATA\\dataM.txt"],
    "sizes": {"reshape": (5, 3), "size 1": (0, 100, 15)},
    "kwargs": {"delim_whitespace": True, "names": "1 2 3 4 5".split()},
    "range": 15,
    "bins": 5,
    "norms": [
        "Transpose",
        "Inner Product",
        "Maximum Sum Of Columns",
        "Maximum Sum Of Rows",
        "Square Root Of Sum Of Squares",
    ],
}

start = time()

# define
X = np.random.uniform(*CONFIG["sizes"]["size 1"])
A = X.reshape(*CONFIG["sizes"]["reshape"])
Y = A.ravel()

# create a larger matrix A
A_lg = hp.create_matrix(1000, 1000)
A = hp.create_matrix(4, 5)
B = A.transpose()
C = np.dot(A, B)

Y_stats = hp.stats(Y)
print("=" * 60)

print("Y Median: ", Y_stats.median)
print("\nX:\n--------------\n", X)
print("more matrix calculations:")


# perform matrix operations on both matrices
A_mat_ops = hp.matrix_ops(A)
A_lg_mops = hp.matrix_ops(A_lg)

print("\nA:\n--------------\n", A)
print("\nB:\n--------------\n", B)
print("\nC:\n--------------\n", C)

# print stats for A
print("\nStasticial values for A:\n")
for i, (ttype, val) in enumerate(zip(CONFIG["norms"], A_mat_ops), 1):
    print("{}. {}:\n{}\n".format(i, ttype, val))

# read data for hisograms
DATA = hp.read_n_prep(*CONFIG["paths"])
WOMN, MEN = hp.split_df(DATA)

# (2) create histogram
fig, (axesm, axesf) = plt.subplots(1, 2, tight_layout=True)
axesm.hist(MEN, bins=CONFIG["bins"])
axesm.set_xlabel("Men")
axesf.hist(WOMN, bins=CONFIG["bins"])
axesf.set_xlabel("Women")
fig.supylabel("Amount")
fig.suptitle("Distribution Of Heights For Men & Women")
fig.savefig("fig1.pdf")

# convert to np.array objects then gather stats
MEN_np, WOMN_np = MEN.to_numpy(), WOMN.to_numpy()
M_stats, W_stats = hp.stats(MEN_np, WOMN_np)
M_ab_median = DATA.loc[DATA[DATA.columns[0]] > M_stats.median]
W_ab_median = DATA.loc[DATA[DATA.columns[1]] > W_stats.median]
print("=" * 60)
print("Number Of Men Above Median: ", M_ab_median.shape[0])
print("Number Of Women Above Median: ", W_ab_median.shape[0])

_msg = "Norms & Stats For Matrix A"
print("=" * 60)
print(_msg)

# print mean, median, and mode for both
print("\nMale Height Distribution Stats:\n----")
print("Mean: ", M_stats.avg)
print("Median: ", M_stats.median)
print("Std. Dev: ", M_stats.stdev)
print("\nFemale Height Distribution Stats:\n----")
print("Mean: ", W_stats.avg)
print("Median: ", W_stats.median)
print("Std. Dev: ", W_stats.stdev)

# (4) solve linear system with `np.linalg.solve`
MAT_A = np.array(
    [
        [7, 1, -1, 2],
        [1, 8, 0, -2],
        [-1, 0, 4, -1],
        [2, -2, -1, 6],
    ]
)

MAT_B = np.array([3, -5, 4, -3])

solution = np.linalg.solve(MAT_A, MAT_B)
print("=" * 60)
print("Solution of A and B: ", solution)
print("=" * 60)
print("Solving the tri-diagonal system")

# solve the tri-diagonal system
M1 = np.array([[2, 2, 0, 0], [2, 4, 4, 0], [0, 1, 3, 3], [0, 0, 2, 5]])
FMAT = np.array([4, 6, 7, 10])

tri_diag_soln = hp.solve_tridiag(M1, FMAT)
print("Tridiagonal solution: ", tri_diag_soln)

print("=" * 60)

print("\nCode execuded in {:0.9f} seconds.".format(abs(start - time())))
