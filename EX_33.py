#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3... 1/N.

#Declarar

N: int = 0 # Número desejado
R: int = 0 # Resultado

#Início

N = int(input("Digite o número desejado: "))
for R in range (N,0,1):
    R = (N+1/2)
    print (R)

#Fim