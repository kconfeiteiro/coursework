#!/usr/bin/env python 
from math import pi, sqrt, erf 
import numpy as np 
import matplotlib.pylab as plt

"""
To implement the midpoint rule (with numpy) for numerical integration   
"""

def f(x):
    y = np.exp(-x**2)
    return y 

def g(x):
    y = 0.5*sqrt(pi)*erf(x) 
    return y 

def mid_sum(f,a,b,n):
    x,dx=np.linspace(a,b,n+1,endpoint='False',retstep='True')
    xbar=x[0:n]+(dx/2)*np.ones(n)    
    return dx*sum(f(xbar)) 


if __name__ == '__main__':
    a=0.0
    b=1.0
    n=1000000

    y=mid_sum(f,a,b,n)
    abs_err=abs(y-g(1))
    print('approx integral={0:}, abs_error={1:}'.format(y,abs_err))
