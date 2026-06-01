#Receba 2 valores reais. Calcule e mostre o maior deles.

#Declarar

X: float = 0 #1º valor
Y: float = 0 #2º valor

#Início

X = float(input("Digite o valor de X: "))
Y = float(input("Digite o valor de Y: "))
if X>Y:
    print (X,Y)
elif X<Y:
    print (Y,X)
else:
    print ("Valores iguais")

#Fim