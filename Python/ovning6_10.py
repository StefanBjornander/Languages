import math;
list = [];
size = int(input("Size: "));

list1 = [];
for index in range (0, size):
    value = int(input(f"Index {index}: "));
    list1.append(value);

list2 = [];
for index in range (0, size):
    value = int(input(f"Index {index}: "));
    list2.append(value);

sum = 0;
for index in range (0, size):
    value1 = list1[index];
    value2 = list2[index];
    sum += value1 * value2;

orthogonal = (sum == 0);
print(orthogonal);
