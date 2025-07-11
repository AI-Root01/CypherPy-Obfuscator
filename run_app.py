import sys
import os
import runpy

BASENAME = "hello"  # Cambia si el script ofuscado tiene otro nombre
SO_FILE = f"{BASENAME}.cpython-{sys.version_info.major}{sys.version_info.minor}-{'x86_64' if sys.maxsize > 2**32 else 'aarch64'}-linux-gnu.so"

try:
    if not os.path.exists(SO_FILE):
        raise FileNotFoundError(f"No se encontró el binario compilado: {SO_FILE}")

    __import__(BASENAME)
    print("✅ Código ofuscado ejecutado correctamente.")
except Exception as e:
    print(f"❌ Error al ejecutar el binario: {e}")
    sys.exit(1)
