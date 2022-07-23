import kortlek

lek = kortlek.ny()

while True:
    kort1 = kortlek.ge(lek)
    kort2 = kortlek.ge(lek)

    if kort1 == None or kort2 == None:
        break

    kortlek.visa(kort1)
    kortlek.visa(kort2)
    
    resultat = kortlek.jfr(kort1, kort2)

    if resultat == -1:
        kortlek.visa(kort1, ' ')
    else:
        kortlek.visa(kort2, ' ')
    print('vann')
    print()
