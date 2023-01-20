def encontrar(sec):
    if sec == 1:
        return (1,1)
    if sec == 2:
        return (1,2)
    if sec == 3:
        return (2,2)
    if sec == 4:
        return (2,1)
    else:
        sec = sec-4

        if sec == 0:
            return (i,j)

        j = 3
        i = 1
        sec-=1

        if sec == 0:
            return (i,j)

        
        if sec == 0:
            return (i,j)
        passos = 2
        while sec > 0:
            
            
            for a in range(passos):
                i+=1
                sec-=1
                if sec ==0:
                    return (i,j)

            for b in range(passos):
                j-=1
                sec-=1
                if sec == 0:
                    return (i,j)
            
            i+=1
            sec-=1
            if sec == 0:
                return (i,j)
            passos+=1

            for a in range(passos):
                j+=1
                sec-=1
                if sec == 0:
                    return (i,j)
            
            for b in range(passos):
                i-=1
                sec-=1
                if sec == 0:
                    return (i,j)

            j+=1
            sec-=1
            if sec == 0:
                return (i,j)
            passos+=1


def main():
    while True:
        sec = int(input())
        if sec == 0:
            return
        pos = encontrar(sec)
        print(pos[1], pos[0])
    
main()
