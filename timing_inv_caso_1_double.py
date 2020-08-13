# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:48:17 2020

@author: MiguelB
"""

from numpy import double,linalg
from time import perf_counter
from matplotlib import pyplot as plt
from numpy import zeros, float32



def matriz_laplaciana(N, dtype=float32):
    A = zeros((N,N), dtype = dtype)
    
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,j] = 2
            if i + 1 == j:
                A[i,j] = -1
            if i - 1 == j:
                A[i,j] = -1
    return A 

Na = [3, 5, 10, 15, 20, 30, 40, 50, 60, 75, 100, 125, 150, 175, 250, 400, 600, 800, 1000, 2000, 6000, 10000]
      
N_corridas = 1

time = []



for i in range(N_corridas):
    memory = []    
    text = (f"caso1_double.txt")
    fid = open(text,"w")
    element = []

    for N in Na:
        print(f"N = {N}")
        
        A = matriz_laplaciana(N,double)
        
        t1 = perf_counter()
        C = linalg.inv(A)
        t2 = perf_counter()
        dt = t2 - t1
        mem = 2*(N**2)*8
        
        element.append(dt)
        memory.append(mem)
        print(f"time = {dt} s")
        print(f"memory = {mem} bytes")
        print(" ")
        fid.write(f"{N} {dt} {mem}\n")
    time.append(element)
            
    fid.close()

x = [3 , 4 , 50 , 100 , 200 , 500 , 1000 , 2000 , 5000 , 10000, 20000] 
xticks_txt = ["", "", "", "", "", "", "", "", "", "", ""]



y = [0.1e-3, 1e-3, 1e-2, 0.1, 1., 10., 60, 600, 3600]
yticks_txt = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min", "1 h"] 


plt.figure()
plt.subplot(2, 1, 1)

for i in range(N_corridas):
    text = (f"caso1_double.txt")
    fid = open(text,"r")
    list_of_lists = []
    times = []
    for line in fid:
      stripped_line = line.strip()
      line_list = stripped_line.split()
      list_of_lists.append(line_list)
    fid.close()
    for fila in list_of_lists:
        times.append(float(fila[1]))
    plt.loglog(Na,times,"o-")


plt.xticks(x , [] , rotation = 45) 
plt.yticks(y, yticks_txt) 
plt.ylabel("time")
plt.title("performance inverse of A")
plt.grid(True)

xticks_txt1 = ["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000"]
y1 = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11]
yticks_txt1 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]

plt.subplot(2, 1, 2)
plt.loglog(Na , memory , "-o")
plt.xticks(x, xticks_txt1, rotation = 45)
plt.yticks(y1, yticks_txt1)
plt.ylabel("memory")
plt.xlabel("matrix size")
plt.grid(True)

plt.axhline(y = 100000000000, xmin=0.001, xmax=0.99, color="black", ls="--")

plt.savefig("graphic_inv_caso_1_double.png" , bbox_inches = "tight")

plt.show()