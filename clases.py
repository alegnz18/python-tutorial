print('\nCLASES')
print('Constructor solo con parámetro por defecto')
class Alumno:
    #Constructor
    def __init__(self):
        self.nombre = "Pablo"

    def saludar(self):
        """Imprime un saludo en pantalla."""
        # Vamos a incluir el valor de un objeto
        print(f"¡Hola, {self.nombre}!")

# Crear una instancia de la clase
alumno = Alumno()
# self no es más que el objeto alumno
alumno.saludar()

print('Constructor con 2 parámetros')
class AlumnoDef:

    #Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        """Imprime un saludo en pantalla."""
        # Vamos a incluir el valor de un objeto
        print(f"¡Hola, {self.nombre}!")

# Crear una instancia de la clase
alumno2 = AlumnoDef("Pedro")
alumno2.saludar()

print('\nCLASES SIN HERENCIA')
class Rectangulo:
    """
    Define un rectángulo según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

rectangulo = Rectangulo(20, 10)
print("Área del rectángulo: ", rectangulo.area())

class Triangulo:
    """
    Define un triángulo según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return (self.b * self.h) / 2

triangulo = Triangulo(20, 12)
print("Área del triángulo: ", triangulo.area())

print('\nCLASES CON HERENCIA')
class Poligono:
    """
    Define un polígono según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

class RectanguloHer(Poligono):

    def area(self):
        return self.b * self.h

class TrianguloHer(Poligono):

    def area(self):
        return (self.b * self.h) / 2

rectanguloHer = RectanguloHer(20, 10)
trianguloHer = TrianguloHer(20, 12)

print("Área del rectángulo: ", rectanguloHer.area())
print("Área del triángulo:", trianguloHer.area())

print('\nCLASE CON ATRIBUTOS PRIVADOS')
class Estudiante:
    def __init__(self, nombre, materias):
        self.set_nombre(nombre)
        if not isinstance(materias, list):
            raise TypeError("Las materias deben ser una lista")
        self.materias = materias
    
    def set_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("name must be a string")
        self._nombre = nombre
    
    def get_nombre(self):
        return self._nombre
    
estudiante = Estudiante("Juan", [1,2,3,4])
print("Nombre Estudiante: ", estudiante.get_nombre())
print("Materias: ", estudiante.materias)



