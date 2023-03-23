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

def buscar_maior(itens):
    return max(itens, key=itens.get)


def buscar_menor(itens):
    return min(itens, key=itens.get)

elevadores = { "A":0 , "B":0 , "C":0 }
turnos = {"M":0, "V":0, "N":0}


while (True):
    elevador = validar("informe o elevador mais utilizado A, B ou C?  ", elevadores.keys)
    elevadores[elevador] +=1
    turno = validar('Informe o turno mais utilizado:( M, V, N)', turnos.keys)
    turnos[turno] +=1
    
    while True:
        continua = str(input("Deseja continuar? S-Sim e N-Não  ")).upper()[0]
        if continua in 'SN':
            break
        print("ERRO! Responda apenas S ou N. ")
    if continua == "N":
        break

buscar_maior(elevadores)
buscar_maior(turnos)
print("O elevador mais utilizado foi o elevador", buscar_maior(elevadores))
print("O turno mais utilizado foi o turno  ", buscar_maior(turnos))
maior_turno = turnos[buscar_maior(turnos)]
menor_turno = turnos[buscar_menor(turnos)]

diferenca = (maior_turno / menor_turno) *100 
print(diferenca)
