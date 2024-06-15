import string

def limpar_palavra(palavra):
    # Remove caracteres não alfabéticos e converte para minúsculas
    palavra_limpa = ''.join(caracter for caracter in palavra if caracter.isalpha())
    return palavra_limpa.lower()

def main():
    # Nome dos arquivos
    arquivo_entrada = "frase.txt"
    arquivo_saida = "palavras.txt"
    
    # Lê a frase do arquivo de entrada
    with open(arquivo_entrada, 'r') as arquivo:
        frase = arquivo.read().strip()
    
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Lista para armazenar palavras limpas
    palavras_limpas = []
    
    # Limpa cada palavra e adiciona na lista
    for palavra in palavras:
        palavra_limpa = limpar_palavra(palavra)
        if palavra_limpa:
            palavras_limpas.append(palavra_limpa)
    
    # Escreve as palavras limpas no arquivo de saída
    with open(arquivo_saida, 'w') as arquivo:
        for palavra in palavras_limpas:
            arquivo.write(palavra + '\n')
    
    # Imprime o conteúdo do arquivo de saída
    with open(arquivo_saida, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

if __name__ == "__main__":
    main()

