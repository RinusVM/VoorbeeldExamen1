
import infoFun
import copy
##################################################################
# Functiedefinities
##################################################################

def formateerTijd(sec):
    """
    WIJZIG DEZE FUNCTIE NIET!
    Met deze functie kan je tijd in seconden om te zetten
    naar het mm:ss.hs formaat.
    """
    return "{:02d}:{:05.2f}".format(int(sec // 60), sec % 60)


def importeerContainer(bestandsnaam):
    gegevens = infoFun.listRead("VoorbeeldExamen1-Bestanden\{}".format(bestandsnaam))
    gegevens_tabel = []
    for gegevens_str in gegevens:
        gegevens_lst = gegevens_str.split(";")
        gegevens_tabel.append(gegevens_lst)
    return gegevens_tabel[1:]
    
def berekenEindtijd(resultaten):
    lopen = int(resultaten[0][:2])*60 + float(resultaten[0][3:])
    g = resultaten[1].split(" ") 
    golf = int(g[0])/3
    roeien = int(resultaten[2][:2])*60 + float(resultaten[2][3:])
    schieten = int(resultaten[3])*10
    eindtijd = lopen - golf + roeien - schieten
    return(eindtijd)
 

def geefKlassement(container):
    print("{:>3}   {:<25}{:^9}".format("Nr","Naam en voornaam","Eindtijd"))
    klassement = []
    for i in container:
        tijd = berekenEindtijd(i[1:])
        klassement.append(tijd)
    klassementcopy = copy.deepcopy(klassement)
    klassement.sort()
    nr = 1
    for i in klassement[:5]:
        teller = 0
        for j in klassementcopy:
            teller += 1
            if i == j:
                tijd = formateerTijd(j)
                print("{:>3}   {:<25}{:^9}".format(nr,container[teller-1][0],tijd))
                nr +=1

def imputeerData(resultaten,container):
    lopenLijst = []
    golfLijst = []
    roeienLijst = []
    schietenLijst = []
    for resultaat in container:
        lopen = int(resultaat[1][:2])*60 + float(resultaat[1][3:])
        lopenLijst.append(lopen)
        g = resultaat[2].split(" ") 
        golf = int(g[0])
        golfLijst.append(golf)
        roeien = int(resultaat[3][:2])*60 + float(resultaat[3][3:])
        roeienLijst.append(roeien)
        schieten = int(resultaat[4])
        schietenLijst.append(schieten)
    gemLopen = sum(lopenLijst)/len(lopenLijst)
    gemLopen = formateerTijd(gemLopen)
    gemGolf = round(sum(golfLijst)/len(lopenLijst))
    gemRoeien = sum(roeienLijst)/len(lopenLijst)
    gemRoeien = formateerTijd(gemRoeien)
    gemSchieten = round(sum(schietenLijst)/len(lopenLijst))
    if resultaten[0] == " ":
        resultaten[0] = gemLopen 
    if resultaten[1] == " ":
            resultaten[1] = gemGolf
    if resultaten[2] == " ":
            resultaten[2] = gemRoeien
    if resultaten[3] == " ":
            resultaten[3] = gemSchieten
    return resultaten



##################################################################
# Instructies
##################################################################

# DEELVRAAG 1
# ----------------------------------------------------------------
container = importeerContainer("containercup.csv")
#print(container)


# DEELVRAAG 2
# ----------------------------------------------------------------
resultaten = container[2][1:] # resultaten 3de atleet in lijst
print(resultaten)
# ['04:29.18', '153 m', '03:12.13', '1']
eindtijd = berekenEindtijd(resultaten)

print(eindtijd)
# 400.31

resultaten = container[5][1:] # resultaten 6de atleet in lijst
print(resultaten)
# ['05:57.53', '119 m', '04:34.13', '3']
eindtijd = berekenEindtijd(resultaten)
print(eindtijd)
# 561.9933333333333


# DEELVRAAG 3
# ----------------------------------------------------------------
geefKlassement(container)
#Nr   Naam en voornaam          Eindtijd
# 1   Dennis Praet              06:40.31
# 2   Mathieu van der Poel      06:54.45
# 3   Oliver Naesen             06:55.63
# 4   Simon Mignolet            06:57.83
# 5   Thibau Nys                07:08.46

# DEELVRAAG 4
# ----------------------------------------------------------------

resultaten1 = [ " " , " 74 m " , " 03:55.80 " , " 2 " ]
resultaten2 = [ " 04:12.32 " , " " , " 02:49.80 " , " " ]
aangevuld1 = imputeerData (resultaten1[:],container)
aangevuld2 = imputeerData (resultaten2[:],container)
print(aangevuld1)
print (aangevuld2)