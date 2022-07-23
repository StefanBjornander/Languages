import datetime
now = datetime.datetime.now()

d = now.date()
ar = d.year
manad = d.month
dag = d.day
print(f'Dagens datum {ar:02}-{manad:02}-{dag:02}')

t = now.time()
tim = t.hour
min = t.minute
sec = t.second
print(f'Klockan ar {tim:02}:{min:02}:{sec:02}')
