text = input('Text: ').lower()

i = 0
buffer = ''
while (i < len(text)):
    c = text[i]

    if c == 'a' and i < len(text) and text[i + 1] == 'a':
        buffer += 'a'
        i += 2
    elif c == 'a' and i < len(text) and text[i + 1] == 'e':
        buffer += 'a'
        i += 2
    elif c == 'o' and i < len(text) and text[i + 1] == 'e':
        buffer += 'o'
        i += 2
    else:
        buffer += c
        i += 1

print(buffer)
