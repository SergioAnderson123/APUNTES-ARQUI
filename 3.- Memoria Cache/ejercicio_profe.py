def suma_acumulada(entrada, resultado, posiciones):
    # Validación de los índices
    cantidad = len(entrada)
    for i in range(cantidad):
        # Verificar que el índice esté dentro del rango
        if posiciones[i] >= cantidad or posiciones[i] < 0:
            print(f"Índice fuera de rango: {posiciones[i]}")
            return

    # Inicializar resultado a 0
    for i in range(cantidad):
        resultado[i] = 0.0  # Inicializamos los valores de resultado a 0

    # Cálculo de la suma:
    for i in range(cantidad):
        for j in range(i + 1):  # Sumamos hasta el índice i
            resultado[i] += entrada[posiciones[j]]  # Sumamos los valores de entrada según las posiciones

# Ejemplo 1:
cantidad = 3  # Tamaño del arreglo
entrada = [0.0, 10.0, 20.0]  # Arreglo de entrada
resultado = [0.0] * cantidad  # Arreglo de resultado
posiciones = [0, 1, 2]  # Posiciones a utilizar

# Llamada a la función suma acumulada
suma_acumulada(entrada, resultado, posiciones)

# Imprimir los resultados
print("Resultados de la suma acumulada (Ejemplo 1):")
for i in range(cantidad):
    print(f"resultado[{i}] = {resultado[i]}")
