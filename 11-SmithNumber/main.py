def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

def decompose(n):
    if n == 1:
        return []
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return [i] + decompose(n // i)

def get_number(teste):
    a = ""
    for i in teste:
        a = a + str(i)
    return int(a)

def is_smith(n1, n2):
    if sum_digits(n1) == sum_digits(n2):
        #print(n1, n2)
        return True
    else:
        return False

#is prime
def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n_input = int(input())
for i in range(n_input):
    try:
        n = int(input())  
        regra = True
        while(regra):
            if(n == 1):
                n+=2
            else:
                n = n + 1
            if(is_prime(n)):
                n+=1    
#            print(f"Anterior: {n} e decomposicao = {get_number(decompose(n))}")

            regra = not is_smith(n, get_number(decompose(n)))
        print(n)
    except Exception:
        break
