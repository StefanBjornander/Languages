input = input("Input: ").lower();

index = 0;
output = "";

while (index < len(input)):
    if (index < (len(input) - 1)):
        if ((input[index] == "a") and (input[index + 1] == "a")):
            output += "å";
            index += 2;
        elif ((input[index] == "a") and (input[index + 1] == "e")):
            output += "ä";
            index += 2;
        elif ((input[index] == "o") and (input[index + 1] == "e")):
            output += "ö";
            index += 2;
        else:
            output += input[index];
            index += 1;
    else:
        output += input[index];      
        index += 1;
print(output);