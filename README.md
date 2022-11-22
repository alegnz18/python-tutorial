English? [Here](README.md)

# python-tutorial

Tutorial de Python 3 usando la imagen de Docker oficial de Python.

## Pre-requisitos

Python cuenta con una imagen oficial lo que hace posible que se puedan ejecutar proyectos y scripts en este lenguaje dentro de un contenedor Docker, crear/extender imágenes, compartir volúmenes, etc.

Tener instalado Docker en tu sistema.
Las imágenes se pueden encontrar en el repo oficial de docker https://hub.docker.com/_/python/

## GroovyShell

En su forma más simple podemos ejecutar un contenedor con cualquiera de estas imágenes y con la ayuda del comando `groovysh` nos iniciará una shell de Groovy como para trabajar ahí dentro.

```console
# docker run --rm -it groovy:latest groovysh
Groovy Shell (3.0.13, JVM: 17.0.5)
Type ':help' or ':h' for help.
groovy:000> println "hola mundo"
hola mundo
===> null
```

(ctrl-c para salir)

En este momento estás ejecutando un contenedor de docker con groovy instalado y con todas las características de cualquier contenedor: network, volúmenes, incluirlo en un docker-compose, etc.

