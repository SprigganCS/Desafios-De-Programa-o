def achaHorizontal(grid, palavras, lin): #precisa fazer a lógica de inserir só a primeira ocorrencia
    result = []
    for i in range(len(palavras)):
        result.append([palavras[i]])
        for j in range(lin):
            aux = ' '.join(grid[j]) #transforma a linha da lista em string
            index = aux.find(palavras[i])
            #print(aux, palavras[i])
            if index != -1:
                result[i].append(j+1)
                result[i].append(index+1)
                #print(palavras[i], j, index) #printa a palavra, linha e coluna, normal

            reverse = palavras[i][::-1]
            index = aux.find(reverse)
            if index != -1:
                result[i].append(j+1)
                result[i].append(index + len(palavras[i]) - 1+1)
                #print(reverse, j+1, index + len(palavras[i]) - 1+1) #printa a palavra, linha e coluna, reversa #precisa somar 1 pq começa em 1
    
    #print(result)
    return result
    print("fim horizontal")


def achaVertical(grid, palavras, col, lin):
    result=[]
    for i in range(len(palavras)):
        result.append([palavras[i]])
        for j in range(col):
            aux = ''
            for k in range(lin):
                aux += grid[k][0][j] #transforma a coluna da lista em string
            #print(aux) #printa a coluna em formato de linha
            if len(result[i]) != 3: 
                index = aux.find(palavras[i])
                if index != -1:
                    #print(palavras[i], index+1, j+1) #printa a palavra, linha e coluna, normal #precisa somar 1 pq começa em 1
                    result[i].append(index+1)
                    result[i].append(j+1)
            
                reverse = palavras[i][::-1]
                index = aux.find(reverse)
                if index != -1:
                    #print(reverse, index + len(palavras[i])-1 +1, j+1) #printa a palavra, linha e coluna, reversa #precisa somar 1 pq começa em 1
                    result[i].append(index + len(palavras[i]) - 1+1)
                    result[i].append(j+1)

    return result
    #print(result)   
    print("fim vertical")

def achaDiagonal(grid, palavras, col, lin):
    result = []
    for i in range(len(palavras)):
        result.append([palavras[i]])
        for j in range(lin):
            for k in range(col):
                aux = ''
                for l in range(lin):
                    for m in range(col):
                        if j+l == k+m:
                            aux += grid[l][0][m]
                            break
                #print(aux) #string de todas as diagonais
                if len(result[i]) != 3: #elimina resultados duplicados, selecionando apenas o primeiro
                    index = aux.find(palavras[i])
                    if index != -1:
                        result[i].append(k+2)
                        result[i].append(j+2)
                        break
                    
                    reverse = palavras[i][::-1]
                    index = aux.find(reverse)
                    if index != -1:
                        result[i].append(k+2)
                        result[i].append(j+2)
                        break
    return result
    #print(result)

def achaDiagonalSec(grid, palavras, col, lin):
    result = []
    for i in range(len(palavras)):
        result.append([palavras[i]])
        for j in range(lin):
            for k in range(col):
                aux = ''
                for l in range(lin):
                    for m in range(col):
                        if j+l == k+m:
                            aux += grid[l][0][m]
                            break
                #print(aux) #string de todas as diagonais
                if len(result[i]) != 3: #elimina resultados duplicados, selecionando apenas o primeiro
                    index = aux.find(palavras[i])
                    if index != -1:
                        result[i].append(lin-k+2)
                        result[i].append(col-(j+2))
                        break
                    
                    reverse = palavras[i][::-1]
                    index = aux.find(reverse)
                    if index != -1:
                        result[i].append(k+2)
                        result[i].append(j+2)
                        break
    return result
    #print(result)
    

def flip(im, w):
	result = []
	for i in im:
		result.append([i[0][w-1::-1]])
	return result


def main():
    cases = int(input()) #numero de casos
    grid=[]
    palavras=[]
    blankline = input()
    for i in range(cases):
        grid=[]
        palavras=[]
        dim = input() #le qtd de linhas e colunas
        dim = dim.split() #divide em duas variaveis
        lin = int(dim[0])
        col = int(dim[1])

        while(1): #o criterio de parada é quando a linha tiver tamanho 1 (o fim da matriz é seguido do numero de palavras), então break
            aux = input().upper()
            if aux.isnumeric() == True: # a comparacão deve ver se aux é um numero ou nao
                break
            else:
                grid.append([aux]) #salva a linha na lista

        for j in range(int(aux)): #aux é a quantidade de palavras a serem buscadas
            palAux = input().upper()
            palavras.append(palAux)


        #chamada de funcoes do caça palavras

        horiz = achaHorizontal(grid, palavras, lin)
        vert = achaVertical(grid, palavras, col, lin)
        diagprin = achaDiagonal(grid, palavras, col, lin)
        diagsec = achaDiagonalSec(flip(grid, col), palavras, col, lin)

        print(horiz, "\n", vert, "\n", diagprin, "\n", diagsec)
        #print("")

        #decisao de qual coordenada printar

        
        for i in range(len(palavras)):
            auxi=[float("inf"), float("inf"), float("inf")] #infinito
            if len(horiz[i]) >= 3:
                auxi = horiz[i]
            elif len(vert[i]) >= 3:
                if auxi[1] > vert[i][1]:
                    auxi = vert[i]
            elif len(diagprin[i]) >= 3:
                if auxi[1] > diagprin[i][1]:
                    auxi = diagprin[i]
            elif len(diagsec[i]) >= 3:
                if auxi[1] > diagsec[i][1]:
                    auxi = diagsec[i]
            else:
                print("lakaka")
        
            print(auxi[1], auxi[2])

        print("\n")
        try:
            blankline = input()
        except EOFError:
            break

main()
