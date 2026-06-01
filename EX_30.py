#Receba a data de nascimento e atual de um ano, mês e dia. Calcule e mostre a idade em anos, meses e dias, considerando os anos bissextos.

#Declarar

AA: int = 0 # Ano atual
MA: int = 0 # Mês atual
DA: int = 0 # Dia atual
AN: int = 0 # Ano de nascimento
MN: int = 0 # Mês de nascimento
DN: int = 0 # Dia do nascimento
A: int = 0

#Início

AA = int(input("DIgite o ano atual: "))
MA = int(input("Digite o mês atual: "))
DA = int(input("Digite o dia atual: "))
AN = int(input("Digite o ano de nascimento: "))
MN = int(input("Digite o mês de nascimento: "))
DN = int(input("Digite o dia do nascimento: "))

if MA == (1,3,5,7,8,10,12):
    MA = 31
elif MA == (4,6,9,11):
    MA = 30
else:
    MA = 28 or 29

#Fim