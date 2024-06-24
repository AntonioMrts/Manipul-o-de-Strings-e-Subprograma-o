def verifica_subsequencia(str1, str2):
    at_str1 = 0
    
    for caracter in str2:
        if at_str1 < len(str1) and caracter == str1[at_str1]:
            at_str1 += 1

    return at_str1 == len(str1)

str1 = "abc"
str2 = "aabbcc"
resultado = verifica_subsequencia(str1, str2)
print(resultado)  
