import math
volume = [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0]
pressure = [29.750, 19.125, 14.375, 9.5, 7.125, 5.625, 4.875, 4.250, 3.750, 3.375, 3.0, 2.625, 2.250, 2.0, 1.875, 1.750, 1.5, 1.375, 1.250]
pv = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
a = 0
average = 0.0
abweichung = [0, 1]
maxabweichung = 0.0

# Berechnung von P * V = c (für jedes P und das dazugehörige V gibt es ein c)
# jedes c wird an die entsprechende Stelle in pv geschrieben
for a in range(0, 19):
    c = volume[a] * pressure [a]
    pv[a] = c

# Berechnung des Durchschnitts von pv
a = 0
for a in range(0, 19):
    average += pv[a]
average = average / 19

# Maximal und Minimalwerte von pv
maxpv = max(pv)
minpv = min(pv)

# Printen der Ergebisse
print("Durchschnitt von P*V:", end=" ")
print(average)
print(" ")
print("Maximaler Wert:", end=" ")
print(maxpv)
print("Minimaler Wert:", end=" ")
print(minpv)
print(" ")

# Berechnung der Maximalen Abweichung vom Durchschnitt für pv mit Hilfe des Mini- bzw Maximalwerts
# abs() damit der Betrag des Ergebnisses genommen wird
abweichung[0] = abs(average - maxpv)
abweichung[1] = abs(average - minpv)

# Printen der Ergebnisse
maxabweichung = max(abweichung)
print("Maximale Abweichung vom Durchschnitt:", end=" ")
print(maxabweichung)

# Maximal zugelassene Abweichung vom Durchschnitt
maxerlabweichung = 10
print("Maximal zugelassene Abweichung:", end=" ")
print(maxerlabweichung)

# Ergebniss mit Berechnung ob die Abweichung die zugelassene Maximalabweichung einhält
print(" ")
print("Ergebnis:")
if maxabweichung < maxerlabweichung:
    print("P * V = konstant")
    print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung nicht)")
else:
    print("P * V ist nicht konstant")
    print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung)")
