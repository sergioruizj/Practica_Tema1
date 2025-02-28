'''Dado un conjunto de reservas de pistas de pádel, cada una con una hora de inicio 
y otra de finalización, diseñe un algoritmo que calcule el número mínimo de pistas 
necesarias  para  que  todas  las  reservas  puedan  llevarse  a  cabo  sin  conflictos  de  
horario. Para ello se dispone de una lista de intervalos de tiempo, donde cada intervalo está 
representado por una hora de inicio y una de finalización de la reserva.'''

def mejor_candidato(candidatos: list) -> any:
    """ Devuelve el mejor candidato """
    return min(candidatos, key=lambda x: x[1])  # Selecciona el candidato que termina más temprano

def es_completable(solucion: list, candidato: any) -> bool:
    """ Comprueba si se puede llegar a la solución usando ese candidato """
    if not solucion:
        return True
    return solucion[-1][1] <= candidato[0]  # No debe solaparse con la última reserva añadida

def voraz(candidatos: list) -> list:
    solucion = []
    candidatos.sort(key=lambda x: x[1])  # Ordenamos por hora de finalización
    while len(candidatos) > 0:
        c = mejor_candidato(candidatos)
        candidatos.remove(c)
        if es_completable(solucion, c):
            solucion.append(c)
    return solucion

# Ejemplo de uso
reservas = [(10, 12), (9, 11), (11, 13)]
print(len(voraz(reservas)))  # Salida: 2