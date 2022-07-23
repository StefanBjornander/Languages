import rektangel2

while True:
    text = input('Top: ')
    if text == '':
        break

    top = int(text)
    left = int(input('Left: '))
    hojd = int(input('Hojd: '))
    bredd = int(input('Bredd: '))

    r = rektangel2.Rektangel(top, left, 0, 0)
    r.hojd = hojd
    r.bredd = bredd
    print('Area', r.area())
    print('Omkrets:', r.omkrets())
