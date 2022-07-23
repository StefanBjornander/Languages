import math

def Newton(x):
    root = 1
    last_root = 0
    while math.fabs(root - last_root) >= 1e-7:
        last_root = root
        root = (root + x / root) / 2
    return root

x = int(input('x: '))
print(f'Newton: {Newton(x):.3}')

