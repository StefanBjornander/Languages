def moms(pris_utan_moms, moms_i_procent):
    return pris_utan_moms / (1 - moms_i_procent / 100)

pris_utan_moms = float(input('Pris exlusive moms (i kronor): '))
moms_i_procent = float(input('Moms (i procent): '))
print(f'Pris inclusive moms: {moms(pris_utan_moms, moms_i_procent):.2f} kr')
