import datetime
d = datetime.datetime.now().date()
manad = d.month
dag = d.day

text = input('Personnummer: ')
m = int(text[2:4])
d = int(text[4:6])

if m == manad and dag == d:
    print('Grattis')