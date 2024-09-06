#!/usr/bin/env python
import math


def f(x):
    return 4 * math.sqrt(1 - x**2)


def left_sum(f, a, b, n):
    """Approximates integral by the sum of area of rectangles, height from the left."""
    dx = (b - a) / n
    lsum = 0
    for i in range(n):
        xi = a + i * dx
        lsum += f(xi)
    return dx * lsum

def right_sum(f, a, b, n):
    """Approximates integral by the sum of area of rectangles, height from the right."""
    dx = (b - a) / n
    rsum = 0
    for i in range(1, n + 1):
        xi = a + i * dx
        rsum += f(xi)
    return dx * rsum

def midpoint_rule(f, a, b, n):
    """Approximates integral by the sum of area of rectangles, height from the midpoint."""
    dx = (b - a) / n
    msum = 0
    for i in range(n):
        xibar = a + (0.5 + i) * dx
        msum += f(xibar)
    return dx * msum

def trapezoid_rule(f, a, b, n):
    """Approximates integral using the Trapezoid rule."""
    dx = (b - a) / n
    tsum = 0
    for i in range(1, n):
        xi = a + i * dx
        tsum += f(xi)
    return dx * (f(a) / 2 + tsum + f(b) / 2)

def simpson_rule(f, a, b, n):
    """Approximates integral using the Simpson's 1/3rd rule."""
    dx = (b - a) / n
    odd_sum = sum(f(a + i * dx) for i in range(1, n, 2))
    even_sum = sum(f(a + i * dx) for i in range(2, n - 2, 2))
    return dx * (f(a) + 4 * odd_sum + 2 * even_sum + f(b)) / 3

if __name__ == '__main__':
    a = 0
    b = 1
    n = int(input('Enter the number n:'))

    print('Left_Sum_approx pi = ', left_sum(f, a, b, n))
    print('Right_Sum_approx pi = ', right_sum(f, a, b, n))
    print('Midpoint_approx pi = ', midpoint_rule(f, a, b, n))
    print('Trapezoid_approx pi =', trapezoid_rule(f, a, b, n))
    print('Simpson_approx pi = ', simpson_rule(f, a, b, n))
