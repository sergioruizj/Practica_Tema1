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


def buscarValores(f: callable, x0: float, x1: float, k: float, epsilon: float) -> list:
    def buscar(a, b) -> list:
        if (abs((b - a) < epsilon)):
           return [[a, b]]
            
        
        mid = (a + b) / 2
        f_mid = f(mid)

        izq = []
        dch = []

        if ((f(a) <= k <= f_mid) or (f(a) >= k >= f_mid)):
            izq = buscar(a, mid)
        if ((f_mid <= k <= f(b)) or (f_mid >= k >= f(b))):
            dch = buscar(mid, b)

        return izq + dch
    
    return buscar(x0, x1)

def cuadrado(x):
    return x**2

def main(): 
    print(buscarValores(cuadrado, -2, 2, 1, 0.0001))

if __name__ == "__main__":
    main()

##############################
#          TESTS             #
##############################