def retrocontador(valor):
        sumatorio += valor
        print("{},".format(valor), end="")
        if valor > 0:
            retrocontador(valor-1)
        print("La suma total es", sumatorio)
    
def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    return 0

sumatorio(4)


