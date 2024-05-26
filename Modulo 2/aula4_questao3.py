
# Solicita os dados do primeiro produto

nome_produto1 = input('Digite o nome do primeiro produto:')
preco_unitario1 = float(input('Digite o preço unitário do primeiro produto: '))
quantidade1 = int(input('Digite a quantidade do primeiro produto:'))

# Solicita os dados do segundo produto

nome_produto2 = input('Digite o nome do segundo produto:')
preco_unitario2 = float(input('Digite o preço unitário do segundo produto: '))
quantidade2 = int(input('Digite a quantidade do segundo produto:'))

# Solicita os dados do terceiro produto

nome_produto3 = input('Digite o nome do terceiro produto:')
preco_unitario3 = float(input('Digite o preço unitário do terceiro produto:'))
quantidade3 = int(input('Digite a quantidade do terceiro produto:'))

# Calcula o preço total de cada produto e a soma total
preco_total_produto1 = preco_unitario1 * quantidade1
preco_total_produto2 = preco_unitario2 * quantidade2
preco_total_produto3 = preco_unitario3 * quantidade3
preco_total = preco_total_produto1 + preco_total_produto2 + preco_total_produto3

# Imprime o preço total da compra
print(f"Total: R${preco_total:,.2f}")
