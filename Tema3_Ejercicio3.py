'''Se tiene acceso a una función f(x) de la que se sabe que en el intervalo real [p1, p2] 
tiene un único mínimo local en el punto x0, que es estrictamente decreciente entre 
[p1, x0] y  que  es  estrictamente  creciente  entre [x0, p2].  Hay  que  observar  que  x0 
puede coincidir con p1 o con p2. Se tiene que buscar, de la manera más eficiente posible, todos los puntos x (si es 
que  existen)  del  intervalo  [p1, p2] tales  que  la  función  f tome  un  cierto  valor  k,  es  
decir, se busca el conjunto de valores { x ∈ [p1, p2]  tal que f(x) = k}. Para 
simplificar  el  proceso,  en  vez  del  valor  exacto  de  cada  x puede  indicarse  un  
intervalo  de  valores  [a, b] ,  con  b - a < 𝜀,  donde  se  encuentre  x.  Los  datos  del  
algoritmo  serán  el  intervalo  [p1, p2],  el  valor k que  se  está  buscando,  y  el  valor  𝜀𝜀 
para la aproximación.'''


def buscarValores(f: callable, p1: float, p2: float, k: float, epsilon: float) -> list:
    def buscar(a, b) -> list:
        if abs(b - a) < epsilon:
            if f(a) <= k <= f(b) or f(a) >= k >= f(b):
                return [[a, b]]  
            else: 
                return []
        
        mid = (a + b) / 2
        f_mid = f(mid)
        
        izq, dch = [], []
        
        if (f(a) <= k <= f_mid) or (f(a) >= k >= f_mid):
            izq = buscar(a, mid)
        if (f_mid <= k <= f(b)) or (f_mid >= k >= f(b)):
            dch = buscar(mid, b)

        ''' Hasta ahora el método sigue buscando aunque se cumpla la condición inicial, a continuación llevamos 
        a cabo un procedimiento para unificar intervalos que sean muy cercanos entre sí '''

        # Unificación de intervalos
        if izq and dch and abs(izq[-1][1] - dch[0][0]) < epsilon:
            return izq[:-1] + [[izq[-1][0], dch[0][1]]] + dch[1:]
        
        return izq + dch
    
    return buscar(p1, p2)

def cuadrado(x):
    return x**2

def main():
    punto = 1
    x0 = -2
    x1 = 2
    resultado = buscarValores(cuadrado, x0, x1, punto, 0.0001)
    print(f'La función f(x) = x^2, en el intervalo [{x0}, {x1}] toma valores igual a {punto} en dos puntos comprendidos en los intervalos ({resultado[0][0]}, {resultado[0][1]}), ({resultado[1][0]}, {resultado[1][1]})')

if __name__ == "__main__":
    def _func1(x: float) -> float:
        return x**3 - 4*x + 4
    
    eps1 = 0.001
    x10 = 0
    x11 = 6
    k1 = 3.9

    resultado1 = buscarValores(_func1, x10, x11, k1, eps1)
    print(resultado1)

    main()


##############################
#          TESTS             #
##############################

def test_buscarValores():
    import math

    def _cuadrado(x):
        return x**2
    
    def _seno(x):
        return math.sin(x)
    
    eps1 = 0.001
    cuadrado = buscarValores(_cuadrado, -2, 2, 1, eps1)
    
    assert len(cuadrado) == 2  # Comprobamos que hay dos puntos que toman ese valor
    assert cuadrado[0][0] <= -1 <= cuadrado[0][1]  # Comprobamos que el mínimo esta en el intervalo
    assert abs(cuadrado[0][0] - cuadrado[0][1]) <= 2 * eps1  # Comprobamos que el intervalo tenga longitud 2 epsilon
    
    seno = buscarValores(_seno, 14, 15, 0.9, eps1)
    
    assert len(seno) == 1  # Comprobamos que hay dos puntos que toman ese valor
    assert abs(seno[0][0] - seno[0][1]) <= 2 * eps1  # Comprobamos que el intervalo tenga longitud 2 epsilon
    

def test_benchmark_buscarValores():
    import Tests_timer
    import math
    
    @Tests_timer.benchmark
    def _timer_buscarValores(func: callable, x0: float, x1: float, k: float, epsilon: float) -> tuple:
        return buscarValores(func, x0, x1, k, epsilon)
    
    Tests_timer.warmup()
    print()

    def _func1(x: float) -> float:
        return x**3 - 4*x
    
    eps1 = 0.001
    x10 = 0
    x11 = 6
    k1 = -2

    resultado1 = _timer_buscarValores(_func1, x10, x11, k1, eps1)
