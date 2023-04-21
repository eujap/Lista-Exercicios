def calcular_notas ():
    with open("notas.txt" , "r") as arquivo:
        texto = arquivo.read()
        texto1 = texto.split("\n")
        lista = texto1.split(",")
        
        media = (float(lista[1]) + float(lista[2]) + float(lista[3])) / 3
        resultado = ""
        if media >= 7:
            resultado = "aprovado.txt"
        elif media >= 5:
            resultado = "exame.txt"
        elif media < 5:
            resultado = "reprovado.txt"
        
        with open (resultado,"a") as resultado:
            legenda = lista[0] + "," + str(media)
            resultado.write(legenda)
            resultado.write("\n")
        resultado.close()    

        print(texto)
        print(lista)        

calcular_notas()