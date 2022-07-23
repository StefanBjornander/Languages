t = float(input("Ange reaktionstiden (s): ")) # Laser in reaktionstiden
v = float(input("Ange hastigheten (km/h): ")) # Laser in hastigheten
v = v / 3.6                                   # Enhetsomvandlar km/h => m/s
s = v * t                                     # Beraknar reaktionsstrackan
print("Reaktionsstrackan (m): ", s)           # Skriver ut reaktionsstrackan
