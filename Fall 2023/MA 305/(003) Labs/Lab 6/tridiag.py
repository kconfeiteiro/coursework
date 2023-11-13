#!/usr/bin/env python3
import numpy as np


def trid(a, b, c, f):
    """Solves a tridiagonal matrix system [a c b][x]=[f]
    a=[0, a1, a2, ...,an-1] sub-diagonal
    b=[b0, b1, b2, ...,bn-2,0] super-diagonal
    c=[c0, c1, c2, ...,cn-1] leading-diagonal
    x=[x0,x1,...,xn-1] unknown vector
    f=[f0,f1,...,fn-1] right hand side vector
    """

    n = len(a)
    y = np.zeros(n)
    alpha = np.zeros(n)
    beta = np.zeros(n)

    alpha[1] = -b[0] / c[0]
    beta[1] = f[0] / c[0]

    for i in range(1, n - 1):
        alpha[i + 1] = -b[i] / (a[i] * alpha[i] + c[i])
        beta[i + 1] = (f[i] - a[i] * beta[i]) / (a[i] * alpha[i] + c[i])

    y[n - 1] = (f[n - 1] - a[n - 1] * beta[n - 1]) / (
        c[n - 1] + a[n - 1] * alpha[n - 1]
    )

    for i in reversed(range(n - 1)):
        y[i] = alpha[i + 1] * y[i + 1] + beta[i + 1]

    return y
