# Solicita ao usuário que insira os dois números decimais
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta entre os dois números e arredonda para duas casas decimais
diferenca_absoluta = round(abs(numero1 - numero2), 2)

# Exibe o resultado
print("A diferença absoluta entre os números é:", diferenca_absoluta)
