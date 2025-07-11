import sys
import os
from setuptools import setup
from Cython.Build import cythonize

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 ofuscar.py archivo.py")
        sys.exit(1)

    target_file = sys.argv[1]
    
    if not os.path.isfile(target_file):
        print(f"❌ Error: archivo '{target_file}' no encontrado.")
        sys.exit(1)

    try:
        setup(
            script_args=["build_ext", "--inplace"],
            ext_modules=cythonize(target_file, compiler_directives={"language_level": "3"})
        )
        print(f"✅ Compilación exitosa: {target_file}")
    except Exception as e:
        print(f"❌ Error en la compilación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
