text1 = input("Text 1: ");
text2 = input("Text 2: ");

if (len(text1) != len(text2)):
    print("Wrong length.");
else:
    index = 0;
    ok = True;
    length = len(text2);

    while (index < len(text1)):
        #print(index, text1[index], text2[length - index - 1]);
        if (text1[index] != text2[length - index - 1]):
            ok = False;
            break;
        index += 1;
    print(ok);