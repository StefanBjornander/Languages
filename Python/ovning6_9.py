import math;
list = [];
size = int(input("Size: "));

for index in range (0, size):
    value = int(input(f"Index {index}: "));
    list.append(value);

sum = 0;
for index in range (0, size):
    value = list[index];
    sum += value * value;

length = math.sqrt(sum);
print(length);
