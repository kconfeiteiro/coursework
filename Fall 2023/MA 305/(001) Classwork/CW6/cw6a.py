"""
Krystian Ojeda Confeitiero
Dr. Sam
MA305 - 06DB
Classwork 6
Purpose:
    To implement Left Sum, Right Sum, and Middle Sum  rules
    approximations for integrals creating some user defined modules.
"""

from math import erf, pi, sqrt

from my_funs import f_func, g_func
from num_int import left_sum, middle_sum, right_sum

if __name__ == "__main__":
    # Limits of integration
    a_lim, b_lim = 0, 1

    # Exact value of the integrals
    g_func_exact = sqrt(pi) * erf(b_lim) / 2
    f_func_exact = 20

    # number_rectangles = int(input("Enter the number of rectangles: "))
    number_rectangles = 70

    # Evaluate the approximate value of the integral for function (a)
    approx1 = left_sum(f_func, a_lim, b_lim, number_rectangles)
    approx2 = middle_sum(f_func, a_lim, b_lim, number_rectangles)
    approx3 = right_sum(f_func, a_lim, b_lim, number_rectangles)

    # Compute the absolute errors
    error1 = abs(approx1 - f_func_exact)
    error2 = abs(approx2 - f_func_exact)
    error3 = abs(approx3 - f_func_exact)

    # Evaluate the approximate value of the integral for function (b)
    approx4 = left_sum(g_func, a_lim, b_lim, number_rectangles)
    approx5 = middle_sum(g_func, a_lim, b_lim, number_rectangles)
    approx6 = right_sum(g_func, a_lim, b_lim, number_rectangles)

    # Compute the absolute errors
    error4 = abs(approx4 - g_func_exact)
    error5 = abs(approx5 - g_func_exact)
    error6 = abs(approx6 - g_func_exact)

    # Print the results in a nice formatted output
    print("\nResults using {} rectangles for function (a):".format(number_rectangles))
    print("=============================================")
    print(f" Exact answer: {f_func_exact}\n")
    print("                 Approximation       Error")
    print("  Left-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx1, error1))
    print(" Right-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx2, error2))
    print("   Mid-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx3, error3))
    print("=============================================\n")

    print("Results using {} rectangles for function (b):".format(number_rectangles))
    print("=============================================")
    print(f" Exact answer: {g_func_exact}\n")
    print("                 Approximation       Error")
    print("  Left-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx4, error4))
    print(" Right-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx5, error5))
    print("   Mid-Sum: \t {0:12.10f}\t {1:12.10f}".format(approx6, error6))
    print("=============================================\n")
