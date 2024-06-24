def interseccao(lista1, lista2):
    lista = []
    for elemento in lista1:
        if elemento in lista1 and elemento in lista2 and not elemento in lista:
            lista.append(elemento)
        
    return lista

num1 = [4,7,2,8,9,3,4,2,5,1]
num2 = [6,7,2,9,11,4,2,5,8,]

lista = interseccao(num1, num2)

print(lista)
