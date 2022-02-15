input = input("Text: ");
output = "";
vokals = "aeiouåäö";

for c in input:
    if (c in vokals):
        output += c;
    else:
        output += c + "o" + c;

print(output);