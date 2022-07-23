def max(a):
   if len(a) == 0:
      return None
   elif len(a) == 1:
      return a[0]
   else:
      first = a[0]
      max_rest = max(a[1:])
      return first if first > max_rest else max_rest

antal = int(input('Antal: '))
list = []
for i in range(1, antal + 1):
    tal = int(input(f'Tal {i}: '))
    list.append(tal)
print(max(list))
