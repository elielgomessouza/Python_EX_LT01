#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

#Declarar

X: int = 0 # Valor inteiro
R1: int = 0 # 1º Resultado
R2: int = 0 # 2º Resultado

#Início

X = int(input("Digite o valor de X: "))
if X % 2 == 0 and X % 3 == 0:
    R1 = (X//2)
    R2 = (X//3)
    print (R1,R2)
    print (f"{X} é Divisível por ambos")
elif X % 2 == 0:
    R1 = (X//2)
    print (R1)
    print (f"{X} é Divisível apenas por 2")
elif X % 3 == 0:
    R2 = (X//3)
    print (R2)
    print (f" {X} é Divisível apenas por 3")
else:
    print (f" {X} não é divisível por nenhum dos dois")

#Fim