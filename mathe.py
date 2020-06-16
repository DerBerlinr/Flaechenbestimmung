import random
import math

runden = input("Bitte die Anzahl der Runden -> ")
intervall_start = input("Bitte den Startpunkt des Intervalls -> ")
intervall_ende = input("Bitte den Endpunkt des Intervalls -> ")
schrittzahl = input("Bitte die Schrittzahl für die Maximum- und Minimum-berechnung -> ")
schrittweite = 1/schrittzahl

# MAXIMUM UND MINIMUM BERECHNEN
maxi = 0
for j in range(float(intervall_start), float(intervall_ende, schrittweite)):
    hoehe = math.log(math.cos(j))+1
    if hoehe > maxi
        maxi = hoehe

mini = 0
for k in range(float(intervall_start), float(intervall_ende), schrittweite):
    hoehe = math.log(math.cos(k))+1
    if hoehe < mini
        mini = hoehe

# FLÄCHE INSGESAMT BERECHNEN
flaeche = (float(intervall_ende) - float(intervall_start)) * (maxi-mini)
treffer = 0


# MAINLOOP
for i in range(int(runden)):
    x = random.uniform(float(intervall_start), float(intervall_ende))
    #print(x)
    y = random.uniform(mini, maxi)
    #print(y)
    if y < math.log(math.cos(x))+1:
        treffer += 1
        #print("Treffer!")
    else:
        pass
        #print("Nicht getroffen!")

for i in range(4):
    print()

print("In", runden, "Runden wurden", treffer, "Treffer auf einer insgesamten Fläche von", round(flaeche, 2), "FE erzielt.")
ergebnis = float(treffer) / float(runden) * flaeche
print("Somit ist die gesuchte Fläche", round(ergebnis, 5), "FE groß.")
