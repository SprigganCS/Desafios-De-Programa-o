def encontrar(num):
    if num == 1:
        return (0,0)
    else:

        num-=1

        baixo = 1
        diagonalEI = 0
        diagonalES = 1
        cima = 1
        diagonalDS = 1
        diagonalID = 1
        

        i=0
        j=0
        while num > 0:
            for a in range(baixo):
                j+=1
                num-=1
                if(num == 0):
                    return (i,j)
            
            for a in range(diagonalEI):
                i-=1
                j+=1
                num-=1

                if(num == 0):
                    return (i,j)
            
            for a in range(diagonalES):
                i-=1
                num-=1

                if(num == 0):
                    return (i,j)

            for a in range(cima):
                j-=1
                num-=1

                if(num == 0):
                    return (i,j)

            for a in range(diagonalDS):
                i+=1
                j-=1
                num-=1

                if(num == 0):
                    return (i,j)

            for a in range(diagonalID):
                i+=1
                num-=1

                if(num == 0):
                    return (i,j)

            baixo+=1
            diagonalEI+=1
            diagonalES+=1
            cima+=1
            diagonalDS+=1
            diagonalID+=1
            
            #print(baixo, diagonalEI, diagonalES, cima, diagonalDS, diagonalID)







def main():
    while True:
        try:
            num = int(input())
            coord = encontrar(num)
            print(coord[0], coord[1])
        except EOFError:
            break
    
main()
