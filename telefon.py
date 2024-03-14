import math
class Szamolas():
    def __init__(self, o, p, mp):
        self.o = int(o)
        self.p = int(p)
        self.mp = int(mp)

    def __str__(self):
        return f'{self.o} óra {self.p} perc {self.mp} másodperc'

    def mpbe(self):
        mp = self.mp + 60*self.p + 3600*self.o
        return mp

class BekapcsoltAdatok:
    def __init__(self, azonosito, kezd, bef, varakozas):
        self.azonosito = int(azonosito)
        self.kezd = int(kezd)
        self.bef = int(bef)
        self.varakozas = int(varakozas)

    def __str__(self):
        return f'{self.azonosito} {vissza(self.kezd)} {vissza(self.bef)} {self.varakozas}'


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
    print(f'{k} óra - {v} hívás')

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

idopont = Szamolas(ora, perc, masodperc).mpbe()

hivok = []
beszelo = 0
for h in hivasok:
    if len(hivok) == 0:
        beszelo += 1
    
    kezd = h[0].mpbe()
    bef = h[1].mpbe()
    if kezd <= idopont and bef >= idopont:
        hivok.append([kezd, bef])

if len(hivok) == 0:
    print("Nem volt beszélő.")
else:
    print(f'{len(hivok)-1} hívó várakozott; a {beszelo}. hívóval beszélt az alkalmazott.')



munkaidonbelul = []

for h in hivasok:
    kezd = h[0].mpbe()
    bef = h[1].mpbe()

    if bef > Szamolas(8,0,0).mpbe() and kezd < Szamolas(12,0,0).mpbe():
        munkaidonbelul.append([kezd, bef, hivasok.index(h)+1])


bekapcsolt = []
varakozasido = 0
bekapcsolt.append(BekapcsoltAdatok(munkaidonbelul[0][2], munkaidonbelul[0][0], munkaidonbelul[0][1], 0))
if bekapcsolt[0].kezd < Szamolas(8,0,0).mpbe():
    bekapcsolt[0].kezd = Szamolas(8,0,0).mpbe()

for i in range(1, len(munkaidonbelul)):
    kezd = munkaidonbelul[i][0]
    bef = munkaidonbelul[i][1]
    if bef > bekapcsolt[-1].bef:
        varakozasido = bekapcsolt[-1].bef - kezd 
        kezd = bekapcsolt[-1].bef
        azonosito = munkaidonbelul[i][2]

        bekapcsolt.append(BekapcsoltAdatok(azonosito, kezd, bef, varakozasido))
        

print('6. feladat:')
print(f'Az utolsó bekapcsolt telefonáló azonosítója: {bekapcsolt[-1].azonosito}, várakozási ideje: {bekapcsolt[-1].varakozas} másodperc')

