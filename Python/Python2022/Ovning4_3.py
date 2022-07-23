lon = 0.01 # 1 öre
dagar = 1

while lon < 10000000:
    lon *= 2
    dagar += 1

print(dagar, 'dagar')