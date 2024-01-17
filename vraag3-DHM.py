import numpy as np
import matplotlib.pyplot as plt

#############################################################################
# Functiedefinities
#############################################################################
def isBergtop(rij, kol, DHM):
    omgv = DHM[rij-1:rij+2,kol-1:kol+2]
    Z = omgv <= DHM[rij,kol]
    return np.all(Z)

def telBergtoppen(DHM):
    teller = 0
    r, k = DHM.shape
    for i in range(1,r-1):
        for j in range(1,k-1):
            bt = isBergtop(i,j,DHM)
            if bt:
                teller += 1
    return teller



def geefBergtoppen(DHM):
    r, k = DHM.shape
    cor = []
    for i in range(1,r-1):
        for j in range(1,k-1):
            bt = isBergtop(i,j,DHM)
            if bt: 
                cor.extend([[i,j]])
    return cor

def isHillClimber(locaties, DHM):
    r,k= locaties.shape
    for i in range(r-1):
        rij = locaties[i,0]
        kol = locaties [i,1]
        rij2 = locaties[i+1,0]
        kol2 = locaties [i+1,1]
        kopie = np.copy(DHM)
        land = kopie[rij-1:rij+2,kol-1:kol+2]
        maxi = np.argmax(land)
        rijmax= maxi//3
        kolmax=maxi%3
        maxnum= np.array([rijmax,kolmax])
        vrij=rij2-rij
        vkol= kol2-kol
        volgende=np.array([vrij+1,vkol+1])
        #print(maxnum)
        #print(volgende)
        if np.any(maxnum != volgende):
            return False
    return True

    



#############################################################################
# Instructies
#############################################################################
DHM = np.loadtxt("VoorbeeldExamen2-Bestanden\DHM.txt", delimiter = ",")

# Deelvraag 1 (a)
res = isBergtop(3, 2, DHM) # False
#print(res)
res = isBergtop(1, 7, DHM) # True
#print(res)


# Deelvraag 1 (b)
aantal = telBergtoppen(DHM)
#print(aantal) # 3


# Deelvraag 1 (c)
toppen = geefBergtoppen(DHM)
#print(toppen) # [[1 , 7], [6, 6], [8, 2]] # [1, 7] --> locatie top 30


# Deelvraag 2
locaties = np.array([[1, 2], [2, 3], [3, 4], [2, 5], [2, 6], [1, 7]])
res =  isHillClimber(locaties, DHM)
print(res)  # True

locaties2 = np.array([[4, 5], [3, 6], [2, 7], [1, 7]])
res2 =  isHillClimber(locaties2, DHM)
print(res2) # False





