#Receba a quantidade de horas trabalhadas de um funcionário, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário (horas trabalhadas x valor por hora). Calcule o salário líquido (Salário bruto-desconto). A cada dependente será acrescido R$100 no salário líquido. Exiba o salário a receber.

#Declarar

Ht: int = 0
Vh: float = 0
Ped: float = 0
NPd: int = 0
SB: float = 0
Desc: float = 0
SL: float = 0

# Início

Ht = int(input("Digite as horas trabalhadas: "))
Vh = float(input("Digite o valor da hora trabalhada: "))
Ped = float(input("Digite a porcentagem de desconto: "))
NPd = int(input("Digite o número de dependentes: "))
SB = Ht * Vh
Desc = SB * (Ped / 100)
SL = SB - Desc
SL = SL + (NPd * 100)
print("Salário a receber:", SL)

#Fim