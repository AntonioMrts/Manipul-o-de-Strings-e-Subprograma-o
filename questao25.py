def bissexto():
    ano = int(input("Digite o ano: "))
    if ano % 4 == 0 or ano % 400 == 0:
        return True
    else:
        return False
    

print(bissexto())
