
import infoFun
import random

def leesElementen(bestand):
    elementen = []
    afkortingen = []
    f = open(bestand)
    inhoud = f.readlines()
    for regel in inhoud:
        element, afkorting = regel.strip().split(" ")
        elementen.append(element)
        afkortingen.append(afkorting)
    f.close()
    return elementen, afkortingen

# Lees het bestand PSE.txt in
elementen, afkortingen = leesElementen("VoorbeeldExamen1-Bestanden\PSE.txt") 

# Instructies
#############################################################################
#%% DEELVRAAG 1
#------------------------------------------------------------------------------
atoomnummer = random.randint(0, len(elementen))+1
antwoord = True

while True:
    symbool = input("Geef het symbool en en het atoomnummer van {}:".format(elementen[atoomnummer]))
    symbool = symbool.split(",")
    controle = True
    if len(symbool) != 2:
        controle = False
    elif symbool[0].isalpha() == False:
        controle = False
    elif symbool[1].isnumeric() == False:
        controle = False
    if controle == False:
        print("Het antwoord is ongeldig.")
    if controle == True:
        break

if symbool[0] != afkortingen[atoomnummer]:
    antwoord = False
if symbool[1] != atoomnummer:
    antwoord = False

if antwoord == True:
    print("Juist!")
if antwoord == False:
    print("Fout, het juiste antwoord was", afkortingen[atoomnummer], atoomnummer)



#%% DEELVRAAG 2
#------------------------------------------------------------------------------
