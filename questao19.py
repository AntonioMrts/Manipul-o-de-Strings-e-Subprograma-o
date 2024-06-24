def inverter_ordem(frase):
    palavras = frase.split()
    palavras_invertida = " ".join(reversed(palavras))
    return palavras_invertida

frase = "A vida é feita de escolhas, e eu escolho ser feliz"
inverter = inverter_ordem(frase)
print(inverter)
