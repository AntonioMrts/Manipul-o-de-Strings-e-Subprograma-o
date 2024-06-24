def calcular_media():
    media = (nota1 + nota2 + nota3) / 3
    if media >= 6:
        print("Aprovado")
    elif media >= 4:
        print("Verificação Suplementar")
    else:
        print("Reprovado")
    return media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media()
print(f"Sua média é: {media:.2f}")

