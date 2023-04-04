def ler_notas ():
    with open("notas.txt" , "r") as arquivo:
        texto = arquivo.read()
        lista = texto.split(",")
        print(lista)

        media = (float(lista[1]) + float(lista[2]) + float(lista[3])) / 3
        resultado = ""
        if media <= 7:
            resultado = "aprovado"
        elif media <= 5:
            resultado = "reprovado"


        print(media)        

ler_notas()