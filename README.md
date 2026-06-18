# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador - Programación 1**  
**Tecnicatura Universitaria en Programación - UTN**

## Descripción

Aplicación de consola desarrollada en Python 3 para gestionar información de países a partir de un archivo CSV.

El sistema permite cargar datos, agregar nuevos países, actualizar información existente, realizar búsquedas, aplicar filtros, ordenar registros y obtener estadísticas generales del dataset.

Cada país se representa mediante un diccionario con los siguientes campos:

* `nombre`
* `poblacion`
* `superficie`
* `continente`

Todos los países se almacenan en una lista de diccionarios.

## Funcionalidades

El programa permite:

* Agregar un nuevo país.
* Actualizar la población y superficie de un país existente.
* Buscar países por nombre, con coincidencia parcial o exacta.
* Filtrar países por continente.
* Filtrar países por rango de población.
* Filtrar países por rango de superficie.
* Ordenar países por nombre, población o superficie.
* Elegir orden ascendente o descendente.
* Mostrar estadísticas generales del dataset.
* Listar todos los países cargados.

## Estadísticas incluidas

El sistema calcula y muestra:

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

## Estructura del proyecto

```text
.
├── paises.py
├── paises.csv
├── README.md
└── informe_tpi.pdf
```

## Requisitos

* Python 3.x
* No se requieren librerías externas.

El programa utiliza únicamente módulos de la biblioteca estándar de Python:

* `csv`
* `os`

## Cómo ejecutar el programa

1. Clonar o descargar el repositorio.
2. Verificar que los archivos `paises.py` y `paises.csv` estén en la misma carpeta.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar el programa con el siguiente comando:

```bash
python paises.py
```

En algunos sistemas puede ser necesario usar:

```bash
python3 paises.py
```

## Menú principal

```text
1. Agregar país
2. Actualizar datos de un país
3. Buscar país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Listar todos los países
0. Salir
```

## Validaciones implementadas

El sistema incluye validaciones para:

* Evitar campos vacíos al agregar países.
* Controlar que población y superficie sean números enteros positivos.
* Evitar países duplicados.
* Controlar errores de formato en el archivo CSV.
* Validar que el CSV tenga los encabezados obligatorios.
* Informar búsquedas sin resultados.
* Informar filtros sin resultados.
* Controlar opciones inválidas en el menú.
* Evitar fallos del programa ante entradas incorrectas del usuario.

## Ejemplos de uso

### Búsqueda por nombre

Entrada:

```text
ar
```

Resultado esperado con el dataset base:

```text
Se encontraron 4 resultado(s):
Argentina
Arabia Saudita
Argelia
Marruecos
```

### Estadísticas generales

El sistema muestra:

```text
Total de países registrados: 44
Mayor población: China
Menor población: Fiyi
Promedio de población
Promedio de superficie
Cantidad de países por continente
```

## Repositorio

Repositorio público del proyecto:

https://github.com/Lau-bor/TPI_Paises_GitHub

## Video demostrativo

Video demostrativo del funcionamiento del sistema:

https://youtu.be/QHzE2zkhyWQ

## Documentación

Informe académico y técnico del proyecto:

[informe_tpi.pdf](./informe_tpi.pdf)

## Integrante

* Lautaro Borges Licciardi

## Observaciones finales

Este proyecto fue desarrollado como Trabajo Práctico Integrador de Programación 1.  
Su objetivo es aplicar los contenidos principales de la materia en una aplicación funcional de consola, utilizando estructuras de datos, funciones, validaciones, archivos CSV, filtros, ordenamientos y estadísticas básicas.
