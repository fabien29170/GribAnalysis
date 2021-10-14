import pygrib
import datetime
import numpy as np
import math
grbs = pygrib.open('../../.xygrib/grib/test.grb2')

grbComposanteUWind = grbs.select(name='10 metre U wind component')
grbComposanteVWind = grbs.select(name='10 metre V wind component')
print(type(grbComposanteUWind))

#Pour calculer nbr d'itérations, prendre la dernière analDate et faire la soustraction
NbrPasdeTemps=len(grbComposanteUWind)
PasdeTemps=datetime.timedelta(hours=1)

gU=grbComposanteUWind [0]
print("Composante",gU.name," Pas de temps = ",NbrPasdeTemps, " Date=",gU.analDate)
gDate=gU.analDate
newTab=np.array(gU.data(),np.float32)
print(newTab[:])
for t in range(NbrPasdeTemps):
    gU=grbComposanteUWind[t]
    gV=grbComposanteVWind[t]
    tabU=gU.data()
    tabV=gV.data()
    for j in range(len(tabU[0])):
        for i in range(len(tabU[0][0])):
            longitude = tabU[2][j][i]
            if longitude >= 180:
                longitude = longitude - 360
                U=tabU[0][j][i]
                V=tabV[0][j][i]
                #chaineOutput=str(tabU[1][j][i])+','+str(longitude)+',U='+str(U)+','+gDate.isoformat()
                #chaineOutput.replace(" ","")
                #print(chaineOutput)
                #chaineOutput=str(tabV[1][j][i])+','+str(longitude)+',V='+str(V)+','+gDate.isoformat()
                #chaineOutput.replace(" ","")
                #print(chaineOutput)
                #Utiliser Arctan2 qui gère le signe de l'angle directement
                Angle=np.arctan2(U,V)*180/np.pi
                if Angle<0 : 
                    Angle +=360
                #print ('Angle',Angle)
                Vitesse=round(math.sqrt(U*U+V*V)*3600/1852,2)
                #print ('Vitesse',Vitesse)
                chaineOutput=str(round(tabV[1][j][i],3))+','+str(round(longitude,3))+','+str(round(Angle,2))+','+str(Vitesse)+','+gDate.isoformat()
                chaineOutput.replace(" ","")
                print(chaineOutput)
    gDate=gU.analDate+datetime.timedelta(hours=t)
    
