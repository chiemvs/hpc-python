from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(ext_modules = cythonize(Extension("heat", sources = ["heat.pyx"], include_dirs = [numpy.get_include()]),language_level = 3))
#setup(ext_modules = cythonize(Extension("heat.py", sources = ["heat.pyx"], include_dirs = [numpy.get_include()], define_macros = [("NPY_NO_DEPRECATED_API","NPY_1_9_API_VERSION")])))
