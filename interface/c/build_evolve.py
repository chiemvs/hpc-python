from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
        void evolve(double *u, double *u_previous, int nx, int ny, double a, double dt, double dx2, double dy2);
        """)

ffibuilder.set_source("_my_evolve",
        """#include "evolve.h" """,
        sources=['evolve.c'],
        library_dirs = [],
        libraries = ['m'])

ffibuilder.compile(verbose=True)
