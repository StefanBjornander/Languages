x = int(input('x: '))
y = int(input('y: '))

min = x if x < y else y
max = x if x > y else y

print('min:', min)
print('max:', max)
