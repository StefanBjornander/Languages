text1 = input('Text 1: ').strip()
text2 = input('Text 2: ').strip()

for c in text1:
    if text1.count(c) != text2.count(c):
        print('Ej Anagram')
        break;
else:
    print('Anagram')
