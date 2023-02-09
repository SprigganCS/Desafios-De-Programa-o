def salao(lista_arvores, size_x, size_y):
    if len(lista_arvores) == 0:
        print(size_x * size_y)
        return
    

    coordenadas = []
    for i in range (len(lista_arvores)):
        for j in range(len(lista_arvores[i])):
            if j == 0:
                qtd_arvore_linha = lista_arvores[i][0]
                coordenadas.append([lista_arvores[i][1], lista_arvores[i][2]])
            else:
                while qtd_arvore_linha-1 > 0:
                    coordenadas.append([lista_arvores[i][j*2+1] + coordenadas[i][j-2], lista_arvores[i][j*2+2] + coordenadas[i][j-1]])
                    qtd_arvore_linha -= 1
                



    #ordena as coordenadas por linhas e depois por colunas
    coordenadas.sort()
    print(coordenadas)

    #tendo dois pontos com o mesmo valor para x ([1,1] e [1,9]) usar o valor do tamanho horizontal do grid 
    # como primeiro termo para calcular o resultado
    #
    #depois, pegar a diferença entre o valor de y dos pontos mais distantes restantes e multiplicar pelo primeiro termo
    #no caso os pontos [9,1] [9,9] a diferença entre os y é 9-1 = 8 e 8 * 10 (tamanho do grid)= 80


    
    

def main():
    qtd_casos = int(input())
    for i in range(qtd_casos):
        try:
            size_x, size_y = input().split()
            size_x = int(size_x)
            size_y = int(size_y)
            
            lista_arvores = []
        except EOFError:
            return 0
        while(True): 
            buffer = input()
            if buffer == '0':
                salao(lista_arvores, size_x, size_y)
                break
            arvores = buffer.split(" ")
            arvores = [int(x) for x in arvores]
            lista_arvores.append(arvores)

main()
