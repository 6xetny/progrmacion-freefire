from data.asignaturas import asignaturas
from data.crear_data import crear_data
import os

# READ
def mostrar_listado_asignaturas():
    print()
    print('Listado de Asignaturas')
    print('======================')
    contador = 0
    for asignatura in sorted(asignaturas):
        contador += 1
        print(f'{contador}.- {asignatura}')

# READ
def buscar_asignatura():
    busqueda = input('Ingrese asignatura a buscar: ')
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            return asignatura

def indice_asignatura(busqueda):
    for i in range(len(asignaturas)):
        if busqueda.lower() in asignaturas[i].lower():
            return i

# CREATE
def agregar_asignatura():
    mostrar_listado_asignaturas()
    nueva_asignatura = input('Ingrese nueva asignatura: ')
    asignaturas.append(nueva_asignatura.title())

    crear_data('asignaturas.py','asignaturas',asignaturas)

    mostrar_listado_asignaturas()

# UPDATE  
def actualizar_asignatura():
    mostrar_listado_asignaturas()
    busqueda = input('Ingrese asignatura a buscar: ')
    indice = indice_asignatura(busqueda)
    # nuevo_dato = input(f'Ingrese nuevo nombre para asignatura {asignaturas[indice]}: ')
    # asignaturas[indice] = nuevo_dato

    crear_data('asignaturas.py','asignaturas',asignaturas)
    mostrar_listado_asignaturas()

actualizar_asignatura()