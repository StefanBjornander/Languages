import math;
today = int(input("Today's setting: "));
ayearago = int(input("A year ago's setting: "));
miles = today - ayearago;
print(f'Miles {miles}');
liters = int(input("Liters: "));
permile = liters / miles;
print(f'Per mile: {permile:.3f}');
