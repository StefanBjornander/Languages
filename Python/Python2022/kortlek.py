import random

def ny():
    lek = []
    for i in range(1, 5):
        for j in range(1, 14):
            lek.append((i,j))
    random.shuffle(lek)
    return lek

def ge(lek):
    if len(lek) > 0:
        return lek.pop()
    else:
        return None

farg = ['\N{BLACK CLUB SUIT}', '\N{WHITE DIAMOND SUIT}', '\N{WHITE HEART SUIT}', '\N{BLACK SPADE SUIT}']

valor = ('Ess', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knekt', 'Dam', 'Kung')

def visa(k, sist = '\n'):
    f, v = k
    print(farg[f - 1], valor [v - 1], end = sist)

def jfr(k1, k2):
    f1, v1 = k1
    f2, v2 = k2

    if f1 != f2:
        if f1 < f2:
            return -1
        else:
            return 1
    else:
        if v1 == v2:
            return 0
        elif v1 == 1:
            return -1
        elif v2 == 1:
            return 1
        elif v1 > v2:
            return -1
        else:
            return 1
