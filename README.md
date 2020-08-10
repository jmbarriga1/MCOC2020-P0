# MCOC2020-P0

# Mi Computador
# Mi computador principal
* Marca/modelo:  300E5EV/300E4EV/270E5EV/270
* Tipo: Notebook
* Año adquisición: 2013
* Procesador:
  * Marca/Modelo: Intel(R) Core(TM) i3-3120M
  * Velocidad Base: 2.50 GHz
  * Velocidad Maxima: 2.5 GHz
  * Numero de núcleos: 2
  * Numero de hilos: 4
  * Arquitectura: Sistema operativo de 64 bits, procesador x64
  * Instrucciones: MMX, SSE, SSE2, SSE3, SSE4.1, SSE4.2, EM64T, VT-x, AVX
* Tamaño de las caches del procesador:
  * L1d: 2 x 32 KB
  * L1i: 2 x 32 KB
  * L2: 2 x 256 KB
  * L3: 3 MB
* Memoria
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad 798.1 MHz
  * Numero de (SO)
* Tarjeta Grafica:
  * Marca/Modelo: Intel HD Graphics 4000
  * Memoria dedicada: 1760 MB
  * Resolución: 1366 x 768
* Disco 0:
  * Marca: Toshiba
  * Tipo: HDD
  * Tamaño: 500 GB
  * Participaciones: 1 
  * Sistema de archivos: NTFS


* Direccion MAC de la tarjeta wifi: 18:67:BO:8D:C2:3E
* Direccion IP (Interna, del router): 192.168.0.57
* Dirección IP (Externa, del ISP): 190.44.145.153
* Proveedor internet: VTR Banda Ancha S.A.

* Procesador Intel(R) Core(TM) i3-3120M CPU @ 2.50GHz
* Numero de nucleos: 2
* Numero de hilos: 4
* Memoria: 8 GB DDR3
* 1 disco duro

# Desempeño MATMUL
![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic.png?raw=true)
* ¿Como difiere del gráfico del profesor/ayudante?
 * Mi grafico se diferencia al del profesor/ayudante  en que el tiempo en multiplicar las matrices de mi computador es significativamente menor al del profesor/ayudante, tambien se pude apreciar en el grafico de memory vs matrix size que la curva es lineal y muy parecida a la del grafico del profesor/ayudante.
 
* ¿A qué se pueden deber las diferencias?
 * Las diferencias se deben a que los porcesadores son diferentes.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
 * Esto se debe a que el tamaño de matriz y el uso de la cantidad de memoria es una función lineal, en cambio el tiempo de demora se da por la multiplicacion de matrices lo cual no es lineal.
 
 * ¿Qué versión de python está usando?
  * Se esta utilizando la version 3.8.
 
 * ¿Qué versión de numpy está usando?
  * Se esta utilizando la version 1.18.5
 
 * Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida     para confirmar.
  * Se utilizaron los 2 nucleos y 4 hilos que posee el procesador.
  ![alt text](link?raw=true)
  
