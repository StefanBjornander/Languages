import math;
min = 0;
max = 0;

while (True):
    number = int(input("Number: "));
    
    if (number < 0):
        break;
    
    if ((min == 0) or (number < min)):
        min = number;

    if ((max == 0) or (number > max)):
        max = number;

print(f"Max: {max}, Min: {min}");
