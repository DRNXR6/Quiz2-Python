from CifradoCésar import Juego

def mostrar_menu():
    print("")
    print("=== MENÚ PRINCIPAL ===")
    print("1. Cifrar una frase")
    print("2. Decifrar una frase")
    print("3. Salir")
    print("======================")
    print("")

def main():
    User = input("Ingresa tu usuario para comenzar: ")
    juego = Juego(User)
    
    valor=True
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            juego.Cifrar()
        
        elif opcion == "2":
            juego.Decifrar()

        elif opcion == "3":
            juego.salir()
            valor=False
        else:
            print("Opción inválida. Intenta de nuevo.\n")

main()
