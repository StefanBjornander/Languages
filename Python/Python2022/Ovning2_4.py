miles_per_gallon = float(input('Miles/gallon: '))
gallon_per_miles = 1 / miles_per_gallon
liter_per_miles = 3.785 * gallon_per_miles
liter_per_km = liter_per_miles / 1.609
liter_per_mil = 10 * liter_per_km
print(f'Liter/mil: {liter_per_mil:.3f}')
