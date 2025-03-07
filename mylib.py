# Algoritmia y Complejidad Curso 2024-25 

##############################
#        BIBLIOTECA          #
##############################
def contar_lineas(fichero :list) -> int:
    """ Cuenta cuantas líneas tiene el fichero pasado como argumento """
    contador = 0
    for _línea in fichero:
        contador = contador + 1
    return contador


def contar_caracteres(cadena :str) -> int:
    """ Cuenta cuantos carácteres tiene la cadena """
    def _contar(s :str, n :int) -> int: # El worker trabaja (la función no es accesible desde fuera)
        if not s:
            return n
        else:
            return _contar(s[1:], n + 1)

    return _contar(cadena, 0) # El wrapper inicializa



##############################
#          TESTS             #
##############################
# Pytest ejecuta las funciones que empiezan por test_
def test_contar_caracteres():
    nombres    = ['Ángel', 'Pepe', 'angel', 'josé']
    valores    = [5, 4, 5, 4]
    resultados = [] # Almacena los valores que devuelve contar_caracteres con cada nombre
    for nombre in nombres:
        resultados += [contar_caracteres(nombre)]
    assert resultados == valores, 'Todos los valores coinciden' # Comprueba que coinciden todos los valores

def test_benchmark_contar_caracteres():
    import Tests_timer
    import sys
    sys.setrecursionlimit(10**6)

    @Tests_timer.benchmark # Usa el decorador de la biblioteca timer
    def _timer_contar_caracteres(cadena :str) -> tuple: # (resultado, tiempo)
        return contar_caracteres(cadena)
    
    Tests_timer.warmup()
    print()
    for n in range(1000, 10001, 1000):
        cadena = '_' * n # Genera una cadena de longitud n
        resultado = _timer_contar_caracteres(cadena) # Devuelve la tupla (resultado, tiempo)
        assert resultado[Tests_timer.RESULT] == len(cadena), 'La longitud es correcta' # Comprueba el resultado de la función
        print(f'Elapsed time ({n}): {resultado[Tests_timer.TIME]:.3f} ms') # Muestra el tiempo por pantalla
