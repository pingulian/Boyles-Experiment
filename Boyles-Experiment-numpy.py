import numpy as np

# Gegebene Werte als NumPy-Arrays
volume = np.array([1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0])
pressure = np.array([29.750, 19.125, 14.375, 9.5, 7.125, 5.625, 4.875, 4.250, 3.750, 3.375, 3.0, 2.625, 2.250, 2.0, 1.875, 1.750, 1.5, 1.375, 1.250])

# Berechnung von P * V
pv = volume * pressure

# Berechnung von Durchschnitt, Maximal- und Minimalwert
average = np.mean(pv)
maxpv = np.max(pv)
minpv = np.min(pv)

# Maximalen Abweichung vom Durchschnitt
abweichungnumb = np.abs([maxpv - average, minpv - average])
maxabweichungnumb = np.max(abweichungnumb)

#Abweichung in %
abweichung = (maxabweichungnumb / average) * 100

# Maximal zugelassene Abweichung
maxerlabweichung = 30

# Ergebnisse ausgeben
print("Durchschnitt von P*V:", average)
print("Maximaler Wert:", maxpv)
print("Minimaler Wert:", minpv)
print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
print("\nErgebnis:")

# Überprüfung der Abweichung
if abweichung < maxerlabweichung:
    print("P * V = konstant")
    print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung nicht)")
else:
    print("P * V ist nicht konstant")
    print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung)")
