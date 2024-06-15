# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Inicializa uma lista para armazenar os índices das vogais
indices_vogais = []

# Inicializa uma variável para contar o número de vogais
contador_vogais = 0

# Percorre cada caractere na frase
for indice, caractere in enumerate(frase):
    # Verifica se o caractere é uma vogal
    if caractere.lower() in "aeiou":
        # Incrementa o contador de vogais
        contador_vogais += 1
        # Adiciona o índice da vogal à lista de índices
        indices_vogais.append(indice)

# Imprime o número de vogais na frase
print(f"{contador_vogais} vogais")

# Imprime os índices das vogais na frase
print("Índices", indices_vogais)
