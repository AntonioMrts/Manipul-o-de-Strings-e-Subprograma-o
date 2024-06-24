def distancia_euclediana(ponto1, ponto2):
    soma = 0

    for i in range(len(ponto1)):
        diferenca = ponto1[i] - ponto2[i]
        soma += diferenca ** 2
        
    distancia = soma ** 0.5
    
    return distancia

px1 = (1,2,3)
py1 = (4,5,6)
distancia = distancia_euclediana(px1, py1)
print(f"Distância: {distancia:.2f}")
