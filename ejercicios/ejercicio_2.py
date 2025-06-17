# lista_peliculas = ["Destino Final","Eternauta","Lilo y Stich","Los Piratas del Caribe","El bueno, el malo y el feo"]

# contador = 1
# for pelicula in lista_peliculas:
#     print(f'{contador}.- {pelicula}')
#     contador = contador + 1

# for i in range(len(lista_peliculas)):
#     print(f'{i}.- {lista_peliculas[i]}')
    
# print(lista_peliculas[2])

# print(len('DOTA'))
# print(len(range(10)))
# print(len(range(3,7)))

lista_estudiantes = [
    ['Aquiles Baeza',[6.5,5.7,6.3]],
    ['Wendy Sulca',[5.0,4.7,5.8]],
    ['Peter Parker',[7.0,6.8,7.0]],
    ['Delfin Quispe',[4.3,3.8,2.9]]
]

rango = [0,1,2]
for estudiante in lista_estudiantes:
    suma = 0
    for i in range(len(estudiante[1])):
        suma = suma + estudiante[1][i]
    promedio = suma / len(estudiante[1])
    print(f'{estudiante[0]}, Notas:{estudiante[1]}, Promedio: {round(promedio,1)}')
    print()