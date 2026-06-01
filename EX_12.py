#Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos

#Declarar

An: int = 0 #Ano de nascimento
Aa: int = 0 #Ano atual
Id: int = 0 #Idade
A17: int = 0 #Idade (Após 17 anos)

#Início

An = int(input("Digite o ano de nascimento: "))
Aa = int(input("Digite o ano atual: "))
if Aa<An:
    print ("Dados inválidos!")
    print ("Tente novamente")
else:
    Id = (Aa-An)
    A17 = (Id+17)
    print (Id)
    print (A17)

#Fim