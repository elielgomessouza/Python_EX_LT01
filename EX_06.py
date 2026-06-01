#Receba os valores de X e Y. Efetua a troca de seus valores e mostre seus conteúdos

#Declarar

X: int = 0 #Valor X
Y: int = 0 #Valor Y

#Início

X = float(input("Digite o valor de X: "))
Y = float(input("Digite o valor de Y: "))
X,Y = Y,X
print (X,Y)

#Fim