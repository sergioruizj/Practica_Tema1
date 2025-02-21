import random

def mejor_candidatoA(candidatos :list) -> any:
    """ Devuelve el mejor candidato """
    pareja = (candidatos[0], candidatos[1])
    candidatos = candidatos[2:]
    return pareja, candidatos

def vorazA(candidatos :list) -> list:
    solucion = []
    while len(candidatos) > 0:
        pareja, candidatos = mejor_candidatoA(candidatos)
        solucion.append(pareja)
    return solucion


#Probador Apartado A
lista = [5,8,1,4,7,9]
parejas = vorazA(lista)
mayor = 0
for pareja in parejas:
    mayor = max(mayor, pareja[0] + pareja[1])
print(f"La solución al apartado A con la lista predeterminada: \n {lista} \nes {mayor}")



########################################################################################################################################



def mejor_candidatoB(candidatos :list) -> any:
    """ Devuelve el mejor candidato """
    pareja = (candidatos[0], candidatos[-1])
    candidatos = candidatos[1:-1]
    return pareja, candidatos

def vorazB(candidatos :list) -> list:
    solucion = []
    candidatos = sorted(candidatos)
    while len(candidatos) > 0:
        pareja, candidatos = mejor_candidatoB(candidatos)
        solucion.append(pareja)
    return solucion


#Probador Apartado B
lista = [5,8,1,4,7,9]
parejas = vorazB(lista)
mayor = 0
for pareja in parejas:
    mayor = max(mayor, pareja[0] + pareja[1])
print(f"\nLa solución al apartado B con la lista predeterminada: \n {lista} \nes {mayor}")


#Probador Apartado B Aleatorio
lista= []
for i in range(20):
    lista.append(random.randint(1,20))
parejas2 = vorazB(lista)
mayor = 0
for pareja in parejas2:
    mayor = max(mayor, pareja[0] + pareja[1])
print(f"\nLa solución al apartado B con la lista aleatoria: \n {lista} \nes {mayor}")