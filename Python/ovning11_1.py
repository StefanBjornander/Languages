while (True):
    try:
        value = int(input("Value: "));
        print(value);
        break;
    except ValueError:
        print("Try again!");
