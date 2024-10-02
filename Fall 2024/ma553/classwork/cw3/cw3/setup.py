from distutils.core import setup
from Cython.Build import cythonize

setup(
     name='C_evolve',
     ext_modules=cythonize("cevolve.pyx"),
)
