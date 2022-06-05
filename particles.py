import numpy as np
from numba import njit, prange
from index import *


def W(r, h):
    '''

    equ. A1 in Robin 2004 (the Kernel function)

    :param r: (float)
    :param h: (float)
    :return: weight
    '''
    pass


def dvdt(pars):
    '''

    equ. A3 in Robin 2004

    :param pars: np.array(float); shape: [NUM_PARTICLE, NUM_QUANTITIES]
    :return: dvdt: np.array(float); shape: [NUM_PARTICLE, NUM_DIMENSION]
    '''

    dvdt_res = np.zeros(pars.shape[0])
    pass


def dudt(pars):
    '''

    equ. A4 in Robin 2004

    :param pars:
    :return:
    '''
    pass


def eos(pars):
    '''

    Use e.o.s to calculate pressure

    :param pars:
    :return:
    '''
    pass