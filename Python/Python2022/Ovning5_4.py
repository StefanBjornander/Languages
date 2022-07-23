text = input('Text: ')
buffer = ''

sma_konsonanter = 'bcdfghjklmnpqrstvwxyz'
stora_konsonanter = 'BCDFGHJKLMNPQRSTVWXYZ'

for c in text:
    if c in sma_konsonanter or c in stora_konsonanter:
        buffer += c + 'o' + c.lower()
    else:
        buffer += c
        
print(buffer)