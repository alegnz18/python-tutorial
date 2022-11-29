English? [Here](README.md)

# python-tutorial

Tutorial de Python 3 usando la imagen de Docker oficial de Python.

## Pre-requisitos

Python cuenta con una imagen oficial lo que hace posible que se puedan ejecutar proyectos y scripts en este lenguaje dentro de un contenedor Docker, crear/extender imágenes, compartir volúmenes, etc.

Tener instalado Docker en tu sistema.
Las imágenes se pueden encontrar en el repo oficial de docker, en:
https://hub.docker.com/_/python/
https://hub.docker.com/r/biowdl/pyyaml


## Modo Shell o Intérprete de Comandos

En su forma más simple podés ejecutar un contenedor con una imagen Python y acceder al modo Shell con el comando python:

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

Podés ver que el intérprete utiliza >>> para indicar que está listo para recibir instrucciones que va procesando una a una a medida que son ingresadas.

Esta forma de trabajo de modo interactivo por la terminal permite probar pequeños fragmentos de código, de forma similar a cuando se usa un intérprete online.


## Ejecución de Script Sintaxis Básica

Una de las características propias de Docker es permitirte (con el parámetro `-v`) montar un directorio del host como si fuera propio del contenedor, de tal forma que pueda leer/escribir en el mismo. Con al parámetro `--rm`, una vez finalizada la prueba eliminaremos el contenedor.

De aquí en adelante será necesario tener descargados los scripts subidos al repo actual en un directorio local; en este primero caso, Python-basico.py

Aquí usaremos el intérprete en modo línea de comando en el cual escribirás un programa completo en un archivo con extensión [nombre_archivo].py y luego será el intérprete python quien ejecutará el contenido del archivo.

```console
# docker run --rm -it -v "$PWD":/home/python/scripts -w /home/python/scripts python:latest python Python-basico.py
```

Siguiendo la salida de este script se tiene una idea básica de cómo maneja Python los distintos tipos de datos, las colecciones, las estructuras de control y una breve intro a la declaración e invocación de funciones.


## Python y POO

Python es un lenguaje orientado a objetos, de modo que ofrece soporte de primer nivel para la creación de clases. Sin embargo, no es condición necesaria hacer uso de ellas para poder crear un programa, como vimos hasta el momento. 

Aquí utilizarás el intérprete en modo script, para lo cual el archivo a ejecutarse deberá cumplir con lo siguiente:
- tener asignado permiso de ejecución
- contar como primera línea de código con una línea de shebang, que indica la ubicación del intérprete
#!/usr/bin/python3.
Luego de lo cual el archivo podrá ejecutarse directamente como se ve a continuación:

```console
# chmod u+x clases.py
# docker run --rm -v "$PWD":/home/python/scripts -w /home/python/scripts python:latest ./clases.py
```
Acá pudiste ver un ejemplo de jerarquía de clases y de manejo de atributos públicos y privados implementado en Python.

## Python - Módulo PyYAML

PyYAML es un Módulo parseador de formato YAML y generador de código Python. 
En este caso usarás una imagen docker que es un container Python donde ya se encuentra instalado el módulo PyYAML, por lo cual podrás realizar el import de la librería requerida dentro del código. 
El presente código lee un archivo en formato YAML y lo carga en un diccionario de Python. Luego recorre el mismo para imprimir sus elementos a la salida por consola.

```console
# docker run --rm -v "$PWD":/home/python/scripts -w /home/python/scripts biowdl/pyyaml python yamltodic.py
```
