# Solicita a quantidade de experimentos registrados
N = int(input("Digite a quantidade de experimentos registrados: "))

# Inicializa variáveis para contar o total de cada tipo de cobaia e o total geral
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Lê os dados de cada experimento
for _ in range(N):
    dados = input("Digite a quantidade de cobaias e o tipo (S para sapo, R para rato, C para coelho): ")
    quantidade, tipo = dados.split()
    quantidade = int(quantidade)

    # Atualiza os contadores de acordo com o tipo de cobaia
    total_cobaias += quantidade
    if tipo == 'S':
        total_sapos += quantidade
    elif tipo == 'R':
        total_ratos += quantidade
    elif tipo == 'C':
        total_coelhos += quantidade

# Calcula os percentuais de cada tipo de cobaia
percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

# Exibe os resultados
print("Total de cobaias: {}".format(total_cobaias))
print("Total de sapos: {}".format(total_sapos))
print("Total de ratos: {}".format(total_ratos))
print("Total de coelhos: {}".format(total_coelhos))
print("Percentual de sapos: {:.2f}%".format(percentual_sapos))
print("Percentual de ratos: {:.2f}%".format(percentual_ratos))
print("Percentual de coelhos: {:.2f}%".format(percentual_coelhos))
