import math

r = 0.50e-2
A = r**2 * math.pi
V = 4 / 3 * r**3 * math.pi
Ds = 7.86e3
m = V * Ds

g = 9.82
C = 0.45
Dl = 1.20

t = 0
dt = 0.00001
h = 300
v = 0
a = g

while h > 0:
 t = t + dt
 v = v + a * dt
 h = h - v * dt
 a = g - 1 / (2 * m) * C * Dl * A * v**2

print("t = %.4f" % t)
print("h = %.4f" % h)
print("v = %.4f" % v)
print("a = %.4f" % a)



  

