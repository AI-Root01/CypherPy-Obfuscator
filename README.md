# GhostPy-Obfuscator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.11-green.svg)
![Status](https://img.shields.io/badge/status-experimental-yellow.svg)

---

## Descripción

GhostPy-Obfuscator es una demo profesional que muestra cómo ofuscar código Python usando Cython para convertir scripts legibles en módulos compilados binarios, dificultando su ingeniería inversa y mejorando la ejecución.

Este repositorio usa un ejemplo sencillo de "Hola Mundo" para ilustrar el proceso completo de:

- Preparar un script Python.
- Crear un setup con Cython para compilarlo.
- Ejecutar el script compilado.
- Limpiar archivos temporales y build.

---

## Archivos principales

- `hello.py` — Script Python simple de ejemplo.
- `ofuscar.py` — Script para compilar `hello.py` con Cython.
- `run_hello.py` — Script para ejecutar el módulo compilado.
- `clean_build.py` — Limpieza de archivos generados durante compilación.

---

## Requisitos

- Python 3.11 o superior
- Cython instalado (`pip install cython`)

---

## Uso

1. Compilar el script:

```bash
python3 ofuscar.py
