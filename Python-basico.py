# COMENTARIOS
print("Hola gente, ando por aquí")
"""
Texto que no se va a interpretar
Texto que no se va a interpretar
"""

# CADENAS-STRINGS
print('\nCADENAS-STRINGS')

titulo = "Tutorial Python"
detalles = "1 hora duración"
año = 2022

#Concatenación -> Imprimo en una sola linea
print(f"{titulo} - {detalles} - {str(año)}")
# Otra forma de hacerlo (ojo con el str, mismos tipos de datos)
print(titulo + "- " + detalles + "- " + str(año))

# Escapado de caracteres
txt = "Ella dice \"Voy a ir pronto\"."
print(txt)

#Sintaxis IN

juego = "Juego Nintendo más popular"
print("l" in juego)
print("x" in juego)

#Indexado de Strings (similar a las listas)
cadena = 'amarillo'
print(cadena[1]) # => 'm'
print(cadena[-1]) # => 'o'
print(cadena[4:6]) # => 'il'
print(cadena[:4]) # => 'amar'
print(cadena[-3:]) # => ‘llo'

# Iterar strings
cadena2 = "hello"
for c in cadena2: 
    print(c)

#Método format de la clase String
men1 = 'Julio obtuvo {} puntos de un total de {} puntos'
print(men1.format(3, 10))
# => 'Julio obtuvo 3 puntos de un total de 10 puntos'

men2 = 'Julio {verbo} una {sustantivo} muy {adjetivo}'
print(men2.format(adjetivo='complicada', verbo='ganó', sustantivo='carrera'))
# => 'Julio ganó una carrera muy complicada’

x = "-".join(["Maria", "es", "genial"])
print(x)
# Imprime: Maria-es-genial

print('\nENTRADA DE DATOS')
""" Entrada de datos
Datos que me ingresó el usuario por teclado
"""
sitioweb = input("Cual es tu página web?: ")

print("El sitio web del usuario es: " + sitioweb)

print('\nSENTENCIA ELIF')
# Statement elif
tipo_mascota = "pez"
if tipo_mascota == "perror":
    print("Sos un perro")
elif tipo_mascota == "gato":
    print("Sos un gato")
elif tipo_mascota == "pez":
    print("Sos un pez")
else:
    print("No estoy seguro!")

# Operador Equal
if 'Si' == 'Si':
    print('Son iguales')

# Operador Not Equal
if 'Si' != 'No':
    print('NO son iguales')

print('\nLISTAS')
primos = [2, 3, 5, 7, 11]
print(primos)
lista_vacia = []

items = ['torta', 'galletita', 'pan']
items_totales = items + ['tarta']
print(items_totales)

numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
#Incluso contener otras listas (Listas 2D)
alumno_hobbie = [["Lucia", "danza"], ["Mario", "fotografia"], ["Marisa", "football"]]

# Método de la lista - append
flores = ['margarita', 'clavel']
flores.append('tulipan')
print(flores)
# Otros metodos - slice / sort

# Método de la lista - remove
flores.remove("margarita")
print(flores)

# Indices negativos
flores2 = ['margarita', 'clavel', 'tulipan', 'rosa']
flores2[-1] # 'rosa'
flores2[-3:] # 'clavel', 'tulipan', 'rosa'
flores2[:-2] # 'margarita', 'clavel',
print(flores2[:-2])

print('\nBUCLES-LISTAS')
numeros = [0, 254, 2, -1, 3]
for num in numeros: 
    if (num < 0): 
        print("Numero negativo detectado!") 
        break 
    print(num)
# 0
# 254
# 2
# Numero negativo detectado!

lista_numeros = [1, 2, -1, 4, -5, 5, 2, -9]
#Imprime solos los números positivos
for i in lista_numeros: 
    if i < 0: 
        continue 
    print(i)
# 1
# 2
# 4
# 5
# 2

# Imprime los números 0, 1, 2:
for i in range(3): 
    print(i)
# Imprime "CUIDADO" 3 veces:
for i in range(3): 
    print("CUIDADO")

# Corre 5 veces
i = 1
while i < 6: 
    print(i) 
    i = i + 1

# Bucles anidados (nested loops)
grupos = [["Medina", "Sanchez"], ["Ramirez", "Gonzalez"], ["Perez", "Pereyra"]]
# El bucle exterior iterará en cada item de la lista 
for grupo in grupos: 
# El bucle interior itera dentro de cada item de la lista, que también es una lista
    for nombre in grupo: 
        print(nombre)

print('\nTUPLA')
mi_tupla = ("uno", "dos", "tres")
print(mi_tupla)
# En el caso de que se intente modificar el contenido de una tupla Python generará un error 
#mi_tupla[0] = "cuatro"

print('\nCONJUNTOS DE DATOS')
mi_conjunto = {1, 3, 2, 9, 3, 1}
for e in mi_conjunto:
    print(e)
    
mi_conjunto.add(7)
print(mi_conjunto)

# Añade los elementos 5, 3, 4 y 6 al conjunto
# Los elementos repetidos no se añaden al conjunto
mi_conjunto.update([5, 3, 4, 6])
print(mi_conjunto)

print('\nDICCIONARIOS (MAPAS)')
diccionario = {'Piloto 1':'Fernando Alonso', 'Piloto 2':'Martin Rama', 'Piloto 3':'Felipe Ramirez'}
print("Diccionario inicial: ", diccionario)

# get(): Devuelve el valor que corresponde con la key introducida.
print("get Piloto 1: ", diccionario.get('Piloto 1'))
#Fernando Alonso

# pop(): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
print("pop Piloto 1: ", diccionario.pop('Piloto 1'))
#Fernando Alonso

print("Diccionario luego del pop: ", diccionario)
#{'Piloto 3': 'Felipe Ramirez', 'Piloto 2': 'Martin Rama'}

# update(): Actualiza el valor de una determinada key o lo crea si no existe.
diccionario.update({'Piloto 4':'Ezequiel Lopez'})
diccionario.update({'Piloto 2':'Sebastian Gomez'})
print("diccionario luego de los updates: ", diccionario)
#{'Piloto 4': 'Ezequiel Lopez', 'Piloto 2': 'Sebastian Gomez', 'Piloto 3': 'Felipe Ramirez'}

# key "in" diccionario: devuelve verdadero (True) o falso (False) si la key existe en el diccionario.
print ("Piloto 2 en Diccionario: ", "Piloto 2" in diccionario)
#True
print ("piloto 2 en Diccionario: ", "piloto 2" in diccionario)
#False
print ("Piloto 1-Fernando Alonso- en Diccionario: ", "Fernando Alonso" in diccionario)
#False

# "definición" in diccionario.values(): devuelve verdadero (True) o falso (False) si la definición existe en el diccionario.
print ("Sebastian Gomez en diccionario.values: ", "Sebastian Gomez" in diccionario.values())
#True

# del diccionario['key']: Elimina el valor (y el key) asociado a la key indicada.
del diccionario['Piloto 2']
print("diccionario luego del del: ", diccionario)
#{'Piloto 4': 'Ezequiel Lopez', 'Piloto 3': 'Felipe Ramirez'}

print('\nFUNCIONES')
# Define la function mi_funcion() con el parámetro x
def mi_funcion(x): 
    return x + 1;
print("Esto no es parte de la función")

# Invocando la función
print(mi_funcion(2)) # Salida: 3
print(mi_funcion(3 + 5)) # Salida: 9

def calcularVolumen(long=1, ancho=1, prof=1): 
    print("Longitud = " + str(long))    
    print("Ancho = " + str(ancho)) 
    print("Profundidad = " + str(prof)) 
    return long * ancho * prof;

calcularVolumen(1, 2, 3)
calcularVolumen(long=5, prof=2, ancho=4)
calcularVolumen(2, prof=3, ancho=4)
calcularVolumen(prof=4, ancho=3)

# Scope (alcance) de las variables, locales y globales
a = 5
def f1(): 
    a = 2 
    print(a) 
    
print(a) # Imprime 5
f1() # Imprime 2

