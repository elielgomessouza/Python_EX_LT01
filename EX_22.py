#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

#Declarar

A: int = 0 #1º valor
B: int = 0 #2º valor

#Início

A = int(input("Digite o 1º valor: "))
B = int(input("Digite o 2º valor: "))
if A>B:
    print (A,B)
elif A<B:
    print (B,A)
else:
    print (A,B)
    print ("Valores iguais")
    
#Fim