import csv
import os

# Estrutura de dados para armazenar usuários e produtos/serviços
usuarios = []
produtos_servicos = []

# Função para carregar dados de arquivo CSV
def carregar_arquivo(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    return data

# Função para salvar dados em arquivo CSV
def salvar_arquivo(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Funções CRUD para usuários
def criar_usuario(username, password, role):
    usuarios.append([username, password, role])
    salvar_arquivo('usuarios.csv', usuarios)

def ler_usuarios():
    return usuarios

def atualizar_usuario(username, new_password, new_role):
    for user in usuarios:
        if user[0] == username:
            user[1] = new_password
            user[2] = new_role
    salvar_arquivo('usuarios.csv', usuarios)

def deletar_usuario(username):
    global usuarios
    usuarios = [user for user in usuarios if user[0] != username]
    salvar_arquivo('usuarios.csv', usuarios)

# Funções CRUD para produtos/serviços
def criar_produto(nome, preco, quantidade):
    produtos_servicos.append([nome, preco, quantidade])
    salvar_arquivo('produtos_servicos.csv', produtos_servicos)

def ler_produtos():
    return produtos_servicos

def atualizar_produto(nome, novo_preco, nova_quantidade):
    for produto in produtos_servicos:
        if produto[0] == nome:
            produto[1] = novo_preco
            produto[2] = nova_quantidade
    salvar_arquivo('produtos_servicos.csv', produtos_servicos)

def deletar_produto(nome):
    global produtos_servicos
    produtos_servicos = [produto for produto in produtos_servicos if produto[0] != nome]
    salvar_arquivo('produtos_servicos.csv', produtos_servicos)

# Funções adicionais para produtos/serviços
def buscar_produto(nome):
    for produto in produtos_servicos:
        if produto[0] == nome:
            return produto
    return None

def listar_produtos_ordenados_por_nome():
    return sorted(produtos_servicos, key=lambda x: x[0])

def listar_produtos_ordenados_por_preco():
    return sorted(produtos_servicos, key=lambda x: x[1])

# Função de login
def login(username, password):
    for user in usuarios:
        if user[0] == username and user[1] == password:
            return user[2]
    return None

# Carregar dados dos arquivos CSV
usuarios = carregar_arquivo('usuarios.csv')
produtos_servicos = carregar_arquivo('produtos_servicos.csv')

# Função principal para executar o sistema
def main():
    print("Bem-vindo ao sistema de gerenciamento de empresa!")
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    role = login(username, password)
    if not role:
        print("Login falhou!")
        return

    print(f"Bem-vindo, {username}! Seu papel é: {role}")

    while True:
        print("\nMenu:")
        if role == 'gerente':
            print("1. Criar usuário")
            print("2. Ler usuários")
            print("3. Atualizar usuário")
            print("4. Deletar usuário")
        print("5. Criar produto/serviço")
        print("6. Ler produtos/serviços")
        print("7. Atualizar produto/serviço")
        print("8. Deletar produto/serviço")
        print("9. Buscar produto/serviço")
        print("10. Listar produtos/serviços por nome")
        print("11. Listar produtos/serviços por preço")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            break
        elif opcao == 1 and role == 'gerente':
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            role = input("Papel (gerente/funcionario/estagiario/cliente): ")
            criar_usuario(username, password, role)
        elif opcao == 2 and role == 'gerente':
            for user in ler_usuarios():
                print(user)
        elif opcao == 3 and role == 'gerente':
            username = input("Nome de usuário: ")
            new_password = input("Nova senha: ")
            new_role = input("Novo papel: ")
            atualizar_usuario(username, new_password, new_role)
        elif opcao == 4 and role == 'gerente':
            username = input("Nome de usuário: ")
            deletar_usuario(username)
        elif opcao == 5:
            nome = input("Nome do produto/serviço: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            criar_produto(nome, preco, quantidade)
        elif opcao == 6:
            for produto em ler_produtos():
                print(produto)
        elif opcao == 7:
            nome = input("Nome do produto/serviço: ")
            novo_preco = float(input("Novo preço: "))
            nova_quantidade = int(input("Nova quantidade: "))
            atualizar_produto(nome, novo_preco, nova_quantidade)
        elif opcao == 8:
            nome = input("Nome do produto/serviço: ")
            deletar_produto(nome)
        elif opcao == 9:
            nome = input("Nome do produto/serviço: ")
            produto = buscar_produto(nome)
            if produto:
                print(produto)
            else:
                print("Produto/serviço não encontrado!")
        elif opcao == 10:
            for produto em listar_produtos_ordenados_por_nome():
                print(produto)
        elif opcao == 11:
            for produto em listar_produtos_ordenados_por_preco():
                print(produto)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
