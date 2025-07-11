import os
import shutil

EXTENSIONS_TO_REMOVE = [".c", ".so", ".pyc"]
DIRS_TO_REMOVE = ["build", "__pycache__"]

def clean():
    removed = 0
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONS_TO_REMOVE):
                path = os.path.join(root, file)
                os.remove(path)
                removed += 1
        for d in dirs:
            if d in DIRS_TO_REMOVE:
                dir_path = os.path.join(root, d)
                shutil.rmtree(dir_path, ignore_errors=True)
    print(f"✅ Limpieza completada. Archivos eliminados: {removed}")

if __name__ == "__main__":
    clean()
