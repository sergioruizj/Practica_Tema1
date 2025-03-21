'''Tras  su  paso  por  la  Sala  de  las  Baldosas  y  conseguir  la  Cuna  de  la  Vida,  ahora  
Indiana  Croft  se  enfrenta  a  un  nuevo  desafío  antes  de  poder  salir  del  Templo  
Maldito. Se encuentra en un puente bajo el que se observa una profunda oscuridad. Afortunadamente,  este  lugar  también  aparece  en  el  diario.  El  puente  cruza  el  
llamado Valle de Sombras, que empieza con una pendiente de bajada (la pendiente 
no es necesariamente constante) para después de llegar al punto más bajo 
empezar  a  subir  hasta  el  otro  extremo  del  puente  (de  nuevo,  no  necesariamente  
con pendiente contante). Justo en la parte inferior del valle hay un río, pero el diario 
no especifica su ubicación con respecto al puente (por ejemplo, no se sabe si el río 
está a 53 metros desde el comienzo del puente) ni la distancia en altura (es decir, 
no se sabe si el río está 228 metros por debajo, por ejemplo). En las pendientes hay 
afiladísimas rocas. Si Indiana Croft tuviese tiempo, podría encontrar sin problema el punto por donde 
descolgarse del puente para llegar exactamente al río, ya que tiene un puntero laser 
para medir alturas que le dice cuántos metros hay desde el puente hasta el suelo 
en  un  punto  determinado.  El  problema  es  que  los  sacerdotes  del  templo  han 
averiguado  que  les  han  robado  la  Cuna  de  la  Vida,  están  persiguiendo  a  Indiana  
Croft  y  le  alcanzarán  enseguida.  El  aventurero  debe  encontrar  rápidamente  la  
posición del río para descolgarse y huir seguro. Diseñar  el  algoritmo  que  debería  usar  Indiana  Croft  para  buscar  el  punto  mínimo  
del valle en las condiciones indicadas. El algoritmo debe ser eficiente: al menos en 
el mejor caso debe tener un orden logarítmico. Se puede considerar el tiempo que 
tarda Indiana Croft en desplazarse a lo largo del puente es nulo y que la estimación 
del punto del río por donde descolgarse puede tener un error de aproximación de ε 
metros (ε es una constante dada).'''

# En la firma del método "buscarMinimo" metémos como parámetro la funcion que defina la forma del supuesto puente.
# Hay que tener cuidado para que dicha función en el intervalo [x0, x1] tenga un solo mínimo.

def buscarMinimo(funcion: callable, x0: int, x1: int, epsilon: float) -> float:
    def buscar(a: int, b: int) -> float:
        mitad = (a + b)/2

        if abs(((b - a)) < epsilon):
            return mitad
       

        if (funcion(mitad - epsilon) > funcion(mitad + epsilon)):
            return buscar(mitad, b)
        else:
            return buscar(a, mitad)

    return buscar(x0, x1)

def cuadrado(x):
    return x**2


def main(): 
    resultado = buscarMinimo(cuadrado, -200, 20, 0.0001)
    print(f'El mínimo de la función f(x) = x^2 en el intervalo [-200, 20] con epsiln 0.0001 es {resultado}')

if __name__ == "__main__":
    main()

##############################
#          TESTS             #
##############################

def test_buscarMinimo():
    def _cuadrado(x: int) -> int: # Mínimo en x = 0
        return x**2
    
    def _cuadrado1(x: int) -> int: # Mínimo en x = 1
        return x**2 -2*x
    
    def _cuadrado2(x: int) -> int: # Mínimo en x = 2
        return x**2 - 4*x
    
    def _cuadrado3(x: int) -> int: # Mínimo en x = 3
        return x**2 - 6*x
    
    def _cuadrado4(x: int) -> int: # Mínimo en x = 4
        return x**2 - 8*x
    

    # Array con los mínimos calculados con "buscarMinimo()"
    resultados = [buscarMinimo(_cuadrado, 0, 10, 0.0001), buscarMinimo(_cuadrado1, 0, 10, 0.0001), 
                  buscarMinimo(_cuadrado2, 0, 10, 0.0001), buscarMinimo(_cuadrado3, 0, 10, 0.0001), 
                  buscarMinimo(_cuadrado4, 0, 10, 0.0001)]
    

    # Comprobación de los mínimos obtenidos con los mínimos reales de las funciones
    for i in range(5):
        assert abs(resultados[i] - i) <= 0.0001

def test_benchmark_buscarMinimo():
    import Tests_timer
    import math
    
    @Tests_timer.timer
    def _timer_buscarMinimo(func: callable, x0: int, x1: int, epsilon: float) -> tuple:
        return buscarMinimo(func, x0, x1, epsilon)
    
    Tests_timer.warmup()
    print()

    def _seno1(x: float) -> float:
        return math.sin(x)
    
    def _seno2(x: float) -> float:
        return math.sin(math.sqrt(x))
    
    def _seno3(x: float) -> float:
        return 5*x*math.sin(x)
    
    eps1 = 0.0001
    eps2 = 0.0000001
    eps3 = 0.001

    x00 = -1
    x01 = 1
    x10 = 3
    x11 = 56
    x20 = 8.2
    x21 = 14.2

    resultado1 = _timer_buscarMinimo(_seno1, x00, x01, eps1)
    resultado2 = _timer_buscarMinimo(_seno2, x10, x11, eps2)
    resultado3 = _timer_buscarMinimo(_seno3, x20, x21, eps3)

    assert abs(resultado1[0] + 1) <= eps1
    assert abs(resultado2[0] - 22.20661) <= eps2
    assert abs(resultado3[0] - 11.08553846) <= eps3

    print(f'\nTiempo empleado para la funcion f(x) = sen(x) en [{x00}, {x01}] con epsilon {eps1}: {resultado1[1]} ms\n')

    print(f'Tiempo empleado para la funcion f(x) = sen(sqrt(x)) en el intervalo [{x10}, {x11}] con epsilon {eps2}: {resultado2[1]} ms\n')

    print(f'Tiempo empleado para la funcion f(x) = 5sen(x) en el intervalo [{x20}, {x21}] con epsilon {eps3}: {resultado3[1]} ms\n')
