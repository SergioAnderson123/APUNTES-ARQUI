import time
import matplotlib.pyplot as plt

# Medir el tiempo de ejecución para Python
def medir_tiempo_python():
    entrada = [random.randint(1, 100) for _ in range(100)]  # Generamos un array de entrada aleatorio
    posiciones = generador_index(100, 1)  # Usamos el modo 1 para los índices
    resultado = [0.0] * len(entrada)

    start_time = time.time()
    suma_acumulada(entrada, resultado, posiciones)
    return time.time() - start_time

# Medir el tiempo de ejecución para C
def medir_tiempo_c():
    entrada = [random.randint(1, 100) for _ in range(100)]
    posiciones = generador_index(100, 1)
    resultado = [0.0] * len(entrada)

    start_time = time.time()
    invocar_funcion_c(entrada, resultado, posiciones)
    return time.time() - start_time

# Comparar tiempos de ejecución para diferentes tamaños de N
N_values = [100, 1000, 10000, 100000]
python_times = []
c_times = []

for N in N_values:
    python_times.append(medir_tiempo_python())
    c_times.append(medir_tiempo_c())

# Graficar resultados
plt.plot(N_values, python_times, label="Python")
plt.plot(N_values, c_times, label="C")
plt.xlabel("N (tamaño del arreglo)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.show()
