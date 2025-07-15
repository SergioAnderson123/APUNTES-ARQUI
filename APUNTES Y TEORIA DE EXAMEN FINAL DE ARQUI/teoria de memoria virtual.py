import math
import numpy as np
import ctypes
import time
import matplotlib.pylab as plt

def calc_pearson(arr_X, arr_Y, N):

    sum_elem_X = 0
    for i in range(N):
        sum_elem_X += arr_X[i]
    media_X = sum_elem_X/N

    sum_elem_Y = 0
    for i in range(N):
        sum_elem_Y += arr_Y[i]
    media_Y = sum_elem_Y/N

    suma_dif_mediaX = 0.0
    for i in range(N):
        suma_dif_mediaX += pow(media_X-arr_X[i],2)
    s_x = math.sqrt(suma_dif_mediaX)

    suma_dif_mediaY = 0.0
    for i in range(N):
        suma_dif_mediaY += pow(media_Y-arr_Y[i],2)
    s_y = math.sqrt(suma_dif_mediaY)

    s_xy = 0.0
    for i in range(N):
        s_xy += (arr_X[i]-media_X)*(arr_Y[i]-media_Y)

    rxy = s_xy/(s_x*s_y)

    return rxy

if __name__ == '__main__':
    #Inciso A
    #(2.0 puntos) Implementar una función en Python que reciba los arreglos x e y y
    #calcule el coeficiente de Pearson. Deberá probar su función creando arreglos desde
    #la función principal para un tamaño de 16 elementos con tamaño de 2 bytes enteros.
    #Comparar su función con lo obtenido por la función np.corrcoef(x,y).

    """
    N = 16
    arr_X = np.random.randint(0,10,N,dtype=np.short)
    arr_Y = np.random.randint(0,10,N,dtype=np.short)

    rxy = calc_pearson(arr_X,arr_Y,N)
    rxy_np = np.corrcoef(arr_X,arr_Y)
    print("El coef pearson es:       ",rxy)
    print("El coef pearson numpy es: ",rxy_np[0,1]) 
    """
#-----------------------------------------------------------------------------------------

    #Inciso B
    #(2.0 puntos) Implementar una función en C la cual será llamada desde Python que
    #calcule el coeficiente de Pearson. Realizar el llamado a través de ctypes
    #considerando los tipos de datos mencionados en a). Validar el funcionamiento de su
    #implementación imprimiendo en el terminal el resultado de su inciso en a) y lo
    #obtenido por la función np.corrcoef() y adjuntarlo en su reporte.

    """
    N = 16
    arr_X = np.random.randint(0,10,N,dtype=np.short)
    arr_Y = np.random.randint(0,10,N,dtype=np.short)

    rxy = calc_pearson(arr_X,arr_Y,N)
    rxy_np = np.corrcoef(arr_X,arr_Y)
    print("El coef pearson es:       ",rxy)
    print("El coef pearson numpy es: ",rxy_np[0,1]) 

    #generar (.so) "gcc -FPIC -shared coef_pearson.c -o coef_pearson.so"

    lib = ctypes.CDLL('./coef_pearson.so')

    lib.coef_pearson.argtypes = [np.ctypeslib.ndpointer(dtype=np.short),
                                 np.ctypeslib.ndpointer(dtype=np.short),
                                 ctypes.c_int]
    
    lib.coef_pearson.restype = ctypes.c_double

    rxy_c = lib.coef_pearson(arr_X,arr_Y,N)
    print("El coef pearson de C es:  ", rxy_c)   
    """

#----------------------------------------------------------------------------------------

    #Inciso C
    #(1.0 puntos) Generar un diferente archivo de sistema utilizando un optimizador
    #diferente al que se genera por default para su función en C. Realizar el llamado a
    #través de ctypes considerando los tipos de datos mencionados en a). Validar el
    #funcionamiento de su implementación imprimiendo en el terminal el resultado de su
    #inciso en a), en b) y lo obtenido por la función np.corrcoef()

    #Comandos para generar optimisador diferente
    #gcc -c coef_pearson.c (creacion de coef_pearson.o)
    #gcc -shared coef_pearson.o -o2 coef_pearson.so

#----------------------------------------------------------------------------------------

    #Inciso D
    #(2.0 puntos) Realizar un análisis temporal acerca de las funciones utilizando
    #diferentes tamaños del arreglo. Considerar que el tamaño N debe ser de 2^8, 2^10,
    #2^12, 2^16, 2^18 y 2^20. Debe generar una gráfica considerando el tiempo
    #representativo de cada función.

    NN = [2**8, 2**10, 2**12, 2**16, 2**18, 2**20]

    lib = ctypes.CDLL('./coef_pearson.so')

    lib.coef_pearson.argtypes = [np.ctypeslib.ndpointer(dtype=np.short),
                                 np.ctypeslib.ndpointer(dtype=np.short),
                                 ctypes.c_int]  

    lib.coef_pearson.restype = ctypes.c_double  

    time_py = []
    time_np = []
    time_c = []

    for N in NN:

        arr_X = np.random.randint(0,10,N,dtype=np.short)
        arr_Y = np.random.randint(0,10,N,dtype=np.short)

        tic = time.perf_counter()
        rxy = calc_pearson(arr_X,arr_Y,N)
        toc = time.perf_counter()
        time_py.append(toc-tic)

        tic = time.perf_counter()
        rxy_np = np.corrcoef(arr_X,arr_Y)
        toc = time.perf_counter()
        time_np.append(toc-tic)

        tic = time.perf_counter()
        rxy_c = lib.coef_pearson(arr_X,arr_Y,N)
        toc = time.perf_counter()
        time_c.append(toc-tic)

    plt.plot(NN, time_py, label = 'Tiempo Py')
    plt.plot(NN, time_np, label = 'Tiempo Numpy')
    plt.plot(NN, time_c, label = 'Tiempo C')
    plt.title('Analisis temporal')
    plt.xlabel('Iteraciones')
    plt.ylabel('Tiempo')
    plt.legend()
    plt.show()

#----------------------------------------------------------------------------------------

    #Inciso E
    #(1.5 puntos) En su reporte, brindar comentarios acerca del experimento y los
    #tiempos de ejecución generados para diferentes N. Incluir comentarios acerca de los
    #tipos de dato y su relación con lo codificado en los diferentes lenguajes de
    #programación. Así mismo, comentar si esperaría que el resultado se replique al
    #utilizar diferentes tipos de dato.

    """
    Python puro es el más lento por su naturaleza interpretada.
    NumPy es más rápido gracias a operaciones vectorizadas en C.
    C es el más eficiente por estar compilado directamente y optimizar el uso de CPU y memoria.
    Se usaron datos tipo short/int16, lo cual permite mejor uso de memoria y caché.
    El patrón de rendimiento se mantendría con otros tipos de datos, aunque los tiempos absolutos aumentarían.
    """

#----------------------------------------------------------------------------------------

    #Inciso F
    #(1.5 puntos) Brindar comentarios en su reporte acerca de sus implementaciones y su
    #aprovechamiento de las técnicas de localidad. Comentar si bajo las características
    #de su PC es posible aprovechar la memoria caché en alguno de sus niveles.

    """
    C aprovecha muy bien la localidad espacial por los accesos secuenciales.
    La localidad temporal es baja (cada dato se usa una sola vez).
    En arreglos pequeños, el uso de cachés L1/L2 mejora el rendimiento.
    Python tiene más overhead, por lo que no aprovecha igual los niveles de caché.
    """

#----------------------------------------------------------------------------------------
