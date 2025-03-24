def mejor_candidato(candidatos):
    """ Devuelve el mejor candidato, el que finaliza antes """
    return min(candidatos, key=lambda x: x[1])

def es_completable(solucion, candidato):
    """ Comprueba si el candidato puede añadirse sin solapamiento """
    for reserva in solucion:
        if not (candidato[0] >= reserva[1] or candidato[1] <= reserva[0]):
            return False
    return True

def organizar_pistas(reservas):
    """ Calcula el número mínimo de pistas necesarias usando un algoritmo voraz """
    if not reservas:
        return 0
    
    reservas.sort()  # Ordenamos por hora de inicio
    pistas = []  # Lista de pistas ocupadas
    
    for reserva in reservas:
        asignado = False
        for pista in pistas:
            if es_completable(pista, reserva):
                pista.append(reserva)
                asignado = True
                break
        
        if not asignado:
            pistas.append([reserva])  # Se necesita una nueva pista
    
    return pistas

def main(): # Ejemplo de uso
    reservas = [(10, 12), (9, 11), (11, 13), (10, 12), (9, 10), (13, 14), (10, 12)]
    solucion = organizar_pistas(reservas)
    print(f'Si tenemos las reservas {reservas}, las organizaremos de esta forma: {solucion}')
    print(f'Por ello, necesitaremos {len(solucion)} pistas')  # Salida: 3

if __name__ == "__main__":
    main()



#######################
#        TEST         #
#######################

def test_tema2_ejercicio6():
    reservas = [(9, 10), (10, 11), (11, 12), (12, 13), (13, 14)]
    pistas = organizar_pistas(reservas)

    assert 1 == len(pistas)

    reservas2 = [(9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (9, 10), (9, 10)]
    pistas2 = organizar_pistas(reservas2)

    assert 3 == len(pistas2)

def test_benchmark_tema2_ejercicio6():
    import Tests_timer

    @Tests_timer.timer
    def _timer_organizar_pistas(reservas: list) -> list:
        return organizar_pistas(reservas)
    
    reservas = [(9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (9, 10), (9, 10),
                 (10, 11), (10, 11), (10, 11), (11, 12), (12, 20) ]
    
    Tests_timer.warmup()
    resultado = _timer_organizar_pistas(reservas)

    assert 4 == len(resultado[0])

    print(f'\n\nEl tiempo empleado para la ejecución del algoritmo es de {resultado[1]} ms\n')
