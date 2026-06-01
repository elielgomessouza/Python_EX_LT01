#Receba os coeficientes A,B e C de uma equação de 2º grau (Ax²+Bx+C=0). Calcule e mostre as raízes reais da equação (considerar que a equação possua 2 raízes)

#Declarar

A: int = 0 #Coeficiente A
B: int = 0 #Coeficiente B
C: int = 0 #Coeficiente C
Rr1: int = 0 #Raíz Real 1
Rr2: int = 0 #Raíz Real 2
Delta: int = 0

#Início

import math

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
Delta = (B*B-4*A*C)
Rr1 = (-B+math.sqrt(Delta))/(2*A)
Rr2 = (-B-math.sqrt(Delta))/(2*A)
print (Rr1,Rr2)

#Fim