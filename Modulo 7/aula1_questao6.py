from itertools import permutations

# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Solicita ao usuário que digite a palavra objetivo
palavra_objetivo = input("Digite a palavra objetivo: ")

# Gera todas as permutações possíveis da palavra objetivo
permutacoes = [''.join(p) for p in permutations(palavra_objetivo)]

# Inicializa uma lista para armazenar os anagramas encontrados na frase
anagramas = []

# Verifica se cada permutação está presente na frase e adiciona à lista de anagramas se estiver
for permutacao in permutacoes:
    if permutacao.lower() in frase.lower():
        anagramas.append(permutacao)

# Imprime os anagramas encontrados
print("Anagramas:", anagramas)
