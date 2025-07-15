#include <stdio.h>
#include <math.h>

void cal_suma_inversa_c(double arr_1[], double arr_2[], int N){

    printf("arreglo 2 %lf", arr_2);
    printf("arreglo 2 %lf", arr_1);

    for(int i=0; i<N; i++){
        arr_2[i] += arr_1[i]/arr_2[i];
    }

    printf("arreglo 2 %lf", arr_2);

}

int main(){

}