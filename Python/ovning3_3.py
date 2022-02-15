import math;
a = float(input("A: "));
b = float(input("B: "));
alpha = float(input("Alpha: "));
c = math.sqrt(a * b + b * b - 2 * a * b * math.cos(alpha));
print(f"A: {a}, B: {b}, C: {c}")

epsilon = 1e-10;
ab = abs(a - b) < epsilon;
ac = abs(a - c) < epsilon;
bc = abs(b - c) < epsilon;

if (ab and ac and bc):
    print("Liksidig.");
elif (ab or ac or bc):
    print("Likbent.");
else:
    print("Ingendera.")
