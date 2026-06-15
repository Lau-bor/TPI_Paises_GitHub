# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador - Programación 1**

## Descripción

Aplicación de consola desarrollada en Python 3 para gestionar información de países.

El programa permite leer datos desde un archivo CSV, agregar nuevos países, actualizar información existente, realizar búsquedas, aplicar filtros, ordenar datos y mostrar estadísticas generales.

Cada país se almacena como un diccionario con los siguientes datos:

* nombre
* población
* superficie
* continente

Todos los países se guardan dentro de una lista de diccionarios.

## Funcionalidades

El sistema permite:

* Agregar un nuevo país.
* Actualizar la población y superficie de un país existente.
* Buscar países por nombre.
* Filtrar países por continente.
* Filtrar países por rango de población.
* Filtrar países por rango de superficie.
* Ordenar países por nombre, población o superficie.
* Elegir orden ascendente o descendente.
* Mostrar estadísticas generales.

## Estadísticas incluidas

El programa muestra:

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
└── README.md
```

## Requisitos

* Python 3.x
* No se requieren librerías externas.

El programa utiliza únicamente módulos de la biblioteca estándar de Python:

* csv
* os

## Cómo ejecutar el programa

1. Descargar o clonar el repositorio.
2. Verificar que los archivos `paises.py` y `paises.csv` estén en la misma carpeta.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar el siguiente comando:

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

* Evitar campos vacíos.
* Controlar que población y superficie sean números enteros positivos.
* Evitar países duplicados.
* Controlar errores en el archivo CSV.
* Mostrar mensajes cuando una búsqueda no tiene resultados.
* Mostrar mensajes cuando un filtro no tiene resultados.
* Controlar opciones inválidas del menú.

## Integrante

* Lautaro Borges Licciardi

## Links de entrega

* Video demostrativo: agregar enlace
* Documentación PDF: agregar enlace o subir el archivo PDF al repositorio

## Observaciones

Para la entrega final, el repositorio debe incluir:

* Código fuente completo.
* Archivo CSV con el dataset base.
* README.md.
* Informe académico en PDF.
* Enlace público al video demostrativo.

