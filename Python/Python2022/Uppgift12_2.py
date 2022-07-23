map1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
print(map1)
print(map1['I'])
map1['V'] = 6
print(map1['V'])

map2 = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
print(map2)
print(map1['X'])
map2['X'] = 11
print(map2['X'])

map3 = dict()
map3['I'] = 1
map3['V'] = 5
map3['X'] = 10
map3['L'] = 50
map3['C'] = 100
map3['D'] = 500
map3['M'] = 1000
print(map3)
print(map3['L'])
map3['L'] = 51
print(map3['L'])

