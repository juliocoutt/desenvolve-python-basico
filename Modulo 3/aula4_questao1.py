#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, 
#o número é par, caso contrário é ímpar. 
#Lembre-se do operador do python % que retorna o resto de uma divisão.

#solicitando a leitura dos dados para o úsuario

n1= int (input ("Digite o primeiro número: "))
n2= int (input ("Digite o segundo número: "))

#processamento 

resto= (n1+n2)%2

if resto == 0:
    print("Par")
if resto == 1:
    print("Impar")