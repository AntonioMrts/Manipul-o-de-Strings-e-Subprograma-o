def calcular_combinacoes(N, M):
    def fatorial(num):
        if num == 0:
            return 1
        return num * fatorial(num - 1)

    combinacoes = fatorial(N) // (fatorial(M) * fatorial(N - M))
    return combinacoes

N = int(input("Digite o valor de N (total de alunos): "))
M = int(input("Digite o valor de M (alunos em um dos grupos): "))

resultado = calcular_combinacoes(N, M)
print(f"O número de combinações possíveis é: {resultado}")
