def sgd(m, n):
    if m == n:
        return m
    elif m > n:
        return sgd(m - n, n)
    else:
        return sgd(m, n - m)

m = int(input('m: '))
n = int(input('n: '))
print(f'sgd: {sgd(m, n)}')
