U = 0
V = 1
PESO = 2

def ordena_aristas(aristas :list) -> list:
    """ Ordena las aristas por peso de menor a mayor """
    peso = lambda arista: arista[PESO]
    return sorted(aristas, key=peso)

def find(conjuntos :list, u :int) -> set:
    """ Devuelve el conjunto al que pertenece un nodo """
    for conjunto in conjuntos:
        if u in conjunto:
            return conjunto
    return None

def union(conjuntos :list, arista :tuple) -> None:
    """ Actualiza los conjuntos """
    set_u = find(conjuntos, arista[U])
    set_v = find(conjuntos, arista[V])
    if set_u != set_v:
        conjuntos.remove(set_u)
        conjuntos.remove(set_v)
        conjuntos.append(set_u.union(set_v))

def is_bucle(conjuntos :list, arista :tuple) -> bool:
    """ Hay un bucle si los nodos pertenecen al mismo conjunto (algoritmo union-find) """
    set_u = find(conjuntos, arista[U])
    set_v = find(conjuntos, arista[V])
    return set_u == set_v

def conectar_ciudades(aristas :list, conjuntos :list) -> list:
    """ Algoritmo de Kruskal """
    aristas = ordena_aristas(aristas)
    solucion = []
    for arista in aristas:
        if not is_bucle(conjuntos, arista):
            solucion.append(arista)
            union(conjuntos, arista)
    return solucion


def main(): # Programa
    nodos = [{'Madrid'}, {'Burgos'}, {'Sevilla'}, {'Barcelona'}, {'Valencia'}, {'Bilbao'}, {'Santander'}, {'Guadalajara'}]
    aristas = []
    aristas.append(('Madrid', 'Burgos', 3000))
    aristas.append(('Madrid', 'Santander', 4000))
    aristas.append(('Burgos', 'Sevilla', 2000))
    aristas.append(('Burgos', 'Valencia', 1000))
    aristas.append(('Sevilla', 'Barcelona', 5000))
    aristas.append(('Barcelona', 'Valencia', 4000))
    aristas.append(('Barcelona', 'Bilbao', 2000))
    aristas.append(('Valencia', 'Bilbao', 9000))
    aristas.append(('Valencia', 'Santander', 7000))
    aristas.append(('Bilbao', 'Santander', 3000))
    aristas.append(('Bilbao', 'Guadalajara', 3000))
    aristas.append(('Santander', 'Guadalajara', 2000))


    arbol_expansion_minima = conectar_ciudades(aristas, nodos)

    for arista in arbol_expansion_minima:
        print(f'El coste de {arista[U]} a {arista[V]} es de {arista[PESO]}€')

    suma_tot = 0
    for arista in arbol_expansion_minima:
        suma_tot += arista[PESO]

    print(f'\nEl coste total de instalación asciende a {suma_tot}€')

if __name__ == "__main__":
    main()


#######################
#        TEST         #
#######################

def test_tema2_ejercicio4():
    nodos = [{1}, {2}, {3}, {4}]
    aristas = []
    aristas.append((1, 2, 1))
    aristas.append((1, 3, 4))
    aristas.append((2, 3, 7))
    aristas.append((2, 4, 5))

    arbol_minimo = conectar_ciudades(aristas, nodos)
    assert 3 == len(arbol_minimo)
    
    resultados = [(1, 2, 1), (1, 3, 4), (2, 4, 5)]

    for i in range(len(arbol_minimo)):
        assert resultados[i] == arbol_minimo[i]

def test_benchmark_tema2_ejercicio4():
    import Tests_timer
    
    @Tests_timer.timer
    def _timer_conectar_ciudades(aristas: list, nodos: list) -> list:
        return conectar_ciudades(aristas, nodos)
    

    nodos = [{'Madrid'}, {'Burgos'}, {'Sevilla'}, {'Barcelona'}, {'Valencia'}, {'Bilbao'}, {'Santander'}, {'Guadalajara'}]
    aristas = []
    aristas.append(('Madrid', 'Burgos', 3000))
    aristas.append(('Madrid', 'Santander', 4000))
    aristas.append(('Burgos', 'Sevilla', 2000))
    aristas.append(('Burgos', 'Valencia', 1000))
    aristas.append(('Sevilla', 'Barcelona', 5000))
    aristas.append(('Barcelona', 'Valencia', 4000))
    aristas.append(('Barcelona', 'Bilbao', 2000))
    aristas.append(('Valencia', 'Bilbao', 9000))
    aristas.append(('Valencia', 'Santander', 7000))
    aristas.append(('Bilbao', 'Santander', 3000))
    aristas.append(('Bilbao', 'Guadalajara', 3000))
    aristas.append(('Santander', 'Guadalajara', 2000))

    Tests_timer.warmup()
    resultado = _timer_conectar_ciudades(aristas, nodos)

    suma_tot = 0
    for arista in resultado[0]:
        suma_tot += arista[PESO]
    
    resultado_teorico = [('Burgos', 'Valencia', 1000), ('Burgos', 'Sevilla', 2000), ('Barcelona', 'Bilbao', 2000), 
                         ('Santander', 'Guadalajara', 2000), ('Madrid', 'Burgos', 3000), ('Bilbao', 'Santander', 3000), ('Madrid', 'Santander', 4000)]
    assert suma_tot == 17000

    for i in range(0, len(resultado[0])):
        assert resultado[0][i] == resultado_teorico[i]

    print(f'\n\nEl tiempo empleado para la ejecución del algoritmo es de {resultado[1]} ms\n')



    