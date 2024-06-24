'''
Escreva um programa que lê uma frase e uma String antiga e uma String nova. O programa deve
imprimir uma String contendo a frase original, mas com a última ocorrência da String antiga
substituída pela String nova.
Exemplo:
Frase: "Quem parte e reparte fica com a maior parte"
String antiga: "parte"
String nova: "parcela"
Resultado a ser impresso no programa principal: "Quem parte e reparte
fica com a maior parcela"
'''

frase = "Quem parte e reparte fica com a maior parte"
string_antiga = "parte"
string_nova = "parcela"

partes = frase.rpartition(string_antiga)
frase_modificada = partes[0] + string_nova + partes[2]

print(f"Resultado: {frase_modificada}")
