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

def cargar_paises(ruta):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Ignora filas con errores de formato, campos vacíos o valores inválidos.
    """
    paises = []

    if not os.path.exists(ruta):
        print(f"[AVISO] No se encontró el archivo '{ruta}'. Se iniciará con lista vacía.")
        return paises

    try:
        with open(ruta, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames is None:
                print("[ERROR CSV] El archivo CSV está vacío o no tiene encabezados.")
                return paises

            for campo in CAMPOS:
                if campo not in lector.fieldnames:
                    print(f"[ERROR CSV] Falta la columna obligatoria '{campo}'.")
                    return paises

            nombres_cargados = []

            for numero_fila, fila in enumerate(lector, start=2):
                try:
                    for campo in CAMPOS:
                        valor = fila.get(campo)
                        if valor is None or valor.strip() == "":
                            raise ValueError(f"Campo '{campo}' vacío o faltante")

                    nombre = fila["nombre"].strip()
                    continente = fila["continente"].strip()

                    try:
                        poblacion = int(fila["poblacion"].strip())
                    except ValueError:
                        raise ValueError("La población debe ser un número entero")

                    try:
                        superficie = int(fila["superficie"].strip())
                    except ValueError:
                        raise ValueError("La superficie debe ser un número entero")

                    if poblacion <= 0:
                        raise ValueError("La población debe ser mayor que cero")

                    if superficie <= 0:
                        raise ValueError("La superficie debe ser mayor que cero")

                    if nombre.lower() in nombres_cargados:
                        raise ValueError("País duplicado en el CSV")

                    pais = {
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente,
                    }

                    paises.append(pais)
                    nombres_cargados.append(nombre.lower())

                except ValueError as error:
                    print(f"[ERROR CSV] Fila {numero_fila} ignorada: {error}")

    except OSError as error:
        print(f"[ERROR] No se pudo leer el archivo CSV: {error}")

    return paises


def guardar_paises(paises, ruta):
    """Escribe la lista de países al archivo CSV."""
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
    except OSError as error:
        print(f"[ERROR] No se pudo guardar el archivo CSV: {error}")