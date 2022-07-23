pris_med_moms = float(input('Pris inklusive moms (i kronor): '))
moms_i_procent = float(input('Moms (i procent): '))

moms_i_kronor = moms_i_procent / 100 * pris_med_moms
pris_utan_moms = pris_med_moms - moms_i_kronor

print(f'Moms: {moms_i_kronor:.2f} kr')
print(f'Pris exlusive moms: {pris_utan_moms:.2f} kr')
