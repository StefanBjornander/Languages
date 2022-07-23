from sys import argv

for name in argv[1:]:
    f = open(name, 'r')
    lines = f.readlines()
    print(name, len(lines))
