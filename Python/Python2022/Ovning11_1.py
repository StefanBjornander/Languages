max = 0
sum = 0
count = 0
first = True

f = open('temperaturer.txt', 'r')
for rad in f:
    temp = int(rad)
    sum += temp
    if first or temp > max:
        max = temp
    count += 1
    first = False
f.close()

print('max', max)
print('medel', sum / count)
