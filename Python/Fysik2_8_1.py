m = 5.14e-7
F = 4.41e-6
k = 9.90e-6

v0 = 0
a0 = F / m
delta_t = 0.001

for i in range(1,1000):
  last_v = v
  last_a = a

  a = last_a - k/ m * last_v
  v = last_v + last_a * delta_t

  print("i = ", i, "a =", a, " v = ", v)

