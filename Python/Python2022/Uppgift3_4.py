t = int(input('Temp? '))

if t < 18:
    print('Det ar kallt')
    print('Satt pa varmen')

    if t < 0:
        print('Svinkallt')
    elif t < 12:
        print('Satt pa jackan')
        
else:
    print('Det ar varmt')
    if t > 30:
        print('Okenhett')        
    elif t >= 22:
        print('Stang av varmen')

print(f'Det ar {t:.1f} grader')