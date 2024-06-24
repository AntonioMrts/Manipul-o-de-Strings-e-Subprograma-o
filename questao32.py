def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero - 1):
        if numero % i == 0:
            return False
    return True

num = int(input("Digite o número: "))

if eh_primo(num):
    print("O número é primo")
else:
    print("Nao é primo")
