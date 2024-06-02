idade = int (input("Qual sua idade ?"))
jogo = int (input("Já jogou pelo menos 3 jogos de tabuleiro? "))
vitoria = int (input("Quantos jogos já venceu?"))

permisao= ((idade>=16 and idade<=18) and (jogo >=3) and (vitoria >=1))
print (f"Apto para ingressar no clube de jogos de tabuleiro: {permisao}")
