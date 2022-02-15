def fyll(list, start, end, value):
    assert start >= 0, ("Less than zero", start);
    assert end <= len(list), ("Not less than size", end, len(list));
    assert start < end, ("End >= Start", start, end);
    for index in range(start, end):
        list[index] = value;
l = [0, 0, 0, 0, 0, 0];        
fyll(l, 2, 4, 1);
#fyll(l, -1, 3, 1);
#fyll(l, 3, 3, 1);
#fyll(l, 3, 10, 1);
print(l);
