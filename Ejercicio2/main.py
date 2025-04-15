from Ordenamiento import Orden

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego")
    print("2. Salir")
    print("======================")

def main():
    nombre = input("Ingresa tu nombre para comenzar: ")
    juego = Orden(nombre)
    valor=True
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            juego.Ordenar()
            
        elif opcion == "2":
            juego.salir()
            valor=False
        else:
            print("Opción inválida. Intenta de nuevo.\n")

main()
