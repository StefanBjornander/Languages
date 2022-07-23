import math

a = float(input('a: '))
b = float(input('c: '))
alpha_grader = float(input('alpha: '))
alpha_radianer = math.pi * alpha_grader / 180
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(alpha_radianer))

# Vi behover inte testa om math.fabs(a - c) < 1e-10
if math.fabs(a - b) < 1e-10 and \
   math.fabs(b - c) < 1e-10:
   print('Liksidig')
elif math.fabs(a - b) < 1e-10 or \
   math.fabs(a - c) < 1e-10 or \
   math.fabs(b - c) < 1e-10:
   print('Likbent')
else:
   print('Oliksidig')
