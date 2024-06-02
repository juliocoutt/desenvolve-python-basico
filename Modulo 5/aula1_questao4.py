from datetime import datetime

# Obtém a data e hora atuais
data_hora_atual = datetime.now()

# Formata a data e hora conforme desejado
data_formatada = data_hora_atual.strftime("%d/%m/%Y")
hora_formatada = data_hora_atual.strftime("%H:%M")

# Exibe a data e hora formatadas
print("Data:", data_formatada)
print("Hora:", hora_formatada)
