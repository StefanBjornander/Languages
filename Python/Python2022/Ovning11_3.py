from sys import argv

name = argv[1]
f = open(name, 'r')
lista = f.readlines()
f.close()

f = open(name, 'w')
for i in range(0, len(lista)):
    text = lista[i].strip().replace('a', 'X')
    print(text)
    f.write(text + '\n')
f.close()
