import emoji

# Lista de emojis sugeridos com seus códigos
emojis_disponiveis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

# Apresenta os emojis disponíveis com seus códigos
print("Emojis disponíveis:")
for codigo, emoji_valor in emojis_disponiveis.items():
    print(f"{emoji_valor} - {codigo}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada: ")

# Decodifica a frase e apresenta ela emojizada
frase_emojizada = emoji.emojize(frase_codificada, aliases=emojis_disponiveis)
print("\nFrase emojizada:")
print(frase_emojizada)
