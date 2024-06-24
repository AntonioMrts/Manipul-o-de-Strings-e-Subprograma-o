def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]

    metade_esquerda = merge_sort(metade_esquerda)
    metade_direita = merge_sort(metade_direita)

    return mesclar(metade_esquerda, metade_direita)

def mesclar(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado += esquerda[i:]
    resultado += direita[j:]

    return resultado

lista = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(lista)
print(lista_ordenada)
