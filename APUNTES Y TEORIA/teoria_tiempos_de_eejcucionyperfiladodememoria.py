"""
TEORIA DE TIEMPOS DE EJECUCION , PERFILADO DE MEMORIA :

LÍNEA BASE Y NATURALEZA DEL WORKLOAD:
- El programa secuencial (`html_fetch_sync.py`) resultó ser claramente I/O-bound.
- Promedio de ejecución: 25.4 s.
- La fase que domina el tiempo es la descarga de HTML, no el análisis de texto.

INSTRUMENTACIÓN POR ETAPAS:
- Se midieron por separado los tiempos de descarga y parsing.
- Descarga y parsing.
- La descarga domina totalmente el tiempo total del programa.

ASYNCIO Y MEJORA:
- El mayor beneficio ocurre en la fase de descarga, ya que asyncio permite concurrencia real sin bloquear el event loop.

 MULTIHILO MANUAL:

- El GIL no afecta porque el programa es I/O-bound.
- Si fuera CPU-bound, el GIL sí sería un cuello de botella.

MULTIPROCESO MANUAL:
- Cada proceso es independiente, no comparten GIL.
- El fork genera mayor overhead y uso de memoria, pero permite paralelismo real.

POOL VS GESTIÓN MANUAL:

- Multihilo manual es más rápido que ThreadPoolExecutor, pero menos escalable.
- ThreadPool ofrece menor complejidad de código y mejor control de recursos.
- En multiproceso, el uso de Pool reduce el overhead y mejora la estabilidad.
- Los pools sacrifican velocidad en favor de mantenibilidad.

PERFILADO DE MEMORIA:

- async: ~60 MiB
- threading: ~105 MiB
- thread pool: ~60 MiB
- process: ~37 MiB/proceso
- process pool: ~36 MiB/proceso
- asyncio es el más eficiente; los procesos consumen más, pero permiten paralelismo real.



- Con 2, 4, 8, 16 hilos:
  - Se mejora el tiempo hasta cierto punto.
  - El beneficio decrece a partir de 8.
  - Memoria crece de manera lineal (~49 → 61 MiB).
  - Punto óptimo entre 8–16 workers.

REINTENTOS EN ASYNCIO:
- Implementar retries no afectó el rendimiento cuando no hubo errores.
- Reintentos mejoran robustez sin penalización si no fallan URLs.



- No hay un modelo único superior. Depende de la carga:
  - I/O-bound: asyncio o threading (con o sin pool).
  - CPU-bound: multiprocessing (mejor con pool).
- Pools mejoran mantenibilidad y uso de memoria.
- El GIL limita hilos solo en CPU-bound.
- Retry, escalabilidad, y profiling son claves en sistemas robustos.

"""
