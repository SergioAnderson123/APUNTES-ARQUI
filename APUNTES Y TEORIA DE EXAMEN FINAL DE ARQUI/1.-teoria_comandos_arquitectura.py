
"""
EXAMEN PARCIAL - SEGUNDA PARTE
Archivo resumen: Teoría, comandos y práctica en Arquitectura de Computadoras.
Incluye desarrollo completo de coeficiente de correlación de Pearson (Python, C y análisis).
"""

# ---------------------------- #
# INCISO A: Implementación en Python
# ---------------------------- #
import numpy as np
import ctypes
import math
import time
import matplotlib.pyplot as plt

def calcular_Pearson(arreglo_x, arreglo_y, N):
    suma_x = 0
    sx = 0
    for i in range(N):
        suma_x += arreglo_x[i]
    prom_x = suma_x / N

    for i in range(N):
        sx += (arreglo_x[i] - prom_x) ** 2
    sx = math.sqrt(sx)

    suma_y = 0
    sy = 0
    for i in range(N):
        suma_y += arreglo_y[i]
    prom_y = suma_y / N

    for i in range(N):
        sy += (arreglo_y[i] - prom_y) ** 2
    sy = math.sqrt(sy)

    sxy = 0
    for i in range(N):
        sxy += (arreglo_x[i] - prom_x) * (arreglo_y[i] - prom_y)

    return sxy / (sx * sy)

# ---------------------------- #
# INCISO B: Implementación en C + ctypes
# ---------------------------- #
"""
Archivo C: calculo_Pearson.c

#include <math.h>
#include <stdio.h>

double calcular_Pearson_c(short *arreglo_x, short *arreglo_y, int N)
{
    double suma_x = 0;
    double sx = 0;
    double prom_x;
    for (int i = 0; i<N; i++)
        suma_x += (double)arreglo_x[i];
    prom_x = suma_x / N;

    for (int i = 0; i<N; i++)
        sx += ((double)arreglo_x[i] - prom_x) * ((double)arreglo_x[i] - prom_x);
    sx = sqrt(sx);

    double suma_y = 0;
    double sy = 0;
    double prom_y;
    for (int i = 0; i<N; i++)
        suma_y += (double)arreglo_y[i];
    prom_y = suma_y / N;

    for (int i = 0; i<N; i++)
        sy += ((double)arreglo_y[i] - prom_y) * ((double)arreglo_y[i] - prom_y);
    sy = sqrt(sy);

    double sxy = 0;
    for (int i = 0; i<N; i++)
        sxy += ((double)arreglo_x[i] - prom_x) * ((double)arreglo_y[i] - prom_y);

    return sxy / (sx * sy);
}
"""

# ---------------------------- #
# COMANDOS DE COMPILACIÓN USADOS
# ---------------------------- #
"""
gcc -fPIC -shared calculo_Pearson.c -o calculo_Pearson.so      # Versión base
gcc -fPIC -O2 -shared calculo_Pearson.c -o calculo_Pearson.so  # Versión optimizada (inciso c)
"""

# ---------------------------- #
# INCISO D: Análisis temporal
# ---------------------------- #
NN = [256, 1024, 4096, 16384, 65536, 262144, 1048576]

lib = ctypes.CDLL('./calculo_Pearson.so')
lib.calcular_Pearson_c.argtypes = [np.ctypeslib.ndpointer(dtype=np.int16),
                                   np.ctypeslib.ndpointer(dtype=np.int16),
                                   ctypes.c_int]
lib.calcular_Pearson_c.restype = ctypes.c_double

time_py = []
time_np = []
time_c = []

for N in NN:
    arr_X = np.random.randint(0, 10, N, dtype=np.int16)
    arr_Y = np.random.randint(0, 10, N, dtype=np.int16)

    tic = time.perf_counter()
    rxy = calcular_Pearson(arr_X, arr_Y, N)
    toc = time.perf_counter()
    time_py.append(toc - tic)

    tic = time.perf_counter()
    rxy_np = np.corrcoef(arr_X, arr_Y)
    toc = time.perf_counter()
    time_np.append(toc - tic)

    tic = time.perf_counter()
    rxy_c = lib.calcular_Pearson_c(arr_X, arr_Y, N)
    toc = time.perf_counter()
    time_c.append(toc - tic)

plt.plot(NN, time_py, label='Tiempo Py')
plt.plot(NN, time_np, label='Tiempo Numpy')
plt.plot(NN, time_c, label='Tiempo C')
plt.title('Analisis temporal')
plt.xlabel('Iteraciones')
plt.ylabel('Tiempo')
plt.legend()
plt.show()

# ---------------------------- #
# INCISO E: Comentario teórico
# ---------------------------- #
"""
Python puro es el más lento por su naturaleza interpretada.
NumPy es más rápido gracias a operaciones vectorizadas en C.
C es el más eficiente por estar compilado directamente y optimizar el uso de CPU y memoria.
Se usaron datos tipo short/int16, lo cual permite mejor uso de memoria y caché.
El patrón de rendimiento se mantendría con otros tipos de datos, aunque los tiempos absolutos aumentarían.
"""

# ---------------------------- #
# INCISO F: Localidad y Caché
# ---------------------------- #
"""
C aprovecha muy bien la localidad espacial por los accesos secuenciales.
La localidad temporal es baja (cada dato se usa una sola vez).
En arreglos pequeños, el uso de cachés L1/L2 mejora el rendimiento.
Python tiene más overhead, por lo que no aprovecha igual los niveles de caché.
"""
