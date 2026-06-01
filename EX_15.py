#Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

#Declarar

Ac1: int = 0 #1º Cateto
Ac2: int = 0 #2º Cateto
H: int = 0 #Hipotenusa

#Início

import math

Ac1 = float(input("Digite o valor do 1º cateto: "))
Ac1 = (Ac1**2)
Ac2 = float(input("Digite o valor do 2º cateto: "))
Ac2 = (Ac2**2)
H = (Ac1+Ac2)
H = math.sqrt (H)
print (H)

#Fim