judges = int(input("Judges: "));

if (judges < 3):
    print("Too few judges.");
else:
    while (True):
        degree = int(input("Degree: "));

        if (degree <= 0):
            break;
            
        min = 0;
        max = 0;
        sum = 0;

        for index in range(1, judges + 1):
            points = int(input(f"Judge {index}: "));

            if ((min == 0) or (points < min)):
                min = points;

            if ((max == 0) or ( points > max)):
                max = points;

            sum += points;

        print(f"Min: {min}, Max: {max}");
        sum -= min;
        sum -= max;
        average = sum / (judges - 2);
        result = degree * average;
        print(f"Average: {average}, Result: {result}");
