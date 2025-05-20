"""
UTILIDADES PARA MEDICIÓN Y ENTORNOS - 1IEE06

Este archivo explica 3 herramientas clave usadas en los laboratorios y exámenes del curso:
1. mprof - Medición del uso de memoria
2. venv - Creación de entornos virtuales
3. matplotlib - Librería para gráficos

────────────────────────────
1. MPROF (Memory Profiler)
────────────────────────────
mprof permite visualizar cómo varía el uso de memoria de un script Python.

Instalación:
    pip install memory_profiler

Uso básico:
    mprof run script.py
    mprof plot

Interpretación:
✓ Más picos = más procesos/hilos en ejecución
✓ multiprocessing genera más picos
✓ asyncio o sync generan trazas más limpias

────────────────────────────────────
2. VENV - ENTORNOS VIRTUALES EN PYTHON
────────────────────────────────────
Permite crear un entorno aislado para instalar dependencias sin afectar el sistema global.

Creación:
    python3 -m venv venv

Activación:
- En Linux/macOS:
    source venv/bin/activate
- En Windows CMD:
    venv\Scripts\activate.bat
- En Windows PowerShell:
    .\venv\Scripts\Activate.ps1

Instalación de paquetes:
    pip install -r requirements.txt

Desactivación:
    deactivate

────────────────────────────
3. MATPLOTLIB - Gráficos
────────────────────────────
Librería estándar para generar gráficos en Python (líneas, barras, dispersión, etc).

Instalación:
    pip install matplotlib

Ejemplo:
    import matplotlib.pyplot as plt

    tiempos = [1.2, 1.5, 1.1, 1.3]
    plt.plot(tiempos)
    plt.title("Tiempo de ejecución")
    plt.xlabel("Ejecución")
    plt.ylabel("Segundos")
    plt.show()
"""
