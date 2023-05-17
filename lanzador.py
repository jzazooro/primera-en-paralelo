from procesos.secuencialmente import secuencial
from procesos.multiprocesamiento import multiproceso
from time import time

def main():
    sec=time()
    print("En secuencial: ", "\n")
    secuencial()
    print("Ha tardado: ", time() - sec, " segundos", "\n")
    mult=time()
    print("En multiprocesamiento: ", "\n")
    multiproceso()
    print("Ha tardado: ", time() - mult, " segundos", "\n")
