#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
# Preço atual: <30      >=30 e <80          >80
#Venda mensal: <500     >=500 e <1000       >1000 
# Preço novo:  +10%     +15%                -5%

#Declarar

PA: float = 0 #Preço atual
MMP: float = 0 #Média mensal do produto
NP: float = 0 #Novo preço do produto
PCM: int = 0 #Porcentagem do produto

#Início

PA = float(input("Digite o preço atual do produto: "))
MMP = float(input("Digite o valor da média mensal do produto: "))
if PA <30 and MMP <500:
    PCM = PA/100
    NP = (PCM*10)+PA
    print (NP)
elif PA >=30 and PA <80:
    if MMP >=500 and MMP <1000:
        PCM = PA/100
        NP = (PCM*15)+PA
        print (NP)
elif PA >=80 and MMP >=1000:
    PCM = PA/100
    NP = (PCM*-5)+PA
    print (NP)

#Fim