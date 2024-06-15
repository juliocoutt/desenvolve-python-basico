def substituir_vogais_por_asterisco(frase):
    # Lista de vogais
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    # Substitui todas as vogais por "*"
    for vogal in vogais:
        frase = frase.replace(vogal, "*")
    
    return frase

# Solicita a frase ao usuário
frase_original = input("Digite uma frase: ")

# Substitui as vogais por "*"
frase_modificada = substituir_vogais_por_asterisco(frase_original)

# Imprime a frase modificada
print("Frase modificada:", frase_modificada)
