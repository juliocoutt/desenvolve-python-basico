import random

def embaralhar_palavras(frase):
    palavras = frase.split()  # Divide a frase em uma lista de palavras
    frase_embaralhada = []
    for palavra in palavras:
        if len(palavra) > 3:  # Embaralha as letras internas se a palavra tiver mais de 3 caracteres
            caracteres = list(palavra[1:-1])  # Obtém os caracteres internos da palavra
            random.shuffle(caracteres)  # Embaralha os caracteres
            palavra_embaralhada = palavra[0] + ''.join(caracteres) + palavra[-1]  # Reconstrói a palavra
            frase_embaralhada.append(palavra_embaralhada)
        else:
            frase_embaralhada.append(palavra)  # Mantém palavras com 3 ou menos caracteres inalteradas
    return ' '.join(frase_embaralhada)  # Retorna a frase como uma string

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Saída possível: "Ptohn é uma lgaugniem de prgromaação"
