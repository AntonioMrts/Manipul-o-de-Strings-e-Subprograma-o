def contar_palavras(frase):
    cont = frase.split()
    return len(cont)

frase = input("Digite uma frase: ")
print(f"Essa string tem {contar_palavras(frase)} palavras.")
