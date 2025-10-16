#In a loop, a part of a program is repeated over and
#over, until a specific goal is reached.
"""
#eksempel 1

counter = 1
while counter <= 10:
    print(counter)
    counter = counter + 1
    

#eksempel 2

number = 1
total = 0

while number <= 100 :
    total = total + number
    number = number + 1
    
print("sum of first 100 numbers = ", total)


#eksempel 3

n = 1729
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print(total)



#eksempel 4

total = 0
count = 0

salary = 0 

while salary >= 0:
    salary = float(input("Enter a salary or any negative number to finish: "))
    if salary >= 0:
        total = total + salary
        count = count + 1
        
        


#eksempel 5


user_input = input("Enter a value or Q to quit")

total = 0

while user_input != "Q":
    value = int(user_input)
    total = total + value
    user_input = input("Enter a value or any characters to quit: ")
    
print("Total ->", total)

"""

#Eksempel 6, finne største verdi

largest = int(input("Enter a value: "))
user_input = input("Enter a value: ")

while user_input != "":
    value = int(user_input)
    if value > largest:
        largest = value
    user_input = input("Enter a value: ")
    
print("Largest number ->", largest)








