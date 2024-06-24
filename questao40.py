def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True

def gerar_lista_primos(n):
    lista_primos = []
    num = 2
    while len(lista_primos) < n:
        if eh_primo(num):
            lista_primos.append(num)
        num += 1
    return lista_primos

n = int(input("Digite os n números primos: "))
numeros_primos = gerar_lista_primos(n)
print(numeros_primos)
