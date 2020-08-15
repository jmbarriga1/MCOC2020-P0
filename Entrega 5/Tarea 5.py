# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:40:53 2020

@author: MiguelB
"""


from time import perf_counter
import scipy as sp
import scipy.linalg as spLinalg
import numpy as np
from numpy import float32
from matplotlib import pyplot as plt

def matriz_laplaceana(N, d= float32):
    A = np.zeros((N,N), dtype = d)
    
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,j] = 2
            if i + 1 == j:
                A[i,j] = -1
            if i - 1 == j:
                A[i,j] = -1
    return A 



Na = [2, 5, 10, 12, 15, 40, 50, 60, 80, 100, 125, 200, 300, 500, 700, 800, 1000, 2000, 4000]
N_corridas = 10


names = ["A_invB_inv.txt", "A_invB_npSolve.txt"]

files = [open(name, "w") for name in names]

for N in Na:
    dts = np.zeros((N_corridas, len(files)))
    print(f"N = {N}")
    
    for i in range (N_corridas):
        
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][0] = dt
        
    
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A, B)
        t2= perf_counter()
        dt = t2-t1
        dts[i][1] = dt
        
        
    print("dts: ", dts)
    dts_mean = [np.mean(dts[:,j]) for j in range (len(files))]
    
    print("dts_mean: ", dts_mean)
    
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()

x = [10 , 20 , 50 , 100 , 200 , 500 , 1000 , 2000 , 5000 , 10000, 20000] 
xticks_txt = ["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000"]
y = [0.1e-3, 1e-3, 1e-2, 0.1, 1., 10., 60, 600, 3600]
yticks_txt = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min", "1 h"] 
plt.figure()
plt.subplot(2, 1, 1)
#primera funcion
for i in range(len(Na)):
    archivo1 = "A_invB_inv.txt" 
    archivo2 = "A_invB_npSolve.txt"
    fid1 = open(archivo1,"r")
    list_of_lists = []
    times = []
    for line in fid1:
      stripped_line = line.strip()
      line_list = stripped_line.split()
      list_of_lists.append(line_list)
    fid1.close()
    for fila in list_of_lists:
        times.append(float(fila[1]))
        
    #segunda funcion
    fid2 = open(archivo2,"r")
    list_of_lists2= []
    times2 = []
    for line2 in fid2:
      stripped_line = line2.strip()
      line_list = stripped_line.split()
      list_of_lists2.append(line_list)
    fid2.close()
    for fila2 in list_of_lists2:
        times2.append(float(fila2[1]))
print (times)
print (times2)
plt.loglog(Na,times,"o-")
plt.loglog(Na,times2,"o-")
plt.xticks(x ,xticks_txt, rotation = 45) 
plt.yticks(y, yticks_txt) 
plt.ylabel("time (s)")
plt.xlabel("Matrix size")
plt.title("performance Ax = B")
plt.legend(["A_invB_inv.txt","A_invB_npSolve.txt"],loc = 'upper left')
plt.grid()
plt.show()