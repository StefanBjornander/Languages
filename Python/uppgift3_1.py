minutesPerMonth = float(input("Minutes per month: "));
pricePerMinute = float(input("Price Per Minute: "));
pricePerMonth = minutesPerMonth * pricePerMinute;

if (minutesPerMonth >= 300):
    pricePerMonth *= 0.90;
print(f'Price per month: {pricePerMonth:.3f}');
