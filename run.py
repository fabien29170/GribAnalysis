import pygrib
import numpy
grbs = pygrib.open('../.xygrib/grib/test.grb2')


grb = grbs.select(name='10 metre U wind component')
PasdeTemps=len(grb)

g=grb[0]
print("Composante",g.name," Pas de temps = ",PasdeTemps, " Date=",g.analDate)

tab=g.data()
for j in range(len(tab[0])):
    for i in range(len(tab[0][0])):
        print(tab[1][j][i],' ',tab[2][j][i],' ',tab[0][j][i])
    print("-------------")

