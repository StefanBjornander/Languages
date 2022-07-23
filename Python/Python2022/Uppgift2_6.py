tid = int(input('Tid i secunder: '))

# // heltalsdivision
tim = tid // 3600
min = (tid % 3600) // 60
sec = tid % 60

print(f'Tim: {tim:d}')
print(f'Min: {min:d}')
print(f'Min: {sec:d}')
