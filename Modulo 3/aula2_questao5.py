#Solicitando o sexo do usuario, idade e tempo de serviço.

genero = input ()
idade = int (input ())
tempo_servico = int (input ())

#processamento
a = (genero == 'f' and idade >= 60 ) or ( genero == 'm' and idade >= 65 )  

b = (tempo_servico > 30) 

c = (idade >= 60 and tempo_servico >= 25)

pode_aposentar = a or b or c 


#saída 
print (pode_aposentar)
