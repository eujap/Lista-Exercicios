aluno = []
continua = []


def salvar_notas ():
    with open ("dados.txt",'a+') as arquivo :
        arquivo.write()


while (continua != "N"):
    nome = input("digite o nome do aluno:").upper()
    nota1 = input("digite a nota da 1 avaliação")
    nota2 = input("Digite a nota da 2ª avaliação")
    nota3 = input("Digite a nota da 3ª avaliação")
    aluno.append({"nome": nome, "nota1": nota1, "nota2": nota2, "nota3": nota3})

    continua = input(str("deseja continuar? S-sim e N-Não")).upper()


print(aluno)