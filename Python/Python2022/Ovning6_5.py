def fabs(x):
    return x if x >= 0 else -x

def Newton(x):
    root = 1
    last_root = 0
    while fabs(root - last_root) >= 1e-7:
        last_root = root
        root = (root + x / root) / 2
    return root

def standaravvikelse(a):
    sum = 0
    n = len(a)
    for x in a:
        sum += x
    m = sum / n
    sum = 0
    for x in a:
        sum += (x - m) ** 2
    return Newton(1 / n * sum)

b = [1, 2, 3, 4, 5]
print(standaravvikelse(b))
c = [10, 20, 30, 40, 50]
print(standaravvikelse(c))
d = [1, 2, 30, 49, 50]
print(standaravvikelse(d))
