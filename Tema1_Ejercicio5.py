'''Realiza  una  función  que  determine  si  un  número  recibido  como  parámetro  es  
primo. Realiza un análisis de eficiencia y complejidad. '''

import math

def esPrimo(n: int) -> bool:
    primo = True
    raiz = math.sqrt(n)
    if n <= 1:
        primo = False
    else:
        i = 2
        while primo and i <= raiz:
            if n % i == 0:
                primo = False
            i+=1
    return primo


def main():
    numeros = [1, 2, 3, 4, 5, 16, 17, 21, 97, 3000, 1009]

    for _num in numeros:
        if esPrimo(_num):
            print(f'El número {_num} es primo.')
        else:
            print(f'El número {_num} no es primo.')


if __name__ == "__main__":
    main()