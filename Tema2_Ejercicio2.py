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



##############################
#          TESTS             #
##############################


def test_orden_ficheros():
    ficheros_entrada = [(10, 100), (20, 50), (5, 200), (15, 30)]
    ficheros_ordenados_esperados = [(5, 200), (10, 100), (20, 50), (15, 30)]  
    resultado = ordenar_ficheros(ficheros_entrada)

    assert resultado == ficheros_ordenados_esperados


def test_benchmark_voraz_10(benchmark):
    ficheros_entrada = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), 
    (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)
    ]
    resultado = benchmark(ordenar_ficheros, ficheros_entrada)  
    assert len(resultado) == len(ficheros_entrada)   


def test_benchmark_voraz_100(benchmark):
    ficheros_entrada = [(i, i % 100 + 1) for i in range(1, 101)]  
    resultado = benchmark(ordenar_ficheros, ficheros_entrada)  
    assert len(resultado) == len(ficheros_entrada)  


def test_benchmark_voraz_500(benchmark):
    ficheros_entrada = [(i, i % 100 + 1) for i in range(1, 501)]  
    resultado = benchmark(ordenar_ficheros, ficheros_entrada)  
    assert len(resultado) == len(ficheros_entrada) 