"""Se tiene que almacenar un conjunto de n ficheros en una cinta magnética (soporte 
de almacenamiento de recorrido secuencial), donde cada fichero tiene una 
longitud  conocida  l1,l2,...,ln.  Para  simplificar  el  problema,  puede  suponerse  que  
la  velocidad  de  lectura  es  constante,  así  como  la  densidad  de  información  en  la  
cinta. 

Se  conoce  de  antemano  la  tasa  de  utilización  de  cada  fichero  almacenado,  es  
decir, se sabe la cantidad de peticiones pi correspondiente al fichero i que se van 
a realizar. Por tanto, el total de peticiones al soporte será la suma total de las peticiones de cada fichero.

Tras la petición de un fichero, al ser encontrado, la cinta se rebobina 
automáticamente hasta el principio. 

El objetivo es decidir el orden en que los ficheros deben ser almacenados para que 
se minimice el tiempo medio de carga, creando un algoritmo voraz correcto.
"""


LONGITUD = 0
PETICIONES = 1

def mejor_candidato(candidatos :list) -> any:
    return max(candidatos, key=lambda x: x[PETICIONES] / x[LONGITUD])


def ordenar_ficheros(ficheros :list) -> list:
    solucion = []
    while len(ficheros) > 0:
        c = mejor_candidato(ficheros)
        ficheros.remove(c)
        solucion.append(c)
    return solucion

def main():
    ficheros_entrada = []
    print(ordenar_ficheros(ficheros_entrada))

if __name__=='__main__':
    main()

##############################
#          TESTS             #
##############################


# Cada posición de la lista ficheros_entrada hace referencia a la longitud y número de llamadas de un fichero "(longitud, número de llamadas)"
def test_ordenar_ficheros():
    ficheros_entrada = [(1000, 5), (200, 1), (500, 10), (300, 10)]
    ficheros_ordenados_esperados = [(300, 10), (500, 10), (1000, 5), (200, 1)]  
    resultado = ordenar_ficheros(ficheros_entrada)

    for i in range(len(ficheros_entrada)):
        assert resultado[i] == ficheros_ordenados_esperados[i]


def test_benchmark_ordenar_10_ficheros(benchmark):
    ficheros_entrada = [(10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
    resultado = benchmark(ordenar_ficheros, ficheros_entrada)  
    ficheros_salida_esperados = ficheros_entrada.reverse
    
    for i in range(len(ficheros_entrada)):
        resultado[i] == ficheros_salida_esperados[i]


def test_benchmark_ordenar_0_ficheros(benchmark):
    ficheros_entrada = []  
    resultado = benchmark(ordenar_ficheros, ficheros_entrada)  
    assert len(resultado) == 0