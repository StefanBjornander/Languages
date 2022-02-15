input = input("Text: ");
output = "";
vokals = "aeiouåäö";

index = 0;
while (index < len(input)):
    output += input[index];
    
    if ((index < len(input) - 2) and (not (input[index] in vokals)) and \
        (input[index + 1] == "o") and (input[index] == input[index + 2])):
        index += 3;
    else:
        index += 1;

print(output);