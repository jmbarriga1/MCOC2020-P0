# MCOC2020-P0

# Mi Computador
# Mi computador principal
* Marca/modelo:  SAMSUNG 300E5EV/300E4EV/270E5EV/270
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
  * Mi grafico se diferencia al del profesor/ayudante  en que posee distintos peaks que el del profesor/ayudante, tambien se pude apreciar en el grafico de memory vs matrix size que la curva es lineal y muy parecida a la del grafico del profesor/ayudante.La maxima matriz que se logro hacer fue de 3000X3000.
 
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
  ![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/Uso_procesador_Desempe%C3%B1o_MATMUL.png?raw=true)
  
  # Desempeño MIMATMUL
  
  ![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphicmimatmul.png?raw=true)
  
* ¿Como difiere del gráfico del profesor/ayudante?
  * Mi grafico se diferencia al del profesor/ayudante  en que el tiempo va en aumento en distinta proporcion al del profesor/ayudante, tambien se pude apreciar en el grafico de memory vs matrix size que la curva es lineal y muy parecida a la del grafico del profesor/ayudante. La maxima matriz que se logro hacer fue de 250X250.

* ¿A qué se pueden deber las diferencias?
  * Las diferencias se deben a que los porcesadores son diferentes y a su vez que al utilizar la funcion creada el procesador hace un mayor esfuerzo por hacer las iteraciones.
  
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  * Esto se debe a que el tamaño de matriz y el uso de la cantidad de memoria es una función lineal, en cambio el tiempo de demora se da por la multiplicacion de matrices lo cual no es lineal.

* ¿Qué versión de python está usando?
   * Se esta utilizando la version 3.8.
  
* ¿Qué versión de numpy está usando?
   * Se esta utilizando la version 1.18.5

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida     para confirmar.
   * Se utilizaron los 2 nucleos y 4 hilos que posee el procesador.
![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/Uso_procesador_Desempe%C3%B1o_MIMATMUL.png?raw=true)

# Desempeño de INV

# Caso 1: numpy.linalg.inv()

* np.half 

-ERROR: ARRAY TYPE FLOAT16 UNSUPPORTED IN LINALG

* np.single

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_1_single.png?raw=true)

* np.double

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_1_double.png?raw=true)

* np.longdouble

-ERROR: ARRAY TYPE FLOAT16 UNSUPPORTED IN LINALG

# Caso 2: scipy.linalg.inv(overwrite_a=False)

* np.half 

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_2_half.png?raw=true)

* np.single

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_2_single.png?raw=true)

* np.double

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_2_double.png?raw=true)

* np.longdouble

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_2_longdouble.png?raw=true)

# Caso 3: scipy.linalg.inv(overwrite_a=True)

* np.half 

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_3_half.png?raw=true)

* np.single

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_3_single.png?raw=true)

* np.double

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_3_double.png?raw=true)

* np.longdouble

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/graphic_inv_caso_3_longdouble.png?raw=true)

* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
  * Segu lo investigado se utiliza la solución analítica, de la regla de Cramer y teorema de Laplace, que basa el calculo del determinante de matrices grandes en la descomposición de sumas de matrices más pequeñas para llegar al resultado esperado.

* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? (Ver clase 10 Agosto)
  * El paralelismo y la estructura de cache de mi procesador incide en la cantidad de tiempo que demora en hacer las operaciones, también hay que tener en cuenta los tipos de datos y el lenguaje para el desempeño del procesador. Por lo tanto si se esta dispuesto a perder precisión hay que disminuir la memoria, si se tiene un gran problema hay que evaluar utilizar tipos de datos mas chicos.
Hay que tener en cuenta el hardware para el rendimiento del procesador, ya que es el problema principal de que se demore mas tiempo en resolver lo que se le pide.
En primer lugar lo mas lento es un disco duro, luego mas rápido es un disco SSD y lo mas rápido es la memoria RAM. Cuando se excede la memoria RAM el computador quiere seguir trabajando por lo que va haciendo paginación, se refiere a que se hagarran pedasos de memoria para trabajar sobre la memoria que se utilizo.	
En mi caso se produce esto por lo que me veo obligado a hacer operaciones mas pequeñas por el tiempo que se demora en resolverlas.

# Entrega 6

![alt text](https://github.com/jmbarriga1/MCOC2020-P0/blob/master/Entrega%206/Performance%20graphic%20Entrega%206.png?raw=true)

* En el grafico  arrojado por la programación hecha se puede apreciar que la performance hasta matrices de 30X30 fue mejor y mas eficiente en el caso de "Numpy Solve" y "Scipy Solve pos". Luego el tiempo de demora con el modulo de "Scipy Solve pos" va en aumento hasta llegar a ser el modulo que mas demora en resolverce cuando la matriz es de 4000X4000 y aumentando.
Se puede apreciar que el metodo mas eficiente para realizar la inversion de matrices es de "Numpy Solve" y el menos eficiente termina siendo el de "Scipy Solve pos".
Tambien se puede ver que la performance de "Scipy Solve", "Scipy Solve symmetric" y "Scipy Solve pos overwrite" son bastante similares hasta las matrices de 100X100, luego de esto "Scipy Solve symmetric" comienza a tener menor eficiencia y "Scipy Solve pos overwrite" tene mejor eficiencia que los demas modos, en el caso de "Scipy Solve pos overwrite" tiene una peor eficiencia en un comienzo debido a que invierte tiempo en hacer análisis para matrices  pequeñas y eso le retrasa los calculos, ya que analiza la simetria y positividad, esto a raiz que la matriz es mas grande comienza a optimizar los calculos lo que alfinal lo hace mas eficiente.
