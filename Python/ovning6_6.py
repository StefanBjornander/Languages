import math;
matrix = [];
size = int(input("Size: "));

for row in range (0, size):
    line = [];
    for column in range (0, size):
        value = int(input(f"[{row}][{column}]: "));
        line.append(value);
    matrix.append(line);

#for row in range (0, size):
#    for column in range (0, size):
#        print(matrix[row][column], " ", sep= "", end="");
#    print();

ok = True;
for row in range (0, size):
    for column in range (0, size):
        if (matrix[row][column] != matrix[column][row]):
            ok = False;
            break;
    if (not ok):
        break;
print(ok);


