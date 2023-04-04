def ler_notas ():
    with open("notas.txt", "r") as arquivo:
        texto = arquivo.read()
        lista = texto.split(",")

        media = (float(lista[1]) + float(lista[2]) + float(lista[3])) / 3
        
        print(media)        

