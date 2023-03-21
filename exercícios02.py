def validar(msg, validos):
    valor = str(input(msg)).upper()
    while not valor in validos:
        print("Digitou errado")
        valor = str(input(msg)).upper()

    return valor    


def buscarMaiorElevador(opcoes):
    itens = [0, 0, 0]
    for resposta in respostas:
        for opcao in opcoes:
            itens[opcao.index(opcao)] +=1
   
        
return opcoes[itens.infr]



elevadores = [ "A", "B", "C"]
turnos = ["M", "V", "N"]
respostas = []

while (True):
    elevador = validar("informe o elevador mais utilizado A, B ou C?  ", elevadores)
    turnos = validar('Informe o turno mais utilizado:( M, V, N)', turnos)

    respostas.append([elevador, turnos])

    while True:
        continua = str(input("Deseja continuar? S-Sim e N-Não  ")).upper()[0]
        if continua in 'SN':
            break
        print("ERRO! Responda apenas S ou N. ")
    if continua == "N":
        break


maiorIndice = elevadoresUtilizados.index(max(elevadoresUtilizados))
print("O elevador mais utilizado foi o elevador", elevadores[maiorIndice])

turnosUtilizado = [0, 0, 0]
for resposta in respostas:
    if resposta[0] == elevadores[maiorIndice]:
        if resposta[1] == "M":
            turnosUtilizado[0] += 1
        if resposta[1] == "V":
            turnosUtilizado[1] += 1
        if resposta[1] == "N":
            turnosUtilizado[2] += 1    

indiceTurno = turnosUtilizado.index(max(turnosUtilizado))
print("O Elevador ", elevadores[maiorIndice], "foi mais utilizado no truno", )
buscarMaiorElevador(elevadores)