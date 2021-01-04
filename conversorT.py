class Termometro():
    def __init__(self):
        self.__unidadM = "C"
        self.__temperatura = 0
        
    def __conversor(self, temperatura, unidad):
        if unidad == "C":
            return "{} ºF".format(temperatura * 9/5 + 32)
        if unidad == "F":
            return "{} ºC".format((temperatura-32) *5/9)
        else:
            return "Unidad incorrecta"
        
    def __str__(self):
        return "{}º {}".format(self.temperatura, self.unidadM)
    
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == "F" or uniM == "C":
                self.__unidadM=uniM
                
    def temp(self, temperatura=None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, uniM=None): # Si queremos convertirlo en la medida que hemos metido, imprimirá lo que has metido. Si es diferente la medida, hará el conversor
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura, self.__unidadM)