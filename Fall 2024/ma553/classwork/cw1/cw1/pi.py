#!/usr/bin/env python
import random 

def alternating_series_pi(n): 
    """ Approximates pi using sum of n terms in the series of 4*arctan(1)."""
    as_sum = 0
    for i in range(1,n+1):
        as_sum += ((-1)**(i+1))/(2*i-1)
    return 4*as_sum

def dart_board_pi(n):
    """ Approximates pi using dart_board algorithm with n darts."""
    count=0
    for i in range(n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if x**2+y**2 < 1: 
           count += 1
    return 4*count/n 


