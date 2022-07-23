import random

size = 0
f = open('namnfil.txt', 'r')
for s in f:
    size += 1
f.close()

index = random.randint(1, size)

f = open('namnfil.txt', 'r')
for i in range(0, index):
    name = f.readline().strip()
f.close()

print(name)
