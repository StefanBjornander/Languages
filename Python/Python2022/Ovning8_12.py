def avtal(ar):
    if ar == 1:
        return 25000
    else:
        return 1.03 * avtal(ar - 1) + 900

for a in range(1, 11):
    print(f'Ar {a}: {avtal(a):2}')