import math

def rectangel_area(hojd, bredd):
    return hojd * bredd

def cirkel_area(radie):
    return radie ** 2 * math.pi

def triangel_area(hojd, bredd):
    return hojd * bredd / 2

h = float(input('Hojd: '))
b = float(input('Bredd: '))
print(f'Ractangle area: {rectangel_area(h, b)}')
print(f'Triangel area: {triangel_area(h, b)}')

r = float(input('Radie: '))
print(f'Cirkel area: {cirkel_area(r)}')
