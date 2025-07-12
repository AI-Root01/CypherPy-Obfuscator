#!/usr/bin/env python3
import sys
import os
import glob

def encontrar_archivo_so():
    """Encuentra el archivo .so ofuscado"""
    archivos_so = glob.glob("/opt/orexx/*.so")
    
    if not archivos_so:
        print("❌ ERROR: No se encontró archivo .so ofuscado")
        print("Ejecuta primero el script de ofuscación")
        sys.exit(1)
    
    return archivos_so[0]

def main():
    try:
        # Encontrar archivo .so
        archivo_so = encontrar_archivo_so()
        print(f"🚀 Ejecutando archivo ofuscado: {os.path.basename(archivo_so)}")
        
        # Agregar directorio al path de Python
        directorio = os.path.dirname(archivo_so)
        if directorio not in sys.path:
            sys.path.insert(0, directorio)
        
        # Importar y ejecutar el módulo ofuscado
        import app
        
        print("✅ Archivo ofuscado ejecutado exitosamente")
        
    except ImportError as e:
        print(f"❌ ERROR: No se pudo importar el módulo ofuscado: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ ERROR durante la ejecución: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
