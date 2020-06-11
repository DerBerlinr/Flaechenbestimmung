import random
import math

runden = input("Bitte die Anzahl der Runden -> ")
intervall_start = input("Bitte den Startpunkt des Intervalls -> ")
intervall_ende = input("Bitte den Endpunkt des Intervalls -> ")
hoehe = float(intervall_ende)*math.e**-float(intervall_ende)
print(hoehe)
flaeche = (float(intervall_ende) - float(intervall_start)) * 1
treffer = 0

for i in range(int(runden)):
    x = random.uniform(float(intervall_start), float(intervall_ende))
    #print(x)
    y = random.uniform(0, 1)
    #print(y)
    if y < -2*(x**2)+x:
        treffer += 1
        #print("Treffer!")
    else:
        pass
        #print("Nicht getroffen!")

print("Treffer: ", treffer)
print("Runden: ", runden)
print("Fläche: ", flaeche)
ergebnis = float(treffer) / float(runden) * flaeche
print("Ergebnis = ", ergebnis)
