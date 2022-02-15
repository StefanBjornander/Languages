rows = int(input("Rows: "));

for row in range(1, rows + 1):
    for column in range(1, rows + 1):
        print(f"{row * column:3}", end="");
    print();
