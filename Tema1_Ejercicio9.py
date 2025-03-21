'''Realiza una función recursiva que calcule el siguiente sumatorio:  
S =  1 + 2 + 3 + 4 + ⋯. + n - 1 + n Realiza un análisis de eficiencia y de complejidad.'''



def sumaRec(n: int) -> int:
    if n == 0:
        return 0
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

def test_comprobar_sumatorio():
    numeros = [5, 15, 30]
    resultados = []
    for num in numeros:
        resultados.append(sumaRec(num))
    
    valores = [15, 120, 465]
    assert resultados == valores
def test_benchmark_coprobar_sumatorio_100(benchmark): 
    resultado = benchmark(sumaRec, 100)

    assert resultado == 5050

def test_benchmark_comprobar_sumatorio_10(benchmark):
    resultado = benchmark(sumaRec, 10)

    assert resultado == 55

def test_benchmark_comprobar_sumatorio_0(benchmark):
    resultado = benchmark(sumaRec, 0)

    assert resultado == 0