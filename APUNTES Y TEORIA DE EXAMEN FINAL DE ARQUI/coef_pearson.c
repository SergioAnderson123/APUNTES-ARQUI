#include <stdio.h>
#include <math.h>

double coef_pearson(short arr_X[], short arr_Y[], int N){

    short suma_elementosX=0;
    for(int i=0; i<N; i++){
        suma_elementosX += arr_X[i];
    }
    double media_x = (double)suma_elementosX/(double)N;

    short suma_elementosY=0;
    for(int i=0; i<N; i++){
        suma_elementosY += arr_Y[i];
    }
    double media_y = (double)suma_elementosY/(double)N;

    double suma_dif_mediaX = 0.0;
    for(int i=0; i<N; i++){
        suma_dif_mediaX += pow(arr_X[i]-media_x,2);
    }
    double s_x = sqrt(suma_dif_mediaX);

    double suma_dif_mediaY = 0.0;
    for(int i=0; i<N; i++){
        suma_dif_mediaY += pow(arr_Y[i]-media_y,2);
    }
    double s_y = sqrt(suma_dif_mediaY);

    double s_xy = 0.0;
    for (int i=0; i<N; i++){
        s_xy += (arr_X[i]-media_x)*(arr_Y[i]-media_y);
    }
    double rxy = s_xy/(s_x*s_y);

    return rxy;
}

int main(){
    
}