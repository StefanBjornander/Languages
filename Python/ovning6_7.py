import math;
matrix = [];
size = int(input("Size: "));

for row in range (0, size):
    line = [];
    for column in range (0, size):
        value = int(input(f"[{row}][{column}]: "));
        line.append(value);
    matrix.append(line);

lastSum = 0;
for index in range(0, size):
    value = matrix[index][index];
    lastSum += value;

currSum = 0;
for index in range(0, size):
    value = matrix[index][size - index - 1];
    currSum += value;

ok = (lastSum == currSum);

if (ok):
    for row in range(0, size):
        currSum = 0;
        for column in range (0, size):
            value = matrix[row][column];
            currSum += value;
        if (lastSum != currSum):
            ok = False;
            break;

if (ok):        
    for column in range (0, size):
        currSum = 0;
        for row in range(0, size):
            value = matrix[row][column];
            currSum += value;
        if (lastSum != currSum):
            ok = False;
            break;
        
print(ok);