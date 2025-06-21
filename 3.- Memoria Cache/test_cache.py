import ctypes
import numpy as np
import time
import matplotlib.pyplot as plt
import statistics

if __name__ == '__main__':

    # Cargamos la librería compartida escrita en C
    lib = ctypes.CDLL('./lib_cache.so')

    # Configuramos los tipos de los argumentos que se pasarán a las funciones C
    lib.test_cache.argtypes = [np.ctypeslib.ndpointer(dtype=np.double), np.ctypeslib.ndpointer(dtype=np.double), ctypes.c_int32]
    lib.test_cache2.argtypes = [np.ctypeslib.ndpointer(dtype=np.double), np.ctypeslib.ndpointer(dtype=np.double), ctypes.c_int32]

    # Lista de diferentes tamaños de matrices (N) que vamos a probar
    Num = [64, 256, 512, 1024, 1024*16, 1024*1024*16]

    # Número de iteraciones para medir el rendimiento
    iteraciones = 30

    # Inicializamos las listas donde guardaremos los tiempos de ejecución
    lista1 = []  # Para los tiempos de test_cache
    lista2 = []  # Para los tiempos de test_cache2

    # Recorremos los diferentes tamaños de matrices (N)
    for N in Num:
        # Generamos arreglos aleatorios para las matrices a y b
        a1 = np.random.rand(N).astype(np.double)
        b1 = np.random.rand(N).astype(np.double)
        a2 = np.random.rand(N).astype(np.double)
        b2 = np.random.rand(N).astype(np.double)

        # Listas para almacenar los tiempos de cada iteración
        lista_in_1 = []
        lista_in_2 = []

        # Realizamos las iteraciones para medir el tiempo de ejecución
        for _ in range(iteraciones):
            # Medimos el tiempo de ejecución de la primera función (test_cache)
            t1 = time.perf_counter()  # Marcamos el tiempo de inicio
            lib.test_cache(a1, b1, N)  # Llamamos a la función C
            t1_out = time.perf_counter()  # Marcamos el tiempo de finalización
            lista_in_1.append(t1_out - t1)  # Almacenamos el tiempo de esta iteración

            # Medimos el tiempo de ejecución de la segunda función (test_cache2)
            t2 = time.perf_counter()  # Marcamos el tiempo de inicio
            lib.test_cache2(a2, b2, N)  # Llamamos a la segunda función C
            t2_out = time.perf_counter()  # Marcamos el tiempo de finalización
            lista_in_2.append(t2_out - t2)  # Almacenamos el tiempo de esta iteración

        # Calculamos la mediana de los tiempos de las iteraciones para cada función
        lista1.append(statistics.median(lista_in_1))  # Mediana de los tiempos para test_cache
        lista2.append(statistics.median(lista_in_2))  # Mediana de los tiempos para test_cache2

    # Graficamos los tiempos de ejecución
    plt.plot(Num, lista1, 'r')  # Tiempos para la primera función (rojo)
    plt.plot(Num, lista2, 'g')  # Tiempos para la segunda función (verde)
    plt.grid()  # Añadimos una cuadrícula para hacer el gráfico más legible
    plt.legend({'Primera funcion', 'Segunda funcion'})  # Leyenda para las líneas
    plt.xlabel("Valor de N")  # Etiqueta para el eje X
    plt.ylabel("Tiempo")  # Etiqueta para el eje Y
    plt.show()  # Mostramos el gráfico
