text = input('text: ')
list = text.split(' ')

print(list)
list.sort(key = lambda word : len(word))
print(list)
