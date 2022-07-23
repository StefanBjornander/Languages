def namnet(rad):
    ord = rad.split()
    namnen = [e for e in ord if not e.isdecimal()]
    namn = ' '.join(namnen)
    return namn.lower()

f = open('elevfil', 'r')
lines = f.readlines()
print(lines)
f.close()

while True:
    rad = input(': ')

    if rad.strip() == '':
        break

    if rad.lower().split()[0] == 'radera':
        rad = ' '.join(rad.split()[1:])
        print(rad)
        for i in range(0, len(lines)):
            if namnet(rad) == namnet(lines[i]):
                del lines[i]
                print('Radered.')
                break
        else:
            print('Ej funnen.')
    else:
        for i in range(0, len(lines)):
            if namnet(rad) == namnet(lines[i]):
                lines[i] = rad
                break
        else:
            lines.append(rad)

f = open('elevfil', 'w')
f.writelines(lines)
f.close()
