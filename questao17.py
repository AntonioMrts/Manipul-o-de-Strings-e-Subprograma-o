texto = input("Digite um texto: ").lower()
texto = texto.split()

dicio = {"vc": "você", "obg": "obrigado", "ex": "exemplo", "blz": "beleza", "ctz" : "certeza", 
       "plmds": "pelo amor de Deus" }

texto_aux = ""

for palavra in texto:
    if palavra in dicio:
        texto_aux += " " + dicio[palavra]
    else:
        texto_aux += " " + palavra

texto = texto_aux

print(texto)
