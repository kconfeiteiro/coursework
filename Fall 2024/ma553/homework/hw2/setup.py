from Cython.Build import cythonize
from setuptools import setup


setup(
    name="heat2d", ext_modules=cythonize("heat2d.pyx", compiler_directives={'language_level': "3"})
)
