def converter_romano(romano):
    valores_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    resultado = 0

    for i in range(len(romano)):
        if i < len(romano) - 1 and valores_romanos[romano[i]] < valores_romanos[romano[i + 1]]:
            resultado -= valores_romanos[romano[i]]
        else:
            resultado += valores_romanos[romano[i]]
    
    return resultado

numero_romano = "XVI"
romano_inteiro = converter_romano(numero_romano)
print(romano_inteiro)
