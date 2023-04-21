continua = []
lista = []

def salvar_notas ():
    with open ("notas.txt", "a") as arquivo :
        arquivo.write(lista)
        arquivo.write("\n")
        
    arquivo.close()    


while (continua != "N"):
    temp = []
    temp.append(input("digite o nome do aluno:").upper())
    temp.append(str(input("digite a nota da 1 avaliação")))
    temp.append(str(input("Digite a nota da 2ª avaliação")))
    temp.append(str(input("Digite a nota da 3ª avaliação")))

    lista = str(temp[0]) + "," + str(temp[1]) + "," + str(temp[2]) + "," + str(temp[3])
    print(lista , end ="\n")
    salvar_notas()

    temp.clear()

    continua = input(str("deseja continuar? S-sim e N-Não")).upper()


print(lista)

