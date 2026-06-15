"""
=============================================================
  TPI - Gestión de Datos de Países en Python
  Programación 1
=============================================================
  Módulo principal: gestión de países con menú interactivo.
  Funcionalidades: agregar, actualizar, buscar, filtrar,
  ordenar y mostrar estadísticas sobre países.
=============================================================
"""

import csv
import os

# ──────────────────────────────────────────────
#  CONSTANTES
# ──────────────────────────────────────────────

CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CSV = os.path.join(CARPETA_PROYECTO, "paises.csv")
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]