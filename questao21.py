def minusculas(texto):
    return texto.lower()

def remover_acentos(texto):
     acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e', 'í': 'i', 'ó': 'o',
        'ô': 'o', 'õ': 'o', 'ú': 'u', 'ü': 'u',
        'ç': 'c',
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A',
        'É': 'E', 'Ê': 'E', 'Í': 'I', 'Ó': 'O',
        'Ô': 'O', 'Õ': 'O', 'Ú': 'U', 'Ü': 'U',
        'Ç': 'C'
    }
     texto_sem_acentos = ""
     for letra in texto:
         if letra in acentos:
             texto_sem_acentos += acentos[letra]
         else:
             texto_sem_acentos += letra
     return texto_sem_acentos

def remover_caracteres_especiais(texto):
    caracteres_especiais = ['?','!', '@', '#', '$', '%', '&', '*']

    texto_sem_caracteres = ""
    for letra in texto:
        if letra not in caracteres_especiais:
            texto_sem_caracteres += letra
    return texto_sem_caracteres

def normalizar_texto(texto):
    texto = minusculas(texto)
    texto = remover_acentos(texto)
    texto = remover_caracteres_especiais(texto)
    return texto

texto = input("Digite o texto: ")
texto_normalizado = normalizar_texto(texto)
print(texto_normalizado)
