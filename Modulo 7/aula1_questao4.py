# Solicita ao usuário que digite um número de celular
numero = input("Digite o número: ")

# Verifica o comprimento do número
if len(numero) == 8:  # Se tiver apenas 8 dígitos
    numero_completo = "9" + numero
elif len(numero) == 9:  # Se tiver 9 dígitos
    if numero[0] == "9":  # Verifica se o primeiro dígito é 9
        numero_completo = numero[:5] + "-" + numero[5:]  # Adiciona o separador "-" na posição correta
    else:
        numero_completo = numero  # Não faz nenhuma modificação
else:
    numero_completo = numero  # Se tiver mais de 9 dígitos, não faz nenhuma modificação

# Imprime o número completo
print("Número completo:", numero_completo)
