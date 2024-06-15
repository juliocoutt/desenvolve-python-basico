def data_por_extenso(data):
    # Dicionário com os nomes dos meses
    meses = {
        "01": "Janeiro",
        "02": "Fevereiro",
        "03": "Março",
        "04": "Abril",
        "05": "Maio",
        "06": "Junho",
        "07": "Julho",
        "08": "Agosto",
        "09": "Setembro",
        "10": "Outubro",
        "11": "Novembro",
        "12": "Dezembro"
    }
    
    # Divide a data em dia, mês e ano
    dia, mes, ano = data.split("/")
    
    # Retorna a data formatada
    return f"{dia} de {meses[mes]} de {ano}"

# Solicita a data de nascimento ao usuário
data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

# Imprime a data por extenso
print("Você nasceu em", data_por_extenso(data_nascimento))
