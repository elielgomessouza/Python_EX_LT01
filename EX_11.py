#Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência

#Declarar

R: int = 0 #Raio
C: int = 0 #Comprimento

#Início

import math

R = float(input("Digite o valor de R: "))
C = (2*math.pi*R)
print (f"Comprimento:{C:.2f}")

#Fim