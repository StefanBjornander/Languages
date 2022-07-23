text = input('Text: ')
list = text.strip().split(' ')
print(f'Storlek: {len(text)}, Forsta: {list[0]}, Sista: {list[len(list) - 1]}')
