import math
import numpy as np
import ctypes
import time
import matplotlib.pylab as plt


def cal_suma_inversa(arr_1, arr_2, N):

    for i in range(N):
        arr_2[i] += arr_1[i]/arr_2[i]

if __name__ == '__main__':

    #Inciso A
    """
    N = 16
    arr_1 = np.random.rand(N)
    arr_2 = np.random.rand(N)

    print("Valores del arreglo 1: ", arr_1)
    print("Valores del arreglo 2: ", arr_2)

    cal_suma_inversa(arr_1,arr_2,N)

    print("Valores del nuevo arreglo 2: ", arr_2)
    
    """
 
    #Inciso B
    N = 16
    arr_1 = np.random.rand(N)
    arr_2 = np.random.rand(N)

    print("Valores del arreglo 1: ", arr_1)
    print("Valores del arreglo 2: ", arr_2)

    arr_2_c = arr_2.copy()

    cal_suma_inversa(arr_1,arr_2,N)

    print("Valores del nuevo arreglo 2: ", arr_2)

    #generar (.so) "gcc -FPIC -shared suma.c -o suma.so"

    lib = ctypes.CDLL('./suma.so')

    lib.cal_suma_inversa_c.argtypes = [np.ctypeslib.ndpointer(dtype=np.double),
                                       np.ctypeslib.ndpointer(dtype=np.double),
                                       ctypes.c_int]

    lib.cal_suma_inversa_c(arr_1,arr_2_c,N)
    print("Valor de arr_2 con c:  ", arr_2_c)  