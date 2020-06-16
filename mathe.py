import random
import math

runden = input("Bitte die Anzahl der Runden -> ")
intervall_start = input("Bitte den Startpunkt des Intervalls -> ")
intervall_ende = input("Bitte den Endpunkt des Intervalls -> ")
hoehe = 1/math.sqrt(1-float(intervall_ende)**2)
flaeche = (float(intervall_ende) - float(intervall_start)) * hoehe
treffer = 0

for i in range(int(runden)):
    x = random.uniform(float(intervall_start), float(intervall_ende))
    #print(x)
    y = random.uniform(0, hoehe)
    #print(y)
    if y < 1/math.sqrt(1-(x**2)):
        treffer += 1
        #print("Treffer!")
    else:
        pass
        #print("Nicht getroffen!")

for i in range(10):
    print()

print("In", runden, "Runden wurden", treffer, "Treffer auf einer insgesamten Fläche von", round(flaeche, 2), "FE erzielt.")
ergebnis = float(treffer) / float(runden) * flaeche
print("Somit ist die gesuchte Fläche", round(ergebnis, 2), "FE groß.")