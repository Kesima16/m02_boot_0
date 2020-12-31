def sumaTodos(limiTo):
    resultado = 0
    for i in range(0, limiTo+1):
        resultado += 1
        
    return resultado

print(sumaTodos(100))


def sumaTodosLosCuadrados(limiTo):
    resultado = 0
    for i in range(limiTo+1):
        resultado += i*i
    
    return resultado

print(sumaTodos(100))
print(sumaTodosLosCuadrados(3))