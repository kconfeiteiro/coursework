"""
Krystian Ojeda Confeiteiro
Dr. Sam
MA-305 06DB: Lab 6
11/13/2023
"""

from time import time

import numpy as np

import helpers as hp

CONFIG = {
    "range": 15,
    "sizes": {"reshape": (5, 3), "size 1": (0, 100, 15)},
    "paths": ["DATA\dataF.txt", "DATA\dataM.txt"],
}


if __name__ == "__main__":
    start = time()
    X = np.random.uniform(*CONFIG["sizes"]["size 1"])
    A = X.reshape(*CONFIG["sizes"]["reshape"])
    Y = A.ravel()

    Y_stats = hp.stats(Y)
    print("\nX:\n--------------\n")
    hp.display_table(X)

    A = hp.create_matrix(4, 5)
    print("\nA:\n--------------\n", A)

    A_mat_ops = hp.matrix_ops(A)

    print("\nCode execuded in {:0.9f} seconds.".format(abs(start - time())))
