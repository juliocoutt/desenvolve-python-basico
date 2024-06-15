import csv

# Dados dos livros
livros = [
    {"Título": "Harry Potter and the Sorcerer's Stone", "Autor": "J.K. Rowling", "Ano de publicação": 1997, "Número de páginas": 320},
    {"Título": "To Kill a Mockingbird", "Autor": "Harper Lee", "Ano de publicação": 1960, "Número de páginas": 281},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "The Catcher in the Rye", "Autor": "J.D. Salinger", "Ano de publicação": 1951, "Número de páginas": 277},
    {"Título": "Pride and Prejudice", "Autor": "Jane Austen", "Ano de publicação": 1813, "Número de páginas": 279},
    {"Título": "The Hobbit", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1937, "Número de páginas": 310},
    {"Título": "The Great Gatsby", "Autor": "F. Scott Fitzgerald", "Ano de publicação": 1925, "Número de páginas": 180},
    {"Título": "The Da Vinci Code", "Autor": "Dan Brown", "Ano de publicação": 2003, "Número de páginas": 454},
    {"Título": "The Alchemist", "Autor": "Paulo Coelho", "Ano de publicação": 1988, "Número de páginas": 197},
    {"Título": "The Hitchhiker's Guide to the Galaxy", "Autor": "Douglas Adams", "Ano de publicação": 1979, "Número de páginas": 224}
]

# Nome do arquivo CSV
nome_arquivo = "meus_livros.csv"

# Abrir o arquivo CSV para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Criar o escritor CSV
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escrever a linha de cabeçalho
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escrever os dados dos livros
    for livro in livros:
        escritor_csv.writerow([livro["Título"], livro["Autor"], livro["Ano de publicação"], livro["Número de páginas"]])

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
