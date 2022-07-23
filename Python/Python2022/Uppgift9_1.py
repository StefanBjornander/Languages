import random

def sten_sax_pase():
    list = ['Sten', 'Sax', 'Pase']
    index = random.randint(0, 2)
    return list[index]

def play(hand1, hand2):
    if (hand1 == 'Sten'):
        if (hand2 == 'Sten'):
            return 0
        elif (hand2 == 'Sax'):
            return -1
        else: # Pase
            return 1
    elif (hand1 == 'Sax'):
        if (hand2 == 'Sten'):
            return 1
        elif (hand2 == 'Sax'):
            return 0
        else: # Pase
            return -1
    else: # Pase
        if (hand2 == 'Sten'):
            return -1
        elif (hand2 == 'Sax'):
            return 1
        else: # Pase
            return 0



