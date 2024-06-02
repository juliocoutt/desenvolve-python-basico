#solicitando a classe dos personagens 

classe_personagem = input ("Classe: ")
pontos_de_magia = int (input ("Magia: "))
pontos_de_forca = int (input ("Força: "))


#procesamento 

#  Como fazer o comparativo sem usar IF e Else ?  
# recebo os dados do usuario e faço o compartivo, mas como faço a apresentação de acordo com a condição 
guerreiro = (pontos_de_forca >= 15  and pontos_de_magia <= 10)
print(guerreiro)
mago = (pontos_de_forca >= 10  and pontos_de_magia >=  15)
print ( mago)
arqueiro = (pontos_de_forca >= 5  and pontos_de_magia >= 5) and (pontos_de_forca <= 15  and pontos_de_magia <= 15 )
print (arqueiro)
