s = input('Skriv ett tal: ')

ok = True
for e in s:
    if not (e >= '0' and e <= '9'):
        ok = False
        break

if ok:
    print('Talet är OK.')
else:
    print('Inget tal.')
