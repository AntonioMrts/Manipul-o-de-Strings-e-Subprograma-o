'''
Faça um programa que lê uma String que representa uma cadeia de DNA e gera a cadeia complementar.
Exemplo:
 Entrada: AATCTGCAC
 Saída: TTAGACGTG
'''

dna = input("Digite a cadeia de DNA: ").upper()
cadeia_complementar = []

for i in range(len(dna)):
    if dna[i] == "A":
        cadeia_complementar.append("T")
    elif dna[i] == "T":
        cadeia_complementar.append("A")
    elif dna[i] == "C":
        cadeia_complementar.append("G")
    elif dna[i] == "G":
        cadeia_complementar.append("C")
print(cadeia_complementar)
