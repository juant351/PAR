# Juan Torres Viloria
# Analiza si un numero es primo.

for i in range(100):
    num = i

    def isPrimo(num):
        cont = 0
        for i in range(1, num+1):
            if num % i == 0:
                cont = cont+1
        if cont==2:
            return True

    if isPrimo(num):
        print(i)