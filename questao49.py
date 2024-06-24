def expandir_intervalos(string_intervalos):
    intervalos = string_intervalos.split(',')
    numeros_expandidos = []

    for intervalo in intervalos:
        if '-' in intervalo:
            inicio, fim = intervalo.split('-')
            inicio = int(inicio)
            fim = int(fim)
            numeros_expandidos += list(range(inicio, fim + 1))
        else:
            numeros_expandidos.append(int(intervalo))

    return numeros_expandidos

string = "1-3,5,6-10"
print(expandir_intervalos(string))
