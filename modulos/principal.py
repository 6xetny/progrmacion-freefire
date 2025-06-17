from funciones.cuadrilatero import perimetro_cuad,area_cuad,volumen_cuad
from funciones.circunferencia import perimetro_circ,area_circ,volumen_circ

def menu():
    print()
    print("Cálculo de funciones geométricas.")
    print("1: Perímetro")
    print("2: Área")
    print("3: Volumen")
    print("0: Salir")
    print()
            
def sub_menu():
    print()
    print("¿Para qué figura geométrica?")
    print("1: Cuadrilátero")
    print("2: Circunferencia")
    print("0: Salir")
    print()

def programa_principal():
    while True:
        menu()
        opcion = input("Seleccione su opción (0-3): ")
        
        if opcion == "1":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
            
            if opcion_sub_menu == "1":
                ancho = float(input("Ingrese el ancho: "))
                largo = float(input("Ingrese el largo: "))
                print(f"Perímetro de Cuadrilatero de Lados {ancho} y {largo}= {perimetro_cuad(ancho,largo)}")
                
            elif opcion_sub_menu == "2":
                radio = float(input("Ingrese el radio: "))
                print(f"Perímetro de Circunferencia de radio {radio}= {perimetro_circ(radio)}")

            elif opcion_sub_menu == "0":
                print("Volviendo al menú principal...")
                menu()
            else:
                print("Opción Inválida!")
                break

        elif opcion == "2":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
            
            if opcion_sub_menu == "1":
                ancho = float(input("Ingrese el ancho: "))
                largo = float(input("Ingrese el largo: "))
                print(f"Área de Cuadrilatero de Lados {ancho} y {largo}= {area_cuad(ancho,largo)}")
                
            elif opcion_sub_menu == "2":
                radio = float(input("Ingrese el radio: "))
                print(f"Área Circunferencia de radio {radio}= {area_circ(radio)}")

            elif opcion_sub_menu == "0":
                return
            else:
                print("Opción Inválida!")
                return

        elif opcion == "3":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
            
            if opcion_sub_menu == "1":
                ancho = float(input("Ingrese el ancho: "))
                largo = float(input("Ingrese el largo: "))
                alto = float(input("Ingrese el alto: "))
                print(f"Volumen de Cubo de Lados {ancho}, {largo} y {alto}= {volumen_cuad(ancho,largo,alto)}")
                
            elif opcion_sub_menu == "2":
                radio = float(input("Ingrese el radio: "))
                print(f"Área de Esfera de radio {radio}= {volumen_circ(radio)}")

            elif opcion_sub_menu == "0":
                return
            else:
                print("Opción Inválida!")
                break

        elif opcion == "0":
            print("saliendo del sistema...")
            break
        else:
            print("Opción inválida...")

programa_principal()