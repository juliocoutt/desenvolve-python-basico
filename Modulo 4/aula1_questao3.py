while True:
    # Solicitar três números do usuário
    n1, n2, n3 = map(int, input("Digite 3 números separados por espaço: ").split())

    # Calcular a média
    media = (n1 + n2 + n3) / 3

    # Verificar e imprimir o resultado baseado na média
    if media >= 60:
        print("Aprovado")
    elif media >= 40:
        print("Recuperação")
    else:
        print("Reprovado")
   
print("Fim")
