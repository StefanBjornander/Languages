f = open('personer.txt', 'a')
while True:
    name = input('Name: ')
    if name == '':
        break
    f.write(name)
f.close()