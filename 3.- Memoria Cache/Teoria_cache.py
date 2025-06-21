# Cálculo de la dirección de memoria en función del tamaño de la RAM

# Paso 1: Determinar el número total de bits de dirección

# El número total de bits de dirección depende del tamaño de la memoria RAM.
# Si tenemos una memoria RAM de tamaño M bytes, el número total de bits de dirección es:
# Bits de dirección = log2(Tamaño de RAM en bytes)

# Ejemplo: 
# Si la memoria RAM tiene 4 GB, que equivale a 4 * 1024^3 bytes,
# entonces calculamos los bits de dirección de la siguiente manera:
# Bits de dirección = log2(4 * 1024^3) = log2(4294967296) = 32 bits
# Por lo tanto, para una RAM de 4 GB se necesitan 32 bits para representar las direcciones de memoria.

# Paso 2: Cálculo del formato de bits en los tres tipos de mapeo de caché

# 1. Mapeo Directo
# En este tipo de mapeo, cada bloque de memoria tiene un único lugar donde puede ser mapeado en la caché.
# La dirección se divide en tres partes:
# | Etiqueta (Tag) | Índice de caché (Índice de bloque) | Desplazamiento (Offset) |
#
# Para calcular el formato de bits en mapeo directo:
# - Desplazamiento (Bits de bloque) = log2(Tamaño del bloque)
# - Índice (Líneas de caché) = log2(Número de líneas en la caché)
# - Etiqueta = Bits de dirección - Índice - Desplazamiento

# 2. Mapeo Totalmente Asociativo
# En el mapeo totalmente asociativo, un bloque de memoria puede ir en cualquier línea de la caché.
# La dirección se divide en dos partes:
# | Etiqueta (Tag) | Desplazamiento (Offset) |
#
# Para calcular el formato de bits:
# - Desplazamiento (Bits de bloque) = log2(Tamaño del bloque)
# - Etiqueta = Bits de dirección - Desplazamiento

# 3. Mapeo por N Vías (Asociativo por Conjunto)


# En el mapeo por N vías, los bloques de memoria se asignan a un conjunto específico, pero pueden ir en cualquier línea de ese conjunto.

# Aqui primero se fija en el numero de bits que se necesita y despues en el desplazamiento que es el numero de bits de bloue que se ncesitan.

# La dirección se divide en tres partes:
# | Etiqueta (Tag) | Índice de conjunto | Desplazamiento (Offset) |
#
# Para calcular el formato de bits:
# - Desplazamiento (Bits de bloque) = log2(Tamaño del bloque)
# - Índice de conjunto = log2(Número de conjuntos)
# - Etiqueta = Bits de dirección - Índice de conjunto - Desplazamiento

# Ejemplo práctico:

# Supón que tienes una memoria RAM de 4 GB y una caché de 1 KB con bloques de 16 bytes y 2 vías (N vías).

# Paso 1: Cálculo de los bits de dirección:
# - Tamaño de la RAM = 4 GB = 4 * 1024^3 bytes
# - Bits de dirección = log2(4 * 1024^3) = 32 bits

# Paso 2: Cálculo para el mapeo directo:
# - Desplazamiento = log2(16) = 4 bits
# - Líneas de caché = 1024 / 16 = 64 → Índice = log2(64) = 6 bits
# - Etiqueta = 32 - 6 - 4 = 22 bits

# Paso 3: Cálculo para el mapeo totalmente asociativo:
# - Desplazamiento = 4 bits
# - Etiqueta = 32 - 4 = 28 bits

# Paso 4: Cálculo para el mapeo por 2 vías:
# - Número de conjuntos = (1024) / (16 * 2) = 32 → Índice de conjunto = log2(32) = 5 bits
# - Desplazamiento = 4 bits
# - Etiqueta = 32 - 5 - 4 = 23 bits