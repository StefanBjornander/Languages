from sys import argv

f = open(argv[1], 'r')
lista = f.readlines()
f.close()

f = open(argv[2], 'w')
for i in range(0, len(lista), 2):
    rad1 = lista[i]
    rad2 = lista[i + 1]

    token = rad2.split(' ')
    h = float(token[1])
    m = float(token[2])
    bmi = m / (h / 100) ** 2

    if bmi > 30:
        f.write(rad1)
        f.write(rad2)
f.close()
