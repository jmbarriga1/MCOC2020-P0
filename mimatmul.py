# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:38:16 2020

@author: MiguelB
"""

import numpy as np

def mimatmul(A,B):
    N = len(A)
    matriz = (N,N)
    C = np.zeros(matriz)
    
    for i in range(len(A)): 
        for j in range(len(B[0])):
            for h in range(len(B)):
                C[i][h]+= A[i][j]*B[j][h]
    return C                
                
                
                    
        
    