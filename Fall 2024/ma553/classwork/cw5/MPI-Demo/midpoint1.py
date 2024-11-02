#!/usr/bin/env python 
from math import pi, sqrt, exp, erf 
import matplotlib.pylab as plt

"""
To implement the midpoint rule for numerical integration   
"""

def f(x):
    y = exp(-x**2)
    return y 

def g(x):
    y = 0.5*sqrt(pi)*erf(x) 
    return y 

def mid_sum(f,a,b,n):
    dx=(b-a)/n
    msum=0.0
    for i in range(n): 
        xibar = a+(0.5+i)*dx
        msum += f(xibar) 
    return dx*msum 


if __name__ == '__main__':
    a=0.0
    b=1.0
    n=1000000

    y=mid_sum(f,a,b,n)
    abs_err=abs(y-g(1))
    print('approx integral={0:}, abs_error={1:}'.format(y,abs_err))
