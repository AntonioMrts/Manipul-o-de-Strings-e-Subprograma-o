def principal_secundaria(matriz):
    tam = len(matriz)
    soma_principal = 0
    soma_secundaria = 0

    for i in range(tam):
        soma_principal += matriz[i][i]
        soma_secundaria += matriz[i][tam - i - 1]
    return soma_principal, soma_secundaria

def linha_coluna(matriz):
    tam = len(matriz)
    soma_coluna = [0] * tam

    for i in range(tam):
        soma_linha = 0
        for j in range(tam):
            soma_linha += matriz[i][j]
            soma_coluna[j] += matriz[i][j]
    return soma_linha, soma_coluna

def quadrado_magico(matriz):
    soma_principal, soma_secundaria = principal_secundaria(matriz)
    soma_linha, soma_coluna = linha_coluna(matriz)

    if soma_principal == soma_secundaria == soma_linha == soma_coluna[0]:
        print("É um quadrado mágico.")
    else:
        print("Não é um quadrado mágico.")

matriz = [
    [2,7,6],
    [9,5,1],
    [4,3,8]
]

quadrado_magico(matriz)
