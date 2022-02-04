import random

# Valinnat
muodot = ["stiletot", "ovaalit", "ovaalin ja neliön välimuodot", "neliöt", "coffinit", "balleriinat"]
pituudet = ["lyhyet", "keskipitkät", "pitkät"]
sävyt = ["vaaleista", "tummista", "vaaleiden ja tummien väliltä olevista"]
värit = ["punaisista", "ruskeista", "oransseista", "keltaisista", "vihreistä", "sinisistä", "violeteisesta", "mustista tai harmaista", "valkoisista"]
koristeet =["koristeita tulee joka kynteen", "koristeita tulee joihinkin kynsiin", "kynsiin ei tule koristeita"]

# Sävyt
vaaleat = []
tummat = []
neutraalit = []

f = "savyt.txt"

# Tiedostosta valittu oikeat rivit kuhunkin listaan
try:
    with open(f, "r") as file:
        vaaleat = file.read().splitlines()
        vaaleat = vaaleat[1:20]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        tummat = file.read().splitlines()
        tummat = tummat[22:33]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        neutraalit = file.read().splitlines()
        neutraalit = neutraalit[35:53]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f,"r") as file:
        kaikki_lakat = file.read().splitlines()
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")

# Kaikki lakat listassa arvontaa varten
kaikki_lakat = list(filter(("").__ne__, kaikki_lakat))
kaikki_lakat.remove("Vaaleat värit:")
kaikki_lakat.remove("Tummat värit:")
kaikki_lakat.remove("Vaalean ja tumman väliltä:")

# Värit
punainen = []
ruskea = []
oranssi = []
keltainen = []
vihreä = []
sininen = []
violetti = []
musta = []
valkoinen = []

f = "varit.txt"

# Tiedostosta valittu oikeat rivit kuhunkin listaan
try:
    with open(f, "r") as file:
        punainen = file.read().splitlines()
        punainen = punainen[1:11]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        ruskea = file.read().splitlines()
        ruskea = ruskea[13:17]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        oranssi = file.read().splitlines()
        oranssi = oranssi[19:22]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        keltainen = file.read().splitlines()
        keltainen = keltainen[24:28]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        vihreä = file.read().splitlines()
        vihreä = vihreä[30:35]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        sininen = file.read().splitlines()
        sininen = sininen[37:43]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        violetti = file.read().splitlines()
        violetti = violetti[45:52]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        musta = file.read().splitlines()
        musta = musta[54:56]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")
try:
    with open(f, "r") as file:
        valkoinen = file.read().splitlines()
        valkoinen = valkoinen[58:60]
except:
    print("Tiedoston " + f + " lukeminen ei onnistunut.")

sävy = " "
väri = " "
lakka = ""

print("")
print("\u2605   \u2605  \u2605  \u2605  \u2605")
print("")
print("Haluatko")
print("1. arpoa satunnaiset kynnet vai")
print("2. tehdä valintoja?")
print("")

arvonta = ""
while arvonta != "1" and arvonta != "2":
    arvonta = input("Valitse 1 tai 2: ")
if arvonta == "1":
    arvonta = True
elif arvonta == "2":
    arvonta = False

print("")
print("\u2605   \u2605  \u2605  \u2605  \u2605")
print("")

if arvonta == False:
    i = 4
    print("Valitse:")
    print("1. Lyhyet")
    print("2. Keskipitkät")
    print("3. Pitkät")
    print("...tai suorita arvonta painamalla enter.")
    while i not in range(1,4):
        pituus = input("Valintani on numero: ")
        if pituus.isnumeric() == True:
            i = int(pituus)
        elif pituus == "":
            break
        else:
            continue
    if pituus != "":
        pituus = int(pituus) - 1
    else:
        pituus = random.randrange(3)

    print("")
    print("\u2605   \u2605  \u2605  \u2605  \u2605")
    print("")

    i = 7
    print("Valitse kynnen muoto seuraavista:")
    print("1. Stiletto")
    print("2. Ovaali")
    print("3. Ovaalin ja neliön välimuoto")
    print("4. Neliö")
    print("5. Coffin")
    print("6. Balleriina")
    print("...tai suorita arvonta painamalla enter.")
    print("")
    
    while i not in range(1, 7):
        muoto = input("Valintani on numero: ")
        if muoto.isnumeric() == True:
            i = int(muoto)
        elif muoto == "":
            break
        else:
            continue
    if muoto != "":
        muoto = int(muoto) - 1
    else:
        muoto = random.randrange(6)
    
    print("")
    print("\u2605   \u2605  \u2605  \u2605  \u2605")  
    print("")

    i = 4
    print("Valitse:")
    print("1. Vaalea väri")
    print("2. Tumma väri")
    print("3. Jotain siltä väliltä")
    print("...tai suorita arvonta painamalla enter.")
    while i not in range(1, 4):
        sävy = input("Valintani on numero: ")
        if sävy.isnumeric() == True:
            i = int(sävy)
        elif sävy ==  "":
            break
        else:
            continue
    if sävy != "":
        sävy = int(sävy) - 1
    else:
        sävy = random.randrange(3)
    
    print("")
    print("\u2605   \u2605  \u2605  \u2605  \u2605")  
    print("")

    i = 10
    print("Valitse:")
    print("1. Punainen")
    print("2. Ruskea tai beige")
    print("3. Oranssi")
    print("4. Keltainen")
    print("5. Vihreä")
    print("6. Sininen")
    print("7. Violetti")
    print("8. Musta tai harmaa")
    print("9. Valkoinen")
    print("...tai suorita arvonta painamalla enter.")
    while i not in range(1, 10):
        väri = input("Valintani on numero: ")
        if väri.isnumeric() == True:
            i = int(väri)
        elif väri == "":
            break
        else:
            continue
    if väri != "":
        väri = int(väri) - 1
    else:
        väri = random.randrange(9)

    print("")
    print("\u2605   \u2605  \u2605  \u2605  \u2605") 
    print("")

    i = 4
    print("Valitse:")
    print("1. Koristeita kaikkiin kynsiin")
    print("2. Koristeita joihinkin kynsiin")
    print("3. Ei koristeita ollenkaan")
    print("...tai suorita arvonta painamalla enter.")
    while i not in range(1, 4):
        koriste = input("Valintani on numero: ")
        if koriste.isnumeric() == True:
            i = int(koriste)
        elif koriste ==  "":
            break
        else:
            continue
    if koriste != "":
        koriste = int(koriste) - 1
    else:
        koriste = random.randrange(3)

    # Lakka valitaan kahden listan yhteisistä lakkavaihtoehdoista
    # Tähän en keksinyt mitän lyhyempää tapaa kirjoittaa koodia...

    if sävy == 0 and väri == 0:
        vPunainen = list(set(vaaleat).intersection(punainen))
        lakka = vPunainen[random.randrange(len(vPunainen) - 1)]
    elif sävy == 0 and väri == 1:
        vRuskea = list(set(vaaleat).intersection(ruskea))
        lakka = vRuskea[random.randrange(len(vRuskea) - 1)]
    elif sävy == 0 and väri == 2:
        vOranssi = list(set(vaaleat).intersection(oranssi))
        lakka = vOranssi[0]
    elif sävy == 0 and väri == 3:
        vKeltainen = list(set(vaaleat).intersection(keltainen))
        lakka = vKeltainen[random.randrange(len(vKeltainen) - 1)]
    elif sävy == 0 and väri == 4:
        vVihreä = list(set(vaaleat).intersection(vihreä))
        lakka = vVihreä[random.randrange(len(vVihreä) - 1)]
    elif sävy == 0 and väri == 5:
        vSininen = list(set(vaaleat).intersection(sininen))
        lakka = vSininen[random.randrange(len(vSininen) - 1)]
    elif sävy == 0 and väri == 6:
        vVioletti = list(set(vaaleat).intersection(violetti))
        lakka = vVioletti[random.randrange(len(vVioletti) - 1)]
    elif sävy == 0 and väri == 7:
        vMusta = list(set(vaaleat).intersection(musta))
        lakka = vMusta[random.randrange(len(vMusta) - 1)]
    elif sävy == 0 and väri == 8:
        vValkoinen = list(set(vaaleat).intersection(valkoinen))
        lakka = vValkoinen[random.randrange(len(vValkoinen) - 1)]
    # Esim. tumman punaisia on vain yksi, randrange ei toimi...
    elif sävy == 1 and väri == 0:
        tPunainen = list(set(tummat).intersection(punainen))
        lakka = tPunainen[0]
    elif sävy == 1 and väri == 1:
        tRuskea = list(set(tummat).intersection(ruskea))
        lakka = tRuskea[random.randrange(len(tRuskea) - 1)]
    # Esim. tumman oransseja ei ole. Tähän en keksinyt hyvää ratkaisua ohittaa tilannetta:
    elif sävy == 1 and väri == 2:
        lakka = "\u2192 Ei sopivaa lakkaa hakuehdoilla"
    elif sävy == 1 and väri == 3:
        tKeltainen = list(set(tummat).intersection(keltainen))
        lakka = tKeltainen[random.randrange(len(tKeltainen) - 1)]
    elif sävy == 1 and väri == 4:
        tVihreä = list(set(tummat).intersection(vihreä))
        lakka = tVihreä[random.randrange(len(tVihreä) - 1)]
    elif sävy == 1 and väri == 5:
        tSininen = list(set(tummat).intersection(sininen))
        lakka = tSininen[random.randrange(len(tSininen) - 1)]
    elif sävy == 1 and väri == 6:
        tVioletti = list(set(tummat).intersection(violetti))
        lakka = tVioletti[random.randrange(len(tVioletti) - 1)]
    elif sävy == 1 and väri == 7:
        tMusta = list(set(tummat).intersection(musta))
        lakka = tMusta[random.randrange(len(tMusta) - 1)]
    elif sävy == 1 and väri == 8:
        lakka = "\u2192 Ei sopivaa lakkaa hakuehdoilla"
    elif sävy == 2 and väri == 0:
        nPunainen = list(set(neutraalit).intersection(punainen))
        lakka = nPunainen[random.randrange(len(nPunainen) - 1)]
    elif sävy == 2 and väri == 1:
        nRuskea = list(set(neutraalit).intersection(ruskea))
        lakka = nRuskea[random.randrange(len(nRuskea) - 1)]
    elif sävy == 2 and väri == 2:
        nOranssi = list(set(neutraalit).intersection(oranssi))
        lakka = nOranssi[random.randrange(len(nOranssi) - 1)]
    elif sävy == 2 and väri == 3:
        nKeltainen = list(set(neutraalit).intersection(keltainen))
        lakka = nKeltainen[random.randrange(len(nKeltainen) - 1)]
    elif sävy == 2 and väri == 4:
        nVihreä = list(set(neutraalit).intersection(vihreä))
        lakka = nVihreä[random.randrange(len(nVihreä) - 1)]
    elif sävy == 2 and väri == 5:
        nSininen = list(set(neutraalit).intersection(sininen))
        lakka = nSininen[random.randrange(len(nSininen) - 1)]
    elif sävy == 2 and väri == 6:
        nVioletti = list(set(neutraalit).intersection(violetti))
        lakka = nVioletti[random.randrange(len(nVioletti) - 1)]
    elif sävy == 2 and väri == 7:
        nMusta = list(set(neutraalit).intersection(musta))
        lakka = nMusta[random.randrange(len(nMusta) - 1)]
    elif sävy == 2 and väri == 8:
        nValkoinen = list(set(neutraalit).intersection(valkoinen))
        lakka = nValkoinen[random.randrange(len(nValkoinen) - 1)]

    print("")
    print("\u2605   \u2605  \u2605  \u2605  \u2605")  
    print("")

    print ("TULOS:")
    print("")
    print("\u00B7 Kynsistä tulee " + pituudet[pituus] + " " + muodot[muoto] + ".")
    print("")
    print("\u00B7 " + sävyt[sävy].capitalize() + " " + värit[väri] + " lakoista valittiin " + lakka + ".")
    print("")
    print("\u00B7 " + koristeet[koriste].capitalize() + ".")
    print("")
    
elif arvonta == True:

    pituus = random.randrange(3)
    muoto = random.randrange(6)
    koriste = random.randrange(3)
    lakka = kaikki_lakat[random.randrange(len(kaikki_lakat)-1)]
       
    print ("TULOS:")
    print("")
    print("\u00B7 Kynsistä tulee " + pituudet[pituus] + " " + muodot[muoto] + ".")
    print("")
    print("\u00B7 Lakoista valittiin " + lakka + ".")
    print("")
    print("\u00B7 " + koristeet[koriste].capitalize() + ".")
    print("")