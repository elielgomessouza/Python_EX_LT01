#Receba 3 coeficientes A,B,C de uma equação de 2º grau da fórmula (Ax²+Bx+C=0). Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

#Declarar

A: int = 0 #Coeficiente 1
B: int = 0 #Coeficiente 2
C: int = 0 #Coeficiente 3
Rr1: int = 0 #Raíz real 1
Rr2: int = 0 #Raíz real 2
D: int = 0 #Delta

#Início

import math

A = float(input("Digite o 1º coeficiente: "))
B = float(input("Digite o 2º coeficiente: "))
C = float(input("Digite o 3º coeficiente: "))
D = (B*B-4*A*C)
if D>0:
    Rr1 = (-B+math.sqrt(D))/(2*A)
    Rr2 = (-B-math.sqrt(D))/(2*A)
    print (Rr1,Rr2)
    print ("Existem duas raízes reais")
elif D==0:
    Rr1 = (-B+math.sqrt(D))/(2*A)
    Rr2 = (-B-math.sqrt(D))/(2*A)
    print (Rr1,Rr2)
    print ("Há apenas uma raíz real")
elif D<0:
    print ("Não existem raízes reais")

#Fim