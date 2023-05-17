from ejercicio.multiproces import multiprocesamiento
from ejercicio.secuencia import secuencial
from time import time

def main():
    tim=time()
    print("En secuencial: ", "\n")
    secuencial()
    print("Ha tardado: ", time()-tim, " segundos", "\n")
    timdos=time()
    print("En multiprocesamiento: ", "\n")
    multiprocesamiento()
    print("Ha tardado: ", time()-timdos, " segundos", "\n")

main()