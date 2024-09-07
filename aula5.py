def inverte_string(string):
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

# Entrada (pode ser fixa ou input do usuário)
string_original = input("Informe uma string: ")
string_invertida = inverte_string(string_original)

print(f"String invertida: {string_invertida}")
