import math
# Definir 3 funciones... Cálculo de perímetro, área y volumen...
pi = math.pi

def perimetro_circ(radio):
    return radio * pi * 2

def area_circ(radio):
    return pi * radio ** 2

def volumen_circ(radio):
    return 4/3 * pi * radio ** 3