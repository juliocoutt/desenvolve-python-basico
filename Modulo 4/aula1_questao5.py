participantes = int(input("Qual o número de participantes: "))

soma = 0
contador = 0

while contador < participantes:  # Deve ser '<' em vez de '<='
    idade = int(input("Digite a idade: "))
    soma += idade
    contador += 1

media = soma / participantes
print("A média de idades é de", media)
