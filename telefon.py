import math

def mpbe(o, p, mp):
    mp = int(mp) + 60*int(p) + 3600*int(o)
    return mp
def vissza(mp):
    o = math.floor(mp/3600)
    mp -= o*3600
    p = math.floor(mp/60)
    mp -= p*60
    return o, p, mp

f = open('hivas.txt', 'rt')

hivasok = []
for sor in f:
    sor = sor.strip().split()
    print(sor)
    tmp = []
    tmp.append(mpbe(sor[0], sor[1], sor[2]))
    tmp.append(mpbe(sor[3], sor[4], sor[5]))
    hivasok.append(tmp)

print(hivasok)
