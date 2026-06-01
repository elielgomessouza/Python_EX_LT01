#Receba um número inteiro. Calcule e mostre o seu fatorial.

#Declarar

N: int = 0 #Número inteiro
F: int = 1 #Fatorial
A: int = 0

#Início

N = int(input("Digite o número requisitado: "))
for A in range (N,0,-1):
    F = (F*A)
    print (F)

#Fim