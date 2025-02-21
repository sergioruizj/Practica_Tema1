'''Realiza  un  programa  que  pida  un  número  entero  positivo  al  usuario  (N)  y  le  diga  
cuantos primos hay entre 1 y ese número N, y cuantos perfectos hay entre 1 y ese 
número N. Realiza un análisis de eficiencia y de complejidad.'''

import math

PRIMOS = 0
PERFECTOS = 1

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

def esPerfecto(n: int) -> bool:
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return n == sum(divisores)

def cuantosPrimos(n: int) -> int:
    numeroPrimos = 0
    for i in range(1, n):
        if esPrimo(i):
            numeroPrimos += 1
    return numeroPrimos

def cuantosPerfectos(n: int) -> int:
    numeroPerfectos = 0
    for i in range(1, n):
        if esPerfecto(i):
            numeroPerfectos += 1
    return numeroPerfectos

def numeros_especiales(n: int):
    return cuantosPrimos(n), cuantosPerfectos(n)

def main():
    numero = int(input("Por favor, introduzca un número entero positivo: "))
    calculo = numeros_especiales(numero)
    print(f"Hay {calculo[PRIMOS]} números primos entre el 1 y el {numero}")
    print(f"Hay {calculo[PERFECTOS]} números perfectos entre el 1 y el {numero}")


if __name__ == "__main__":
    main()


#######################
#        TEST         #
#######################

def test_numeros_especiales():
    numeros = [5, 15, 100]
    resultados = []
    for num in numeros:
        resultados.append(numeros_especiales(num)[PRIMOS])
        resultados.append(numeros_especiales(num)[PERFECTOS])
    
    valores = [2, 0, 6, 1, 25, 2]
    assert resultados == valores