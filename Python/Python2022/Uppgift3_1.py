min = int(input('Antal minuter: '))
kr_per_min = float(input('Kronor/minut: '))
total_kostnad = min * kr_per_min

if total_kostnad >= 300:
    total_kostnad = 0.9 * total_kostnad # Indentering

print(f'Total kostnad: {total_kostnad:.1f}')
