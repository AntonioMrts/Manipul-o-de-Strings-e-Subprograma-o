def palavra_censurada(texto, palavra):
    palavras = texto.split()
    texto_censurado = ""
    for i in range(len(palavras)):
        if palavras[i] == palavra:
            palavras[i] = "*" * len(palavra)
        texto_censurado += palavras[i] + " "
    return texto_censurado

texto = input("Digite o texto: ")
censura = input("Digite a palavra à ser censurada: ")
texto_censurado = palavra_censurada(texto, censura)
print(texto_censurado)
