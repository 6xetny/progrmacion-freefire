# Crear un programa que convierta unidades de temperatura 
# Celsius, Kelvin o Fahrenheit.
# 1.- El usuario deberá ingresar el valor de T°.
# 2.- El usuario deberá ingresar escala de T° original.
# 3.- El usuario deberá ingresar escala de T° final.
# 4.- El sistema deberá entregar resultados de conversión.

# de °C a °K => °C + 273.15
# de °K a °C => °K - 273.15

# de °C a °F => (°C * 9/5) + 32
# de °F a °C => (°F -32) * 5/9

# de °F a °K => (°F -32) * 5/9 + 273.15
# de °K a °F => ((°K - 273.15)* 9/5) + 32


    
def convertidor_temp(temperatura, inicio, fin):
    resultado = 0
    
    if inicio == "K":
        if fin == "C":
            resultado = temperatura - 273.15
        elif fin == "F":
            resultado = ((temperatura - 273.15) * 9/5) + 32
        else:
            print("Escala final errónea")
    elif inicio == "C":
        if fin == "K":
            resultado = temperatura + 273.15
        elif fin == "F":
            resultado = (temperatura * 9/5) + 32
        else:
            print("Escala final errónea")
    elif inicio == "F":
        if fin == "K":
            resultado = (temperatura -32) * 5/9 + 273.15
        elif fin == "C":
            resultado = (temperatura -32) * 5/9
        else:
            print("Escala final errónea")
    else:
            print("Escala inicial errónea")
    
    print(f"{temperatura}°{inicio} = {resultado}°{fin}")

temp = float(input("Ingrese su temperatura a convertir: "))
escala_inicial = input("Indique escala inicial: C, F o K: ").upper().strip()
escala_final = input("Indique escala final: C, F o K: ").upper().strip()

convertidor_temp(temp,escala_inicial,escala_final)