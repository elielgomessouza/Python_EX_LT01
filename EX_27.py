#Receba o número de voltas, a extensão do cirtcuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

#Declarar

Nv: int = 0 #Número de voltas
ECm: int = 0 #Extensão do circuito em metros
Tmn: int = 0 #Duração do circuito em minutos
Vm: int = 0 #Velocidade média

#Início

Nv = int(input("Digite o número de voltas: "))
ECm = int(input("Digite a extensão do circuito em metros: "))
Tmn = int(input("Digite a duração do circuito em minutos: "))
Tmn = Tmn/0.060
Vm = (Nv*ECm)/Tmn
print (Vm)

#Fim