#Receba dois números reais. Calcule e mostre a diferença desses valores

#Declarar

X: float = 0 #Número real 1
Y: float = 0 #Número real 2
D: float = 0 #Diferença

#Início

X = float(input("Digite o valor de X: "))
Y = float(input("Digite o valor de Y: "))
D = abs(X-Y)
print (f"D:{D:.2f}")

#Fim