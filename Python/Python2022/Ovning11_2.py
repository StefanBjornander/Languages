from sys import argv

name = argv[1]
f = open(name, 'r')
lista = f.readlines()
f.close()

for i in range(0, len(lista)):
    print(lista[i].strip().replace('\t', '   '))

