

class Juego:
  
  
    def __init__(self, usuario):
      
        self.usuario = usuario
        self.jugando = False
        self.abecedario = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        self.nivel_Cifrado = 0
        self.lista_frase_cifrada = []
        self.lista_frase_decifrada = []


    def Cifrar(self):
                
        self.jugando = True
        print(f"\n¡Bienvenido al sistema de cifrado, {self.usuario}!")

        frase = input("Ingresa la palabra o frase a cifrar: ")
        self.nivel_Cifrado = int(input("Ingresa el nivel de cifrado: "))
        
        for c in frase:
            
            if c.isdigit():
                c = int(c)
                cifrar_numero = c + self.nivel_Cifrado
                
                numero_cifrado = str(cifrar_numero)
                
                self.lista_frase_cifrada.append(numero_cifrado)
                
            elif c.isalpha():
                
                for i, letra in enumerate(self.abecedario):
                    c = c.lower()
                    
                    if c == letra:
                        cifrar_letra = i + self.nivel_Cifrado
                        self.lista_frase_cifrada.append(self.abecedario[cifrar_letra])
                    
            elif c == " ":
                print("Espacios : ", c)
                self.lista_frase_cifrada.append(" ")
                              
        frase_cifrada = "".join(self.lista_frase_cifrada)
        
        print("-----------------------------------------")
        print("Mensaje cifrado: ", frase_cifrada)
        # print("Mensaje cifrado2: ", lista_frase_cifrada)
        print("-----------------------------------------")

    def Decifrar(self):
                
        self.jugando = True
        print(f"\n¡Bienvenido al sistema de decifrado, {self.usuario}!")
        
        Frase_cifrada = "".join(self.lista_frase_cifrada)

        if Frase_cifrada:
            print("-----------------------------------------")
            print("Mensaje cifrado anteriormente:", Frase_cifrada)
            print("-----------------------------------------")
            print("")
            
            frase = input("Ingresa la palabra o frase a decifrar: ")
            self.nivel_Decifrado = self.nivel_Cifrado
            
        else:
            
            frase = input("Ingresa la palabra o frase a decifrar: ")
            self.nivel_Cifrado = int(input("Ingresa el nivel de decifrado: "))
            
        
        for c in frase:
            
            if c.isdigit():
                c = int(c)
                cifrar_numero = c - self.nivel_Cifrado
                
                numero_cifrado = str(cifrar_numero)
                
                self.lista_frase_decifrada.append(numero_cifrado)
                
            elif c.isalpha():
                
                for i, letra in enumerate(self.abecedario):
                    c = c.lower()
                    
                    if c == letra:
                        cifrar_letra = i - self.nivel_Cifrado
                        self.lista_frase_decifrada.append(self.abecedario[cifrar_letra])
                    
            elif c == " ":
                print("Espacios : ", c)
                self.lista_frase_decifrada.append(" ")
                              
        frase_decifrada = "".join(self.lista_frase_decifrada)
        
        print("-----------------------------------------")
        print("Mensaje decifrado: ", frase_decifrada)
        print("-----------------------------------------")
               
        
    def salir(self):
        print(f"\nHasta luego, {self.usuario}. ¡Vuelve pronto!")

  
    


