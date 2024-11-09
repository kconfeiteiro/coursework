#!/usr/bin/env python 
import matplotlib.pylab as plt
from math import pi, sqrt, erf
import numpy as np

"""
To implement the midpoint rule for numerical integration   
"""

def f(x):
    y = np.exp(-x**2)
    return y 

def g(x):
    y = 0.5*sqrt(pi)*erf(x) 
    return y 

def trapezoid_rule(f,a,b,n):
    x,dx=np.linspace(a,b,n+1,retstep=True)
    y=f(x)
    tsum=np.sum(y[1:-1])
    return dx*(tsum+0.5*(y[0]+y[-1]))

##############################################################################
if __name__ == '__main__':
    a=0.0
    b=1.0
    n=1000000

    y=trapezoid_rule(f,a,b,n)
    abs_err=abs(y-g(1))
    print('approx integral={0:}, abs_error={1:}'.format(y,abs_err))
