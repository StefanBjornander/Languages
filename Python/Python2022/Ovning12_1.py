letterToMorse = {'A' : '.-',
                 'B' : '-...',
                 'C' : '-.-',
                 'D' : '-..',
                 'E' : '.',
                 'F' : '..-.',
                 'G' : '--.',
                 'H' : '....',
                 'I' : '..',
                 'J' : '.---',
                 'K' : '-.-',
                 'L' : '.-..',
                 'M' : '--',
                 'N' : '-.',
                 'O' : '---',
                 'P' : '.--.',
                 'Q' : '--.-',
                 'R' : '.-.',
                 'S' : '...',
                 'T' : '-',
                 'U' : '..-',
                 'V' : '...-',
                 'W' : '.--',
                 'X' : '-..-',
                 'Y' : '-.--',
                 'Z' : '--..'}
print(letterToMorse)

morseToLetter = dict()
for letter, morse in letterToMorse.items():
    morseToLetter[morse] = letter
print(morseToLetter)

morses = []
letters = input('Text: ')
for l in letters.upper():
    morses.append(letterToMorse[l])
for m in morses:
    print(m, ' ')

letters = []
morses = input('Morse: ')
for m in morses.split(' '):
    letters.append(morseToLetter[m])
for l in letters:
    print(l, end = '')




print()