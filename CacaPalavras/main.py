def achaHorizontal(grid, palavras, lin): #precisa fazer a lógica de inserir só a primeira ocorrencia
    result = []
    for i in range(len(palavras)):
        result.append([palavras[i]])
        for j in range(lin):
            aux = ' '.join(grid[j]) #transforma a linha da lista em string
            index = aux.find(palavras[i])
            #print(aux, palavras[i])
            if index != -1:
                result[i].append(j)
                result[i].append(index)
                #print(palavras[i], j, index) #printa a palavra, linha e coluna, normal

            reverse = palavras[i][::-1]
            index = aux.find(reverse)
            if index != -1:
                result[i].append(j+1)
                result[i].append(index + len(palavras[i]) - 1+1)
                #print(reverse, j+1, index + len(palavras[i]) - 1+1) #printa a palavra, linha e coluna, reversa #precisa somar 1 pq começa em 1
    
    print(result)
    print("fim horizontal")


def achaVertical(grid, palavras, col, lin):
    result=[]
    for i in range(len(palavras)):
        for j in range(col):
            aux = ''
            for k in range(lin):
                aux += grid[k][0][j] #transforma a coluna da lista em string
            #print(aux) #printa a coluna em formato de linha
            index = aux.find(palavras[i])
            if index != -1:
                print(palavras[i], index+1, j+1) #printa a palavra, linha e coluna, normal #precisa somar 1 pq começa em 1
            
            reverse = palavras[i][::-1]
            index = aux.find(reverse)
            if index != -1:
                print(reverse, index + len(palavras[i])-1 +1, j+1) #printa a palavra, linha e coluna, reversa #precisa somar 1 pq começa em 1
            
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
                        print(result)
                        break
                    
                    reverse = palavras[i][::-1]
                    index = aux.find(reverse)
                    if index != -1:
                        print(reverse, j+2, k+2)
                        break
    print("fim diagonal principal")
            
                

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
            if len(aux) == 1:
                break
            else:
                grid.append([aux]) #salva a linha na lista

        for i in range(int(aux)): #aux é a quantidade de palavras a serem buscadas
            palAux = input().upper()
            palavras.append(palAux)
        
        achaHorizontal(grid, palavras, lin)
        achaVertical(grid, palavras, col, lin)
        achaDiagonal(grid, palavras, col, lin)


        try:
            blankline = input()
        except EOFError:
            break

main()
