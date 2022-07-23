text = input('Text: ')
stripped_text = text.replace(' ', '')
reversed_text = stripped_text[::-1]

if stripped_text == reversed_text:
    print('Palindrom')
else:
    print('Ej Palindrom')
