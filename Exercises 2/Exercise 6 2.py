#Oppgave 2

from random import randint

values = []

for i in range(10):
    number = randint(0, 100)
    values.append(number)

    
print(values, "\n") #\n lager mellom me

#4
even=[] #definere liste for even tall
odd=[] #definere liste for odd tall
for number in values: # går igjennom hvert tall i lista
    if number %2 == 0: # hvis tallet er even
        even.append(number) #legges det til i even lista
    else: #hvis ikke 
        odd.append(number) #legges den inn i oss lista
print("Even list",even,"Odd list",odd) #printer ut begge listene


#5
count = 0
if count < 10:
    for number in values: # går igjennom hvert tall i lista    
        if number %2 != 0: # hvis tallet er even
            values.remove(number)
            count += 1

print(values)
  


#c1


total = 0

for number in values:
    if number % 2 == 0:
        total = total + 1

print(total)