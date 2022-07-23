sma_konsonanter = 'bcdfghjklmnpqrstvwxyz'
stora_konsonanter = 'BCDFGHJKLMNPQRSTVWXYZ'

# ovning 5.4 sidan 90 -> sidan 98

def tonormal(text):
    i = 0
    buffer = ''
    while i < len(text):
        c = text[i]
        buffer += c

        if i < len(text) - 2 and \
        (c in sma_konsonanter or c in stora_konsonanter) and \
            text[i + 1] == 'o' and text[i + 2] == c.lower():
            i += 3
        else:
            i += 1
    return buffer


f = open('rovarsprak.txt', 'r')
for s in f:
    print(s, '->', tonormal(s))
f.close()
