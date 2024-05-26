comprimento= int (input ('Digite o comprimento do terreno:'))
largura= int(input ('Digite a largura do terreno:'))
preco= float (input ('Digite o preço por metro quadrado:'))

area = comprimento*largura
preco_total = preco*area

print (f"O terreno possui {area} m2 e custa R$' {preco_total}.")
