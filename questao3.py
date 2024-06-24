'''
Faça um programa que lê uma frase e retorna o número de palavras que a frase contém. Considere que
a palavra pode começar e/ou terminar por espaços.
'''

frase = input("Digite a frase: ")
frase = frase.split(" ")

numero_palavras = len(frase)

print(f"Essa frase contém {numero_palavras} número de palavras.")
