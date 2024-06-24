def calcular_potencia(base, expoente):
    resultado = 1
    for x in range(expoente):
        resultado *= base
    return resultado

base = int(input("Digite a base: "))
exp = int(input("Digite o expoente: "))

potencia = calcular_potencia(base, exp)
print(potencia)
