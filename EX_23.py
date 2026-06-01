#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

#Declarar

A: int = 0 # 1º valor
B: int = 0 # 2º valor
C: int = 0 # 3º valor
X: int = 0 # 4º valor
V: int = 0 # Valores

#Início

A = float(input("Digite o 1º valor: "))
B = float(input("Digite o 2º valor: "))
C = float(input("Digite o 3º valor: "))
X = float(input("Digite o 4º valor: "))
V = [A,B,C,X]
V.sort()
print (V)

if X<=A:
    print (X,A,B,C)
elif X<=B:
    print (A,X,B,C)
elif X<=C:
    print (A,B,X,C)

#Fim