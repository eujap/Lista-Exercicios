with open("exame.txt") as arquivo:
    texto = arquivo.read()
    lista = texto.split(",")
    nota_exame = float(input("nota exame: "))

    media = float(lista[1])
    media_final = (nota_exame + media)/2

    if (media_final >= 5):
        resultado = "aprovado.txt"
    else:
        resultado = "reprovado.txt"

    with open( resultado, "w") as resultado:
           
    print(media_final)

