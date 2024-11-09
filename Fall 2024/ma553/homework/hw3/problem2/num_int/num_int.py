#!/usr/bin/env python
import time
import math
import numpy as np
import numexpr as ne
import numba as nb
from mycytlib import trapezoid_rule_cyt, trapezoid_rule_omp

def f(x):
    y=4*math.sqrt(1-x**2)
    return y

@nb.jit(nopython=True, nogil=True)
def fnb(x):
    y=4*math.sqrt(1-x**2)
    return y

def fnp(x):
    y=4*np.sqrt(1-x**2)
    return y

def fne(x):
    y=4*ne.evaluate("sqrt(1-x**2)")
    return y

def trapezoid_rule(a, b, n):
    dx=(b-a)/n
    tsum=0.5*(f(a)+f(b))
    for i in range(1,n):
        xi = a+i*dx
        tsum += f(xi)
    return dx*tsum

@nb.jit(nopython=True, nogil=True)
def trapezoid_rule_nb(a, b, n):
    dx=(b-a)/n
    tsum=0.5*(fnb(a)+fnb(b))
    for i in range(1,n):
        xi = a+i*dx
        tsum += fnb(xi)
    return dx*tsum

@nb.jit(nopython=True, parallel=True)
def trapezoid_rule_np(a, b, n):
    x, dx = np.linspace(a, b, n+1, retstep=True)
    y = fnp(x)
    tsum = np.sum(y[1:-1])
    return dx * (tsum + 0.5 * (y[0] + y[-1]))

def trapezoid_rule_ne(a, b, n):
    x,dx=np.linspace(a,b,n+1,retstep=True)
    y=fne(x)
    yy=y[1:-1]
    tsum=ne.evaluate("sum(yy)")
    return dx*(tsum+0.5*(y[0]+y[-1]))

##############################################################################
if __name__=="__main__":
   a, b, n = 0, 1, 10_000_000
   print(" Trapezoid rule numerical integration n={} using".format(n))

   t0 = time.time()
   p1 = trapezoid_rule(a, b, n)
   t1 = time.time()

   p2 = trapezoid_rule_np(a, b, n)
   t2 = time.time()

   p3 = trapezoid_rule_ne(a, b, n)
   t3 = time.time()

   p4 = trapezoid_rule_cyt(a, b, n)
   t4 = time.time()

   p5 = trapezoid_rule_omp(a, b, n)
   t5 = time.time()

   p6 = trapezoid_rule_nb(a, b, n)
   t6 = time.time()

   print(" Method  \t Aproximate value \t Time")
   print(" Python  \t {} \t {}".format(p1, t1-t0))
   print(" NumPy   \t {} \t {}".format(p2, t2-t1))
   print(" Cython  \t {} \t {}".format(p4, t4-t3))
   print(" OpenMP  \t {} \t {}".format(p5, t5-t4))
   print(" Numexpr \t {} \t {}".format(p3, t3-t2))
   print(" Numba   \t {} \t {}".format(p6, t6-t5))
