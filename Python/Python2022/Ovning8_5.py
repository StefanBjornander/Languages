def relativa_primtal(i, j):    
    min = i if i < j else j

    for k in range(2, min):
        if i % k == 0 and j % k == 0:
            return False
    return True

tal1 = int(input('Tal1: '))
tal2 = int(input('Tal2: '))
print(relativa_primtal(tal1, tal2))