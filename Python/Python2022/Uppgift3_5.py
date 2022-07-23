langd = int(input('Langd (mm): '))
bredd = int(input('Bredd (mm): '))
tjocklek = int(input('Tjocklek (mm): '))

if langd <= 600 and tjocklek <= 100 and \
   bredd + langd + tjocklek <= 900 and \
   langd >= 140 and bredd >= 90:
    print('Ok')
else:
    print('Not Ok')
