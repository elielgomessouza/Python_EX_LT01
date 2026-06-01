#Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12Km/L. Receber o tempo de percurso e a velocidade média.

#Declarar

Lg: int = 0 #Litros gastos
Kml: int = 12 #Quilômetros por litro
TP: int = 0 # Tempo de percurso
Vm: int = 0 # Velocidade média
D: int = 0 #Distância

#Início

Vm = float(input("Digite a velocidade média do veículo"))
D = float(input("Digite a distância percorrida pelo automóvel"))
TP = (Vm/D)
Lg = (D/Kml)
print (Lg)

#Fim