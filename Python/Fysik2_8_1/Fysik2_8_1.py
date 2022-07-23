import math

F = 4.41e-6
m = 5.14e-7
k = 4.90e-6

v = 0
a = F / m
dt = 0.00001

while True:
  last_v = v
  last_a = a
  a = F / m - k / m * v
  v = v + last_a * dt
  if math.fabs(v - last_v) < 1e-6:
    break

print("a = %.6f" % a)
print("v = %.6f" % v)
