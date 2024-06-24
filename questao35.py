def calcular_media(lista):
    if len(lista) == 0:
        return 0 
    else:
        soma = 0
        for elementos in lista:
            soma += elementos
        media = soma / len(lista)
        return media

lista = [8,9.5,7,7.5]
media = calcular_media(lista)
print(media)
