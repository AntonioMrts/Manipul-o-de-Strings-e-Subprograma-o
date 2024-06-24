'''
Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando
apenas letras maiúsculas.
Exemplo:
Nome =Vanessa
Resultado gerado pelo programa:
V
VA
VAN
VANE
VANES
VANESS
VANESSA
'''

nome = input("Digite seu nome: ").upper()

for i in range(1, len(nome) + 1):
    print(nome[:i])
