cadastros = []
temp = []

while True:
    temp.append(str(input(" Nome do colaborador:  ")))
    temp.append(float(input(" Quantidade de horas trabalhadas:  ")))
    temp.append(str(input(" Turno de trabalho: M=Matutino, V=Vespertino e N=Noturno:  ")))
    temp.append(str(input(" Ocupação do colaborador: Gerente = G, Operario = O:  ")))
    cadastros.append(temp[:])
    temp.clear()

    continua = input("Dejesa cadastar outro? 1= Sim ou 2 = Não")
    if continua == "2":
        contiua = ''
        break

print(f' os dados foram {cadastros}')    


#def valor_hora_trabalhada():
#    ocupacao = ''
#    turno_de_trabalho = 0
#    valor_base = 1_320.00
#    
#    if ocupacao == "G" and (turno_de_trabalho == "V" or "M") :
#            valor_hora_trabalhada = float(valor_base*0.15)
#    elif ocupacao == "G" and (turno_de_trabalho == "N") :      
#            valor_hora_trabalhada = (valor_base*0.10)
#    elif ocupacao == "O" and (turno_de_trabalho == "N") :
#            valor_hora_trabalhada = (valor_base*0.09)
#    elif ocupacao == "O" and (turno_de_trabalho == "V" or "M") :
#            valor_hora_trabalhada = (valor_base*0.14)

#

#valor_hora_trabalhada()
#print(valor_hora_trabalhada)
 
#def calcular_salario():
#    horas_tabalhadas_mes = float(horas_tabalhadas_mes())
#    valor_hora_trabalhada = float(valor_hora_trabalhada())
#    if horas_tabalhadas_mes:
#        salario=horas_tabalhadas_mes*valor_hora_trabalhada
#    return salario

#cadastro()
#valor_hora_trabalhada()
#print(valor_hora_trabalhada())
#calcular_salario()
#print(calcular_salario())

