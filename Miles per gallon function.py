#Funksjon for å printe pris per mile og hvor langt man kommer på x antall gallon fuel

MILES = 100

gallons = float(input("Enter the number of gallons of gas in the tank: "))
fuel_efficiency = float(input("Enter the fuel efficiency in miles per gallon: "))
price_per_gallon = float(input("Enter price of gas per gallon: "))
cost = (MILES/fuel_efficiency) * price_per_gallon
miles = gallons * fuel_efficiency

print (f"Cost per {MILES} miles = {cost:.2f} USD.")
print(f"The car can go {miles:.3f} miles with {gallons} gallons of gas in the tank.")
