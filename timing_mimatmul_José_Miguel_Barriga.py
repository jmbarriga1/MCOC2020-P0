# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:42:49 2020

@author: MiguelB
"""

from scipy import rand
from time import perf_counter
from matplotlib import pyplot as plt
from mimatmul import mimatmul

Na = [3, 5, 10, 15, 20, 30, 40, 50, 60, 75, 100, 125, 150, 175, 250]#, 400, 600, 800, 1000, 2000, 3000]

      
N_corridas = 10


time = []


for i in range(N_corridas):
    memory = []    
    text = (f"matmul{i}.txt")
    fid = open(text,"w")
    element = []

    for N in Na:
        print(f"N = {N}")
        A = rand(N, N)
        B = rand(N, N)
       
        t1 = perf_counter()
        C = mimatmul(A, B)
        t2 = perf_counter()
        dt = t2 - t1
        mem = 3*(N**2)*8
        
        element.append(dt)
        memory.append(mem)
        print(f"time = {dt} s")
        print(f"memory = {mem} bytes")
        print(" ")
        fid.write(f"{N} {dt} {mem}\n")
    time.append(element)
            
    fid.close()

x = [10 , 20 , 50 , 100 , 200 , 500 , 1000 , 2000 , 5000 , 10000, 20000] 
xticks_txt = ["", "", "", "", "", "", "", "", "", "", ""]



y = [0.1e-3, 1e-3, 1e-2, 0.1, 1., 10., 60, 600, 3600]
yticks_txt = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min", "1 h"] 


plt.figure()
plt.subplot(2, 1, 1)

for i in range(N_corridas):
    text = (f"matmul{i}.txt")
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
plt.title("performance A@B")
plt.grid()

xticks_txt1 = ["10", "20", "50", "100", "200", "500", "1000", "2000", "5000", "10000"]
y1 = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11]
yticks_txt1 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]

plt.subplot(2, 1, 2)
plt.loglog(Na , memory , "-o")
plt.xticks(x, xticks_txt1, rotation = 45)
plt.yticks(y1, yticks_txt1)
plt.ylabel("memory")
plt.xlabel("matrix size")
plt.grid()

plt.axhline(y = 100000000000, xmin=0.001, xmax=0.99, color="black", ls="--")

plt.savefig("graphicmimatmul.png" , bbox_inches = "tight")

plt.show()
