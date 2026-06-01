#Receba dois números inteiros. Verifique e mostre se o maior é múltiplo do menor

#Declarar

V1: int = 0
V2: int = 0

#Início

V1 = int(input("Digite o valor do 1º número: "))
V2 = int(input("Digite o valor do 2º número: "))
if (V1>V2):
    if (V1%V2 == 0):
        print ("V1 é múltiplo de V2")
    else:
        print ("V1 não é múltiplo de V2")
elif (V1<V2):
    if (V2%V1 == 0):
        print ("V2 é múltiplo de V1")
    else:
        print ("V2 não é múltiplo de V1")
else:
    print ("Os valores são iguais")

#Fim