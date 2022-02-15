list = [];
while (True):
    value = int(input(": "));
    
    if (value == 0):
        break;

    if (not (value in list)):
        list.append(value);

for value in list:
    print(value, " ", sep = "", end = "");
