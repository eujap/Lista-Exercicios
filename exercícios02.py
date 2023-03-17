elevadores = [ "A", "B", "C"]
turnos = ["M", "V", "N"]
elevador = []
periodo = []
respostas = []

while (True):
    elevador = str(input("informe o elevador mais utilizado A, B ou C?  ")).upper()
    while not elevador in elevadores:
        print("digitou errado")
        elevador = str(input("informe o elevador utilizado: A, B ou  C?  ")).upper()
        if elevador in elevadores:
            break
    periodo = str(input("Em qual período em que utiliza o elevador, entre (M = Matutino, V = Vespertino, N = Noturno)?  ")).upper()
    while not periodo in turnos:
        print("Informe opção valida")
        periodo = str(input("Em qual período em que utiliza o elevador, entre (M = Matutino, V = Vespertino, N = Noturno)?  ")).upper()
        if periodo in turnos:
            break
    respostas.append(elevador[:])
    respostas.append(periodo[:])
    
    

    while True:
        continua = str(input("Deseja continuar? S-Sim e N-Não  ")).upper()[0]
        if continua in 'SN':
            break
        print("ERRO! Responda apenas S ou N. ")
    if continua == "N":
        break

def conta_elevador():
    elevador = ''
    periodo = ''
    if elevador == "A" and (periodo == "M"):
        elev_A_manha = 0
        elev_A_manha += 1
    elif elevador == "A" and (periodo == "V"):
        elev_A_tarde = 0
        elev_A_tarde = +1 
                

print(respostas)
conta_elevador()
print(conta_elevador)