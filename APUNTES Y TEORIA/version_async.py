import asyncio
import aiohttp
import aiofiles
from PIL import Image
from io import BytesIO
from time import perf_counter
from statistics import mean, median, stdev

urls = [
    'https://picsum.photos/200/300',
    'https://picsum.photos/300/300',
    'https://picsum.photos/400/300',
]

async def download_and_process(session, url, i):
    async with session.get(url) as resp:
        data = await resp.read()
        img = Image.open(BytesIO(data))
        img = img.convert("L")
        async with aiofiles.open(f"imagen_async_{i}.jpg", 'wb') as f:
            img.save(f)

async def async_version():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(download_and_process(session, url, i) for i, url in enumerate(urls)))

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