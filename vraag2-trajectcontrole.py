import infoFun
    
#############################################################################
# Functiedefinities
#############################################################################
def tijd_str2sec(tijd):
    """
    WIJZIG DEZE FUNCTIE NIET!
    Deze functie wordt gebruikt in de functie tijdsverschil.
    """
    tijd_lst = tijd.replace('.', ':').split(':')
    for i in range(len(tijd_lst)):
        tijd_lst[i] = int(tijd_lst[i])
    omzetting = [3600, 60, 1, 0.01]
    tijd_sec = 0.0
    for i in range(len(tijd_lst)):
        tijd_sec += tijd_lst[i] * omzetting[i]
    return tijd_sec

def tijdsverschil(tijd1, tijd2):
    """
    WIJZIG DEZE FUNCTIE NIET!
    Deze functie wordt gebruikt in DEELVRAAG 4 om het tijdsverschil
    in seconden te bepalen tussen twee tijdstippen van de vorm HH.MM.SS.hh.
    Je hoeft de syntax in deze functie niet te begrijpen om
    deze opdracht op te lossen!!
    """
    tijd1_sec = tijd_str2sec(tijd1)
    tijd2_sec = tijd_str2sec(tijd2)
    return tijd2_sec - tijd1_sec


def leesData(bestandsnaam):
    data = infoFun.listRead(f"VoorbeeldExamen2-Bestanden\{bestandsnaam}")
    dataLijst = []
    for i in data:
        i = i.split(";")
        dataLijst.extend([i])
    return dataLijst

    
def geefNummers(lijst_cam):
    dataLijst = []
    for i in lijst_cam:
        dataLijst.append([i[1]])
    return dataLijst
 


#############################################################################
# Instructies
#############################################################################

# VOORBEELD GEBRUIK VAN FUNCTIE tijdsverschil
# --------------------------------------------------------------------------
delta_t = tijdsverschil("11:08:15.30", "11:15:28.95")
#print(delta_t)                     # 433.65


# DEELVRAAG 1 --> leesData oproepen
# ---------------------------------------------------------------------------
lijst_cam1 = leesData("data_meetpunt1.csv")
lijst_cam2 = leesData("data_meetpunt2.csv")
#print(len(lijst_cam1), len(lijst_cam2))      # 412 430


# DEELVRAAG 2 --> geefNummers oproepen
# ---------------------------------------------------------------------------
lijst_cam1_nr = geefNummers(lijst_cam1)
#print(len(lijst_cam1_nr))                           # 412
lijst_cam2_nr = geefNummers(lijst_cam2)
#print(len(lijst_cam2_nr))                           # 430



# DEELVRAAG 3 --> Aantal gecontroleerden
# ---------------------------------------------------------------------------
teller = 0
selectie = []

for i in lijst_cam1_nr:
    for j in lijst_cam2_nr:
        if i == j:
         selectie.append(i)
         teller += 1

print("Aantal gecontroleerden:", teller)


# DEELVRAAG 4 --> Aantal overtredingen + tabel
# ---------------------------------------------------------------------------
vTijd = 3600/77
teller = 0
Nummerplaat = []
Snelheid = []
for i in selectie:
    for j in range(len(lijst_cam1)):
        if i == [lijst_cam1[j][1]]:
           for k in range(len(lijst_cam2)):
                if i == [lijst_cam2[k][1]]:
                    delta_t = tijdsverschil(lijst_cam1[j][0] , lijst_cam2[k][0])
                    if delta_t < vTijd:
                        teller +=1
                        Nummerplaat.append(lijst_cam1[j][1])
                        Snelheid.append(3600/delta_t)

print(f"Aantal overtredingen:{teller}")
print("Nummerplaat    Snelheid (km/h)")       
print("="*30)
for i in range(len(Nummerplaat)):
    print("{:<20s}  {:>8.2f}".format(Nummerplaat[i],Snelheid[i]))

