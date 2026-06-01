#Receba um número. Calcule e mostre os resultados da tabuada desse número.

#Declarar

N: float = 0 #Número
R: float = 0 #Resultado

#Início

N = float(input("Digite o número desejado: "))
for R in range (1,11):
    R = (R*N)
    print (R)

#Fim