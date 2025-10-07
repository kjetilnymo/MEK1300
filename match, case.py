#Oppgave 1
letter = input("Input a letter: ")

if letter.lower() in "aeiou":
    print("It is a vowel")
    
elif letter.lower() == "y":
    print("Sometimes it is a vowel, sometimes it is a consonant")
    
else:
    print("It is a consonant")
    
    
#Oppgave 2
num_sides = int(input("Enter the number of sides: "))

match num_side:
   case 3:
        name = "Triangle"
        
   case 4:
        name = "Quadrilaternal"
        
   case 5:
        name = "Pentagon"
        
   case 6:
        name = "Hexagon"
        
   case 7:
        name = "Heptagon"
        
   case 8:
        name = "Octagon"
        
   case 9:
        name = "Nonagon"
        
   match:
        print("Jesus christ mate, how man sides do you need??")
        
    if name == "":
        
    else:
        print("This is a" {name})

    
#Bruke match/case

#Oppgave 3
month = input("Enter the name of a month: ").capitalize()

if month == if month == "January" or month == "March" or \
    month == "May" or month == "July" or \
        month == "August" or month == "October" or \
            month == "December":
                days = 31
                
elif month == "April" or month == "June" or \
    month == "September" or month == "November":
        days = 30
        
elif month == "February":
    days = "28 or 29"

else:
    days = 0
    
if days == 0:
    print("Invalid month name")
    
    
else:
    print(month, "has", days, "days in it")
    
    












