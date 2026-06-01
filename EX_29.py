#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa  = 5%. Demais tipos não serão considerados.

#Declarar

P: int = 1.03 #Poupança
RF: int = 1.05 #Renda fixa
VI: int = 0 #Valor do investimento
TI: int = 0 #Tipo do investimento
R: int = 0 #Resultado final

#Início

TI = int(input("Receba o tipo do investimento: "))
VI = int(input("Digite o valor do investimento: "))
if (TI == 1):
    R = (VI*P)
    print (R)
elif (TI == 2):
    R = (VI*RF)
    print (R)
else:
    print ("Digite um tipo de investimento válido")

#Fim