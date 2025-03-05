def mejor_candidato(candidatos :list) -> any:
    return max(candidatos, key=lambda x: x[1] / x[0])


def voraz(candidatos :list) -> list:
    solucion = []
    while len(candidatos) > 0:
        c = mejor_candidato(candidatos)
        candidatos.remove(c)
        solucion.append(c)
    return solucion



##############################
#          TESTS             #
##############################
# Pytest ejecuta las funciones que empiezan por test_
def test_orden_ficheros():
    ficheros_entrada = [(10, 100), (20, 50), (5, 200), (15, 30)]
    ficheros_ordenados_esperados = [(5, 200), (10, 100), (20, 50), (15, 30)]  
    resultado = voraz(ficheros_entrada)

    assert resultado == ficheros_ordenados_esperados


def test_benchmark_voraz_10(benchmark):
    ficheros_entrada = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), 
    (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)
    ]
    resultado = benchmark(voraz, ficheros_entrada)  
    assert len(resultado) == len(ficheros_entrada)   

def test_benchmark_voraz_100(benchmark):
    ficheros_entrada = [(i, i % 100 + 1) for i in range(1, 101)]  
    resultado = benchmark(voraz, ficheros_entrada)  
    assert len(resultado) == len(ficheros_entrada)  

# Test 3: Benchmark para 500 ficheros
def test_benchmark_voraz_500(benchmark):
    ficheros_entrada = [(i, i % 100 + 1) for i in range(1, 501)]  # 500 ficheros
    resultado = benchmark(voraz, ficheros_entrada)  # Medir tiempo de ejecución
    assert len(resultado) == len(ficheros_entrada)  # Comprobar que procesó todos los ficheros