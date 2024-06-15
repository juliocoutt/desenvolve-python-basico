import random

def encrypt(nomes):
    # Gera um valor n aleatório entre 1 e 10
    chave_aleatoria = random.randint(1, 10)
    
    # Inicializa uma lista para armazenar os nomes criptografados
    nomes_cript = []
    
    # Percorre cada nome na lista de nomes
    for nome in nomes:
        nome_criptografado = ""
        # Percorre cada caractere no nome
        for char in nome:
            # Verifica se o caractere está dentro do intervalo de caracteres visíveis
            if ord(char) >= 33 and ord(char) <= 126:
                # Calcula o novo caractere criptografado usando o valor de chave aleatório
                novo_char = chr((ord(char) - 33 + chave_aleatoria) % 94 + 33)
                nome_criptografado += novo_char
            else:
                # Se estiver fora do intervalo, mantém o caractere original
                nome_criptografado += char
        # Adiciona o nome criptografado à lista de nomes criptografados
        nomes_cript.append(nome_criptografado)
    
    # Retorna os nomes criptografados e a chave de criptografia
    return nomes_cript, chave_aleatoria


