#Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50 gramas ao dia.

#Declarar

Akg: int = 0 #Alimento em quilos
G: int = 50 #Gramas
Qd: int = 0 #Quantos dias esse alimento vai durar

#Início

Akg = float(input("Digite o valor da quantidade: "))
Akg = Akg*1000
Qd = (Akg/G)
print (Qd)

#Fim