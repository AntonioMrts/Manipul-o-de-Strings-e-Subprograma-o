'''
Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase.
Por exemplo, "Iracema" é um anagrama para "America". Escreva um programa que decida se uma
String é um anagrama de outra String, ignorando os espaços em branco. O programa deve considerar
maiúsculas e minúsculas como sendo caracteres iguais, ou seja, "a" = "A".
'''

anagrama1 = input("Digite a palavra: ")
anagrama2 = input("Digite a palavra: ")

str1 = anagrama1.replace(" ", "").lower()
str2 = anagrama2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("As strings são anagramas.")
else:
    print("As strings não são anagramas.")
