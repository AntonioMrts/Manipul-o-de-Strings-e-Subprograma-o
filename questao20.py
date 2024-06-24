def validar_email(usuario, dominio):
    validar = False 

    if "@" in usuario and ".com" in dominio:
        validar = True
    else:
        validar = False
    
    return validar

email = input("Digite seu email: ")

usuario = email.partition("@")
dominio = email.partition(".com")

validar = validar_email(usuario, dominio)

if validar:
    print("Email é válido.")
else:
    print("Email não é valido.")
