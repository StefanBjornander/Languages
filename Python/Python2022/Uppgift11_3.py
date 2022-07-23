name = input('Name: ')

try:
    f = open(name, 'r')

    lines = 0
    comments = 0

    for s in f:
        lines += 1
        if '#' in s:
            comments += 1
    f.close()

    print(f'{100 * comments / lines:.2f}%')
except FileNotFoundError:
    print(f'Cannot open "{name}".')
