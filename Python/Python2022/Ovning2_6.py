import math

T = 5730
L = math.log(2) / T # lambda

t = float(input('t: '))
n = 100 * math.exp(-L * t)

print(f'Återstar {n:.1f}%')
