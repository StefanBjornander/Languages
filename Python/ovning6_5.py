import math;

size = int(input("Size: "));
list = [];
sum = 0;

for index in range(0, size):
    value = int(input(f"Index {index + 1}: "));
    list.append(value);
    sum += value;

average = sum / size;
squareSum = 0;

for value in list:
    difference = value - average;
    squareSum += difference * difference;

derivation = math.sqrt(squareSum / size);
print(derivation);