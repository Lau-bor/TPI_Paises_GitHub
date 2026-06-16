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

def buscar_indice_exacto(paises, nombre):
    """
    Devuelve el índice del país cuyo nombre coincide exactamente
    sin distinguir mayúsculas/minúsculas. Si no existe, devuelve None.
    """
    for indice, pais in enumerate(paises):
        if pais["nombre"].lower() == nombre.lower():
            return indice
    return None


def pedir_entero_positivo(mensaje):
    """Solicita un número entero positivo y repite hasta que el dato sea válido."""
    while True:
        entrada = input(mensaje).strip()

        try:
            valor = int(entrada)

            if valor <= 0:
                print("  [ERROR] El valor debe ser mayor que cero.")
            else:
                return valor

        except ValueError:
            print("  [ERROR] Ingrese un número entero válido.")


def mostrar_tabla(paises):
    """Imprime la lista de países en formato de tabla."""
    if len(paises) == 0:
        print("[INFO] No hay datos para mostrar.")
        return

    ancho_nombre = 8
    for pais in paises:
        if len(pais["nombre"]) > ancho_nombre:
            ancho_nombre = len(pais["nombre"])

    encabezado = (
        f"  {'Nombre':<{ancho_nombre}}  {'Población':>15}  "
        f"{'Superficie':>14}  Continente"
    )
    separador = "  " + "-" * (ancho_nombre + 50)

    print(encabezado)
    print(separador)

    for pais in paises:
        print(
            f"  {pais['nombre']:<{ancho_nombre}}  "
            f"{pais['poblacion']:>15,}  "
            f"{pais['superficie']:>12,} km²  "
            f"{pais['continente']}"
        )

def listar_paises(paises):
    """Muestra todos los países cargados en formato tabla."""
    if len(paises) == 0:
        print("[INFO] No hay países registrados.")
        return

    print(f"\n  Total: {len(paises)} países")
    mostrar_tabla(paises)


def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n" + "═" * 50)
    print("   SISTEMA DE GESTIÓN DE PAÍSES")
    print("═" * 50)
    print("  1. Agregar país")
    print("  2. Actualizar datos de un país")
    print("  3. Buscar país por nombre")
    print("  7. Listar todos los países")
    print("  0. Salir")
    print("─" * 50)


def main():
    """Función principal: carga datos e inicia el bucle del menú."""
    print("Cargando datos desde el archivo CSV...")
    paises = cargar_paises(ARCHIVO_CSV)
    print(f"[OK] {len(paises)} países cargados.")

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
            input("\n  Presione Enter para continuar...")
        elif opcion == "2":
            actualizar_pais(paises)
            input("\n  Presione Enter para continuar...")
        elif opcion == "3":
            buscar_pais(paises)
            input("\n  Presione Enter para continuar...")
        if opcion == "7":
            listar_paises(paises)
            input("\n  Presione Enter para continuar...")
        elif opcion == "0":
            print("\n[OK] ¡Hasta luego!\n")
            break
        else:
            print("[ERROR] Opción no válida. Intente de nuevo.")

def agregar_pais(paises):
    """
    Solicita los datos de un nuevo país al usuario,
    valida que no exista y lo agrega a la lista.
    """
    print("\n── Agregar nuevo país ──")

    nombre = input("  Nombre: ").strip()
    if nombre == "":
        print("[ERROR] El nombre no puede estar vacío.")
        return

    if buscar_indice_exacto(paises, nombre) is not None:
        print(f"[ERROR] El país '{nombre}' ya existe en el sistema.")
        return

    poblacion = pedir_entero_positivo("  Población: ")
    superficie = pedir_entero_positivo("  Superficie (km²): ")

    continente = input("  Continente: ").strip()
    if continente == "":
        print("[ERROR] El continente no puede estar vacío.")
        return

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }

    paises.append(pais)
    guardar_paises(paises, ARCHIVO_CSV)
    print(f"[OK] País '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    """Permite actualizar la población y superficie de un país existente."""
    if len(paises) == 0:
        print("[INFO] No hay países cargados para actualizar.")
        return

    print("\n── Actualizar país ──")
    nombre = input("  Nombre del país a actualizar: ").strip()

    if nombre == "":
        print("[ERROR] Debe ingresar un nombre.")
        return

    indice = buscar_indice_exacto(paises, nombre)

    if indice is None:
        print(f"[ERROR] No se encontró el país '{nombre}'.")
        return

    print(f"  Datos actuales → Población: {paises[indice]['poblacion']:,} | "
          f"Superficie: {paises[indice]['superficie']:,} km²")

    nueva_poblacion = pedir_entero_positivo("  Nueva población: ")
    nueva_superficie = pedir_entero_positivo("  Nueva superficie (km²): ")

    paises[indice]["poblacion"] = nueva_poblacion
    paises[indice]["superficie"] = nueva_superficie

    guardar_paises(paises, ARCHIVO_CSV)
    print(f"[OK] Datos de '{paises[indice]['nombre']}' actualizados.")

def buscar_pais(paises):
    """Busca países por coincidencia parcial o exacta en el nombre."""
    if len(paises) == 0:
        print("[INFO] No hay países cargados para buscar.")
        return

    print("\n── Buscar país ──")
    termino = input("  Ingrese nombre (parcial o exacto): ").strip().lower()

    if termino == "":
        print("[ERROR] Debe ingresar un término de búsqueda.")
        return

    resultados = []
    for pais in paises:
        if termino in pais["nombre"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print(f"[INFO] No se encontraron países con '{termino}'.")
    else:
        print(f"\n  Se encontraron {len(resultados)} resultado(s):")
        mostrar_tabla(resultados)

if __name__ == "__main__":
    main()