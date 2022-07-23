map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman = input('Romerskt tal: ')

arabic = []
for r in roman.upper():
    arabic.append(map[r])

for i in range(len(arabic) - 2, -1, -1):
    if arabic[i] < arabic[i + 1]:
        arabic[i] = arabic[i + 1] - arabic[i]
        del arabic[i + 1]
result = sum(arabic)
print('Arabiskt tal:', result)