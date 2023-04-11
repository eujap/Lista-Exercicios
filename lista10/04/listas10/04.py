paises = []


def cad_pais ():
    continua = False
    lista = []
    lista_ordenada = []
    while (True):
        pais = input("Informe um país:  ")
        lista.append(pais)
        continua = input("Deseja continuar: Sim-S ou Não-N ").upper()
        if continua == "N":
            break
    lista_ordenada = sorted(lista)
    paises.append(lista_ordenada)


def buscar ():
    pais_digitado = input("Digite um país")
    return (paises.index(pais_digitado))
    
    
    
        





cad_pais()
print(paises)
buscar()
