import random
from math import sqrt

# Solicita ao usuário o valor de n
n = int(input("Digite o valor de n: "))

# Gera n valores inteiros aleatórios entre 0 e 100 e calcula a soma
valores = [random.randint(0, 100) for _ in range(n)]
soma = sum(valores)

# Calcula a raiz quadrada da soma dos valores
raiz_quadrada_soma = sqrt(soma)

# Exibe o resultado
print("A raiz quadrada da soma dos {} valores aleatórios é: {:.2f}".format(n, raiz_quadrada_soma))
