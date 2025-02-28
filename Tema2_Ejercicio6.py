def mejor_candidato(candidatos):
    """ Devuelve el mejor candidato, el que finaliza antes """
    return min(candidatos, key=lambda x: x[1])

def es_completable(solucion, candidato):
    """ Comprueba si el candidato puede añadirse sin solapamiento """
    for reserva in solucion:
        if not (candidato[0] >= reserva[1] or candidato[1] <= reserva[0]):
            return False
    return True

def voraz(reservas):
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

# Ejemplo de uso
reservas = [(10, 12), (9, 11), (11, 13), (10, 12)]
solucion = voraz(reservas)
print(solucion)
print(len(solucion))  # Salida: 3
