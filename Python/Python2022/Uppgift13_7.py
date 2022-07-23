import rektangel

while True:
    text = input('Top: ')
    if text == '':
        break

    top = int(text)
    left = int(input('Left: '))
    hojd = int(input('Hojd: '))
    bredd = int(input('Bredd: '))

    r = rektangel.Rektangel(top, left, 0, 0)
    r.set_hojd(hojd)
    r.set_bredd(bredd)
    print('Area', r.area())
    print('Omkrets:', r.omkrets())
