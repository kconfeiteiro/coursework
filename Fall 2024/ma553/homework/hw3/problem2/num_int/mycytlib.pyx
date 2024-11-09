cimport cython 
from libc.math cimport sqrt
from cython.parallel cimport prange 

cdef double f(double x):
    y=4*sqrt(1-x**2) 
    return y

cdef double f1(double x) nogil:
    y=4*sqrt(1-x**2) 
    return y

#cdef double trapz_cyt(function_type f, double a, double b, int n):
#cdef double trapz_cyt(void *f, double a, double b, int n):
#    cdef double dx
#    cdef double xi
#    cdef int i 
#    cdef double tsum 
#    dx=(b-a)/n
#    tsum=((<object>f)(a) + (<object>f)(b))/2
#    for i in range(1,n):
#        xi = a+i*dx
#        tsum += (<object>f)(xi)	
#    return dx*tsum 

cdef double trapz_cyt(double a, double b, int n):
    cdef double dx
    cdef double xi
    cdef int i 
    cdef double tsum 
    dx=(b-a)/n
    tsum=(f(a)+f(b))/2
    for i in range(1,n):
        xi = a+i*dx
        tsum += f(xi)	
    return dx*tsum 

def trapezoid_rule_cyt(a,b,n):
    return trapz_cyt(a,b,n)

cdef double trapz_omp(double a, double b, int n) nogil:
    cdef double dx
    cdef double xi
    cdef int i 
    cdef double tsum 
    dx=(b-a)/n
    tsum=(f1(a)+f1(b))/2
    for i in prange(n, nogil=True):
        xi = a+(i+1)*dx
        tsum += f1(xi)	
    return dx*tsum 

def trapezoid_rule_omp(a,b,n):
    return trapz_omp(a,b,n)
