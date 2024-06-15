def main():
    # Solicita uma frase do usuário
    frase = input("Digite uma frase: ")
    
    # Nome do arquivo onde a frase será salva
    nome_arquivo = "frase.txt"
    
    # Salva a frase no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(frase)
    
    # Obtém o caminho completo do arquivo
    import os
    caminho_completo = os.path.abspath(nome_arquivo)
    
    # Imprime o caminho completo do arquivo salvo
    print(f"Frase salva em {caminho_completo}")

if __name__ == "__main__":
    main()
