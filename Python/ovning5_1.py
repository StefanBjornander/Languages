text1 = input("Text: ");
text2 = text1.strip();
lastSpace = text2.rindex(" ");
lastWord = text2[lastSpace + 1:];
print(f"Last Word: <{lastWord}>");