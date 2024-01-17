##################################################################
# Instructies
##################################################################


# DEELVRAAG 1 --> vul aan
# ----------------------------------------------------------------
# Je kan volgende strings gebruiken om je script te testen:
params = "v = 145.0 mm, f = 40.0 mm" #, b = 55.2 mm, m = -0.38"
#params = "v = -22.0 mm, b = 56.0 mm, f = -36.2 mm, m = 2.55"
#params = "b = 56.0 mm, v = -22.0 mm, f = -36.2 mm, m = 2.55"
#params = "b = 80.0 mm, v = 120.0 mm, f = 48.0 mm, m = -0.67"

lijst = []
param = params.split(", ")
param = sorted(param)
for i in param:
    l = i.split(" = ")
    l[1] = float(l[1].strip(" mm"))
    lijst.append(l)


if lijst[0][0] != "f" and lijst[1][0] != "f":
     f = round(1/((1/lijst[0][1])+(1/lijst[1][1])),1)
     m = -round((lijst[0][1]/lijst[1][1]),2)
     params = f"f = {f} mm, v = {lijst[1][1]} mm, b = {lijst[0][1]} mm, m ={m}"


if lijst[0][0] != "b" and lijst[1][0] != "b":
    b  = round(1/((1/lijst[0][1])-(1/lijst[1][1])),1)
    m = -round((b/lijst[1][1]),2)
    params = f"f = {lijst[0][1]} mm, v = {lijst[1][1]} mm, b = {b} mm, m ={m}"


if lijst[0][0] != "v" and lijst[1][0] != "v":
    v = round(1/((1/lijst[1][1])-(1/lijst[0][1])),1)
    m = -round((lijst[0][1]/v),2)
    params = f"f = {lijst[1][1]} mm, v = {v} mm, b = {lijst[0][1]} mm, m ={m}"
print(params)





# DEELVRAAG 2 --> vul aan
# ----------------------------------------------------------------
# Je kan volgende strings gebruiken om je script te testen:
params = "v = 120.0 mm, b = 80.0 mm"
# resultaat: v = 120.0 mm, b = 80.0 mm, f = 48.0 mm, m = -0.67
#params = "b = 80.0 mm, f = 48.0 mm"
## resultaat: b = 80.0 mm, f = 48.0 mm, v = 120.0 mm, m = -0.67
#params = "v = 145.0 mm, f = 40.0 mm"
## resultaat: v = 145.0 mm, f = 40.0 mm, b = 55.2 mm, m = -0.38
#params = "b = 56.0 mm, v = -22.0 mm"
## resultaat: b = 56.0 mm, v = -22.0 mm, f = -36.2 mm, m = 2.55
#params = "v = -22.0 mm, b = 56.0 mm"
## resultaat: v = -22.0 mm, b = 56.0 mm, f = -36.2 mm, m = 2.55

# VUL AAN





