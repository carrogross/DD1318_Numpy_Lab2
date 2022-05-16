# UPPGIFT 1 
from matplotlib import pyplot as plt
import numpy as np


# a) 
def mandelbrot(c): 
    z = 0
    for i in range(100): 
        z = z*z + c 
    return np.abs(z) <= 2 
    # Returns True if the absolute value of z is not more than 2 => c is stable


# b) 
M = np.zeros((401, 401)) # creating a 401x401 matrix with all zeros
amin = -2
amax = 2
bmin = -2
bmax = 2
steplength = 0.01
A = np.arange(amin, amax, steplength)
B = np.arange(bmin, bmax, steplength)

def runUppg2b(): 
    for a in A: 
        for b in B: # for all combinations of values in A and B, do the following: 
            stable = mandelbrot(np.complex(a, b)) # a+bi == np.complex(a, b)
            if stable: 
                M[(a+2)*100, (b+2)*100] = 1
    
    plt.imshow(M, cmap='gray', extent=(amin, amax, bmin, bmax))
    plt.show()

runUppg2b()


# c) 


