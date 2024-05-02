class Perro:

    def correr(self):
        print(" ")
        print("El perro esta corriendo")
        print(" ")

    def ladrar(self):
        print(" ")
        print("el perro ladra")
        print(" ")

    def muerde(self):
        print(" ")
        print("el perro Muerde")
        print(" ")


try:   
    exit=False
    
    while not exit:

        betoven =Perro()
        print(" ")
        print("  que desea hacer: ")
        print("     1: Ladrar")
        print("     2: Correr")
        print("     3: Muerde")


        try:
            command=int(input("> "))

            if command == 1:
                betoven.ladrar()

            elif command ==2:
                betoven.correr()

            elif command ==3:
                betoven.muerde()
            
            else:
                print("no se que hacer")
        except:
            print("entrada invalida")
            
        
        salir=input("salir ?: ")
    
        if salir.upper() == "Y":
            print("adios")
            exit=True
        else:
            print(" ")
            print(" ***********  ")
            print("yeah baby")
            print(" ")
except:
    print("error fatal")   