import math

numeros = [2,4,6,8,10,12]
decimal = 12.3456

print(f"El número mayor de la lista {numeros} es {max(numeros)}")
print(f"El número menor de la lista {numeros} es {min(numeros)}")

print(f"Redondear el decimal {decimal} = {round(decimal)}")
print(f"Redondear el decimal {decimal} a 2 decimales = {round(decimal,2)}")
print(f"Truncar el decimal {decimal} = {math.trunc(decimal)}")
print(f"Valor absoluto de -45= {math.fabs(-45)}")
print(f"Raiz cuadrada de 25= {math.sqrt(25)}")
print(f"Dumatoria de los numeros {numeros} = {math.fsum(numeros)}")