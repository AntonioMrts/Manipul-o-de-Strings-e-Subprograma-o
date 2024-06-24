frase = input("Digite a frase: ")

quantidade_espacos = frase.count(" ")
print(f"Espaços em branco: {quantidade_espacos}")

contador_vogais = 0
vogais = "aeiou"

for caractere in frase:
    if caractere.lower() in vogais:
        contador_vogais += 1

print(f"Quantidade de vogais: {contador_vogais}")
