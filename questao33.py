def numero_vogais(frase):
    vogais = "aeiou"
    quantidade = 0
    for vogal in vogais:
        qtd_vogais = frase.count(vogal)
        quantidade += qtd_vogais
    return quantidade

frase = input("Digite uma frase:")

cont_vogais = numero_vogais(frase)
print(f" O texto possui {cont_vogais} vogais")
