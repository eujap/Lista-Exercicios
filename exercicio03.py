continua = []

def salvar_notas ():
    with open ("notas.txt", "w") as arquivo :
        arquivo.write(lista)


while (continua != "N"):
    nome = input("digite o nome do aluno:").upper()
    nota1 = str(input("digite a nota da 1 avaliação"))
    nota2 = str(input("Digite a nota da 2ª avaliação"))
    nota3 = str(input("Digite a nota da 3ª avaliação"))
    lista = (nome +","+ nota1 + "," + nota2 + "," + nota3)

    continua = input(str("deseja continuar? S-sim e N-Não")).upper()


print(lista)
salvar_notas()
