size = int(input("Size: "));
list = [];

for index in range(0, size):
    value = int(input(f"Index {index + 1}: "));
    list.append(value);

print(list);
list.sort();
print(list);

if ((size % 2) == 0):
    median = (list[(size // 2) - 1] + list[size // 2]) / 2;
else:
    median = list[size // 2];
print(median);