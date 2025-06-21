import ctypes

def invocar_funcion_c(entrada, resultado, posiciones):
    # Cargar la biblioteca C
    lib = ctypes.CDLL('./libfunc.so')
    
    # Definir la firma de la función C
    lib.suma_acumulada.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    lib.suma_acumulada.restype = None
    
    # Convertir los arreglos de Python a tipos de ctypes
    entrada_ctypes = (ctypes.c_double * len(entrada))(*entrada)
    posiciones_ctypes = (ctypes.c_int * len(posiciones))(*posiciones)
    resultado_ctypes = (ctypes.c_double * len(resultado))(*resultado)
    
    # Llamar a la función suma_acumulada
    lib.suma_acumulada(entrada_ctypes, resultado_ctypes, posiciones_ctypes, len(entrada))

    # Mostrar el resultado
    for i in range(len(entrada)):
        print(f"resultado[{i}] = {resultado_ctypes[i]}")

# Ejemplo de prueba
entrada = [0.0, 10.0, 20.0]
posiciones = [0, 1, 2]
resultado = [0.0] * len(entrada)

# Invocar la función C
invocar_funcion_c(entrada, resultado, posiciones)
