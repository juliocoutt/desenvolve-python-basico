import random

# Função para ler as palavras do arquivo "gabarito_forca.txt"
def ler_palavras():
    try:
        with open("gabarito_forca.txt", "r") as arquivo:
            palavras = arquivo.read().splitlines()
        return palavras
    except FileNotFoundError:
        print("Arquivo 'gabarito_forca.txt' não encontrado.")
        return []

# Função para ler os estágios do enforcado do arquivo "gabarito_enforcado.txt"
def ler_estagios_enforcado():
    try:
        with open("gabarito_enforcado.txt", "r") as arquivo:
            estagios_enforcado = arquivo.read().strip().split("\n\n")
        return estagios_enforcado
    except FileNotFoundError:
        print("Arquivo 'gabarito_enforcado.txt' não encontrado.")
        return []

# Função para imprimir a palavra oculta com underscores para letras não reveladas
def exibir_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra + " "
        else:
            palavra_oculta += "_ "
    return palavra_oculta.strip()

# Função para imprimir o enforcado de acordo com o número de erros
def imprime_enforcado(erros):
    if erros > len(estagios_enforcado) - 1:
        erros = len(estagios_enforcado) - 1  # Caso haja mais erros do que estágios definidos

    print(estagios_enforcado[erros])

# Função principal do jogo da forca
def jogar_forca():
    # Ler palavras do arquivo
    palavras = ler_palavras()
    if not palavras:
        return

    # Escolher uma palavra aleatoriamente
    palavra_sorteada = random.choice(palavras).upper()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6
    erros = 0

    # Ler estágios do enforcado
    estagios_enforcado = ler_estagios_enforcado()
    if not estagios_enforcado:
        return

    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra secreta.")
    print(exibir_palavra_oculta(palavra_sorteada, letras_corretas))

    while True:
        # Verificar se o jogador ganhou
        if all(letra in letras_corretas for letra in palavra_sorteada):
            print("Parabéns! Você acertou a palavra!")
            break

        # Verificar se o jogador perdeu
        if erros >= tentativas:
            print("Você perdeu! A palavra era:", palavra_sorteada)
            break

        # Pedir ao jogador para adivinhar uma letra
        letra = input("Digite uma letra: ").strip().upper()

        # Validar entrada do jogador
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        # Verificar se a letra já foi tentada
        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        # Verificar se a letra está na palavra sorteada
        if letra in palavra_sorteada:
            letras_corretas.add(letra)
            print("Letra correta!")
            print(exibir_palavra_oculta(palavra_sorteada, letras_corretas))
        else:
            letras_erradas.add(letra)
            erros += 1
            print("Letra errada!")
            imprime_enforcado(erros)
            print(exibir_palavra_oculta(palavra_sorteada, letras_corretas))

# Executar o jogo
if __name__ == "__main__":
    jogar_forca()
