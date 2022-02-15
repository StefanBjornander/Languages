t = (1, 2, 3, 4);
l = [1, 2, 3, 4];

if (len(t) == len(l)):
    index = 0;
    ok = True;
    while (index < len(t)):
        if (t[index] != l[index]):
            ok = False;
            break;
        index += 1;
    print(ok);
else:
    print("Wrong sizes.");
