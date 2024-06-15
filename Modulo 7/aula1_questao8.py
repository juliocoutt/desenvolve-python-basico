def validar_cpf(cpf):
    # Remove os caracteres de formatação do CPF
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto
    
    # Verifica se o primeiro dígito verificador é igual ao fornecido pelo usuário
    if int(cpf[9]) != digito_verificador_1:
        return False
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto
    
    # Verifica se o segundo dígito verificador é igual ao fornecido pelo usuário
    if int(cpf[10]) != digito_verificador_2:
        return False
    
    # Se passou por todas as verificações, o CPF é válido
    return True

# Exemplo de uso
cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")
