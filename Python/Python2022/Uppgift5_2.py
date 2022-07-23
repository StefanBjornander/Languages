text = input('Text: ');
if text[0] == text[len(text) - 1]:
    print('Lika');
else:    
    print('Olika');

print('Lika' if text[0] == text[len(text) - 1] else 'Olika');    