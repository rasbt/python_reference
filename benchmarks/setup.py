
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("ccy_classic_lstsqr", ["ccy_classic_lstsqr.pyx"])]
)