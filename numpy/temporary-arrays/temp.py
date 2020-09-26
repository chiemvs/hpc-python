import numpy as np
import os

def maxmem():
    # Check maximum memory from /proc/
    # Based on Python Cookbook
    # http://code.activestate.com/recipes/286222/
    # Works on most Linux systems but not in Mac OSX or Windows

    _scale = {'kB': 1024.0, 'mB': 1024.0 * 1024.0,
              'KB': 1024.0, 'MB': 1024.0 * 1024.0}

    _proc_status = '/proc/{0}/status'.format(os.getpid())
    with open(_proc_status) as f:
        v = f.read()

    # Find VmHWM value
    i = v.index('VmHWM:')
    v = v[i:].split(None, 3)
    return float(v[1]) * _scale[v[2]]

# Python and Numpy library memory usage
overhead = maxmem()

# Investigate temporary memory usage for computation: s = np.sin(np.sqrt(x**2 + y**2 + z**2) / x)

x = np.random.random((1000,1000,5))
y = np.random.random((1000,1000,5))
z = np.random.random((1000,1000,5))

#c = x**2
#c += y**2
#c += z**2
#c = np.sqrt(c)
##c = np.sin(c/x)
#c = c/x
#c = np.sin(c) 

s = np.sin(np.sqrt(x**2 + (y**2 + z**2)) / x)

mem = maxmem() - overhead

print(mem)
