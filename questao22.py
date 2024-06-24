def verificar_balanceamento(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == '(' or caractere == '[' or caractere == '{':
            pilha.append(caractere)
        elif caractere == ')' and (not pilha or pilha.pop() != '('):
            return False
        elif caractere == ']' and (not pilha or pilha.pop() != '['):
            return False
        elif caractere == '}' and (not pilha or pilha.pop() != '{'):
            return False

    return not pilha

expressao = "({[}])"
balanceada = verificar_balanceamento(expressao)
print(balanceada)
