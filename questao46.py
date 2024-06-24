def intercalar_strings(str1, str2):
    resultado = ''
    tamanho_maximo = max(len(str1), len(str2))

    for i in range(tamanho_maximo):
        if i < len(str1):
            resultado += str1[i]
        if i < len(str2):
            resultado += str2[i]

    return resultado

str1 = "Eu não estou suportando mais."
str2 = "Minha mente está explodindo."
print(intercalar_strings(str1, str2))
