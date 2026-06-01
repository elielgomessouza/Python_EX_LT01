#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença entre o maior e o menor.

#Declarar

V1: int = 0 #Valor 1
V2: int = 0 #Valor 2
D: int = 0 #Diferença

#Início

V1 = int(input("Digite o 1º valor: "))
V2 = int(input("Digite o 2º valor: "))
if V1>V2:
    D = (V1-V2)
    print (D)
elif V1<V2:
    D = (V2-V1)
    print (D)
else:
    print ("Os valores são iguais")

#Fim