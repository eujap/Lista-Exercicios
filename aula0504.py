class excessao(Exception):
    pass

try :
    numero = input("Digite um numero:   ")
    if int(numero) % 2 == 0:
        print("sim é numer par par")
    else:     
        raise excessao("o numero tem de ser par")

except excessao as e :
        print(e)


try:
    palavra = input("Digite algo:    ")
    if palavra == palavra.upper():
        print("Ok Digitou correto")
    
    raise excessao("digite apenas palavras em letra maiscula")
except excessao as e:
     print(e)     
     
               
try:
     num_x = input("Digite um numero inteiro:   ")
     if int(num_x):
        raise excessao("o numero deve ser inteiro")
     elif:
          a = 10/num_x
            print(a)
        
except excessao as e:
     print(e)