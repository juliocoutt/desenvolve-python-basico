import random

# Gera um número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

# Loop para adivinhar o número
while True:
    # Solicita ao usuário que adivinhe o número
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    
    # Verifica se o palpite é correto
    if palpite == numero_aleatorio:
        print("Correto! O número é", numero_aleatorio)
        break
    elif palpite < numero_aleatorio:
        print("Muito baixo, tente novamente!")
    else:
        print("Muito alto, tente novamente!")
