import random

def generador_index(N, modo):
    if modo == 1:
        # Modo 1: Lista ordenada secuencialmente
        return list(range(N))
    elif modo == 2:
        # Modo 2: Lista aleatoria sin repeticiones
        return random.sample(range(N), N)
    else:
        print("Modo no válido")
        return []

# Ejemplo de prueba
N = 20
modo1 = 1
modo2 = 2

# Generar listas
lista_modo1 = generador_index(N, modo1)
lista_modo2 = generador_index(N, modo2)

print(f"Lista generada en modo 1: {lista_modo1}")
print(f"Lista generada en modo 2: {lista_modo2}")
