def nome_mes(numero_mes):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio",
             "junho", "julho", "agosto", "setembro", "outubro", 
             "novembro", "dezembro"]
    if numero_mes >= 1 and numero_mes <= 12:
        return meses[numero_mes - 1]
    else:
        return("Mes inválido")

numero_mes = 8
nome_do_mes = nome_mes(numero_mes)
print(nome_do_mes)
