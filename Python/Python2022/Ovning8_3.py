def test(s):
    sma = 0
    stora = 0
    for c in s:
        if (c.islower()):
            sma += 1
        elif (c.isupper()):
            stora += 1
    return (sma, stora)

print(test("Hello, World!"))