def crescente(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista_numeros = [10,5,22,6,2,8,1]
crescente = crescente(lista_numeros)
print(crescente)
