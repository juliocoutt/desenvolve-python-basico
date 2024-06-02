"""Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base 
na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote 
em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg"""


#solicitando os dados ao usuario 

distancia= float (input ("Qual a distancia para entrega em KM:  "))
peso= float (input ("Qual a peso em KG:  "))
frete = 0

if ( distancia >=100):
    frete = 1*distancia
    print(frete)
    if peso >= 10:
        frete= frete +10
        print(frete)
if ( distancia >100 and distancia <= 300):
    frete = 1.50*distancia
    print(frete)
    if peso >= 10:
        frete= frete +10
        print(frete)
if ( distancia > 300):
    frete = 2*distancia
    print(frete)
    if peso >= 10:
        frete= frete +10
        print(frete)