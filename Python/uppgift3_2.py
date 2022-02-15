priceYearCard = float(input("Price year card: "));
priceOneTime = float(input("Price one time: "));
numberOfTimes = int(input("Number of times: "));

if (numberOfTimes * priceOneTime > priceYearCard):
    print("Year card");
else:
    print("One-time tickets");
