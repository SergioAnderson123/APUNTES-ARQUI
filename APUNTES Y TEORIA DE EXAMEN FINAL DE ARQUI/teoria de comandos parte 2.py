
"""
EXAMENES PROPUESTOS – FUNCIONES MATEMÁTICAS CON PYTHON + C

Este archivo contiene el desarrollo completo de ejercicios estilo "coeficiente de Pearson",
inspirado en el examen original. Incluye:

- Teoría y fórmulas de referencia
- Implementación en Python (slow/fast)
- Preparación para implementación en C
- Enlace con ctypes
- Análisis temporal y gráfico
"""

import numpy as np
import ctypes
import math
import time
import matplotlib.pyplot as plt

# ==========================================================
# EJERCICIO 1: RAÍZ CUADRÁTICA MEDIA (RMS)
# ==========================================================

"""
Fórmula:
    RMS = sqrt( (1/N) * sum(x_i^2) )

Objetivo:
- Implementar en Python
- Crear versión en C
- Comparar con numpy.sqrt(mean(x**2))
"""

def py_rms(x, N):
    suma = 0
    for i in range(N):
        suma += x[i]**2
    return math.sqrt(suma / N)

# ----------------------------------------------------------
# C para RMS:
"""
double rms(double *x, int N) {
    double suma = 0;
    for (int i = 0; i < N; i++) {
        suma += x[i] * x[i];
    }
    return sqrt(suma / N);
}
"""
# ----------------------------------------------------------

# ==========================================================
# EJERCICIO 2: VARIANZA
# ==========================================================

"""
Fórmula:
    Var = (1/N) * sum((x_i - x̄)^2)

Implementar en Python puro. Luego comparar con numpy.var()
"""

def py_varianza(x, N):
    prom = sum(x) / N
    suma = 0
    for i in range(N):
        suma += (x[i] - prom) ** 2
    return suma / N

# ==========================================================
# EJERCICIO 3: ln(1 + x) CON SERIE DE TAYLOR
# ==========================================================

"""
Serie:
    ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ...

1. Función lenta usando potencia y división explícita.
2. Función rápida usando recurrencia entre términos.
3. Comparar con math.log1p(x)
"""

def py_ln_slow(x, n_terms):
    suma = 0
    for i in range(1, n_terms + 1):
        suma += ((-1) ** (i + 1)) * (x ** i) / i
    return suma

def py_ln_fast(x, n_terms):
    term = x
    suma = x
    for i in range(2, n_terms + 1):
        term *= -x * (i - 1) / i
        suma += term
    return suma

# ----------------------------------------------------------
# C para ln(1 + x) fast:
"""
double ln_fast(double x, int n_terms) {
    double term = x, suma = x;
    for (int i = 2; i <= n_terms; i++) {
        term *= -x * (i - 1.0) / i;
        suma += term;
    }
    return suma;
}
"""
# ----------------------------------------------------------

# ==========================================================
# COMANDOS DE COMPILACIÓN C
# ==========================================================
"""
gcc -c funciones.c               # Crear archivo objeto
gcc -shared funciones.o -o funciones.so   # Crear shared library

# En Python:
lib = ctypes.CDLL('./funciones.so')
lib.rms.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]
lib.rms.restype = ctypes.c_double
"""

# ==========================================================
# BENCHMARK DE TIEMPOS
# ==========================================================

NN = [256, 1024, 4096, 16384, 65536, 262144]

def benchmark(f, gen, label):
    resultados = []
    for N in NN:
        datos = gen(N)
        tic = time.perf_counter()
        f(datos, N)
        toc = time.perf_counter()
        resultados.append(toc - tic)
    return resultados

if __name__ == "__main__":
    # RMS
    tiempos_rms = benchmark(py_rms, lambda N: np.random.rand(N), "RMS")

    # Varianza
    tiempos_var = benchmark(py_varianza, lambda N: np.random.rand(N), "Varianza")

    # ln(1 + x)
    tiempos_ln = []
    for N in NN:
        x = np.random.uniform(0, 1)
        tic = time.perf_counter()
        py_ln_fast(x, 100)
        toc = time.perf_counter()
        tiempos_ln.append(toc - tic)

    # Gráfica
    plt.plot(NN, tiempos_rms, label="RMS (Python)")
    plt.plot(NN, tiempos_var, label="Varianza (Python)")
    plt.plot(NN, tiempos_ln, label="ln(1+x) fast (Python)")
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo [s]")
    plt.title("Benchmark de funciones matemáticas")
    plt.grid(True)
    plt.legend()
    plt.show()
