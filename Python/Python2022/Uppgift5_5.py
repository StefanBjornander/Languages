s = input('Text: ')
i = 0
position = -1

for c in s:
    if c == ' ' or c == '\t':
        print(f'Whitespace på plats {i}')    
        break
    i += 1
else:
    print('Inget whitespace')
