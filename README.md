English? [Here](README.md)

# python-tutorial

Tutorial de Python 3 usando la imagen de Docker oficial de Python.

## Pre-requisitos

Python cuenta con una imagen oficial lo que hace posible que se puedan ejecutar proyectos y scripts en este lenguaje dentro de un contenedor Docker, crear/extender imágenes, compartir volúmenes, etc.

Tener instalado Docker en tu sistema.
Las imágenes se pueden encontrar en el repo oficial de docker https://hub.docker.com/_/python/

## PythonShell

En su forma más simple podemos ejecutar un contenedor con cualquiera de estas imágenes y con la ayuda del comando `groovysh` nos iniciará una shell de Groovy como para trabajar ahí dentro.

```console
# docker run --rm -it python:latest python
Python 3.11.0 (main, Nov 15 2022, 19:58:01) [GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('hola mundo')
hola mundo
>>>
```

(ctrl-d para salir)

En este momento estás ejecutando un contenedor de docker con python instalado y con todas las características de cualquier contenedor: network, volúmenes, incluirlo en un docker-compose, etc.

## Ejecución de Script Sintaxis Básica

Una de las características propias de Docker es permitirte (con el parámetro `-v`) montar un directorio del host como si fuera propio del contenedor, de tal forma que pueda leer/escribir en el mismo. Con al parámetro `--rm`, una vez finalizada la prueba eliminaremos el contenedor.

De aquí en adelante será necesario tener descargados los scripts subidos al repo actual en un directorio local; en este primero caso, Python-basico.py

```console
# docker run --rm -it -v "$PWD":/home/python/scripts -w /home/python/scripts python:latest python Python-basico.py
```

Siguiendo la salida de este script tenemos una idea básica de cómo maneja Python los distintos tipos de datos, como maneja las colecciones, las estructuras de control y una breve intro a la declaración e invocación de funciones.

## Python y POO

Python es un lenguaje orientado a objetos, de modo que tiene soporte de primer nivel para la creación de clases. Sin embargo, no es condición necesaria hacer uso de ellas para poder crear un programa, como vimos hasta el momento. Veremos un ejemplo de jerarquía de clases y de atributos públicos y privados:

```console
# docker run --rm -it -v "$PWD":/home/python/scripts -w /home/python/scripts python:latest python clases.py
```

