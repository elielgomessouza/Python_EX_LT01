#Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que ele rende 1,3%

#Declarar

D: int = 0 #Depósito
D1m: int = 0 #Depósito (Após 1 mês de aplicação)

#Início

D = float(input("Digite o valor do depósito: "))
D1m = round(D*1.013)
print (D1m)

#Fim