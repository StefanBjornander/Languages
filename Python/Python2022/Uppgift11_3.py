f = open('loggfil', 'r')
max_time = 0

for line in f:
    if line.strip() != '':
        list = line.split(' ')
        name = list[0]
        time = sum(int(x) for x in list[1:] if True) # list comprehension, page 104

        if max_time == 0 or time > max_time:
            max_name = name
            max_time = time

print(max_name, max_time, 'minuter')
f.close()