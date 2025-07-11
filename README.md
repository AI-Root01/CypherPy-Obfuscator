# CypherPy-Obfuscator 🛡️🐍

> **Secure, compile, and obfuscate your Python code like a pro.**

`CypherPy-Obfuscator` es una utilidad profesional basada en [Cython](https://cython.org/) que convierte tus scripts `.py` en binarios `.so`, dificultando su ingeniería inversa y mejorando el rendimiento. Ideal para proteger lógica crítica o distribuir software con una capa extra de seguridad.

Repositorio: [https://github.com/AI-Root01/CypherPy-Obfuscator](https://github.com/AI-Root01/CypherPy-Obfuscator)  
Perfil del autor: [https://github.com/AI-Root01](https://github.com/AI-Root01)

---

## 🚀 Características

- 🔐 **Ofuscación real** mediante conversión a C.
- ⚡ **Compilación directa a binarios `.so`** (Linux).
- 🧪 **Compatible con scripts simples o complejos**.
- 🛠️ **Sin modificar el comportamiento original del código**.
- 💻 **Fácil integración en cualquier proyecto**.

---

## 📦 Requisitos

- Python 3.8+
- Cython
- build-essential (Linux)
- setuptools

---

## 🔧 Estructura del Proyecto

```
CypherPy-Obfuscator/
│
├── ofuscar.py        # Compila el archivo objetivo con Cython
├── clean_build.py    # Elimina archivos temporales: .c, .so, build/
├── run_app.py        # Ejecuta el binario compilado
├── hello.py          # Ejemplo básico ("Hola Mundo")
├── README.md         # Este archivo
```

---

## ⚙️ Instalación Rápida

```bash
sudo apt update && sudo apt install build-essential python3-pip -y
pip install cython setuptools
```

---

## 🔐 ¿Cómo usar?

### Paso 1: Ofuscar el archivo

```bash
python3 ofuscar.py hello.py
```

### Paso 2: Limpiar archivos innecesarios

```bash
python3 clean_build.py
```

### Paso 3: Ejecutar el código compilado

```bash
python3 run_app.py
```

> **Nota:** `run_app.py` está diseñado para cargar automáticamente el archivo `hello.so` generado por Cython.

---

## 📊 Comparativa (Texto vs Binario)

| Aspecto                  | Código Python (.py) | Binario Compilado (.so) |
|--------------------------|---------------------|--------------------------|
| Legible por humanos      | ✅ Sí               | ❌ No                   |
| Fácil de modificar       | ✅ Sí               | ❌ No                   |
| Protegido contra copia   | ❌ No               | ✅ Parcialmente         |
| Performance              | ⚠️ Depende          | ⚡ Mejora notable        |
| Requiere intérprete      | ✅ Sí               | ✅ Sí                   |
| Compatible con Cython    | -                   | ✅ Sí                   |

---

## 🧠 ¿Por qué usar CypherPy-Obfuscator?

- Ideal para **entornos industriales, comerciales o críticos**.
- Reduce el riesgo de **robo intelectual o modificación maliciosa**.
- Útil para distribución de código en **sistemas embebidos o kioscos**.
- Permite **mantener el mismo flujo de ejecución** sin pérdida de funcionalidad.

---

## 📁 Limpieza de Archivos de Build

El script `clean_build.py` elimina:

- Archivos `.c` generados
- Archivos `.so` obsoletos
- Carpeta `/build`
- Archivos `.pyc` y `__pycache__`

---

## 🔒 Nota de Seguridad

> Este método **no es invulnerable**. Aunque Cython compila a binario, usuarios expertos aún podrían desensamblar el `.so`. Este sistema es una **capa adicional**, no una solución definitiva contra ingeniería inversa.

---

## 📄 Licencia

Distribuido bajo la licencia [MIT](LICENSE). Libre de usar, modificar y distribuir.
