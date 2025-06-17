import calculadora

while True:
    num_1 = float(input("Ingrese su primer número: "))
    num_2 = float(input("Ingrese su segundo número: "))
    operacion = input("Ingrese su operación: ")

    calculadora.calculadora(num_1,num_2,operacion)