from multiprocessing import Process
import requests
from PIL import Image
from io import BytesIO
from time import perf_counter
from statistics import mean, median, stdev

urls = [
    'https://picsum.photos/200/300',
    'https://picsum.photos/300/300',
    'https://picsum.photos/400/300',
]

def process_task(url, i):
    r = requests.get(url)
    img = Image.open(BytesIO(r.content))
    img = img.convert("L")
    img.save(f"imagen_proc_{i}.jpg")

def multiprocessing_version():
    procesos = []
    for i, url in enumerate(urls):
        p = Process(target=process_task, args=(url, i))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()

if __name__ == '__main__':
    
    tiempos = [ ]
    
    for i in range(5):

        inicio = time.perf_counter()
        download_all_sites(sites)
        fin = time.perf_counter()
        duracion = fin - inicio
        print(f"Iteración {i+1}: {duracion:.2f} segundos")
        tiempos.append( duracion )
        
    promedio = sum(tiempos) / len (tiempos)
    mediana = statistics.median(tiempos)
    desviacion = statistics.stdev(tiempos)
    speedup = 11.32841420279999 / promedio

    print("\n Resultados Síncrono:")
    print(f"→ Promedio: {promedio} segundos")
    print(f"→ Mediana : {mediana} segundos")
    print(f"→ Desviación estándar: {desviacion} segundos")
