class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
    
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
            return
        elif self.peso >= 8:
            print('GUAU, GUAU')
        else:
            print('guau, guau')

class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad= e
        self.peso= p
    
    def ladrar(self):
        if self.peso >= 8:
            print('GUAU, GUAU')
        else:
            print('guau, guau')
    
    def __str__(self): #para que al hacer un print, nos de algo lógico
        return "Perro: {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)
        
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
        
    def __str__(self):
        return "Perro: {}, edad: {}, peso: {}, amo: {}".format(self.nombre, self.edad, self.peso, self.amo)
    
    def pasear(self):
        print("Yo, {}, ayudo a mi dueño {} a pasear".format(self.nombre, self.amo))

    def ladrar(self):
        if self.trabajando:
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
    
salchicho = Perro('Salchicho', 3, 1.5)
lola = Perro('Lola', 3, 15)
gerardo = PerroAsistencia('Gerardo', 5, 10, 'Roberto')
mike = Dog()
mike.nombre="Mike"
mike.peso= 3
mike.edad = 15