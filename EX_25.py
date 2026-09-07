#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar em um dia e terminar noutro.

#Declarar

HI: int = 0 # Hora inicial do jogo
MI: int = 0 # Minuto inicial do jogo
HF: int = 0 # Hora final do jogo
MF: int = 0 # Minuto final do jogo
TJ: int = 0 #Tempo de jogo
TJH: int = 0 # Tempo total do jogo em horas
TJM: int = 0 # Tempo total do jogo em minutos

#Início

HI = int(input("Digite a hora inicial do jogo: "))
MI = int(input("Digite o minuto inicial do jogo: "))
HF = int(input("Digite a hora final do jogo: "))
MF = int(input("Digite o minuto final do jogo: "))
HI = (HI*60+MI)
HF = (HF*60+MF)
if HF < HI:
    HF = HF + (24*60)
TJ = HF-HI
TJH = (TJ//60)
TJM = (TJ%60)
print (f"Duração do jogo: {TJH} hora(s) e {TJM} minuto(s)")

#Fim
