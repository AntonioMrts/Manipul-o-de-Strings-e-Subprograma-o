def calcular_determinante(matriz):
    diagonal_principal = 1
    diagonal_secundaria = 1
    for i in range(len(matriz)):
        diagonal_principal *= matriz[i][i]
        diagonal_secundaria *= matriz[i][len(matriz) - 1 - i]
    subtracao = diagonal_principal - diagonal_secundaria
    return subtracao

matriz = [
    [2,3],
    [4,5]
]

determinante= calcular_determinante(matriz)
print(f"Determinante da matriz: {determinante}")
