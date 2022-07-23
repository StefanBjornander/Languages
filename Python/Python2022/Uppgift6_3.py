import random

list = []
for i in range(0, 100):
    list.append(random.randint(1, 1000));

min = 0
max = 0
summa = 0
for tal in list:
    summa += tal
    if min == 0 or tal < min:
        min = tal
    if tal > max:
        max = tal

medel = summa / 100    
print(f'min: {min}, max: {max}, medel: {medel}')
