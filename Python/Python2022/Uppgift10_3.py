s = input('Skriv ett tal: ')

for e in s:
    if not (e >= '0' and e <= '9'):
        print('Inget tal.')
        break
else:
    print('Talet är OK.')    