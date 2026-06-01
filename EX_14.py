#Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.

#Declarar

A1: int = 0 #Ângulo 1
A2: int = 0 #Ângulo 2
A3: int = 0 #Ângulo 3
ATt: int = 180 #Ângulo total do triângulo

#Início

A1 = int(input("Digite o valor do 1º ângulo do triângulo: "))
A2 = int(input("Digite o valor do 2º ângulo do triângulo: "))
A3 = ATt - (A1+A2)
print (A3)

#Fim