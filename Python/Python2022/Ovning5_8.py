text1 = input('Tid 1: ')
tim1 = int(text1[:2])
min1 = int(text1[3:])
minuter1 = 60 * tim1 + min1

text2 = input('Tid 2: ')
tim2 = int(text2[:2])
min2 = int(text2[3:])
minuter2 = 60 * tim2 + min2

if minuter2 < minuter1:
    minuter2 += 24 * 60

minuter = minuter2 - minuter1
tim = minuter // 60
min = minuter % 60

print(f'{tim:02}:{min:02}')
