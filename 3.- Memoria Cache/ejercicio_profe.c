#include <stdio.h>

void suma_acumulada(double *entrada, double *resultado, int *posiciones, int cantidad) {
    // Validación de los índices
    for (int i = 0; i < cantidad; i++) {
        // Verificar que el índice esté dentro del rango
        if (posiciones[i] >= cantidad || posiciones[i] < 0) {
            printf("Índice fuera de rango: %d\n", posiciones[i]);
            return;
        }
    }

    // Inicializar resultado a 0
    for (int i = 0; i < cantidad; i++) {
        resultado[i] = 0.0;  // Inicializamos los valores de resultado a 0
    }

    // Cálculo de la suma acumulada
    for (int i = 0; i < cantidad; i++) {
        for (int j = 0; j <= i; j++) {
            resultado[i] += entrada[posiciones[j]];  // Sumamos los valores de entrada según las posiciones
        }
    }
}

int main() {
    // Ejemplo 1:
    int cantidad = 3;  // Tamaño del arreglo
    // Arreglo de entrada
    double entrada[] = {0.0, 10.0, 20.0};  // Arreglo de entrada
    double resultado[cantidad];  // Arreglo de resultado
    // Posiciones a utilizar
    int posiciones[] = {0, 1, 2};  // Posiciones

    // Llamada a la función suma acumulada
    suma_acumulada(entrada, resultado, posiciones, cantidad);

    // Imprimir los resultados
    printf("Resultados de la suma acumulada (Ejemplo 1):\n");
    for (int i = 0; i < cantidad; i++) {
        printf("resultado[%d] = %f\n", i, resultado[i]);
    }

    return 0;
}


//entrada en vez de array_input (representa los datos de entrada).

//resultado en vez de array_output (almacena la suma acumulada).

//posiciones en vez de index (indica las posiciones de entrada[] que se deben sumar).

//cantidad en vez de N (es más descriptivo del tamaño del arreglo).