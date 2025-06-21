#include <stdio.h>

void test_cache (double *a, double *b, int N)
{   
    // En este código, el bucle recorre ambas matrices a y b en el mismo ciclo.
    // El bucle va accediendo a b[i] y luego a a[i] en la misma iteración.
    
    // Localidad temporal: El procesador accede a b[i] y luego a a[i] en la misma iteración.
    // Sin embargo, como se accede a dos matrices diferentes, es probable que los datos
    // de una matriz sobrescriban los de la otra en la caché, lo que provoca fallos de caché.
    // El procesador accede a la memoria principal para obtener los valores de las matrices
    // cada vez que no están en caché.

    // Localidad espacial: El acceso a dos matrices diferentes interfiere con la localidad espacial.
    // Los elementos consecutivos de a y b pueden no estar en bloques de caché contiguos, 
    // lo que hace que el procesador tenga que acceder a la memoria principal más veces
    // en lugar de aprovechar la proximidad de los datos en la caché.

    // Por lo tanto, el acceso a ambas matrices en un solo ciclo no es eficiente para la caché
    // y hace que el programa sea más lento debido a más fallos de caché.
    
    for (int i = 0; i < N; i++) {
        b[i] = b[i] + 1;  // Modificación de la matriz b
        a[i] = a[i] + 1;  // Modificación de la matriz a
    }
}

void test_cache2 (double *a, double *b, int N)
{   
    // En este código, los bucles están separados para acceder primero a la matriz b
    // y luego a la matriz a en un bucle separado. Esto mejora el uso de la memoria caché.
    
    // Localidad temporal: Debido a que el procesador accede a b[i] para todos los elementos de b primero,
    // los datos de b permanecen en la caché durante todo el primer bucle, lo que reduce los fallos de caché.
    // Luego, los datos de a permanecen en la caché durante todo el segundo bucle.
    // Este acceso secuencial es eficiente porque mantiene los datos en la caché durante más tiempo.

    // Localidad espacial: Cuando se accede a b[i] secuencialmente, los elementos consecutivos de b
    // están cerca en la memoria y es más probable que estén en la misma línea de caché, lo que mejora el rendimiento.
    // Lo mismo ocurre para a[i] en el segundo bucle. Al acceder a una sola matriz en cada bucle, aprovechamos
    // la proximidad de los datos en memoria, lo que es más eficiente para la caché.
    
    // Este tipo de acceso optimiza el uso de la caché y minimiza los accesos a la memoria principal,
    // mejorando el rendimiento en comparación con el primer código.

    for (int i = 0; i < N; i++) {
        b[i] = b[i] + 1;  // Modificación de la matriz b en el primer bucle
    }

    for (int i = 0; i < N; i++) {
        a[i] = a[i] + 1;  // Modificación de la matriz a en el segundo bucle
    }
}
