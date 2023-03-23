def validar(msg, validos):
    valor = str(input(msg)).upper()
    while not valor in validos:
        print("Digitou errado")
        valor = str(input(msg)).upper()

    return valor    


def buscar_maior_quantidade(opcoes):
    itens = []
    for opcao in opcoes:
        itens.append(0)

    for resposta in respostas:
        for opcao in opcoes:
            if (opcao in resposta):
                itens[opcao.index(opcao)] +=1
   
        
    return opcoes[itens.index(max(itens))]



elevadores = [ "A", "B", "C"]
turnos = ["M", "V", "N"]
respostas = []

while (True):
    elevador = validar("informe o elevador mais utilizado A, B ou C?  ", elevadores)
    turno = validar('Informe o turno mais utilizado:( M, V, N)', turnos)

    respostas.append([elevador, turnos])

    while True:
        continua = str(input("Deseja continuar? S-Sim e N-Não  ")).upper()[0]
        if continua in 'SN':
            break
        print("ERRO! Responda apenas S ou N. ")
    if continua == "N":
        break

buscar_maior_quantidade(elevadores)
print("O elevador mais utilizado foi o elevador", buscar_maior_quantidade(elevadores))
buscar_maior_quantidade(turnos)
print("O turno mais utilizado foi i turno  ", buscar_maior_quantidade(turnos))

