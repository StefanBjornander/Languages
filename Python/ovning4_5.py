endYear = int(input("Year: "));
size = 26_000;

for year in range(2020, endYear + 1):
    size = int((size * 1.04 * 0.993) + 300 - 325);
print(f"Size: {size}");
