text = input('Personnummer: ')
siffra = int(text[8])

if siffra % 2 == 0:
    print('Kvinna')
else:
    print('Man')    