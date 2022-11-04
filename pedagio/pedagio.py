  from array import array
from pexpect import EOF

def calcula(prices, e1, e2):
    km = int(int(e2[3]) - int(e1[3]))

    horaE1 = e1[1].split(":")[2]
    prices = [float(i) for i in prices]
    preco = km * (prices[int(horaE1)] / 100)
    return preco

numero_ocasioes = int(input())
input()
array_precos = []
for i in range(numero_ocasioes):
    prices = input()  
    prices = prices.split()
    entradas = []
    while(True):
        try:         
            entrada = input()
            entrada = entrada.split(" ")
            entradas.append(entrada)
        except Exception: 
            break

    entradas.sort(key=lambda x: (x[0], x[1], x[-2]))
    #print(entradas[0][1].split(":")[1]) split data
    #print(entradas)
    cont = 0
    placas = []
    precox = 0
    while(cont < len(entradas) / 2):
        if(entradas[cont][0] == entradas[cont + 1][0]):
            if(entradas[cont][0] in placas):
                index = placas.index(entradas[cont][0])

            else:
                index = len(placas)
                placas.append([entradas[cont][0]])    
            
            if(entradas[cont][2] == "enter" and entradas[cont + 1][2] == "exit"): 
                array_precos.append(calcula(prices, entradas[cont], entradas[cont + 1]))
            else:
                print()

        else :

            cont += 1

        cont+=1
    
