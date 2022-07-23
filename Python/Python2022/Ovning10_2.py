import math

def medelv(a):
    sum = 0
    for x in a:
        sum += x
        return sum / len(a)

def stdav(a):
    try:        
        n = medelv(a)
        sum = 0
        for x in a:
            sum += (x - n) ** 2
        return math.sqrt(sum / len(a))
    except TypeError:
        return 0

def median(a):
    try:        
        b = sorted(a)
        n = len(b)
        if n % 2 == 0:
            return b[(n - 1) //2]
        else:
            return (b[n // 2 - 1] + b[n // 2]) / 2
    except TypeError:
        return 0

a = [1, 2, 3, 4, 5]
print('median', median(a))
print('median', median(1))