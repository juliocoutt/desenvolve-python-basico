def remover_pontuacao_e_espacos(frase):
    # Lista de caracteres de pontuação e espaços em branco
    caracteres_pontuacao = ''',.!?;:()[]{}"'<>'''
    # Remove todos os caracteres de pontuação e espaços em branco da frase
    frase_sem_pontuacao = ''.join(caracter for caracter in frase if caracter not in caracteres_pontuacao)
    # Retorna a frase sem pontuação e espaços em branco, convertida para minúsculas
    return frase_sem_pontuacao.lower()

def verificar_palindromo(frase):
    # Remove pontuação e espaços em branco da frase
    frase = remover_pontuacao_e_espacos(frase)
    # Verifica se a frase é igual à sua forma invertida
    if frase == frase[::-1]:
        return True
    else:
        return False

# Loop para verificar palíndromos até que o usuário digite "Fim"
while True:
    # Solicita uma frase ao usuário
    frase = input("Digite uma frase (digite 'fim' para encerrar): ")
    # Verifica se o usuário deseja encerrar o programa
    if frase.lower() == 'fim':
        break
    # Verifica se a frase é um palíndromo e imprime o resultado
    if verificar_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
