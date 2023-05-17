# primera-en-paralelo

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/primera-en-paralelo.git)

He resuelto el ejercicio de nuestra primera tarea en paralelo

### Main

```
from lanzador import main

if __name__ == '__main__':
    main()
```


### Lanzador

```
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
```

### scrape

```
import random
from time import sleep

def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration
```

### Procesos (multiprocesamiento)

```
from multiprocessing import Pool
from scrape import scrape


urls = ["a.com", "b.com", "c.com", "d.com"]

def multiproceso():
    pool=Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()
    print()
    for row in data: 
        print(row)
```

### Procesos (secuencialmente)

```
from scrape import scrape

urls = ["a.com", "b.com", "c.com", "d.com"]


def secuencial():
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)
    print('\n')
    for i in output:
        print(i)
```
