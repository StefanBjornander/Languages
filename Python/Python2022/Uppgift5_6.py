svensk_datum = input('Svensk datum som aa-mm-dd: ')
ar = svensk_datum[:2]
manad = svensk_datum[3:5]
dag = svensk_datum[6:]
amerikanskt_datum = f'20{manad:2}/{dag:2}/{ar:2}/'
print(amerikanskt_datum)