totalprice = float(input("Price: "));
momspercent = float(input("Moms: "));
moms = momspercent / 100;
momsprice = moms * totalprice;
partprice = totalprice * (1 - moms);
print(f'Part price: {partprice:06.2f}, Moms price: {momsprice:06.2f}');
