'''Realiza  un  programa  que  pida  un  número  entero  positivo  al  usuario  (N)  y  le  diga  
cuantos primos hay entre 1 y ese número N, y cuantos perfectos hay entre 1 y ese 
número N. Realiza un análisis de eficiencia y de complejidad.'''

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
        if esPrimo(i):
            numeroPerfectos += 1
    return numeroPerfectos

def main():
    numero = input("Por favor, introduzca un número entero positivo: ")
    print(f"Hay {cuantosPrimos(numero)} números primos entre el 1 y el {numero}")