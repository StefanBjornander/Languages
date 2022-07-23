s = input('Text: ')
i = 0
position = -1

for c in s:
    if c == ' ' or c == '\t':
        position = i
    i += 1

if position == -1:
    print('Inget whitespace')
else:
    print(f'Whitespace på plats {position}')
