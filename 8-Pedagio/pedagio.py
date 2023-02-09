def calcula(prices, e1, e2):
    km = int(int(e2[3]) - int(e1[3]))

    horaE1 = e1[1].split(":")[2]
    prices = [float(i) for i in prices]
    preco = km * (prices[int(horaE1)] / 100)
    preco+=3
    return preco

def elimina_repeticoes(lista):
    cont = 0
    while(cont < len(lista)):
        if(cont + 1 < len(lista) and lista[cont] == lista[cont + 1]): 
            lista[cont][1]+=1
           
        
        if(lista[cont][2][1] > 0):
            lista[cont][1] += 2
        cont += 1
    return lista

def calcula_diferenca_data(data1, data2):
    data1 = data1.split(":")
    data2 = data2.split(":")
    data1 = [int(i) for i in data1]
    data2 = [int(i) for i in data2]
    
    diferenca = [0, 0, 0]
    diferenca[2] = data2[2] - data1[2]
    if(diferenca[2] < 0):
        diferenca[2] += 60
        data2[1] -= 1
    diferenca[1] = data2[1] - data1[1]
    if(diferenca[1] < 0):
        diferenca[1] += 60
        data2[0] -= 1
    diferenca[0] = data2[0] - data1[0]
    return diferenca

def cria_output(lista):
    for i in lista:
        print(f"{i[0]} ${i[1]}")

numero_ocasioes = int(input())
input()
array_precos = []
for i in range(numero_ocasioes):
    try:
        prices = input()  
    except EOFError:
        break
    prices = prices.split()
    entradas = []
    while(True):
        try:         
            entrada = input()
            entrada = entrada.split(" ")
            entradas.append(entrada)
        except Exception: 
            break

  
    entradas.sort()

    cont = 0
    final_array = []
    precox = 0
    while(cont < len(entradas)):
        if ((cont + 1) < len(entradas)):
            if(entradas[cont][0] == entradas[cont + 1][0]):
                try:
                    if(entradas[cont][2] == "enter" and entradas[cont + 1][2] == "exit"): 
                        final_array.append([entradas[cont][0], calcula(prices, entradas[cont], entradas[cont + 1]).__round__(2), calcula_diferenca_data(entradas[cont][1], entradas[cont + 1][1])])
                except Exception as e:
                    pass
                    
                   
        cont+=1
    
    final_array = elimina_repeticoes(final_array)
    cria_output(final_array)
