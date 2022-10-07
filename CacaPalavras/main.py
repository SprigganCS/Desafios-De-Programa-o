def achaHorizontal(grid, palavras, lin):
    for i in range(len(palavras)):
        for j in range(lin):
            aux = ' '.join(grid[j])
            index = aux.find(palavras[i])
            if index != -1:
                print(palavras[i], j, index)

            reverse = aux[::-1]
            index = aux.find(reverse)
            if index != -1:
                print(reverse, j, index)

def main():
    cases = int(input()) #numero de casos
    grid=[]
    palavras=[]
    for i in range(cases):
        grid=[]
        palavras=[]
        dim = input()
        dim = dim.split()
        lin = int(dim[0])
        col = int(dim[1])

        for j in range(col):
            aux = input().upper()
            if len(aux) == 1:
                #aux guarda o numero de palavras
                break
            else:
                grid.append([aux])

        for i in range(int(aux)):
            palAux = input().upper()
            palavras.append(palAux)
        
        achaHorizontal(grid, palavras, lin)
main()
