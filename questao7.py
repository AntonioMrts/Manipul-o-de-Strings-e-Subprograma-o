'''
Faça um programa que leia o nome do usuário e mostre o nome de traz para frente, utilizando somente
letras maiúsculas.
Exemplo:
Nome = Swainstainger
Resultado gerado pelo programa:
REGNIATSNIAWS
'''

nome = input("Digite seu nome: ")
contrario = ''

for i in range(len(nome) - 1, -1, -1):
    contrario += nome[i]

nome = contrario.upper()
print(nome)
