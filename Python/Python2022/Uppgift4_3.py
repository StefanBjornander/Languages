n = int(input('n: '))
k = 1
harmoniska_serien = 0
while k <= n:
    harmoniska_serien = harmoniska_serien + 1 / k
    k += 1
print("Harmoniska serien:", harmoniska_serien)
