#%% Vul dit bestand verder aan

import numpy as np
import matplotlib.pyplot as plt

################################################################################
#                               Functiedefinities                              #
################################################################################
def bosbrand(kaart,iteraties):
    nr, nk = kaart.shape
    for iteratie in range(iteraties):
        kaart_nieuw = np.array(kaart)
        for i in range(1, nr-1):
            for j in range(1, nk-1):
                omgeving = kaart[i-1:i+2, j-1:j+2]
                if kaart[i, j] == 1 and np.any(omgeving == 2):
                    kaart_nieuw[i,j] = 2 
                    
        kaart = np.array(kaart_nieuw) 
    return kaart

#%% deelvraag 1
#-------------------------------------------------------------------------------
def afstand(M, p_1, p_2):
    teller = 0
    r, k = M.shape
    M[p_1[0],p_1[1]] = 2
    M[p_2[0],p_2[1]] = 3
    while True:
        if teller > 0:
            M = stapX
        A = np.array([[2,2,2],[2,2,2],[2,2,2]]) #np.any(B == 2):
        B = M[p_2[0]-1:p_2[0]+2,p_2[1]-1:p_2[1]+2] == A
        stapX = np.copy(M)
        for i in range(r):
            for j in range(k):
                if M[i][j] == 2:
                    pad = M[i-1:i+2, j-1:j+2]
                    Z = pad == 1
                    stapX[i-1:i+2, j-1:j+2][Z] = 2
        #plt.imshow(M) #Verwijder # om stap per stap te zien
        #plt.show()
        teller += 1
        if np.any(B):
            break
    return teller  
   


#%% deelvraag 2
#-------------------------------------------------------------------------------
def bosbrand_uitbreiding(kaart,iteraties):
    pass # verwijder pass en vul aan
def bosbrand_uitbreiding(kaart,iteraties):
    r, k = kaart.shape
    doof = np.zeros((r,k))
    for iteratie in range(iteraties):
        kaart_nieuw = np.array(kaart)
        for i in range(1, r-1):
            for j in range(1, k-1):
                omgeving = kaart[i-1:i+2, j-1:j+2]
                if kaart[i, j] == 1 and np.any(omgeving == 2):
                    kaart_nieuw[i,j] = 2 
                if kaart[i,j] == 2:
                    doof[i,j] += 1          
        kaart = np.array(kaart_nieuw) 
    vergelijk = doof > 2
    kaart[ : , : ][vergelijk] = 3
    #plt.imshow(doof) #Verwijder # om stap per stap te zien
    #plt.show()
    #plt.imshow(kaart) #Verwijder # om stap per stap te zien
    #plt.show()
    return kaart
################################################################################
#                               Instructies                                    #
################################################################################
kaart1 = np.loadtxt('VoorbeeldExamen1-Bestanden\landschap.txt')
kaart_nieuw = bosbrand(kaart1, 3)
plt.imshow(kaart_nieuw, cmap="coolwarm")

#%% deelvraag 1
#-------------------------------------------------------------------------------
kaart2 = np.loadtxt('VoorbeeldExamen1-Bestanden\landschap.txt')
d = afstand(kaart2,(17, 2),(20, 3))
print(d)


#%% deelvraag 2
#-------------------------------------------------------------------------------
kaart3 = np.loadtxt('VoorbeeldExamen1-Bestanden\landschap_bosbrand.txt')
kaart_uitbreiding_nieuw = bosbrand_uitbreiding(kaart3, 7)
plt.imshow(kaart_uitbreiding_nieuw, cmap="coolwarm")
plt.show()
