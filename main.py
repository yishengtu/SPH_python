import numpy as np
from numba import njit, prange
from index import *
from particles import dvdt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    NUM_PARTICLE = 10
    NUM_DIMENSION = 3

    particles = np.zeros((NUM_PARTICLE, NUM_QUANTITIES))

    ot = 0        # time now
    t_tot = 10    # total time
    dt = 0.1      # time-step (Is there a CFL-like condition?)
    while ot < t_tot:
        # step 1: calculate acceleration, speed and position
        # step 2: calculate internal energy at new position
        # step 3: calculate density and pressure at new position
        dv = dvdt(particles)
        ot += dt

    # output
