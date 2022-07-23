def EratosthenesSall(n):
    list = [False]
    for i in range(1, n + 1):
        list.append(True)
    
    for i in range(2, n + 1):
        if list[i]:
            for j in range(2 * i, n + 1, i):
                list[j] = False

    result = []
    for i in range(2, n + 1):
        if list[i]:
            result.append(i)

    return result

n = int(input('n: '))
print(EratosthenesSall(n))