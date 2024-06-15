import csv

# Função para verificar se uma linha deve ser ignorada devido a múltiplos artistas entre aspas
def deve_ignorar_linha(artist_name):
    return artist_name.startswith('"') and artist_name.endswith('"')

# Lista para armazenar as músicas mais populares de cada ano
musicas_populares = []

# Abre o arquivo CSV
with open('spotify-2023.csv', mode='r', encoding='latin-1') as arquivo_csv:
    csv_reader = csv.reader(arquivo_csv)
    
    # Ignora o cabeçalho
    next(csv_reader)
    
    # Dicionário para manter a música mais popular de cada ano
    musica_por_ano = {}

    # Processa cada linha do arquivo CSV
    for linha in csv_reader:
        # Extrai as informações relevantes
        track_name = linha[0].strip()
        artist_name = linha[1].strip()
        artist_count = int(linha[2].strip())
        released_year = int(linha[3].strip())
        streams = int(linha[8].strip())

        # Verifica se a linha deve ser ignorada devido a múltiplos artistas entre aspas
        if deve_ignorar_linha(artist_name):
            continue
        
        # Verifica se a música está dentro do intervalo de anos desejado (2012 a 2022)
        if released_year >= 2012 and released_year <= 2022:
            # Verifica se já temos uma música registrada para o ano atual
            if released_year not in musica_por_ano:
                musica_por_ano[released_year] = [track_name, artist_name, released_year, streams]
            else:
                # Compara o número de streams para decidir se esta música é mais popular
                if streams > musica_por_ano[released_year][3]:
                    musica_por_ano[released_year] = [track_name, artist_name, released_year, streams]

    # Converte o dicionário em uma lista no formato solicitado
    musicas_populares = list(musica_por_ano.values())

# Ordena a lista pelo ano de lançamento
musicas_populares.sort(key=lambda x: x[2])

# Imprime a lista de músicas populares
for musica in musicas_populares:
    print(musica)
