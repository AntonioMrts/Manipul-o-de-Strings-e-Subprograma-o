string1 = input("Informe o conteúdo: ")
string2 = input("Informe mais um conteúdo: ")

tam1 = len(string1)
tam2 = len(string2)

print(f"Tamanho de '{string1}': {tam1} caracteres.\nTamanho de {string2}: {tam2} caracteres.")

if tam1 == tam2:
    print("As strings tem o mesmo tamanho.")
else:
    print("As strings são de tamanhos diferentes.")

if string1 == string2:
    print("As strings possuem o mesmo conteúdo.")
else:
    print("As strings possuem conteúdos diferentes.")
