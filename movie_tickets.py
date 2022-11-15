from theater.User import User

class pelicula (User):
    def __init__(self, nombre = str):
        self.nombre = nombre
    
    def search(fila, numero):
        sillas = User()
        if fila in sillas.sillas:
            for x in sillas.sillas:
                if sillas.sillas[x] == numero:
                    sillas.sillas[x].pop()
                    return True
                else:
                    False
        else:
            print("eliga otra fila por favor")
            
    
    def get_pelicula(f):
        print("Qué película desea ver?")
        print("Las peliculas disponibles son: ")
        for i in f():
            print(i)
        opc = input("Ingrese la que desee: ")
        while True:
            if opc not in f():
                opc = input("Ingrese una película válida: ")  
            else:
                break
        
        cant_tickets = int(input("Ingrese la cantidad de tickets a comprar: "))
        fila = input("Ingrese la fila de su asiento:")
        numero = int(input("Ingrese el número de su asiento:"))
        pelicula.search(fila, numero)

        x = [opc, cant_tickets, fila, numero]
        
        return x
        
        
    @get_pelicula       
    def peliculas():
        x = ["Rapidos y furiosos 7","Matrix", "Godzilla", "Avengers: era de ultron"]
        return x
        
    
                
    