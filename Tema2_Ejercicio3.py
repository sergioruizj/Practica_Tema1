def encontrar_min_max(vector):
    n = len(vector)
    
    if n == 0:
        return None, None  # Caso de vector vacío
    
    # Inicialización dependiendo de si n es par o impar
    if n % 2 == 0:
        minimo, maximo = min(vector[0], vector[1]), max(vector[0], vector[1])
        i = 2  # Comenzamos desde el tercer elemento
    else:
        minimo, maximo = vector[0], vector[0]
        i = 1  # Comenzamos desde el segundo elemento

    # Recorremos en pares
    while i < n - 1:
        if vector[i] < vector[i + 1]:
            minimo = min(minimo, vector[i])
            maximo = max(maximo, vector[i + 1])
        else:
            minimo = min(minimo, vector[i + 1])
            maximo = max(maximo, vector[i])
        i += 2  # Avanzamos de dos en dos

    return minimo, maximo

# Ejemplo de uso
vector = [7, 2, 9, 3, 1, 6, 8, 4]
minimo, maximo = encontrar_min_max(vector)
print(f"Mínimo: {minimo}, Máximo: {maximo}")
