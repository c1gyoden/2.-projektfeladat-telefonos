import math
class Szamolas():
    def __init__(self, o, p, mp):
        self.o = o
        self.p = p
        self.mp = mp

    def mpbe(self):
        mp = int(self.mp) + 60*int(self.p) + 3600*int(self.o)
        return mp

f = open('hivas.txt', 'rt')

hivasok = []
for sor in f:
    sor = sor.strip().split()
    print(sor)
    tmp = []
    tmp.append(Szamolas(sor[0], sor[1], sor[2]))
    tmp.append(Szamolas(sor[3], sor[4], sor[5]))
    hivasok.append(tmp)



