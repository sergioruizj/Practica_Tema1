'''Realiza  una  función  que  determine  si  un  número  recibido  como  parámetro  es  
perfecto. Realiza un análisis de eficiencia y complejidad.'''

def esPerfecto(n: int) -> bool:
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return n == sum(divisores)

def main():
    numeros = [1, 2, 3, 6, 16, 17, 28, 97, 496, 1009, 8128]

    for _num in numeros:
        if esPerfecto(_num):
            print(f'El número {_num} es perfecto.')
        else:
            print(f'El número {_num} no es perfecto.')


if __name__ == "__main__":
    main()