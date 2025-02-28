def mejor_candidato(candidatos: list) -> any:
    """ Devuelve un candidato (el primero disponible) """
    return candidatos[0]  # Tomamos el primero para evaluar y lo eliminamos luego

def es_completable(solucion: list, candidato: any) -> bool:
    """ Siempre se puede agregar un candidato, ya que buscamos mínimo y máximo """
    return True

def voraz(candidatos: list) -> list:
    """ Algoritmo voraz para encontrar el mínimo y el máximo """
    solucion = []
    
    # Inicializamos con el primer elemento
    if len(candidatos) == 0:
        return None, None

    minimo = maximo = candidatos[0]
    
    while len(candidatos) > 0:
        c = mejor_candidato(candidatos)
        candidatos.remove(c)

        # Actualizamos mínimo y máximo si es necesario
        if c < minimo:
            minimo = c
        if c > maximo:
            maximo = c
    
    return [minimo, maximo]

# Ejemplo de uso
vector = [7, 2, 9, 3, 1, 6, 8, 4]
resultado = voraz(vector)
print(f"Mínimo: {resultado[0]}, Máximo: {resultado[1]}")
