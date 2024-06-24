import math

def calcular_area_perimetro():
    figura = input("1. Circuferência\n2.Triângulo\n3.Retângulo\nQual o tipo de figura: ")

    if figura == "1":
        raio = float(input("Qual o tamanho do raio da circuferência: "))
        area = math.pi * raio ** 2
        perimetro = 2 * math.pi * raio
        print(f"Tamanho da área: {area:.2f}")
        print(f"Tamanho do perímetro: {perimetro:.2f}")
    elif figura == "2":
        lado1 = float(input("Informe o lado1 do triangulo: "))
        lado2 = float(input("Informe o lado2 do triangulo: "))
        lado3 = float(input("Informe o lado3 do triangulo: "))
        base = float(input("Informe a base do triangulo: "))
        altura = float(input("informe a altura do triangulo: "))
        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3
        print(f"Área do triangulo: {area}")
        print(f"Perimtero do triangulo: {perimetro}")
    elif figura == "3":
        base = float(input("Informe a base do retangulo: "))
        altura = float(input("Informe a altura do retangulo: "))
        area = base * altura
        perimetro = 2 * (base + altura)
        print(f"Area do retangulo: {area}")
        print(f"Perimetro do retangulo: {perimetro}")
    else:
        print("Opção inválida.")

calcular_area_perimetro()
