def compressa_string(texto):
    compressa_string = ""
    pala_cont = {}

    for palavra in texto:
        if palavra in pala_cont:
            pala_cont[palavra] += 1
        else:
            pala_cont[palavra] = 1

    for palavra in pala_cont:
        compressa_string += palavra + str(pala_cont[palavra])
    return compressa_string

original_string = "aaabbc"
compressed_result = compressa_string(original_string)
print(compressed_result)
