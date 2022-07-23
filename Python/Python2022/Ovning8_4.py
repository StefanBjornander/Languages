def primtal(n):
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

tal = int(input('Tal: '))
print(primtal(tal))