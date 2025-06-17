# Ejercicio 1
# Definir función saludar
def saludar(nombre):
    print(f"Buen día estimado(a) {nombre}")

nombre = input("Ingrese su nombre: ")

# Ejecutar función saludar
saludar(nombre)

# Ejercicio 2
# Definir función sumar
def suma(a,b):
    # resultado = a + b
    print(f"El resultado de sumar {a} + {b} = {a+b}")

numero_1 = int(input("Ingrese su primer número: "))
numero_2 = int(input("Ingrese su segundo número: "))

# Ejecutar función suma
suma(numero_1,numero_2)

# Ejercicio 3
# Definición de variables
num_1 = float(input("Ingrese su primer número: "))
num_2 = float(input("Ingrese su segundo número: "))
operacion = input("Ingrese su operación: ")

lado = float(input("Ingrese la medida de su lado"))

def area_cuadrado(a):
    print(f"El área de su cuadrado de lado {a}= {a*a}")

area_cuadrado(lado)