class Orden:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False
        self.lista_numeros = [10,77,44,80,9]

        self.numeros_ordenados = []

    def Ordenar(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")

        n = len(self.lista_numeros)
    
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.lista_numeros[j] > self.lista_numeros[j + 1]:
                    
                    self.lista_numeros[j], self.lista_numeros[j + 1] = self.lista_numeros[j + 1], self.lista_numeros[j]
        
        print(self.lista_numeros)

        print("¡Gracias por jugar!\n")

    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")


  
    


