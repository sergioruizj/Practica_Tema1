def emparejar_botellas_corchos(botellas, corchos):
    if not botellas or not corchos:
        return []
    
    if len(botellas) == 1:
        if (probar_corcho(botellas[0], corchos[0]) == "justo"):
            return [(botellas[0], corchos[0])] 
        else:
            return []
    

    mitad = len(botellas) // 2
    botella_mid = botellas[mitad]
    
    botellas_izq, botellas_der = [], []
    corchos_izq, corchos_der = [], []
    parejas = []
    
    for corcho in corchos:
        resultado = probar_corcho(botella_mid, corcho)
        if resultado == "pequeño":
            corchos_izq.append(corcho)
        elif resultado == "grande":
            corchos_der.append(corcho)
        else:
            parejas.append((botella_mid, corcho)) 
    
    
    for botella in botellas:
        if botella != botella_mid:
            if botella < botella_mid:
                botellas_izq.append(botella)
            else:
                botellas_der.append(botella)
    
    
    parejas_izq = emparejar_botellas_corchos(botellas_izq, corchos_izq)
    parejas_der = emparejar_botellas_corchos(botellas_der, corchos_der)
    
    return parejas + parejas_izq + parejas_der


def probar_corcho(botella, corcho):
    if corcho < botella:
        return "pequeño"
    elif corcho > botella:
        return "grande"
    else:
        return "justo"



# Probador
botellas = [5, 2, 8, 3, 7]  # Representación ficticia de los tamaños de las botellas
corchos = [3, 7, 2, 8, 5]  # Representación ficticia de los tamaños de los corchos
parejas = emparejar_botellas_corchos(botellas, corchos)
print(parejas)