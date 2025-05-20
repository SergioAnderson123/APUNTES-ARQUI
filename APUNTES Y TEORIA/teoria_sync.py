import requests
from PIL import Image
from io import BytesIO
from time import perf_counter
from statistics import mean, median, stdev
import time
import statistics

urls = [
    'https://picsum.photos/200/300',
    'https://picsum.photos/300/300',
    'https://picsum.photos/400/300',
]

def sync_version():
    for i, url in enumerate(urls):
        r = requests.get(url)
        img = Image.open(BytesIO(r.content))
        img = img.convert("L")
        img.save(f"imagen_sync_{i}.jpg")

if __name__ == '__main__':
    
    tiempos = [ ]
    
    for i in range(5):

        inicio = time.perf_counter()
        download_all_sites(sites)
        fin = time.perf_counter()
        duracion = fin - inicio
        tiempos.append( duracion )
        
    promedio = sum(tiempos) / len (tiempos)
    mediana = statistics.median(tiempos)
    desviacion = statistics.stdev(tiempos)

    print("\n Resultados Síncrono:")
    print(f"→ Promedio: {promedio} segundos")
    print(f"→ Mediana : {mediana} segundos")
    print(f"→ Desviación estándar: {desviacion} segundos")
