from functools import reduce

def doble(x):
    return x+x

lista = [1, 3, -1, 15, 9]

listaDobles= map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)

listaPares = filter(lambda x: x % 2 == 0, listaDobles)

sumatorio = reduce(lambda x, y: x + y, lista) ##x es el acumulado, y son los valores
sumatorio1 = reduce(lambda x, y:x + y, range(101))