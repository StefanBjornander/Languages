stations = int(input("Stations: "));
index = 0;
list = [];
sum = 0;
for index in range(0, stations):
    value = int(input(f"Station {index + 1}: "));
    list.append(value);
    sum += value;
    index += 0;

average = sum / stations;
print(f"Average: {average}");

index = 0;
while (index < len(list)):
    value = list[index];
    if (value > average):
        print(f"Index {index + 1}: {value}");
#        print(index, " ", value, sep = "", end = "");
    index += 1;