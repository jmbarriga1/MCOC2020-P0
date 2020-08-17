# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:23:26 2020

@author: MiguelB
"""

from time import perf_counter
import scipy as sp
import scipy.linalg as spLinalg
import numpy as np
from numpy import float32
from matplotlib import pyplot as plt
from scipy.sparse import lil_matrix, eye
from scipy import linalg

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

def matriz_laplaciana_llena(N, type=np.float32):
    e= np.eye(N) - np.eye(N,N,1)
    return type(e+e.T)



Na = [2, 5, 10, 12, 15, 40, 50, 60, 80, 100, 125, 200, 300, 500, 700, 800, 1000, 2000, 4000]
N_corridas = 5


names = ["A_invB_inv.txt", "A_invB_npSolve.txt", "A_invB_spSolve.txt", "A_invB_spSolve_symmetric.txt", "A_invB_spSolve_pos.txt", "A_invB_spSolve_pos_overwrite.txt"]

files = [open(name, "w") for name in names]

for N in Na:
    dts = np.zeros((N_corridas, len(files)))
    print(f"N = {N}")
    
    for i in range (N_corridas):
        
        A = matriz_laplaciana_llena(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][0] = dt
        
    
        A2 = matriz_laplaciana_llena(N)
        B2 = np.ones(N)
        t3 = perf_counter()
        A_invB = np.linalg.solve(A2, B2)
        t4= perf_counter()
        dt2 = t4-t3
        dts[i][1] = dt2
        
        A3 = matriz_laplaciana_llena(N)
        B3 = np.ones(N)
        t5 = perf_counter()
        A_invB = linalg.solve(A3, B3, assume_a="sym")
        t6 = perf_counter()
        dt3 = t6-t5
        dts[i][2] = dt3
        
        A4 = matriz_laplaciana_llena(N)
        B4 = np.ones(N)
        t7 = perf_counter()
        A_invB = linalg.solve(A4, B4, assume_a="sym")
        t8 = perf_counter()
        dt4 = t8-t7
        dts[i][3] = dt4
        
        A5 = matriz_laplaciana_llena(N)
        B5 = np.ones(N)
        t9 = perf_counter()
        A_invB = linalg.solve(A5, B5, assume_a = "pos")
        t10 = perf_counter()
        dt5 = t10-t9
        dts[i][4] = dt
        
        A6 = matriz_laplaciana_llena(N)
        B6 = np.ones(N)
        t11 = perf_counter()
        A_invB = linalg.solve(A6, B6, assume_a = "pos", overwrite_a=True,overwrite_b=True)
        t12 = perf_counter()
        dt6 = t12-t11
        dts[i][5] = dt6
        
        
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

#primera funcion
for i in range(len(Na)):
    archivo1 = "A_invB_inv.txt" 
    archivo2 = "A_invB_npSolve.txt"
    archivo3 = "A_invB_spSolve.txt"
    archivo4 = "A_invB_spSolve_symmetric.txt"
    archivo5 = "A_invB_spSolve_pos.txt"
    archivo6 = "A_invB_spSolve_pos_overwrite.txt"
    
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
        
    #tercera funcion
    fid3 = open(archivo3,"r")
    list_of_lists3= []
    times3 = []
    for line3 in fid3:
      stripped_line = line3.strip()
      line_list = stripped_line.split()
      list_of_lists3.append(line_list)
    fid3.close()
    for fila3 in list_of_lists3:
        times3.append(float(fila3[1]))
        
    #cuarta funcion
    fid4 = open(archivo4,"r")
    list_of_lists4= []
    times4 = []
    for line4 in fid4:
      stripped_line = line4.strip()
      line_list = stripped_line.split()
      list_of_lists4.append(line_list)
    fid4.close()
    for fila4 in list_of_lists4:
        times4.append(float(fila4[1]))    
        
    #quinta funcion
    fid5 = open(archivo5,"r")
    list_of_lists5= []
    times5 = []
    for line5 in fid5:
      stripped_line = line5.strip()
      line_list = stripped_line.split()
      list_of_lists5.append(line_list)
    fid5.close()
    for fila5 in list_of_lists5:
        times5.append(float(fila5[1]))  
        
        
    #sexta funcion
    fid6 = open(archivo6,"r")
    list_of_lists6= []
    times6 = []
    for line6 in fid6:
      stripped_line = line6.strip()
      line_list = stripped_line.split()
      list_of_lists6.append(line_list)
    fid5.close()
    for fila6 in list_of_lists6:
        times6.append(float(fila6[1]))        
        
print (times)
print (times2)
print (times3)
print (times4)
print (times5)
print (times6)

plt.loglog(Na,times,"o-")
plt.loglog(Na,times2,"o-")
plt.loglog(Na,times3,"o-")
plt.loglog(Na,times4,"o-")
plt.loglog(Na,times5,"o-")
plt.loglog(Na,times6,"o-")

plt.xticks(x ,xticks_txt, rotation = 45) 
plt.yticks(y, yticks_txt) 
plt.ylabel("time (s)")
plt.xlabel("Matrix size")
plt.title("performance Ax = B")
plt.legend(["A_invB_inv.txt","A_invB_npSolve.txt", "A_invB_spSolve.txt", "A_invB_spSolve_symmetric.txt", "A_invB_spSolve_pos.txt", "A_invB_spSolve_pos_overwrite.txt"],loc = 'upper left')
plt.grid()
plt.show()
plt.tight_layout()