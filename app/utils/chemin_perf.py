from chemin import *
from line_profiler import *
from random import randint

@profile
def profiler():
    for i in range(1000):
        L = []
        for j in range(randint(4, 6)):
            L.append((randint(0,1000),randint(0,1000)))
        pluscourtchemin(L)

    for i in range(1000):
        L = []
        for j in range(randint(4, 6)):
            L.append((randint(0,1000),randint(0,1000)))
        pluscourtcheminexhaustif(L)

profiler()