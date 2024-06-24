def binario_para_decimal(numero_binario):
    decimal = 0
    for digito in numero_binario:
        decimal = decimal * 2 + int(digito)
    return decimal

binario = input("Digite o número binário: ")
print(f"O número {binario} convertido para decimal é: {binario_para_decimal(binario)}")
