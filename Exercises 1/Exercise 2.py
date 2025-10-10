from math import sqrt

"""
#Oppgave 1
print(""
Oppgave 1:")
#a)
n = 1
m = -1
if n < -m :
    print ("a =", n)
else :
    print("a =", m)
    
#b)
n = 1
m = -1
if -n >= m :
    print("b =", n)
else :
    print("b =", m)

#c)
x=0.0
y = 1.0
if abs(x-y) < 1:
    print("c =", x)
else:
    print("c =", y)
    
#d)
x = sqrt(2.0)
y = 2.0
if x * x ==y :
    print("d =", x)
else:
    print("d =", y)
    
    
#Oppgave 2
print(""
      
Oppgave 2:"")
number_input = int(input("Enter a number from 1-10: "))


if 0 < number_input < 10:
    print("The number you entered is:", number_input)

elif 1 > number_input:
    print("The number you entered is < 1")

elif number_input > 10:
    print("The number you entered is > 10")


#Oppgave 3
print(""
      
Oppgave 3:"")
score = int(input("Enter the score (0-100): "))

if 90 <= score <= 100:
    print("The letter grade is A")

elif 80 <= score <= 89:
    print("The letter grade is B")

elif 70 <= score <= 79:
    print("The letter grade is C")
        
elif 60 <= score <= 69:
      print("The letter grade is D")
          
elif 0 <= score <= 59:
    print("The letter grade is F")
    
else:
    print("Invalid input. The score must be in the range: (0-100)")
 
    
#Oppgave 4
print(""
      
Oppgave 4:"")      
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
operator = input("Enter the operator type: ")

if operator == "*":
    print("Result is:", number_one * number_two)
    
elif operator == "/":
    if number_two == 0:
        print("Division by 0 is not allowed")
    else:
        print("Result is:", number_one / number_two)
     
elif operator == "+":
    print("Result is:", number_one + number_two)
     
elif operator == "-":
    print("Result is:", number_one - number_two)

else:
    print("Invalid operator or operator is not in the list")



#Oppgave 5
print(""
      
Oppgave 5:"")
kg = 1
lbs = 1

weight = int(input("Enter your weight: "))
unit = input("Have you entered your weight in lbs or kg: ")

kg_to_lbs = weight * 2.2
lbs_to_kg = weight * 0.45


if unit == "kg":
    print("Your weight is:", kg_to_lbs, "lbs.")
    
elif unit == "lbs":
    print("Your weight is:", lbs_to_kg, "kg.")
    
else:
    print("You have not entered lbs or kg. Why??")
          
""" 
    
#Oppgave 6
print("""
      
Oppgave 6:""")

type = str(input("Skriv her: "))






