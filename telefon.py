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
    tmp = []
    tmp.append(Szamolas(sor[0], sor[1], sor[2]))
    tmp.append(Szamolas(sor[3], sor[4], sor[5]))
    hivasok.append(tmp)


print('\n3. feladat')
stat = {}
for h in hivasok:
    ora = h[0].o
    if ora in stat.keys():
        stat[ora] += 1
    else:
        stat[ora] = 1

for k,v in stat.items():
    print(f'{k} óra - {v} db')

print('\n4. feladat')
hivasidoLista = []
for h in hivasok:
    hivasido = h[1].mpbe() - h[0].mpbe()
    hivasidoLista.append(hivasido)

print(f'A leghosszabb hívás hossza {max(hivasidoLista)} másodperc, sorszáma: {hivasidoLista.index((max(hivasidoLista)))+1}')

print('\n5. feladat')

idopont = str(input('Kérek egy időpontot szóközzel elválasztva (óra perc másodperc): '))
idopont = idopont.split()
while len(idopont) != 3:
    print('Helytelen adatbevitel!')
    idopont = str(input('Kérek egy új időpontot szóközzel elválasztva (óra perc másodperc): '))
    idopont = idopont.split()
ora = int(idopont[0])
perc = int(idopont[1])
masodperc = int(idopont[2])

while ora < 8 or ora > 12 or perc > 60 or perc < 0 or masodperc > 60 or masodperc < 0 or len(idopont) != 3:
    if ora > 23 or ora < 0 or perc > 60 or perc < 0 or masodperc > 60 or masodperc < 0:
        print('Az időpont nem létezik!')
        idopont = str(input('Kérek egy új időpontot szóközzel elválasztva (óra perc másodperc): '))
    elif ora < 8 or ora > 12:
        print('Az időpont munkaidőn kívül esik!')
        idopont = str(input('Kérek egy új időpontot szóközzel elválasztva (óra perc másodperc): '))
    idopont = idopont.split()    
    while len(idopont) != 3:
        print('Helytelen adatbevitel!')
        idopont = str(input('Kérek egy új időpontot szóközzel elválasztva (óra perc másodperc): '))
        idopont = idopont.split()

    ora = int(idopont[0])
    perc = int(idopont[1])
    masodperc = int(idopont[2])

print(idopont)