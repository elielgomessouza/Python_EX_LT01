#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:

# Se a média for >/6,0, exibir "Aprovado";
# Se a média for >/3,0 e <6,0, exibir "Exame";
# Se a média for \<3,0, exibir "Retido".

#Declarar

A: int = 0 # 1ª Nota
B: int = 0 # 2ª Nota
C: int = 0 # 3ª Nota
D: int = 0 # 4ª Nota
M: int = 0 #Média aritmética

#Início

A = float(input("Digite a 1ª nota do aluno: "))
B = float(input("Digite a 2ª nota do aluno: "))
C = float(input("Digite a 3ª nota do aluno: "))
D = float(input("Digite a 4ª nota do aluno: "))
M = (A+B+C+D)/4
if M<3:
    print ("Retido")
elif M>=3 and M<6:
    print ("Exame")
elif M>=6:
    print ("Aprovado")

#Fim