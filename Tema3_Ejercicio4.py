def emparejar_botellas_corchos(botellas, corchos) -> list:
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


def probar_corcho(botella, corcho) -> str:
    if corcho < botella:
        return "pequeño"
    elif corcho > botella:
        return "grande"
    else:
        return "justo"



# Probador
def main():
    botellas = [5, 2, 8, 3, 7]  # Representación ficticia de los tamaños de las botellas
    corchos = [3, 7, 2, 8, 5]  # Representación ficticia de los tamaños de los corchos
    parejas = emparejar_botellas_corchos(botellas, corchos)
    print(parejas)


if __name__ == "__main__":
    main()


##############################
#          TESTS             #
##############################

def test_emparejar_botellas_corchos():
    botellas = [5, 2, 8, 3, 7]  
    corchos = [3, 7, 2, 8, 5]  


    parejas = emparejar_botellas_corchos(botellas, corchos)

    assert 5 == len(parejas)

    for pareja in parejas:
        assert pareja[0] == pareja[1]

def test_benchmark_emparejar_botellas_corchos():
    import Tests_timer
    import random

    @Tests_timer.timer
    def _timer_emparejar(botellas: list, corchos: list) -> list:
        return emparejar_botellas_corchos(botellas, corchos)
    

    botellas = list(range(1, 1001))
    corchos = list(range(1, 1001))  
    random.shuffle(botellas)
    random.shuffle(corchos)

    Tests_timer.warmup()
    resultado = _timer_emparejar(botellas, corchos)

    assert 1000 == len(resultado[0])

    for pareja in resultado[0]:
        assert pareja[0] == pareja[1]

    print(f'\n\nSe ha empleado un total de {resultado[1]} ms en la ejecución del test para un ejemplo de {len(botellas)} elementos')