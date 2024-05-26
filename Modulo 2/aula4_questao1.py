
# solicitando o usuario a entrada de dados, especificando qual o tipo, para garantir que o calculo ocorra
comprimento= int (input ('Digite o comprimento do terreno:'))
largura= int(input ('Digite a largura do terreno:'))
preco= float (input ('Digite o preço por metro quadrado:'))

# realizado os calculos necessarios de acordo com as entrandas fornecidas
area = comprimento*largura
preco_total = preco*area

# apresentando ao usuario a solucação. 
print (f"O terreno possui {area} m2 e custa R$' {preco_total}.")
