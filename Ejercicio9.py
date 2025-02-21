'''Realiza una función recursiva que calcule el siguiente sumatorio:  
S =  1 + 2 + 3 + 4 + ⋯. + n - 1 + n Realiza un análisis de eficiencia y de complejidad.'''



def sumaRec(n: int) -> int:
    if n == 0:
        return n
    else:
        return n + sumaRec(n-1)
    
def main():
    numero = int(input("Introducza un número entero positivo: "))
    print(f"La suma de todos los números enteros desde 1 hasta {numero} es {sumaRec(numero)}")

if __name__ == "__main__":
    main()


#######################
#        TEST         #
#######################

def test_coprobar_sumatorio_100(benchmark): 
    resultado = benchmark(sumaRec, 100)

    return resultado == 5050