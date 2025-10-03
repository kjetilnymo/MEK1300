#input funkjson som gjør om kilo til pounds

KG_TO_POUND = 2.2

kg = float(input("Enter a weighgt in KG: "))

pound = kg * KG_TO_POUND

print(kg, "kilogram(s) =", "%.2f" % pound, "Pound(s")
print(f"{kg} Kilogram(s) = {pound:.2f} Pound(s)")
