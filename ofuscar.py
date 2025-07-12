#!/usr/bin/env python3
import sys
import os
import shutil
from setuptools import setup
from Cython.Build import cythonize

APP_FILE = "/opt/orexx/app.py"

def validar_archivo(path):
    if not os.path.isfile(path):
        print(f"❌ ERROR: No se encontró el archivo: {path}")
        sys.exit(1)

def limpiar_archivos_temporales():
    """Limpia archivos temporales generados por la compilación"""
    archivos_temp = ["app.c", "build"]
    for archivo in archivos_temp:
        if os.path.exists(archivo):
            if os.path.isdir(archivo):
                shutil.rmtree(archivo)
                print(f"🗑️  Directorio {archivo} eliminado")
            else:
                os.remove(archivo)
                print(f"🗑️  Archivo {archivo} eliminado")

def main():
    validar_archivo(APP_FILE)
    
    try:
        print("🚀 Iniciando ofuscación (compilación) de app.py con Cython...")
        
        # Configuración de Cython para máxima ofuscación
        setup(
            ext_modules=cythonize(
                APP_FILE, 
                compiler_directives={
                    "language_level": "3",
                    "boundscheck": False,
                    "wraparound": False,
                    "cdivision": True,
                    "embedsignature": False,
                    "emit_code_comments": False
                }
            ),
            script_args=["build_ext", "--inplace"]
        )
        
        print("✅ Ofuscación completada con éxito.")
        
        # Mostrar archivos generados
        print("\n📁 Archivos generados:")
        for archivo in os.listdir("/opt/orexx/"):
            if archivo.endswith('.so'):
                print(f"   - {archivo} (archivo ejecutable ofuscado)")
            elif archivo.endswith('.c'):
                print(f"   - {archivo} (código C generado)")
        
        # Preguntar si limpiar archivos temporales
        respuesta = input("\n🧹 ¿Eliminar archivos temporales? (y/n): ").lower()
        if respuesta in ['y', 'yes', 's', 'si']:
            limpiar_archivos_temporales()
            
    except Exception as e:
        print(f"❌ ERROR durante la ofuscación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
