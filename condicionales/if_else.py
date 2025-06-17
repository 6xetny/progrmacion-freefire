# Condicionales
print("Ingrese su edad:")
edad = input()
edad_int = int(edad)

if edad_int >= 18:
    print("Ud. es mayor de edad.")
else:
    print("Ud. es menor de edad.")

# AB: El grupo de mayor ingreso, con un promedio de $7.177.530
# C1a: Clase media acomodada, con un promedio de $3.010.391
# C1b: Clase media emergente, con un promedio de $2.072.853
# C2: Clase media típica, con un promedio de $1.500.774
# C3: Clase media baja, con un promedio de  $1.003.426
# D: Vulnerables, con un promedio de $640.667
# E: Pobres, con un promedio de $361.583.

print("Ingrese su sueldo:")
sueldo_str = input()
sueldo_int = int(sueldo_str)
mensaje = ""

if sueldo_int >= 7177530:
    mensaje = "Ud. pertenece a la clase AB: El grupo de mayor ingreso"
elif sueldo_int >= 3010391:
    mensaje = "Ud. pertenece a la clase C1a: Clase media acomodada"
elif sueldo_int >= 2072853:
    mensaje = "Ud. pertenece a la clase C1b: Clase media emergente"
elif sueldo_int >= 1500774:
    mensaje = "Ud. pertenece a la clase C2: Clase media típica"
elif sueldo_int >= 1003426:
    mensaje = "Ud. pertenece a la clase C3: Clase media baja"
elif sueldo_int >= 640667:
    mensaje = "Ud. pertenece a la clase D: Vulnerables"
else:
    mensaje = "Ud. pertenece a la clase E: Pobres"

print(mensaje)