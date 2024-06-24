telefone = input("Digite o numero de telefone (7 dígitos): ")

traco = telefone.replace("-", "")

if len(telefone) == 7:
    telefone_corrigido = '3' + telefone
    telefone_formatado = telefone_corrigido[:4] + '-' + telefone_corrigido[4:]
    print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
    print("Telefone corrigido sem formatação:", telefone_corrigido)
    print("Telefone corrigido com formatação:", telefone_formatado)
else:
    print(f"Numero de telefone valido: {telefone}")
