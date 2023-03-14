
def cadastros():
    nome=''
    horas_tabalhadas_mes=0
    turno_de_trabalho=0
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
  
#    print(colaboradores)

#def valor_hora_trabalhada(ocupacao, turno_de_trabalho, valor_hora_trabalhada ):
#    valor_hora_trabalhada = float () 

def calcular_salario():
    horas_tabalhadas_mes = float(input("Numeros de Horas Trabalhadas: "))
    valor_hora_trabalhada = float(input("valor_hora_trabalhada"))
    if horas_tabalhadas_mes:
        salario=horas_tabalhadas_mes*valor_hora_trabalhada
    return salario

cadastros()  
calcular_salario()
