richter = float(input("Enter a magnitude on the Richter scale: "))

if richter > 8:
    print("Most structures fall")
    
elif richter >= 7:
    print("Many buildings destroyed")

elif richter >= 6:
    print("Many buildings ...")
    
else:
    print("Damage to poorly constructed buildings")
    
#if / else / elif

#boolean values
#    - and / or, false / true

string = "Python Programming"
print("P" in string)
print(string.count("y"))
print(string.startswith("P"))
print(string.find("n"))
