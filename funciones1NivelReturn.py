def maximo(*l):
    if len(l) == 0:
        return 0
    n = l[0]
    for i in range(1, len(l)):
        if l[i] > n:
            n = l[i]
    return n
            

def minimo(*l):
    if len(l) == 0:
        return 0
    n = l[0]
    for i in range(1, len(l)):
        if l[i] < n:
            n = l[i]
    return n

def media(*l):
    if len(l) == 0:
        return 0
    
    suma = 0
    for valor in l:
        suma += valor
    
    return suma/len(l)

funciones = {
    'max': maximo,
    'min': minimo,
    'med': media
}

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    
    return None
   
returnF('max')(1, 3, -1, 15, 9)