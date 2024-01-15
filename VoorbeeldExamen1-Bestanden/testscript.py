# test met infoFun
import infoFun

containercup = infoFun.listRead("containercup.csv")
print(containercup[0])



# test met numpy
import numpy as np

M = np.arange(25).reshape(5, 5)
print(M)



# test met matplotlib
import matplotlib.pyplot as plt
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

plt.figure()
plt.plot(t, s)
plt.xlabel("tijd (s)")
plt.ylabel("spanning (mV)")
plt.title("Eenvoudige plot")
plt.show()