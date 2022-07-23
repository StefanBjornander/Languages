m = int(input('m: '))
n = int(input('n: '))

while True:
    if m > n:
        r = m % n
        if r == 0:
            result = n
            break
        else:
            m = n
            n = r
    else:
        r = n % m
        if r == 0:
            result = m
            break
        else:
            n = m
            m = r

print (f'Storsta gemensamma delaren: {result}')
