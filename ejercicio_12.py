l = [6, 3, -2, 5, -8, 2, 3, -2, 1]


def ordena_positivos(lista):
    positivos = []
    for pos in lista:
        if pos > 0:
            positivos.append(pos)
    positivos.sort()
    for i in range(len(lista)):
        if lista[i] > 0:
            lista[i] = positivos[0]
            positivos.remove(positivos[0])


print(l)
ordena_positivos(l)
print(l, " resultado de la definición", )
