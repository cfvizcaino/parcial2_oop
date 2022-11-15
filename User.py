class User:    
    def register(self):
        print("Por favor registrese")
        __username = input("Ingrese su username: ")
        password = input("Ingrese su password: ")
        email = input("Ingrese su email: ")
        print("Ingrese su silla de preferencia")
        fila = input("Ingrese la fila (de la a hasta la f): ")
        numero = input("Ingrese el número de la fila (1 a 11): ")
        while numero < 1 and numero > 11:
            numero = input("Ingrese el número de la fila (1 a 11): ")
        
        self.username = __username
        self.email = email
        self.password = password
        self.fila = fila
        self.numero = numero
        
    def sillas():
        x = {
            "a" : ["1","2","3","4","5","6","7","8","9","10","11"],
            "b" : ["1","2","3","4","5","6","7","8","9","10","11"],
            "c" : ["1","2","3","4","5","6","7","8","9","10","11"],
            "d" : ["1","2","3","4","5","6","7","8","9","10","11"],
            "e" : ["1","2","3","4","5","6","7","8","9","10","11"],
            "f" : ["1","2","3","4","5","6","7","8","9","10","11"],   
        }
        return x
    
    