while True:
    hojd = float(input('Hojd (m): '))

    if hojd < 0:
        break
        
    antal = 0
    while hojd > 0.01:
        hojd = 0.7 * hojd
        antal += 1
    print('Antal studsar: ', antal)
