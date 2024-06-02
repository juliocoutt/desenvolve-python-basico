"""
### Q5.

Você está projetando um sistema de autenticação baseado na análise da íris (parte colorida do olho). Ao acionado, o sistema coleta 
e retorna 3 valores inteiros referentes a atributos da íris visível. Mas o sistema não é perfeito, tendo uma margem de erro do sensor 
de +/- $5$. 

O código abaixo tem os atributos dos 4 usuários cadastrados no sistema. Você deve completar om código, pedindo ao usuário para inserir 
uma nova leitura de padrão de íris. O programa deve comparar o padrão inserido com os padrões cadastrados no banco de dados. Se o padrão
 estiver dentro da tolerância estabelecida, o usuário é autenticado com sucesso. Caso contrário, a autenticação falha.

**Dica:** A função do python ```abs()``` retorna o valor absoluto de um elemento. Ex: 
```
>>> print(abs(987-982))
5
>>> print(abs(987-992))
5
```

Seguem alguns exemplos de interação com seu código no terminal.

```
Insira o padrão de íris para autenticação.
Atributo 1: 111
Atributo 2: 222
Atributo 3: 333
Autenticação bem-sucedida! 
Usuário: 3
```

```
Insira o padrão de íris para autenticação.
Atributo 1: 111
Atributo 2: 200
Atributo 3: 333
Autenticação falhou! 
```

```
Insira o padrão de íris para autenticação.
Atributo 1: 982
Atributo 2: 653
Atributo 3: 324
Autenticação bem-sucedida! 
Usuário: 2
```

"""

# Padrões cadastrados dos usuários
usuarios = {
    "Usuario1": [982, 1001, 990],
    "Usuario2": [975, 995, 988],
    "Usuario3": [990, 1010, 1005],
    "Usuario4": [1002, 980, 997]
}

def autenticar_usuario(entrada):
    for usuario, padrao in usuarios.items():
        if all(abs(entrada[i] - padrao[i]) <= 5 for i in range(len(entrada))):
            return True, usuario
    return False, None

def main():
    entrada = []
    print("Insira os valores dos atributos da íris:")
    for i in range(3):
        atributo = int(input(f"Atributo {i+1}: "))
        entrada.append(atributo)

    autenticado, usuario_autenticado = autenticar_usuario(entrada)

    if autenticado:
        print(f"Usuário autenticado: {usuario_autenticado}")
    else:
        print("Autenticação falhou.")

if __name__ == "__main__":
    main()
