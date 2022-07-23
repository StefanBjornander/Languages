text = input('Text: ')
buffer = ''

sma_konsonanter = 'bcdfghjklmnpqrstvwxyz'
stora_konsonanter = 'BCDFGHJKLMNPQRSTVWXYZ'

i = 0
while i < len(text):
    c = text[i]
    buffer += c

    if i < len(text) - 2 and \
       (c in sma_konsonanter or c in stora_konsonanter) and \
        text[i + 1] == 'o' and text[i + 2] == c.lower():
        i += 3
    else:
        i += 1
        
print(buffer)