def antal_siffror(n):
    siffror = 0
    while n > 0:
        siffror += 1
        n //= 10
    return siffror

tal = int(input('Tal: '))
print(f'Siffror: {antal_siffror(tal)}')
