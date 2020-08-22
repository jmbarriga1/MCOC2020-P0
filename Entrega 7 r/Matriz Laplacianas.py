# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 23:25:20 2020

@author: MiguelB
"""


import numpy as np
def matriz_laplaciana_llena(N, type=np.float32):
    e= np.eye(N) - np.eye(N,N,1)
    return type(e+e.T)

from scipy.sparse import eye

def matriz_laplaciana_dispersa(N,t=np.float32):
    e=eye(N,N,dtype=t)-eye(N,N,1,dtype=t)
    return e+e.T 