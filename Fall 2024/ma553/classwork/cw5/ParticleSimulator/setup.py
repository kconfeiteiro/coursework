from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

my_openmp = Extension('my_openmp',
                           ['my_openmp.pyx'],
                           extra_compile_args=['-fopenmp'],
                           extra_link_args=['-fopenmp'])

#setup(
#   ext_modules = cythonize('my_openmp.pyx'),
#)

cevolve = Extension('cevolve',
                    ['cevolve.pyx'],
                    extra_compile_args=['-fopenmp'],
                    extra_link_args=['-fopenmp'])

setup(
   name='Hello',
   ext_modules = cythonize(['cevolve.pyx','my_openmp.pyx']),
)
