elevadores = [ "A", "B", "C"]
turnos = ["M", "V", "N"]
respostas =[]

while (True):
    elevador = str(input("informe o elevador mais utilizado A, B ou C")).upper()
    while not elevador in elevadores:
        print("digitou errado")
        elevador = str(input("informe o elevador utilizado: A, B, C")).upper()
