n = int(input("Digite a quantidade de números: "))

maior = 0

while n > 0:
    x = int(input("Digite o valor de X: "))
    
    if x > maior:
        maior = x

    n = n - 1

print("O maior número digitado foi", maior)
