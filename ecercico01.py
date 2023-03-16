def cadastros():
    
    nome=''
    horas_tabalhadas_mes = 0
    turno_de_trabalho=''
    ocupacao=''

    while True:
        nome = input(" Nome do colaborador: ")
        horas_tabalhadas_mes = input("Numeros de Horas Trabalhadas: ")
        turno_de_trabalho = input("Informe M = Matutino, V = Vespertino e N = Noturno : ")
        ocupacao = input("Informe ocupação (G = Gerente e O = Operário):  ")

        continua = input("deseja continuar? 1-Sim e 2-Não")
        if continua  == "2":
            continua = ''
            return False
  


def valor_hora_trabalhada():
    ocupacao = ''
    turno_de_trabalho = ''
    valor_base = 1_320.00
    
    if ocupacao == "G" and (turno_de_trabalho == "V" or "M") :
            valor_hora_trabalhada = float(valor_base*0.15)
    elif ocupacao == "G" and (turno_de_trabalho == "N") :      
            valor_hora_trabalhada = (valor_base*0.10)
    elif ocupacao == "O" and (turno_de_trabalho == "N") :
            valor_hora_trabalhada = (valor_base*0.09)
    elif ocupacao == "O" and (turno_de_trabalho == "V" or "M") :
            valor_hora_trabalhada = (valor_base*0.14)

 
def calcular_salario():
    horas_tabalhadas_mes = float(horas_tabalhadas_mes())
    valor_hora_trabalhada = float(valor_hora_trabalhada())
    if horas_tabalhadas_mes:
        salario=horas_tabalhadas_mes*valor_hora_trabalhada
    return salario

cadastros()
print(cadastros)
valor_hora_trabalhada()
print(valor_hora_trabalhada())
calcular_salario()
print(calcular_salario())

