"""
TEORÍA CONSOLIDADA - CONCURRENCIA Y RENDIMIENTO EN PYTHON (1IEE06 - Sergio)

────────────────────────────────────────────────────────────
1. CLASIFICACIÓN DE TAREAS: I/O-BOUND, CPU-BOUND Y MIXTAS
────────────────────────────────────────────────────────────
- I/O-BOUND: tareas que pasan la mayor parte del tiempo esperando entrada/salida (red, disco, archivos).
  Ej: leer archivos, descargar imágenes, hacer peticiones HTTP.
  Recomendado: asyncio o threading.

- CPU-BOUND: tareas que consumen intensamente el procesador sin pausas.
  Ej: cálculos matemáticos, procesamiento de imágenes, compresión.
  Recomendado: multiprocessing (procesos separados).

- MIXTO: combinación de ambos. Ej: descargar imágenes y procesarlas con PIL.

──────────────────────────────
2. ASYNCIO - Concurrencia asincrónica
──────────────────────────────
- Basado en corrutinas y event loop.
- Ideal para I/O-bound (espera no bloqueante).
- Usa: async def, await, asyncio.gather, asyncio.run

Ejemplo:
  async def tarea():
      await asyncio.sleep(1)

Ventajas:
✓ Bajo uso de memoria
✓ Eficiente en muchas tareas pequeñas de red

Limitaciones:
✗ No acelera tareas CPU-bound
✗ Todas las funciones deben ser compatibles con async

──────────────────────────────
3. THREADING - Multihilo
──────────────────────────────
- Ejecuta varias tareas en paralelo lógico usando hilos.
- Los hilos comparten la misma memoria.

Conceptos:
  - Thread(target=func).start()
  - join() espera a que termine
  - Lock() para evitar race conditions

Ventajas:
✓ Útil en tareas I/O con espera activa
✓ Fácil acceso a memoria compartida

Limitaciones:
✗ GIL impide paralelismo real en CPU-bound
✗ Necesidad de sincronización con locks

──────────────────────────────────────────
4. MULTIPROCESSING - Procesamiento paralelo real
──────────────────────────────────────────
- Ejecuta múltiples procesos independientes (cada uno con su propia memoria).
- Ideal para CPU-bound.

Herramientas:
  - Process()
  - Pool() para mapear múltiples tareas

Ventajas:
✓ Paralelismo real (cada núcleo puede trabajar)
✓ Acelera procesamiento intenso

Limitaciones:
✗ Más memoria
✗ Comunicación compleja entre procesos

─────────────────────
5. GIL (Global Interpreter Lock)
─────────────────────
- En Python CPython, solo un hilo puede ejecutar código Python a la vez.
- Afecta solo a threading. No afecta a multiprocessing ni a extensiones en C.
- Por eso, threading no acelera tareas CPU-bound.

────────────────────────
6. SPEEDUP
────────────────────────
- Medida de mejora de rendimiento:

      SpeedUp = Tiempo_sincrónico / Tiempo_concurrente

- Se usa para comparar si una versión concurrente realmente mejora el rendimiento.
- Valores > 1 indican mejora, < 1 empeora.

────────────────────────
7. MPROF - Perfilamiento de memoria
────────────────────────
- Herramienta para visualizar uso de memoria durante ejecución.

Uso:
  mprof run script.py
  mprof plot

Interpretación:
✓ Más líneas = más procesos/hilos activos
✓ Altos picos = operaciones pesadas
✓ multiprocessing genera más procesos → más líneas/picos
✓ asyncio usa un solo hilo → trazas simples

──────────────────────────────
8. ENTRADA/SALIDA (E/S) EN SISTEMAS
──────────────────────────────
- Toda operación de lectura/escritura a dispositivos externos es una operación de E/S.
- El CPU queda bloqueado esperando respuesta.
- La concurrencia permite al CPU avanzar con otras tareas mientras espera.

Tipos de acceso:
✓ Acceso secuencial (registro a registro)
✓ Acceso por bloque
✓ Buffer intermedio (lectura eficiente)

"""

