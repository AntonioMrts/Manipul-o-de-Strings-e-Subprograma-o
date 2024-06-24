def remove_duplicatas(lista):
    lista_sem_duplicata = []
    for elementos in lista:
        if elementos not in lista_sem_duplicata:
            lista_sem_duplicata.append(elementos)
    return lista_sem_duplicata

lista1 = [4, 6, 8, 6, 12, 7, 2, 2]

lista_sem_duplicata = remove_duplicatas(lista1)
print(lista_sem_duplicata)
