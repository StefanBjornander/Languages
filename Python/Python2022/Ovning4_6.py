sum = 0
index = 1
sign = 1
while True:
    term = 1 / index
    if term < 0.00001:
        break;
    sum += sign * term
    index += 1
    sign *= -1
print(sum)