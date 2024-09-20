#!/usr/bin/env python 
from math import sqrt
import numpy as np

def f(x):
    y=4*sqrt(1-x**2) 
    return y

def f_np(x): # NumPy version
    y=4*np.sqrt(1-x**2) 
    return y

def trapezoid_rule(f,a,b,n):
    """Approximates integral using the Trapezoid rule."""

    dx=(b-a)/n
    tsum=0
    for i in range(1,n):
        xi = a+i*dx
        tsum += f(xi)
    return dx*(f(a)/2+tsum+f(b)/2)

def trapezoid_rule_np(f_np,a,b,n): # NumPy version
    """Approximates integral using the Trapezoid rule (NumPy version)."""

    [x,dx]=np.linspace(a,b,n+1,retstep=True)
    fx=f_np(x)
    return dx*(fx[0]/2+np.sum(fx[1:n])+fx[-1]/2)

##############################################################################
if __name__=='__main__':
   a=0
   b=1
   n=int(input('Enter the number n:'))
   print('===============================')
   print('      Trapezoid_approx: pi=', trapezoid_rule(f,a,b,n))
   print('Trapezoid_approx_numpy: pi=', trapezoid_rule_np(f_np,a,b,n))

