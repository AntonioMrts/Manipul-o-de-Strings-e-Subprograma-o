def fibonacci(n):
    ultimo = 0
    penultimo = 1
    cont = 0
    if n == 1 and n == 2:
        print(1)
    else:
        while cont < n:
            termo = ultimo + penultimo
            ultimo = penultimo
            penultimo = termo
            cont += 1
        return termo

numero = 8
sequencia = fibonacci(numero)
print(sequencia)
