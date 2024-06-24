'''
Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma
é igual à outra quando lida de traz para frente.
Exemplo: amor e roma.
'''

string1 = input("Digite uma palvra: ").lower()
string2 = input("Digite outra palavra: ").lower()

if string1 == string2[::-1] and string2 == string1[::-1]:
    print("As palavras são palíndromas mútuas.")
else:
    print("As palavras não são palíndromas.")
